# Optional fields:
#   more_links  extra links shown after the main one, e.g. [{'label': 'Deck', 'href': '/x.pdf'}]
#   doc_link    the PRD, teardown or case study file (PDFs live in public/), with doc_label
#   case_page   False when the doc itself is the write-up, so there's no /work/<slug> page
CASE_FILES = [
    {
        'title': 'Blinkit Discovery Engine & Pehli Baar',
        'slug': 'blinkit-discovery-engine-pehli-baar',
        'tag': 'Built',
        'deck': 'An AI research engine that found Blinkit shoppers re-order rather than browse, and Pehli Baar, a concept MVP that protects a shopper’s first order in a new category.',
        'role': 'NextLeap Fellowship',
        'stack': 'Python, Groq, Next.js, TypeScript',
        'year': '2026',
        'link': 'https://pehli-baar.vercel.app/',
        'liveUrl': 'https://pehli-baar.vercel.app/',
        'liveDomain': 'pehli-baar.vercel.app',
        'more_links': [
            {'label': 'Research engine', 'href': 'https://web-three-ashy-40.vercel.app/'},
        ],
        'link_note': 'An independent concept, not affiliated with or endorsed by Blinkit.',
        'preview_image': '/previews/pehli-baar.png',
        'narrative': [
            'Part 1 of my NextLeap fellowship project: an AI research engine that collected 4,876 Blinkit reviews and posts from Google Play, Reddit and the App Store, kept the 1,582 that carried shopping-behavior signal, and sorted them into 11 themes.',
            'The finding: shoppers don’t browse Blinkit, they re-order. Convenience and habit reordering drew 649 labels and product quality distrust 397; discovery and recommendations drew just 40.',
            'Discovery can’t be a browse mode bolted onto a reorder-first app. Pehli Baar lowers the risk of a first try instead: if a shopper’s first order in a new category isn’t right, they get a refund with one tap.',
        ],
        'pullQuote': 'Users don’t browse Blinkit — they re-order it.',
    },
    {
        'title': 'Spotify Review Analysis & Taste Bridge',
        'slug': 'spotify-review-analysis-taste-bridge',
        'tag': 'Built',
        'deck': 'An AI review engine that surfaces why users get stuck in listening ruts — feeding directly into Unstick, the MVP that bridges them out of one.',
        'role': 'Product Builder',
        'stack': 'React, Vite, Groq, Spotify API',
        'year': '2025',
        'link': 'https://taste-unstick.vercel.app/',
        'liveUrl': 'https://taste-unstick.vercel.app/',
        'liveDomain': 'taste-unstick.vercel.app',
        'more_links': [
            {'label': 'Deck', 'href': '/spotify-taste-bridge-deck.pdf'},
        ],
        'doc_link': '/spotify-taste-bridge-deck.pdf',
        'preview_image': '/previews/spotify-taste-bridge.png',
        'narrative': [
            'Users weren\'t asking for more recommendations — they were stuck in repeat-listening loops. I scraped App Store, Play Store, and Reddit reviews to find the root causes before designing anything.',
            'The problem wasn\'t taste; it was habit. Discovery shouldn\'t reset what people already love — it should bridge from where they already are.',
            'Unstick implements that thesis in one session: pick an activity, set a novelty dial, and get a five-track path from familiar to new. One nudge, one action, under thirty seconds — no full library reset.',
            'Shipped the review engine and the Unstick MVP on Vercel with real review data and a graduation deck documenting the full product arc from signal to solution.',
        ],
        'pullQuote': 'The best discovery features don\'t reset taste — they bridge from where users already are.',
    },
    {
        'title': 'Groww Weekly Review Pulse',
        'slug': 'groww-weekly-review-pulse',
        'tag': 'Built',
        'deck': 'AI dashboard that turns 1,499 real app reviews into a weekly brief any PM can act on in under 30 seconds.',
        'role': 'Solo Builder',
        'stack': 'React, Groq, Gemini, Vercel',
        'year': '2026',
        'link': 'https://groww-weekly-pulse.vercel.app/',
        'liveUrl': 'https://groww-weekly-pulse.vercel.app/',
        'liveDomain': 'groww-weekly-pulse.vercel.app',
        'preview_image': '/previews/groww-weekly-pulse.png',
        'narrative': [
            'PM teams drown in reviews. The job isn\'t to read them all — it\'s to surface what\'s actually broken. I scraped 1,499 real Groww reviews and built a pipeline that handles Hindi text, emoji-only posts, and one-word ratings.',
            'Every Monday, the dashboard auto-refreshes: five themes, top actions, user quotes, and a ready-to-send team email. Zero manual steps after the initial build.',
        ],
        'pullQuote': 'Real reviews are messy. Keyword matching alone fails — the hardest part wasn\'t the AI, it was the data pipeline.',
    },
    {
        'title': 'HDFC MF FAQ Chatbot',
        'slug': 'hdfc-mf-faq-chatbot',
        'tag': 'Built',
        'deck': 'A RAG-powered chatbot that makes dense mutual-fund documents conversational and accessible.',
        'role': 'Product Builder',
        'stack': 'Python, RAG, Streamlit, LLM',
        'year': '2026',
        'link': 'https://hdfc-mf-faq.streamlit.app/',
        'liveUrl': 'https://hdfc-mf-faq.streamlit.app/',
        'liveDomain': 'hdfc-mf-faq.streamlit.app',
        'link_note': "Hosted on Streamlit's free tier — it may take a moment to wake up.",
        'preview_image': '/previews/hdfc-mf-faq.png',
        'narrative': [
            'HDFC MF documentation is dense and hard to navigate — users can\'t find answers without reading entire PDFs. Financial products fail people not because they\'re complex, but because complexity is never translated.',
            'I chunked and embedded FAQ documents, built a retrieval pipeline, and wrapped it in Streamlit so users can query in plain English. Next iteration: source citations per answer so trust isn\'t assumed.',
        ],
        'pullQuote': 'The best interface for complex information is a conversation, not a document.',
    },
    {
        'title': 'Mastercard Checkout Teardown',
        'slug': 'mastercard-checkout-teardown',
        'tag': 'Teardown',
        'deck': 'Why paying online with a card in India feels slower than UPI — card details, tokenization and OTP waits — and three bets for Mastercard, led by passkeys.',
        'role': 'Independent',
        'year': '2026',
        'figure_label': 'Teardown',
        'doc_link': '/Mastercard-Checkout-Teardown.pdf',
        'doc_label': 'Read the teardown',
        'case_page': False,
        'narrative': [],
        'pullQuote': '',
    },
    {
        'title': 'Passkeys for Card Checkout',
        'slug': 'passkeys-card-checkout',
        'tag': 'PRD',
        'deck': 'A PRD that picks up the teardown’s top bet: offer a passkey right after a successful OTP card payment, so the next payment takes one fingerprint instead of an SMS wait.',
        'role': 'Independent',
        'year': '2026',
        'cover_metric': '+5 pts',
        'cover_label': 'Card checkout success vs OTP · pilot target',
        'figure_label': 'PRD',
        'doc_link': '/Passkeys-Card-Checkout-PRD.pdf',
        'doc_label': 'Read the PRD',
        'case_page': False,
        'narrative': [],
        'pullQuote': '',
    },
    {
        'title': 'First SIP',
        'slug': 'first-sip',
        'tag': 'Concept',
        'deck': 'A UX case study for first-time investors who finish KYC but never start a SIP: a goal-first start, a short fund list with visible criteria, and money shown in rupees rather than percentages.',
        'role': 'Independent',
        'year': '2026',
        'figure_label': 'UX case study (concept)',
        'doc_link': '/First-SIP-UX-Case-Study.pdf',
        'doc_label': 'Read the case study',
        'case_page': False,
        'narrative': [],
        'pullQuote': '',
    },
    {
        'title': 'ChatGPT Voice Adoption',
        'slug': 'chatgpt-voice-adoption',
        'tag': 'PRD',
        'deck': 'A PRD for ChatGPT voice among Indian university students — habitual use near 11%, awareness near 95%.',
        'role': 'NextLeap Fellowship',
        'year': '2026',
        'cover_metric': '11% → 25%',
        'cover_label': 'Voice-to-query · 90 days',
        'figure_label': 'PRD',
        'doc_link': '/chatGPT_PRD.pdf',
        'doc_label': 'Read the PRD',
        'narrative': [
            'Among Indian university students, awareness of ChatGPT voice is about 95%. Habitual usage stays near 11%.',
            'The response is Whisper Mode, plus a Technical Trust Buffer.',
            'Success metrics: voice-to-query ratio from 11% to 25% in 90 days, L7 stickiness up 15% by day 90, and word error rate under 5% on technical terms.',
        ],
        'pullQuote': 'Two root causes — social friction in shared spaces + performance distrust for STEM terms.',
    },
    {
        'title': 'Goodreads Quick Log',
        'slug': 'goodreads-quick-log',
        'tag': 'PRD',
        'deck': 'A PRD and teardown for Quick Log — a widget that cuts logging from 7 steps to 2.',
        'role': 'Independent',
        'year': '2026',
        'cover_metric': '+15%',
        'cover_label': 'North star · DAU logging YoY',
        'figure_label': 'PRD & teardown',
        'doc_link': '/Goodreads-PRD.pdf',
        'doc_label': 'Read the PRD',
        'more_links': [
            {'label': 'Teardown', 'href': '/Goodreads-ProductTeardown.pdf'},
        ],
        'narrative': [
            '4 of 6 interviewees log their reading progress after the fact.',
            'Quick Log cuts that logging from 7 steps to 2.',
            'The north star is DAU logging, up 15% year over year. The counter-metric — review conversion rate — is held flat.',
        ],
        'pullQuote': 'The intent exists — the in-feed trigger is missing.',
    },
]

