from datetime import timezone, datetime
import httpx
import git
import os
import pathlib
from urllib.parse import urlencode
import sqlite_utils
from sqlite_utils.db import NotFoundError
import time
import frontmatter
import sys

import sys

sys.path.append(".")
from dendron_sdk.client import DendronClient
from dendron_sdk.environment import FernApiEnvironment


root = pathlib.Path(__file__).parent.resolve()
DENDRON_CLIENT = DendronClient(environment=FernApiEnvironment.LOCAL)


def build_database(repo_path):
    db = sqlite_utils.Database(repo_path / "tils.db")
    table = db.table("til", pk="path")
    for filepath in root.glob("dendron/**/*.md"):
        print(filepath)
        fp = filepath.open()
        metadata, content = frontmatter.parse(fp.read().strip())
        title = metadata["title"]
        body = content
        id = metadata["id"]
        htag = metadata.get("htag", "none")
        topic = htag.rsplit(".", 1)[-1]
        created = datetime.fromtimestamp(metadata["created"] / 1000).isoformat()
        updated = datetime.fromtimestamp(metadata["updated"] / 1000).isoformat()
        path = str(filepath.relative_to(root))
        slug = filepath.stem
        # TODO: update
        url = "https://github.com/simonw/til/blob/main/{}".format(path)
        # Do we need to render the markdown?
        path_slug = path.replace("/", "_")
        try:
            row = table.get(path_slug)
            previous_body = row["body"]
            previous_html = row["html"]
        except (NotFoundError, KeyError):
            previous_body = None
            previous_html = None
        record = {
            "id": id,
            "path": path_slug,
            "slug": slug,
            "topic": topic,
            "htag": htag,
            "title": title,
            "url": url,
            "body": body,
            # TODO
            "created_utc": created,
            "created": created,
            "updated_utc": updated,
            "updated": updated,
        }
        # TODO: use dendron version
        if (body != previous_body) or not previous_html:
<<<<<<< HEAD
            retries = 0
            response = None
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
        record.update(all_times[path])
=======
            response = DENDRON_CLIENT.markdown_render(request={"content": body})
            record["html"] = response.content
            print("Rendered HTML for {}".format(path))
>>>>>>> kevin
        with db.conn:
            table.upsert(record, alter=True)

    table.enable_fts(
        ["title", "body"], tokenize="porter", create_triggers=True, replace=True
    )


if __name__ == "__main__":
    print("building database...")
    build_database(root)
