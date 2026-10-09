"""Capture viewport screenshots of each live project preview.

One-off local tool. Playwright is installed on this machine only and is not
listed in requirements.txt, which Vercel uses for the Flask app.
"""

import re
import sys
import time
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from case_files import CASE_FILES  # noqa: E402

VIEWPORT = {"width": 1440, "height": 900}
SETTLE_MS = 3000
WAKE_TIMEOUT_MS = 3 * 60 * 1000
MAX_BYTES = 500 * 1024
WAKE_PATTERN = re.compile(r"get this app back up", re.I)


def destination(preview_image):
    return ROOT / "public" / preview_image.lstrip("/")


def _frame_text(frame):
    try:
        return frame.locator("body").inner_text(timeout=1000)
    except Exception:
        return ""


def _spinner_visible(frame):
    spinner = frame.locator('[data-testid="stSpinner"], [data-testid="stStatusWidget"], .stSpinner')
    try:
        return spinner.count() > 0 and spinner.first.is_visible()
    except Exception:
        return False


def _click_wake_button(page):
    for frame in page.frames:
        button = frame.get_by_role("button", name=WAKE_PATTERN)
        try:
            if button.count() and button.first.is_visible():
                button.first.click()
                return True
        except Exception:
            continue
    return False


def wake_streamlit(page):
    """Click Streamlit's sleep button, then wait until the app iframe has content.

    Community Cloud renders the app inside an iframe, so the parent document
    stays nearly empty while the assistant is loading.
    """
    deadline = time.monotonic() + (WAKE_TIMEOUT_MS / 1000)
    while time.monotonic() < deadline:
        _click_wake_button(page)
        chunks = []
        spinning = False
        for frame in page.frames:
            if "statuspage.io" in frame.url:
                continue
            if _spinner_visible(frame):
                spinning = True
            chunks.append(_frame_text(frame))
        text = "\n".join(chunks)
        if WAKE_PATTERN.search(text) or spinning:
            page.wait_for_timeout(1000)
            continue
        cleaned = re.sub(r"Created by[\s\S]*", "", text, flags=re.I)
        cleaned = re.sub(r"Hosted with Streamlit", "", cleaned, flags=re.I).strip()
        if len(cleaned) > 30:
            return
        page.wait_for_timeout(1000)
    raise SystemExit("Streamlit app did not finish waking within 3 minutes.")


def shrink_if_needed(path, preview_image):
    size = path.stat().st_size
    if size <= MAX_BYTES:
        print(f"  {path.name}: {size / 1024:.0f} KB")
        return preview_image

    webp_path = path.with_suffix(".webp")
    image = Image.open(path)
    chosen = None
    for quality in (80, 70, 60, 50, 40, 30):
        image.save(webp_path, "WEBP", quality=quality, method=6)
        if webp_path.stat().st_size <= MAX_BYTES:
            chosen = quality
            break
    if chosen is None:
        raise SystemExit(f"{path.name} is still over 500 KB as WebP.")

    path.unlink()
    new_image = preview_image.rsplit(".", 1)[0] + ".webp"
    source = ROOT / "case_files.py"
    text = source.read_text(encoding="utf-8")
    updated = text.replace(preview_image, new_image, 1)
    if updated == text:
        raise SystemExit(f"Could not update the reference for {preview_image}.")
    source.write_text(updated, encoding="utf-8")
    print(f"  {webp_path.name}: {webp_path.stat().st_size / 1024:.0f} KB (WebP q{chosen})")
    return new_image


def capture(page, project):
    url = project["liveUrl"]
    preview_image = project["preview_image"]
    path = destination(preview_image)
    path.parent.mkdir(parents=True, exist_ok=True)
    print(f"Capturing {url}")
    page.goto(url, wait_until="load", timeout=WAKE_TIMEOUT_MS)
    if "streamlit.app" in url:
        wake_streamlit(page)
    page.wait_for_timeout(SETTLE_MS)
    page.screenshot(path=str(path), full_page=False, type="png")
    shrink_if_needed(path, preview_image)


def main():
    wanted = [arg.lower() for arg in sys.argv[1:]]
    projects = [project for project in CASE_FILES if project.get("preview_image") and project.get("liveUrl")]
    if wanted:
        projects = [
            project for project in projects
            if project["slug"].lower() in wanted or any(arg in project["preview_image"].lower() for arg in wanted)
        ]
    if not projects:
        raise SystemExit("No preview_image entries found in case_files.py.")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(viewport=VIEWPORT, device_scale_factor=1)
        page = context.new_page()
        try:
            for project in projects:
                capture(page, project)
        finally:
            browser.close()


if __name__ == "__main__":
    main()
