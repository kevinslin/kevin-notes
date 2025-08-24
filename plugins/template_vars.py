from datasette import hookimpl
from bs4 import BeautifulSoup as Soup
import html
import re
import time
from datetime import datetime
import feedparser

non_alphanumeric = re.compile(r"[^a-zA-Z0-9\s]")
multi_spaces = re.compile(r"\s+")


def SITE_ROOT():
  return "http://localhost:8001"
  #return "https://notes.kevinslin.com"

# --- Utilities ---

def first_paragraph(html):
    soup = Soup(html, "html.parser")
    paragraphs = soup.find_all("p")
    for p in paragraphs:
        # Skip paragraphs that only contain images
        if p.find("img") and len(p.contents) == 1:
            continue
        return str(p)
    return ""


def noteURLSlugWithTopic(note):
    return f"{note['topic']}-{note['slug']}-{note['id']}"


def noteURLPath(note):
    return f"/pages/{noteURLSlugWithTopic(note)}"


def highlight(s):
    s = html.escape(s)
    s = s.replace("b4de2a49c8", "<strong>").replace("8c94a2ed4b", "</strong>")
    return s

# --- Newsletter feed cached fetcher ---

_FEED_URL = "https://thetortoiseandhare.substack.com/feed.xml"
_FEED_CACHE = None
_FEED_CACHE_TS = 0.0
_FEED_CACHE_TTL_SECONDS = 60 * 10  # 10 minutes


def _parse_feed_datetime(entry):
    struct_time = entry.get("published_parsed") or entry.get("updated_parsed")
    if struct_time:
        try:
            ts = time.mktime(struct_time)
            return datetime.fromtimestamp(ts).isoformat()
        except Exception:
            return ""
    return ""


def newsletter_entries(limit=5):
    global _FEED_CACHE, _FEED_CACHE_TS
    now = time.time()
    if _FEED_CACHE is None or (now - _FEED_CACHE_TS) > _FEED_CACHE_TTL_SECONDS:
        parsed = feedparser.parse(_FEED_URL)
        items = []
        for e in parsed.entries:
            html_content = ""
            if e.get("content"):
                try:
                    html_content = e["content"][0].get("value", "")
                except Exception:
                    html_content = ""
            if not html_content:
                html_content = e.get("summary", "")
            items.append({
                "title": e.get("title", ""),
                "url": e.get("link", ""),
                "created": _parse_feed_datetime(e),
                "html": html_content,
                "topic": "newsletter",
            })
        _FEED_CACHE = items
        _FEED_CACHE_TS = now
    return _FEED_CACHE[:limit]


@hookimpl
def extra_template_vars(request, datasette):
    async def related_tils(note):
        text = note["title"] + " " + note["body"]
        text = non_alphanumeric.sub(" ", text)
        text = multi_spaces.sub(" ", text)
        words = list(set(text.lower().strip().split()))
        sql = """
        select
          note.id, note.topic, note.slug, note.title, note.created
        from
          note
          join note_fts on note.rowid = note_fts.rowid
        where
          note_fts match :words
          and not (
            note.slug = :slug
            and note.topic = :topic
          )
        order by
          note_fts.rank
        limit
          5
        """
        result = await datasette.get_database().execute(
            sql,
            {"words": " OR ".join(words), "slug": note["slug"], "topic": note["topic"]},
        )
        return result.rows

    return {
        "q": request.args.get("q", ""),
        "highlight": highlight,
        "first_paragraph": first_paragraph,
        "related_tils": related_tils,
        "noteURLPath": noteURLPath,
        "noteURLSlugWithTopic": noteURLSlugWithTopic,
        "SITE_ROOT": SITE_ROOT,
        "newsletter_entries": newsletter_entries,
    }


@hookimpl
def prepare_connection(conn):
    conn.create_function("first_paragraph", 1, first_paragraph)
