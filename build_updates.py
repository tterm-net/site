#!/usr/bin/env python3
"""
build_updates.py — rewrites the update list on both pages from `updates.md`.

The text used to be written twice, once per language page. It stayed in step
only because both were edited in the same minute; a month of that and the two
lists say different things, with no way to tell which is right.

Now `updates.md` is the only place an entry exists, and this script puts it on
both pages. Editing a page's update list by hand is pointless — the next run
overwrites it.

The file is not served: it lives in the repository for its history, not for
visitors.
"""
from __future__ import annotations

import html
import pathlib
import re
import textwrap
from dataclasses import dataclass

ROOT = pathlib.Path(__file__).parent
SOURCE = ROOT / "updates.md"

PAGES = {
    "en": ROOT / "index.html",
    "ru": ROOT / "ru" / "index.html",
}

#: Month names for the date shown on each page. English abbreviations are the
#: standard three letters; Russian ones are what a Russian reader expects to
#: see, not a transliteration of the English.
MONTHS = {
    "en": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
           "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "ru": ["янв", "фев", "мар", "апр", "мая", "июн",
           "июл", "авг", "сен", "окт", "ноя", "дек"],
}


@dataclass
class Entry:
    date: str                 # ISO, as written in the file
    text: dict[str, str]      # language -> paragraph


def parse(source: str) -> list[Entry]:
    """Reads the update file.

    Deliberately hand-rolled: the format has to stay editable by someone who
    is adding a release note, not maintaining a parser. Comment lines start
    with `#`, an entry with `## date`, a language with `@en` or `@ru`.
    """
    entries: list[Entry] = []
    lang: str | None = None
    buffer: list[str] = []

    def flush() -> None:
        if entries and lang and buffer:
            entries[-1].text[lang] = " ".join(
                " ".join(buffer).split()          # collapse the wrapping
            )
        buffer.clear()

    for raw in source.splitlines():
        line = raw.rstrip()
        if line.startswith("#") and not line.startswith("##"):
            continue
        if line.startswith("## "):
            flush()
            lang = None
            entries.append(Entry(date=line[3:].strip(), text={}))
            continue
        if line.startswith("@"):
            flush()
            lang = line[1:].strip()
            continue
        if lang:
            buffer.append(line)
    flush()

    for entry in entries:
        missing = set(PAGES) - set(entry.text)
        if missing:
            raise SystemExit(
                f"  {entry.date}: no text for {', '.join(sorted(missing))}.\n"
                f"  Every entry needs all languages, or one page quietly falls "
                f"behind — which is the thing this file exists to prevent."
            )
    return entries


def human_date(iso: str, lang: str) -> str:
    year, month, day = iso.split("-")
    return f"{int(day)} {MONTHS[lang][int(month) - 1]} {year}"


def render(entries: list[Entry], lang: str) -> str:
    out = []
    for entry in entries:
        body = textwrap.fill(html.escape(entry.text[lang]), width=72,
                             initial_indent=" " * 10, subsequent_indent=" " * 10)
        out.append(
            f'      <li>\n'
            f'        <time datetime="{entry.date}">'
            f'{human_date(entry.date, lang)}</time>\n'
            f'        <p>\n{body}\n        </p>\n'
            f'      </li>'
        )
    return "\n".join(out)


def main() -> None:
    entries = parse(SOURCE.read_text(encoding="utf-8"))
    print(f"tterm.net — {len(entries)} updates")

    for lang, page in PAGES.items():
        text = page.read_text(encoding="utf-8")
        new, count = re.subn(
            r'(<ul class="updates">\n).*?(\n    </ul>)',
            lambda m: m.group(1) + render(entries, lang) + m.group(2),
            text, count=1, flags=re.S,
        )
        if not count:
            raise SystemExit(f"  {page.name}: no update list found to replace")
        page.write_text(new, encoding="utf-8")
        print(f"  {page.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
