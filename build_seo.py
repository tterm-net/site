#!/usr/bin/env python3
"""
build_seo.py — writes robots.txt and sitemap.xml.

Generated rather than hand-written so the list of pages cannot drift: a page
added and forgotten is a page Google never learns about. Blog posts come from
`updates.md`, every entry with a page of its own, so a new post needs nothing
here.

`lastmod` comes from `updates.md` rather than from the file system, because
the deploy rewrites every file and would otherwise claim the whole site
changed on every push. Search engines discount a site that says that.
"""
from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import sitelib as S  # noqa: E402

ROOT = S.ROOT
SITE = S.SITE

#: Pages worth indexing, besides the posts: how much of the site each one is,
#: its own last change when that is not the newest entry (None: take the
#: entry's date), and the switch it waits for. Each is listed in every
#: language it has a file in: the Terms and the Policy are English only.
#: The donation pages are deliberately absent: they carry a `noindex` tag,
#: since a page of wallet addresses is not what anyone should arrive at from
#: a search.
PAGES = [
    ("/", 1.0, None, None),
    ("/download/", 0.9, None, "mac"),
    ("/blog/", 0.8, None, None),
    ("/terms/", 0.3, "2026-10-16", None),
    ("/privacy/", 0.3, "2026-10-16", None),
]

ROBOTS = f"""# tterm.net

User-agent: *
Allow: /

# Wallet addresses are not a search result anyone wants to land on.
Disallow: /donate/
Disallow: /ru/donate/

Sitemap: {SITE}/sitemap.xml
"""


def entries() -> list[tuple[str, str | None]]:
    """Every entry's date, and the path of its page if it has one, read by
    the blog's own parser: a pinned post is a post too."""
    import build_updates
    found = build_updates.parse((ROOT / "updates.md").read_text(encoding="utf-8"))
    return [(e.date, e.path) for e in found] or [("2026-08-30", None)]


def url(lang, path: str, langs, priority: float, lastmod: str) -> list[str]:
    out = ["  <url>", f"    <loc>{SITE}{S.page_url(lang, path)}</loc>"]
    # Each page points at its other languages. Without this Google treats
    # them as competing pages instead of one page in several languages.
    if len(langs) > 1:
        for other in langs:
            out.append(f'    <xhtml:link rel="alternate" hreflang="{other.code}"'
                       f' href="{SITE}{S.page_url(other, path)}"/>')
        out.append(f'    <xhtml:link rel="alternate" hreflang="x-default"'
                   f' href="{SITE}{S.page_url(S.ENGLISH, path)}"/>')
    out.append(f"    <lastmod>{lastmod}</lastmod>")
    out.append(f"    <priority>{priority}</priority>")
    out.append("  </url>")
    return out


def sitemap() -> tuple[str, int, str]:
    found = entries()
    newest = max(date for date, _ in found)
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"'
           ' xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    count = 0
    pages = [(path, priority, own) for path, priority, own, flag in PAGES
             if flag is None or S.FLAGS[flag]]
    pages += [(path, 0.7, date) for date, path in found if path]
    for path, priority, own in pages:
        langs = S.languages_of(path)
        if not langs:
            S.fail(f"{path} is in the sitemap but has no page.")
        for lang in langs:
            out += url(lang, path, langs, priority, own or newest)
            count += 1
    out.append("</urlset>")
    return "\n".join(out) + "\n", count, newest


def main() -> None:
    text, count, newest = sitemap()
    (ROOT / "robots.txt").write_text(ROBOTS, encoding="utf-8")
    (ROOT / "sitemap.xml").write_text(text, encoding="utf-8")
    print(f"tterm.net — {count} pages, last change {newest}")
    print("  robots.txt")
    print("  sitemap.xml")


if __name__ == "__main__":
    main()
