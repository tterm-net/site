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

import pathlib
import re

ROOT = pathlib.Path(__file__).parent
SITE = "https://tterm.net"

#: Pages worth indexing, besides the posts: how much of the site each one is,
#: whether it has a version in the other language, and its own last change
#: when that is not the newest entry (None: take the entry's date).
#: The donation pages are deliberately absent: they carry a `noindex` tag,
#: since a page of wallet addresses is not what anyone should arrive at from
#: a search. The Terms and the Policy are English only.
PAGES = [
    ("/", 1.0, True, None),
    ("/blog/", 0.8, True, None),
    ("/terms/", 0.3, False, "2026-10-16"),
    ("/privacy/", 0.3, False, "2026-10-16"),
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
    """Every entry's date, and the path of its page if it has one."""
    text = (ROOT / "updates.md").read_text(encoding="utf-8")
    return re.findall(r"^## (\d{4}-\d{2}-\d{2}) \w+(?: (/blog/[a-z0-9-]+/))?\s*$",
                      text, re.M) or [("2026-08-30", "")]


def url(path: str, priority: float, bilingual: bool, lastmod: str) -> list[str]:
    out = ["  <url>", f"    <loc>{SITE}{path}</loc>"]
    # Each page points at the other language. Without this Google treats
    # them as two competing pages instead of one page in two languages.
    if bilingual:
        en = path[3:] if path.startswith("/ru/") else path
        for lang, other in (("en", en), ("ru", "/ru" + en)):
            out.append(f'    <xhtml:link rel="alternate" hreflang="{lang}"'
                       f' href="{SITE}{other}"/>')
        out.append(f'    <xhtml:link rel="alternate" hreflang="x-default"'
                   f' href="{SITE}{en}"/>')
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
    for path, priority, bilingual, own in PAGES:
        variants = [path, "/ru" + path] if bilingual else [path]
        for variant in variants:
            out += url(variant, priority, bilingual, own or newest)
            count += 1
    for date, path in found:
        if path:
            for variant in (path, "/ru" + path):
                out += url(variant, 0.7, True, date)
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
