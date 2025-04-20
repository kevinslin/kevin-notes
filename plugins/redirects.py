from datasette import hookimpl
from datasette.utils.asgi import Response


@hookimpl
def register_routes():
    print("register_routes")
    return (
        (
            r"^/note/note/(?P<topic>[^_]+)_(?P<slug>[^\.]+)\.md$",
            lambda request: Response.redirect(
                "/{topic}/{slug}".format(**request.url_vars), status=301
            ),
        ),
        ("^/note/feed.atom$", lambda: Response.redirect("/notes/feed.atom", status=301)),
        (
            "^/note$",
            lambda request: Response.redirect(
                "/notes"
                + (("?" + request.query_string) if request.query_string else ""),
                status=301,
            ),
        ),
        (
            "^/note/search$",
            lambda request: Response.redirect(
                "/notes/search"
                + (("?" + request.query_string) if request.query_string else ""),
                status=301,
            ),
        ),
    )
