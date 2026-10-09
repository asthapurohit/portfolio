from flask import Flask, abort, render_template
from datetime import datetime
from time import strftime
from urllib.parse import urlsplit
import feedparser
import html
import math
import re
import socket
import time

from case_files import CASE_FILES, NOW_BUILDING, case_sections

app = Flask(__name__, static_folder='public', static_url_path='')

SUBSTACK_RSS = "https://asthapurohit.substack.com/feed"
RSS_TIMEOUT_SECONDS = 5
RSS_CACHE_TTL_SECONDS = 15 * 60

_rss_cache = {
    'posts': None,
    'fetched_at': 0.0,
    'ok': False,
}

# Featured Thoughts, matched by URL path. Edit this list in one place.
FEATURED_POST_URLS = [
    "https://asthapurohit.substack.com/p/the-boy-with-the-keychain",
    "https://asthapurohit.substack.com/p/everyone-is-a-classist",
]


WORDS_PER_MINUTE = 220


def _is_coming_soon(url):
    path = (url or '').split('?', 1)[0].split('#', 1)[0].rstrip('/')
    return path.endswith('/p/coming-soon')


def _remove_subscription_widget(raw):
    marker = 'subscription-widget-wrap-editor'
    start = raw.find(marker)
    if start == -1:
        return raw
    open_at = raw.rfind('<div', 0, start)
    if open_at == -1:
        return raw
    depth = 0
    i = open_at
    length = len(raw)
    while i < length:
        next_open = raw.find('<div', i)
        next_close = raw.find('</div>', i)
        if next_close == -1:
            return raw
        if next_open != -1 and next_open < next_close:
            depth += 1
            i = next_open + 4
        else:
            depth -= 1
            i = next_close + len('</div>')
            if depth == 0:
                return raw[:open_at] + raw[i:]
    return raw


def _plain_text(raw):
    text = _remove_subscription_widget(raw or '')
    text = re.sub(r'(?is)<(script|style)\b[^>]*>.*?</\1>', ' ', text)
    text = re.sub(r'<[^>]+>', ' ', text)
    return html.unescape(text)


def _word_count(raw):
    return len(_plain_text(raw).split())


def reading_time_minutes(raw_html):
    count = _word_count(raw_html)
    if count <= 0:
        return None
    return math.ceil(count / WORDS_PER_MINUTE)


def _full_post_html(entry):
    parts = [
        item.get('value', '')
        for item in (entry.get('content') or [])
        if item.get('value', '').strip()
    ]
    if not parts:
        return None
    body = ''.join(parts)
    summary = entry.get('summary') or entry.get('description') or ''
    if _word_count(body) <= _word_count(summary):
        return None
    return body


def normalize_tags(entry, series):
    tags = [t.term for t in entry.get('tags', []) if t.term]
    if series == 'classism' and not any('classism' in t.lower() for t in tags):
        tags.insert(0, 'Classism Series')
    return tags[:2]


def _entries_to_posts(feed):
    posts = []
    for entry in feed.entries:
        url = entry.get('link', '#')
        if _is_coming_soon(url):
            continue

        raw_summary = entry.get('summary', '') or entry.get('description', '')
        summary = re.sub('<[^<]+?>', '', raw_summary)
        summary = ' '.join(summary.split())
        if len(summary) > 180:
            summary = summary[:177] + '...'

        published = entry.get('published_parsed')
        date = strftime('%b %Y', published) if published else ''

        title = entry.get('title', '')
        series = None
        if any('classism' in t.term.lower() for t in entry.get('tags', [])) or 'classist' in title.lower() or 'classism' in title.lower():
            series = 'classism'

        body = _full_post_html(entry)
        posts.append({
            'title': title,
            'url': url,
            'summary': summary,
            'date': date,
            'reading_time': reading_time_minutes(body) if body else None,
            'tags': normalize_tags(entry, series),
            'series': series,
        })
    return posts


def _url_path(url):
    return urlsplit(url or '').path.rstrip('/').lower()


def _is_classism_post(post):
    if post.get('series') == 'classism':
        return True
    return any(tag == 'Classism Series' for tag in (post.get('tags') or []))


def group_thoughts(posts):
    """Featured, then classism series, then the rest. No duplicates."""
    by_path = {}
    for post in posts:
        by_path.setdefault(_url_path(post.get('url')), post)

    featured = []
    featured_paths = set()
    for url in FEATURED_POST_URLS:
        path = _url_path(url)
        post = by_path.get(path)
        if not post or path in featured_paths:
            continue
        featured.append(post)
        featured_paths.add(path)

    series = []
    rest = []
    for post in posts:
        path = _url_path(post.get('url'))
        if path in featured_paths:
            continue
        if _is_classism_post(post):
            series.append(post)
        else:
            rest.append(post)

    latest_path = _url_path(posts[0].get('url')) if posts else None

    def mark(items):
        marked = []
        for post in items:
            item = dict(post)
            item['is_latest'] = bool(latest_path) and _url_path(post.get('url')) == latest_path
            marked.append(item)
        return marked

    return mark(featured), mark(series), mark(rest)


def fetch_substack_posts():
    """Return cached Substack posts. Always a list, so len() stays a stable essay count."""
    cached_posts = _rss_cache['posts']
    now = time.monotonic()
    if cached_posts is not None and (now - _rss_cache['fetched_at']) < RSS_CACHE_TTL_SECONDS:
        return cached_posts

    try:
        previous_timeout = socket.getdefaulttimeout()
        socket.setdefaulttimeout(RSS_TIMEOUT_SECONDS)
        try:
            feed = feedparser.parse(SUBSTACK_RSS)
            if not getattr(feed, 'entries', None):
                raise Exception('RSS feed returned no entries')
            posts = _entries_to_posts(feed)
        finally:
            socket.setdefaulttimeout(previous_timeout)

        _rss_cache['posts'] = posts
        _rss_cache['fetched_at'] = now
        _rss_cache['ok'] = True
        return posts
    except Exception as e:
        print(f"RSS fetch error: {e}")

    if cached_posts is not None:
        _rss_cache['fetched_at'] = now
        return cached_posts

    _rss_cache['posts'] = []
    _rss_cache['fetched_at'] = now
    _rss_cache['ok'] = False
    return []


@app.route("/")
def home():
    return render_template(
        "index.html",
        case_files=CASE_FILES,
        now_building=NOW_BUILDING,
        year=datetime.now().year,
    )


@app.route("/thoughts")
def thoughts():
    posts = fetch_substack_posts()
    featured, series, rest = group_thoughts(posts)
    return render_template(
        "thoughts.html",
        posts=posts,
        featured=featured,
        series=series,
        rest=rest,
        feed_ok=_rss_cache['ok'],
    )


@app.route("/work/<slug>")
def work_case(slug):
    # Items whose PDF is the write-up (case_page False) have no page here.
    pages = [project for project in CASE_FILES if project.get('case_page', True)]
    index = next((i for i, project in enumerate(pages) if project.get('slug') == slug), None)
    if index is None:
        abort(404)
    project = pages[index]
    previous_case = pages[index - 1] if index else None
    next_case = pages[index + 1] if index + 1 < len(pages) else None
    return render_template(
        "case.html",
        project=project,
        study=case_sections(project),
        previous_case=previous_case,
        next_case=next_case,
    )


if __name__ == "__main__":
    app.run(debug=True)
