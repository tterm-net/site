#!/usr/bin/env python3
"""
build_site.py — builds the site.

The pages written once for every language come from `templates/` and the
strings in `i18n/`: the main page, the blog page and its posts, the 404 page
and, while tTerm for Mac is switched on, the download page. The pages written
by hand (the Terms, the Policy, the donation pages) get the header, the
footer and the version every page has. Then the blog is filled in from
`updates.md` (build_updates.py) and the sitemap written (build_seo.py).

    python3 build_site.py

What it writes is committed like any other page: nothing is built on
Cloudflare, and every page still works with no script at all.
"""
from __future__ import annotations

import sys

# The build scripts import each other; this keeps __pycache__ out of the
# repository and off the site.
sys.dont_write_bytecode = True

import build_seo  # noqa: E402
import build_updates  # noqa: E402
import sitelib as S  # noqa: E402

#: The pages built from templates: the template, the page's path, the item of
#: the header it belongs to, and the switch it waits for.
PAGES = [
    ("index.html", "/", None, None),
    ("blog.html", "/blog/", "blog", None),
    ("404.html", "/404.html", None, None),
    ("download.html", "/download/", "download", "mac"),
]


def posts() -> list:
    """The posts of the blog, one for each entry of updates.md with a page:
    the template of /blog/<name>/ is templates/blog/<name>.html, its strings
    post.<name>.* in i18n/."""
    entries = build_updates.parse(build_updates.SOURCE.read_text(encoding="utf-8"))
    return [(f"blog/{e.path.strip('/').split('/')[-1]}.html", e.path, "blog", None)
            for e in entries if e.path]


def render_page(name: str, path: str, current: str | None, lang) -> str:
    # The 404 page answers for any address: its language menu leads to the
    # main pages.
    langs = [] if path == "/404.html" else S.LANGUAGES
    ctx = S.context(lang, path, langs=langs, current=current)
    return S.render(S.template(name), lang, ctx)


def dry_run() -> None:
    """Every template with every switch on, thrown away: a mistake in a part
    that is switched off stops the build now, not on the day it is switched
    on."""
    saved = dict(S.FLAGS), S.MAC_DOWNLOAD
    try:
        S.FLAGS.update({k: True for k in S.FLAGS})
        S.MAC_DOWNLOAD = "https://example.invalid/tTerm.dmg"
        for name, path, current, _ in PAGES + posts():
            for lang in S.LANGUAGES:
                render_page(name, path, current, lang)
    finally:
        S.FLAGS.clear()
        S.FLAGS.update(saved[0])
        S.MAC_DOWNLOAD = saved[1]


def build() -> tuple[dict, list]:
    """Every page in memory, and the files of pages switched off."""
    pages, gone = {}, []
    for name, path, current, flag in PAGES + posts():
        for lang in S.LANGUAGES:
            out = S.page_file(lang, path)
            if flag and not S.FLAGS[flag]:
                gone.append(out)
                continue
            if flag == "mac" and not S.MAC_DOWNLOAD:
                S.fail("tTerm for Mac is on but MAC_DOWNLOAD in sitelib.py is empty: "
                       "the download button would lead nowhere.")
            pages[out] = render_page(name, path, current, lang)
    for file in sorted(S.ROOT.rglob("*.html")):
        if file.relative_to(S.ROOT).parts[0] in build_updates.NOT_PAGES or file in pages or file in gone:
            continue
        text = file.read_text(encoding="utf-8")
        if '<header class="top">' not in text:
            # Not a page of the site (a search engine's verification file):
            # served as it is.
            continue
        pages[file] = S.shell_text(file, text)
    entries = build_updates.load(pages)
    for file, text in pages.items():
        if "<!-- updates:" in text:
            pages[file] = build_updates.fill(text, file, entries)
    return pages, gone


def main() -> None:
    S.check_strings()
    print(f"tterm.net {S.version()}: {', '.join(l.code for l in S.LANGUAGES)}; "
          + ", ".join(f"{k} {'on' if v else 'off'}" for k, v in S.FLAGS.items()))
    dry_run()
    pages, gone = build()
    # Nothing failed: now the files.
    for file in gone:
        if file.exists():
            file.unlink()
            print(f"  removed {file.relative_to(S.ROOT)}: switched off")
    for file, text in sorted(pages.items()):
        file.parent.mkdir(parents=True, exist_ok=True)
        if not file.exists() or file.read_text(encoding="utf-8") != text:
            file.write_text(text, encoding="utf-8")
            print(f"  {file.relative_to(S.ROOT)}")
    print(f"  {len(pages)} pages")
    build_seo.main()


if __name__ == "__main__":
    main()
