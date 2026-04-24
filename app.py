from flask import Flask, render_template
import feedparser
import re

app = Flask(__name__)

SUBSTACK_RSS = "https://asthapurohit.substack.com/feed"

def fetch_substack_posts():
    try:
        feed = feedparser.parse(SUBSTACK_RSS)
        posts = []
        for entry in feed.entries:
            summary = re.sub('<[^<]+?>', '', entry.get('summary', ''))
            summary = ' '.join(summary.split())[:180] + '...'
            
            published = entry.get('published_parsed')
            if published:
                from time import strftime
                date = strftime('%b %Y', published)
            else:
                date = ''

            title = entry.get('title', '')
            tags = [t.term for t in entry.get('tags', [])]
            
            series = None
            if any('classism' in t.lower() for t in tags) or 'classist' in title.lower() or 'classism' in title.lower():
                series = 'classism'

            posts.append({
                'title': title,
                'url': entry.get('link', '#'),
                'summary': summary,
                'date': date,
                'series': series,
            })
        return posts
    except Exception as e:
        print(f"RSS fetch error: {e}")
        return []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/thoughts")
def thoughts():
    posts = fetch_substack_posts()
    return render_template("thoughts.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)