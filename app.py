from flask import Flask, render_template
from time import strftime
import feedparser
import re
import socket
import time

from case_files import CASE_FILES

app = Flask(__name__, static_folder='public', static_url_path='')

SUBSTACK_RSS = "https://asthapurohit.substack.com/feed"
RSS_TIMEOUT_SECONDS = 5
RSS_CACHE_TTL_SECONDS = 15 * 60

_rss_cache = {
    'posts': None,
    'fetched_at': 0.0,
}

PLACEHOLDER_POSTS = [
    {
        'title': 'Why stated preferences lie — and what to measure instead',
        'url': 'https://substack.com/@asthadiaries',
        'summary': 'Surveys capture what people think they want. Product decisions need what they actually do under friction, social pressure, and incomplete information.',
        'date': 'Mar 2026',
        'reading_time': 7,
        'tags': ['Behavioral Design'],
        'series': None,
    },
    {
        'title': 'The habit loop is not the job — intent timing is',
        'url': 'https://substack.com/@asthadiaries',
        'summary': 'Retention frameworks borrowed from consumer apps break when the moment of intent passes before the product shows up. A case for designing around when, not how often.',
        'date': 'Feb 2026',
        'reading_time': 6,
        'tags': ['Habit Formation', 'Product Strategy'],
        'series': None,
    },
    {
        'title': 'Class signals in everyday consumption',
        'url': 'https://substack.com/@asthadiaries',
        'summary': 'How people buy status, safety, and belonging through small daily choices — and why brands that ignore class anxiety misread the real job-to-be-done.',
        'date': 'Jan 2026',
        'reading_time': 9,
        'tags': ['Classism Series'],
        'series': 'classism',
    },
    {
        'title': 'Good friction vs bad friction in onboarding',
        'url': 'https://substack.com/@asthadiaries',
        'summary': 'Not every step removed is a win. Some friction builds trust, sets expectations, or filters for the users who will actually stay.',
        'date': 'Dec 2025',
        'reading_time': 5,
        'tags': ['UX', 'Onboarding'],
        'series': None,
    },
]


def estimate_reading_time(text):
    words = len(re.sub(r'<[^>]+>', '', text).split())
    return max(1, round(words / 200))


def normalize_tags(entry, series):
    tags = [t.term for t in entry.get('tags', []) if t.term]
    if series == 'classism' and not any('classism' in t.lower() for t in tags):
        tags.insert(0, 'Classism Series')
    return tags[:2]


def _entries_to_posts(feed):
    posts = []
    for entry in feed.entries:
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

        posts.append({
            'title': title,
            'url': entry.get('link', '#'),
            'summary': summary,
            'date': date,
            'reading_time': estimate_reading_time(raw_summary),
            'tags': normalize_tags(entry, series),
            'series': series,
        })
    return posts


def fetch_substack_posts():
    cached_posts = _rss_cache['posts']
    now = time.monotonic()
    if cached_posts and (now - _rss_cache['fetched_at']) < RSS_CACHE_TTL_SECONDS:
        return cached_posts

    try:
        previous_timeout = socket.getdefaulttimeout()
        socket.setdefaulttimeout(RSS_TIMEOUT_SECONDS)
        try:
            feed = feedparser.parse(SUBSTACK_RSS)
            posts = _entries_to_posts(feed)
        finally:
            socket.setdefaulttimeout(previous_timeout)

        if posts:
            _rss_cache['posts'] = posts
            _rss_cache['fetched_at'] = now
            return posts
    except Exception as e:
        print(f"RSS fetch error: {e}")

    if cached_posts:
        return cached_posts
    return PLACEHOLDER_POSTS


@app.route("/")
def home():
    return render_template("index.html", case_files=CASE_FILES)


@app.route("/thoughts")
def thoughts():
    return render_template("thoughts.html", posts=fetch_substack_posts())


if __name__ == "__main__":
    app.run(debug=True)
