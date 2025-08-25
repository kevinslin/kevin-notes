from dataclasses import dataclass
import markdown2
from markdown2 import UnicodeWithAttrs
import os
import pathlib
import sys
import time
from datetime import datetime, timezone
from typing import List
from urllib.parse import urlencode

import frontmatter
import httpx
import sqlite_utils
from sqlite_utils.db import NotFoundError,  COLUMN_TYPE_MAPPING

sys.path.append(".")
COLUMN_TYPE_MAPPING.update({UnicodeWithAttrs: "TEXT"})
# from dendron_sdk.client import DendronClient
# from dendron_sdk.environment import FernApiEnvironment
from pathlib import Path
import feedparser
import hashlib
import re


root = pathlib.Path(__file__).parent.resolve()
# DENDRON_CLIENT = DendronClient(environment=FernApiEnvironment.LOCAL)
GITHUB_BASE_URL = "https://github.com/kevinslin/kevinweblog"

# === Types

@dataclass
class Note:
    filepath: Path
    metadata: dict
    content: str
    title: str
    body: str
    id: str
    htag: str
    topic: str
    created: str
    updated: str
    path: str
    slug: str
    url: str
    tags: List[str]
    path_slug: str

    @staticmethod
    def get_note(filepath: str):
        filepath = Path(filepath)
        fp = filepath.open()
        metadata, content = frontmatter.parse(fp.read().strip())
        title = metadata["title"]
        body = content
        id = metadata["id"]
        htag = metadata.get("htag", "none")
        topic = metadata.get("topic", "none")
        tags = metadata.get("tags", [])
        created = datetime.fromtimestamp(metadata["created"] / 1000).isoformat()
        updated = datetime.fromtimestamp(metadata["updated"] / 1000).isoformat()
        path = str(filepath.relative_to(root))
        slug = filepath.stem
        url = f"{GITHUB_BASE_URL}/blob/main/{path}"
        path_slug = path.replace("/", "_")
        return Note(
            filepath=filepath,
            metadata=metadata,
            content=content,
            title=title,
            body=body,
            id=id,
            htag=htag,
            topic=topic,
            created=created,
            updated=updated,
            path=path,
            slug=slug,
            url=url,
            tags=tags,
            path_slug=path_slug
        )


#

def render_md(body, path, record):
    # Convert markdown to HTML using markdown2
    html: str = markdown2.markdown(body, extras=["fenced-code-blocks", "tables"]) 

    # The rendered HTML is stored in the record
    record["html"] = html
    print("Rendered HTML for {}".format(path))


def _slugify(text: str) -> str:
    text = (text or "").strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "post"


def _parse_feed_datetime(entry) -> str:
    struct_time = entry.get("published_parsed") or entry.get("updated_parsed")
    if struct_time:
        try:
            ts = time.mktime(struct_time)
            return datetime.fromtimestamp(ts).isoformat()
        except Exception:
            pass
    return datetime.now(timezone.utc).isoformat()


def build_database(repo_path):
    db = sqlite_utils.Database(repo_path / "notes.db")
    table = db.table("note", pk="path")
    seen = []
    for filepath in root.glob("dendron/**/*.md"):
        print(filepath)
        note = Note.get_note(filepath)
        seen.append(note.id)
        try:
            row = table.get(note.path_slug)
            previous_body = row["body"]
            previous_html = row["html"]
        except (NotFoundError, KeyError):
            previous_body = None
            previous_html = None
        record = {
            "id": note.id,
            "path": note.path_slug,
            "slug": note.slug,
            "topic": note.topic,
            "htag": note.htag,
            "title": note.title,
            "url": note.url,
            "body": note.body,
            "tags": note.tags,
            "created_utc": note.created,
            "created": note.created,
            "updated_utc": note.updated,
            "updated": note.updated,
        }
        if (note.body != previous_body) or not previous_html:
            render_md(note.body, note.path, record)
            # response = DENDRON_CLIENT.markdown_render(request={"content": note.body})
            # record["html"] = response.content
            # print("Rendered HTML for {}".format(note.path))
        with db.conn:
            table.upsert(record, alter=True)

    # Build newsletter posts from RSS into the same table with topic=newsletter
    FEED_URL = "https://thetortoiseandhare.substack.com/feed.xml"
    parsed = feedparser.parse(FEED_URL)
    for e in parsed.entries:
        link = e.get("link", "")
        raw_id = e.get("id") or link or e.get("title", "")
        digest = hashlib.sha1(raw_id.encode("utf-8")).hexdigest()
        entry_id = f"newsletter-{digest[:16]}"
        created_iso = _parse_feed_datetime(e)
        title = e.get("title", "")
        slug = _slugify(title)
        path_slug = f"newsletter_{slug}_{digest[:8]}"
        # Prefer content HTML, fallback to summary
        html_content = e.get("description", "")
        # if e.get("content"):
        #     try:
        #         html_content = e["content"][0].get("value", "")
        #     except Exception:
        #         html_content = ""
        # if not html_content:
        #     html_content = e.get("summary", "")
        record = {
            "id": entry_id,
            "path": path_slug,
            "slug": slug,
            "topic": "newsletter",
            "htag": "none",
            "title": title,
            "url": link,
            "body": html_content,
            "tags": [],
            "created_utc": created_iso,
            "created": created_iso,
            "updated_utc": created_iso,
            "updated": created_iso,
        }
        seen.append(entry_id)
        try:
            row = table.get(path_slug)
            previous_body = row.get("body")
            previous_html = row.get("html")
        except NotFoundError:
            previous_body = None
            previous_html = None
        if (record["body"] != previous_body) or not previous_html:
            render_md(record["body"], path_slug, record)
        with db.conn:
            table.upsert(record, alter=True)

    delete_removed_notes(db, seen)
    table.enable_fts(
        ["title", "body"], tokenize="porter", create_triggers=True, replace=True
    )

def delete_removed_notes(db: sqlite_utils.Database, seen: List[str]):
    seen_clean = [f"'{x}'" for x in seen]
    sql = f'delete from note where id not in ({",".join(seen_clean)})'
    cursor = db.execute(sql)
    db.conn.commit()
    print("Deleted {} notes".format(cursor.rowcount))


if __name__ == "__main__":
    print("building database...")
    build_database(root)
