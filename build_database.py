from dataclasses import dataclass
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
from sqlite_utils.db import NotFoundError

sys.path.append(".")
from dendron_sdk.client import DendronClient
from dendron_sdk.environment import FernApiEnvironment
from pathlib import Path


root = pathlib.Path(__file__).parent.resolve()
DENDRON_CLIENT = DendronClient(environment=FernApiEnvironment.LOCAL)
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
        tags = metadata.get("tags", [])
        topic = htag
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
    retries = 0
    while retries < 3:
        headers = {}
        if os.environ.get("MARKDOWN_GITHUB_TOKEN"):
            headers = {
                "authorization": "Bearer {}".format(
                    os.environ["MARKDOWN_GITHUB_TOKEN"]
                )
            }
        response = httpx.post(
            "https://api.github.com/markdown",
            json={
                # mode=gfm would expand #13 issue links and suchlike
                "mode": "markdown",
                "text": body,
            },
            headers=headers,
        )
        if response.status_code == 200:
            record["html"] = response.text
            print("Rendered HTML for {}".format(path))
            break
        elif response.status_code == 401:
            assert False, "401 Unauthorized error rendering markdown"
        else:
            print(response.status_code, response.headers)
            print("  sleeping 60s")
            time.sleep(60)
            retries += 1
    else:
        assert False, "Could not render {} - last response was {}".format(
            path, response.headers
        )

def build_database(repo_path):
    db = sqlite_utils.Database(repo_path / "notes.db")
    table = db.table("note", pk="path")
    seen = []
    for filepath in root.glob("dendron/**/*.md"):
        print(filepath)
        note = Note.get_note(filepath)
        seen.append(id)

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


    delete_removed_notes(db, seen)
    table.enable_fts(
        ["title", "body"], tokenize="porter", create_triggers=True, replace=True
    )

def delete_removed_notes(db: sqlite_utils.Database, seen: List[str]):
    seen_clean = [f"'{x}'" for x in seen]
    sql = f'delete from note where id not in ({",".join(seen_clean)})'
    print(sql)
    cursor = db.execute(sql)
    db.conn.commit()
    print("Deleted {} notes".format(cursor.rowcount))


if __name__ == "__main__":
    print("building database...")
    build_database(root)
