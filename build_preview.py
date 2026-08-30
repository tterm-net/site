#!/usr/bin/env python3
"""
build_preview.py — one self-contained file for review.

The site itself is two pages with a shared stylesheet, as it should be. But
a reviewer looking at a single downloaded file cannot follow a link to its
sibling, and should not have to start a web server to read a landing page.

So this writes one file holding both languages, with the stylesheet and the
logo inlined and the language switch wired to swap them in place. It exists
to be looked at — never edit it, edit the pages.
"""
from __future__ import annotations

import base64
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
VERSION = (ROOT / "VERSION").read_text().strip()
OUT = ROOT / "preview"

#: The switch runs on radio buttons and labels, not on a script. Review tools
#: often open a file in a sandbox where scripts never execute, and a language
#: switch that silently does nothing is worse than none at all.
SWITCH_CSS = """
.pv-radio { position: absolute; opacity: 0; pointer-events: none; }
.pv-page { display: none; }

/* Sibling rules for the plain case. */
#pv-ru:checked ~ .pv-page-ru { display: block; }
#pv-en:checked ~ .pv-page-en { display: block; }

/* And the same through :has, which survives a viewer that wraps the body
   in a container of its own and breaks the sibling relationship. */
body:has(#pv-ru:checked) .pv-page-ru { display: block; }
body:has(#pv-en:checked) .pv-page-en { display: block; }
body:has(#pv-en:checked) .pv-page-ru { display: none; }

.lang-menu label { cursor: pointer; }

.pv-divider {
  max-width: 62rem;
  margin: 3rem auto 0;
  padding: .5rem 1.5rem;
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: #5a6068;
  border-top: 1px dashed #2b3038;
}
"""


def body_of(html: str) -> str:
    start = html.index("<div class=\"glow\"")
    end = html.rindex("</body>")
    return html[start:end]


def build() -> None:
    css = (ROOT / "style.css").read_text(encoding="utf-8")
    logo = base64.b64encode((ROOT / "assets" / "logo.svg").read_bytes()).decode()
    logo_url = f"data:image/svg+xml;base64,{logo}"

    # The support page is stitched under the landing page so a reviewer sees
    # both without a server. On the real site they are separate URLs.
    pages = {}
    for lang, paths in (("en", (ROOT / "index.html", ROOT / "donate" / "index.html")),
                        ("ru", (ROOT / "ru" / "index.html",
                                ROOT / "ru" / "donate" / "index.html"))):
        body = ""
        for n, path in enumerate(paths):
            part = body_of(path.read_text(encoding="utf-8"))
            if n:
                # The donate page carries its own body class for tighter
                # spacing; the preview keeps only body contents, so the class
                # is re-applied on a wrapper or the page comes out airy.
                part = ('<div class="pv-divider">donate page</div>'
                        '<div class="donate">' + part + "</div>")
            body += part
        body = re.sub(r"(?:\.\./)*assets/logo\.svg", logo_url, body)
        for net in ("trc20", "erc20"):
            qr = base64.b64encode(
                (ROOT / "assets" / f"qr-{net}.svg").read_bytes()).decode()
            # Both depths, because the support pages sit one level apart.
            for prefix in ("../..", ".."):
                body = body.replace(f"{prefix}/assets/qr-{net}.svg",
                                    f"data:image/svg+xml;base64,{qr}")
        body = body.replace(
            '<a href="/ru/" hreflang="ru" lang="ru">Русский</a>',
            '<label for="pv-ru" lang="ru">Русский</label>')
        body = body.replace(
            '<a href="/" hreflang="en" lang="en">English</a>',
            '<label for="pv-en" lang="en">English</label>')
        pages[lang] = body

    out = (
        '<!DOCTYPE html>\n<html lang="ru">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f'<title>tTerm {VERSION} — preview</title>\n'
        '<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;800'
        '&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">\n'
        f'<style>\n{css}\n{SWITCH_CSS}\n</style>\n</head>\n<body>\n'
        '<input class="pv-radio" type="radio" name="pv-lang" id="pv-ru" checked>\n'
        '<input class="pv-radio" type="radio" name="pv-lang" id="pv-en">\n'
        f'<div class="pv-page pv-page-ru">{pages["ru"]}</div>\n'
        f'<div class="pv-page pv-page-en">{pages["en"]}</div>\n'
        '</body>\n</html>\n'
    )

    OUT.mkdir(exist_ok=True)
    target = OUT / f"tterm-site-v{VERSION}-preview.html"
    for old in OUT.glob("*.html"):
        old.unlink()
    target.write_text(out, encoding="utf-8")
    print(f"  {target.relative_to(ROOT)}  ({len(out) // 1024} KB)")


if __name__ == "__main__":
    print(f"tterm.net {VERSION} — preview")
    build()