NOW_BUILDING = {
    'title': 'GeoBehaviour',
    'tag': '0→1',
    'role': 'Independent',
    'year': '2026–present',
    'stack': 'Python, SQL, Maps API',
    'narrative': [
        'Small businesses in Indian urban markets lack reliable local demand signals. Surveys capture intent, not behavior.',
        'Building a geo-analytics platform that infers demand from proxy signals: foot traffic, search velocity, review patterns.',
    ],
}


def _text(text):
    return {'text': text, 'todo': None}


def _todo(hint):
    return {'text': None, 'todo': hint}


def _figure(project):
    if not project.get('cover_metric'):
        return None
    return {
        'metric': project['cover_metric'],
        'label': project.get('cover_label') or '',
    }


def _doc(project, todo):
    href = project.get('doc_link')
    return {'label': 'Deck or PRD', 'href': href, 'note': None, 'todo': None if href else todo}


def case_sections(project):
    """Case-study sections using only copy already stored on the case file."""
    slug = project['slug']
    narrative = project['narrative']
    quote = project['pullQuote']
    live = project.get('link')
    built = project.get('tag') == 'Built'
    links = []
    if live or built:
        links.append({
            'label': 'Live demo',
            'href': live,
            'note': project.get('link_note'),
            'todo': None if live else 'add the live demo link.',
        })
    for extra in project.get('more_links', []):
        if extra['href'] != project.get('doc_link'):
            links.append({'label': extra['label'], 'href': extra['href'], 'note': None, 'todo': None})
    if built:
        links.append({
            'label': 'GitHub',
            'href': None,
            'note': None,
            'todo': 'add the GitHub URL.',
        })

    if slug == 'blinkit-discovery-engine-pehli-baar':
        problem = (
            'Shoppers keep buying from the same few categories on Blinkit. '
            'The fellowship brief asked why, and what stops them exploring new ones.'
        )
        links.append(_doc(project, 'add the fellowship deck link.'))
        return {
            'tldr': [
                {'label': 'Problem', **_text(problem)},
                {'label': 'What I did', **_text(
                    'Built an AI research engine over 4,876 reviews and posts, then turned its main finding into '
                    'Pehli Baar, a concept MVP that protects a first order in a new category.'
                )},
                {'label': 'Result', **_text(
                    'Part of the fellowship work that made me a NextLeap Top Fellow: 223.13 of 300, against a 208.57 cutoff.'
                )},
            ],
            'context': [problem, narrative[1]],
            'research': [
                {'label': 'Sources', **_text('Google Play (3,600 items), Reddit (915) and the App Store (250).')},
                {'label': 'Sample size', **_text('4,876 collected, 3,256 usable, 1,582 with shopping-behavior signal.')},
                {'label': 'Method', **_text(
                    'An LLM pipeline filtered items for shopping-behavior relevance and tagged each with one or more '
                    'of 11 themes: 2,264 labels across 1,582 items.'
                )},
            ],
            'insight': quote,
            'solution': [narrative[2]],
            'not_built': [
                'The first version’s product-matching features: image matching, dupe finding and scene recreation. '
                'The research showed shoppers rarely talk about discovering products, so the MVP leaves them out.',
            ],
            'not_built_todo': None,
            'metrics': [],
            'metrics_figure': None,
            'metrics_todo': "add what you measured, or how you'd measure success.",
            'tradeoffs': [
                'Theme audits so far compare the LLM with a written rubric, not independent human labels, '
                'so they are sanity checks rather than proof.',
                'Review text over-represents complaints, so theme counts overstate dissatisfaction.',
            ],
            'tradeoffs_todo': "add what's next.",
            'links': links,
        }

    if slug == 'spotify-review-analysis-taste-bridge':
        links.append(_doc(project, 'add the graduation deck link.'))
        return {
            'tldr': [
                {'label': 'Problem', **_text(
                    "Users weren't asking for more recommendations — they were stuck in repeat-listening loops."
                )},
                {'label': 'What I did', **_text(
                    'I scraped App Store, Play Store, and Reddit reviews to find the root causes before designing anything. '
                    'Unstick implements that thesis in one session: pick an activity, set a novelty dial, and get a five-track path from familiar to new.'
                )},
                {'label': 'Result', **_text(narrative[3])},
            ],
            'context': [
                "Users weren't asking for more recommendations — they were stuck in repeat-listening loops.",
                narrative[1],
            ],
            'research': [
                {'label': 'Sources', **_text('App Store, Play Store, and Reddit reviews.')},
                {'label': 'Sample size', **_todo('add how many reviews were scraped.')},
                {'label': 'Method', **_text(
                    'I scraped App Store, Play Store, and Reddit reviews to find the root causes before designing anything.'
                )},
            ],
            'insight': quote,
            'solution': [narrative[2], narrative[3]],
            'not_built': [
                'One nudge, one action, under thirty seconds — no full library reset.',
                "Discovery shouldn't reset what people already love — it should bridge from where they already are.",
            ],
            'not_built_todo': None,
            'metrics': [],
            'metrics_figure': None,
            'metrics_todo': "add what you measured, or how you'd measure success.",
            'tradeoffs': [],
            'tradeoffs_todo': "add the trade-offs and what's next.",
            'links': links,
        }

    if slug == 'groww-weekly-review-pulse':
        links.append(_doc(project, 'add the deck or PRD link.'))
        return {
            'tldr': [
                {'label': 'Problem', **_text(
                    "PM teams drown in reviews. The job isn't to read them all — it's to surface what's actually broken."
                )},
                {'label': 'What I did', **_text(
                    'I scraped 1,499 real Groww reviews and built a pipeline that handles Hindi text, emoji-only posts, and one-word ratings.'
                )},
                {'label': 'Result', **_text(narrative[1])},
            ],
            'context': [
                "PM teams drown in reviews. The job isn't to read them all — it's to surface what's actually broken.",
            ],
            'research': [
                {'label': 'Sources', **_text('1,499 real Groww reviews.')},
                {'label': 'Sample size', **_text('1,499')},
                {'label': 'Method', **_text(
                    'I scraped 1,499 real Groww reviews and built a pipeline that handles Hindi text, emoji-only posts, and one-word ratings.'
                )},
            ],
            'insight': quote,
            'solution': [narrative[1]],
            'not_built': [],
            'not_built_todo': 'add what you chose not to build and why.',
            'metrics': [
                project['deck'],
                'Zero manual steps after the initial build.',
            ],
            'metrics_figure': None,
            'metrics_todo': None,
            'tradeoffs': [],
            'tradeoffs_todo': "add the trade-offs and what's next.",
            'links': links,
        }

    if slug == 'hdfc-mf-faq-chatbot':
        links.append(_doc(project, 'add the deck or PRD link.'))
        return {
            'tldr': [
                {'label': 'Problem', **_text(
                    "HDFC MF documentation is dense and hard to navigate — users can't find answers without reading entire PDFs."
                )},
                {'label': 'What I did', **_text(
                    'I chunked and embedded FAQ documents, built a retrieval pipeline, and wrapped it in Streamlit so users can query in plain English.'
                )},
                {'label': 'Result', **_todo('add the result for this case.')},
            ],
            'context': [narrative[0]],
            'research': [
                {'label': 'Sources', **_text('FAQ documents.')},
                {'label': 'Sample size', **_todo('add how many FAQ documents were used.')},
                {'label': 'Method', **_text(
                    'I chunked and embedded FAQ documents, built a retrieval pipeline, and wrapped it in Streamlit so users can query in plain English.'
                )},
            ],
            'insight': quote,
            'solution': [
                'I chunked and embedded FAQ documents, built a retrieval pipeline, and wrapped it in Streamlit so users can query in plain English.',
            ],
            'not_built': [],
            'not_built_todo': 'add what you chose not to build and why.',
            'metrics': [],
            'metrics_figure': None,
            'metrics_todo': "add what you measured, or how you'd measure success.",
            'tradeoffs': [
                "Next iteration: source citations per answer so trust isn't assumed.",
            ],
            'tradeoffs_todo': 'add the trade-offs.',
            'links': links,
        }

    if slug == 'chatgpt-voice-adoption':
        links.append(_doc(project, 'add the PRD link.'))
        return {
            'tldr': [
                {'label': 'Problem', **_text(narrative[0])},
                {'label': 'What I did', **_text(narrative[1])},
                {'label': 'Result', **_todo('add the result for this case.')},
            ],
            'context': [narrative[0]],
            'research': [
                {'label': 'Sources', **_todo('add the research sources.')},
                {'label': 'Sample size', **_todo('add the sample size.')},
                {'label': 'Method', **_todo('add the research method.')},
            ],
            'insight': quote,
            'solution': [narrative[1]],
            'not_built': [],
            'not_built_todo': 'add what you chose not to build and why.',
            'metrics': [narrative[2]],
            'metrics_figure': _figure(project),
            'metrics_todo': None,
            'tradeoffs': [],
            'tradeoffs_todo': "add the trade-offs and what's next.",
            'links': links,
        }

    if slug == 'goodreads-quick-log':
        links.append(_doc(project, 'add the PRD link.'))
        return {
            'tldr': [
                {'label': 'Problem', **_text(narrative[0])},
                {'label': 'What I did', **_text(narrative[1])},
                {'label': 'Result', **_todo('add the result for this case.')},
            ],
            'context': [narrative[0]],
            'research': [
                {'label': 'Sources', **_todo('add the research sources.')},
                {'label': 'Sample size', **_todo('add the sample size.')},
                {'label': 'Method', **_todo('add the research method.')},
            ],
            'insight': quote,
            'solution': [narrative[1]],
            'not_built': [],
            'not_built_todo': 'add what you chose not to build and why.',
            'metrics': [narrative[2]],
            'metrics_figure': _figure(project),
            'metrics_todo': None,
            'tradeoffs': [
                'The counter-metric — review conversion rate — is held flat.',
            ],
            'tradeoffs_todo': "add what's next.",
            'links': links,
        }

    raise KeyError(slug)
