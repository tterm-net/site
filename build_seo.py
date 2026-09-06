#!/usr/bin/env python3
"""
build_seo.py — writes robots.txt and sitemap.xml.

Generated rather than hand-written so the list of pages cannot drift: a page
added and forgotten is a page Google never learns about.

`lastmod` comes from the newest entry in `updates.md` rather than from the file
system, because the deploy rewrites every file and would otherwise claim the
whole site changed on every push. Search engines discount a site that says that.
"""
from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).parent
SITE = "https://tterm.net"

#: Pages worth indexing, with how much of the site each one is.
#: The donation pages are deliberately absent: they carry a `noindex` tag,
#: since a page of wallet addresses is not what anyone should arrive at from
#: a search.
PAGES = [
    ("/", 1.0),
    ("/ru/", 1.0),
]

ROBOTS = f"""# tterm.net

User-agent: *
Allow: /

# Wallet addresses are not a search result anyone wants to land on.
Disallow: /donate/
Disallow: /ru/donate/

Sitemap: {SITE}/sitemap.xml
"""


def newest_update() -> str:
    """The date of the latest entry, as the site's own last-modified."""
    text = (ROOT / "updates.md").read_text(encoding="utf-8")
    dates = re.findall(r"^## (\d{4}-\d{2}-\d{2})", text, re.M)
    return max(dates) if dates else "2026-08-30"


def sitemap(lastmod: str) -> str:
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"'
           ' xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for path, priority in PAGES:
        out.append("  <url>")
        out.append(f"    <loc>{SITE}{path}</loc>")
        # Each page points at the other language. Without this Google treats
        # them as two competing pages instead of one page in two languages.
        for lang, other in (("en", "/"), ("ru", "/ru/")):
            out.append(f'    <xhtml:link rel="alternate" hreflang="{lang}"'
                       f' href="{SITE}{other}"/>')
        out.append(f'    <xhtml:link rel="alternate" hreflang="x-default"'
                   f' href="{SITE}/"/>')
        out.append(f"    <lastmod>{lastmod}</lastmod>")
        out.append(f"    <priority>{priority}</priority>")
        out.append("  </url>")
    out.append("</urlset>")
    return "\n".join(out) + "\n"


def main() -> None:
    lastmod = newest_update()
    (ROOT / "robots.txt").write_text(ROBOTS, encoding="utf-8")
    (ROOT / "sitemap.xml").write_text(sitemap(lastmod), encoding="utf-8")
    print(f"tterm.net — {len(PAGES)} pages, last change {lastmod}")
    print("  robots.txt")
    print("  sitemap.xml")


if __name__ == "__main__":
    main()
