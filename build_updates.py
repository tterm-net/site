#!/usr/bin/env python3
"""
build_updates.py — builds the blog from `updates.md`.

`updates.md` is the only place an entry is written. This script puts it
everywhere it shows, in every language of the site:

  - the blog block on the main page (`/`, `/ru/`): the newest post with a
    page of its own, or the one pinned, and the three newest other entries
    beside it;
  - the blog page (`/blog/`, `/ru/blog/`): that post on top, then every
    other entry, month by month;
  - on each post's page (`/blog/<post>/`): its date and reading time under
    the title, its structured data for search engines, and "more from the
    blog" at the bottom.

Each of these sits in its page between two comments, `<!-- updates:NAME -->`
and `<!-- /updates:NAME -->`. Editing what is between them by hand is
pointless: the next run overwrites it. The posts themselves are written by
hand, one page per language; their date lives here and nowhere else.

An entry needs a title and text in every language or the build stops: written
twice by hand, two lists drift apart within a month and nothing says which
one is right.

The words around the entries ("Read the post", the months, "4 min read")
are strings of each language, in `i18n/` beside the rest of the site.

The file is not served: it lives in the repository for its history, not for
visitors.
"""
from __future__ import annotations

import html
import json
import re
import sys
from dataclasses import dataclass, field

sys.dont_write_bytecode = True

import sitelib as S  # noqa: E402

ROOT = S.ROOT
SOURCE = ROOT / "updates.md"
LANGS = tuple(lang.code for lang in S.LANGUAGES)

#: What an entry is about; each reads on the page as blog.tag.<name>.
TAGS = ("web", "bot", "site")


def word(lang: str, key: str) -> str:
    """A string of the blog in a language: blog.read, date.long, ..."""
    return S.strings(lang)[key]


def listed(lang: str, key: str) -> list[str]:
    """A string that is a list, "January | February | ...", as a list."""
    return word(lang, key).split(" | ")

#: The picture on a post's card: the product itself, drawn in markup like
#: the demo on the main page, so it stays sharp and weighs nothing.
COVER = """<div class="cover" aria-hidden="true">
        <div class="cover-window">
          <div class="cover-bar"><i></i><i></i><i></i><span>app.tterm.net</span></div>
          <div class="cover-tabs"><span class="on"><b class="dot"></b><span><em>P/</em>web-01</span></span><span><b class="dot"></b><span><em>A/</em>api-prod</span></span></div>
          <div class="cover-feed">
            <p class="cover-meta"><b class="dot"></b>~/app<span>main</span><span class="cover-time">1.4 s</span></p>
            <p class="cover-cmd"><em>&#x276F;</em> git pull</p>
            <p>Updating 3f2c1a9..8d4e7b2</p>
            <p>Fast-forward</p>
            <p> src/server.ts | 12 <ins>+++++++</ins><del>-----</del></p>
            <p class="cover-meta cover-gap"><b class="dot busy"></b>~/app<span>main</span><span class="cover-time">running</span></p>
            <p class="cover-cmd"><em>&#x276F;</em> npm run build</p>
            <p>vite v7.1.4 building for production...</p>
            <p class="cover-ok">&#x2713; 412 modules transformed.</p>
          </div>
        </div>
      </div>"""


@dataclass
class Entry:
    date: str                   # ISO, as written in the file
    tag: str                    # a key of TAGS
    path: str | None            # "/blog/x/" when the entry has a page
    pinned: bool = False        # leads the blog whatever came after it
    title: dict[str, str] = field(default_factory=dict)
    text: dict[str, str] = field(default_factory=dict)
    minutes: dict[str, int] = field(default_factory=dict)


def fail(message: str) -> None:
    raise SystemExit(f"  {message}")


#: Chinese and Japanese, which put no spaces between words.
CJK = "\u3000-\u303f\u3040-\u30ff\u3400-\u9fff\uf900-\ufaff\uff00-\uffef"


def joined(lines: list[str]) -> str:
    """Lines of an entry as one paragraph. A line break is a space, except
    between two characters of Chinese or Japanese; runs of spaces become one.
    Only plain spaces and tabs count: the no-break space French puts before
    : ; ? ! stays."""
    out = ""
    for line in lines:
        line = re.sub(r"[ \t]+", " ", line).strip(" \t")
        if not line:
            continue
        if out and not (re.match(f"[{CJK}]", out[-1]) and re.match(f"[{CJK}]", line[0])):
            out += " "
        out += line
    return out


def parse(source: str) -> list[Entry]:
    """Reads the update file.

    Deliberately hand-rolled: the format has to stay editable by someone who
    is adding a release note, not maintaining a parser. Comment lines start
    with `#`, an entry with `## date tag [path [pinned]]`, a language with
    `@en Title`.
    """
    entries: list[Entry] = []
    lang: str | None = None
    buffer: list[str] = []

    def flush() -> None:
        if entries and lang and buffer:
            entries[-1].text[lang] = joined(buffer)
        buffer.clear()

    for raw in source.splitlines():
        line = raw.rstrip()
        if line.startswith("#") and not line.startswith("##"):
            continue
        if line.startswith("## "):
            flush()
            lang = None
            parts = line[3:].split()
            if len(parts) not in (2, 3, 4):
                fail(f"'{line}': expected '## date tag', '## date tag /path/' "
                     f"or '## date tag /path/ pinned'.")
            date, tag = parts[0], parts[1]
            path = parts[2] if len(parts) >= 3 else None
            if len(parts) == 4 and parts[3] != "pinned":
                fail(f"'{line}': after the path only 'pinned' may follow.")
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
                fail(f"'{line}': the date must be written as 2026-10-07.")
            if tag not in TAGS:
                fail(f"{date}: tag '{tag}' is none of {', '.join(TAGS)}.")
            if path and not re.fullmatch(r"/blog/[a-z0-9-]+/", path):
                fail(f"{date}: a page path looks like /blog/name/, not {path}.")
            entries.append(Entry(date=date, tag=tag, path=path,
                                 pinned=len(parts) == 4))
            continue
        if line.startswith("@"):
            flush()
            code, _, title = line[1:].partition(" ")
            lang = code.strip()
            if lang not in LANGS:
                fail(f"'{line}': no such language, expected one of {LANGS}.")
            if not entries:
                fail(f"'{line}': a language before the first entry.")
            entries[-1].title[lang] = joined([title])
            continue
        if lang:
            buffer.append(line)
    flush()

    seen: set[str] = set()
    for entry in entries:
        if entry.date in seen:
            fail(f"{entry.date}: two entries on one date. The date is the "
                 f"entry's address on the blog page, so it has to be unique.")
        seen.add(entry.date)
        for lang in LANGS:
            if not entry.title.get(lang) or not entry.text.get(lang):
                fail(f"{entry.date}: no title or text for {lang}. Every entry "
                     f"needs all languages, or one page quietly falls behind: "
                     f"the thing this file exists to prevent.")
    if [e.date for e in entries] != sorted((e.date for e in entries), reverse=True):
        fail("entries must go newest first.")
    if sum(e.pinned for e in entries) > 1:
        fail("only one entry may be pinned: the blog has one place on top.")
    return entries


# ------------------------------------------------------------------ helpers


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def page_file(path: str, lang: str):
    return S.page_file(S.language(lang), path)


def url(entry: Entry, lang: str) -> str:
    language = S.language(lang)
    if entry.path:
        return S.page_url(language, entry.path)
    return S.page_url(language, f"/blog/#{entry.date}")


def ymd(iso: str) -> tuple[int, int, int]:
    year, month, day = (int(x) for x in iso.split("-"))
    return year, month, day


def date_text(pattern: str, iso: str, lang: str) -> str:
    """A date by a pattern of the language: "{d} {month} {y}" and the like.
    `month` is the month after a day ("7 октября", the genitive), `month_heading`
    a month on its own ("Октябрь 2026"), `month_short` the short one. The
    first of a month is date.day_one: "1er" in French, "1º" in Portuguese."""
    y, m, d = ymd(iso)
    values = {"{y}": str(y), "{d}": word(lang, "date.day_one") if d == 1 else str(d),
              "{month}": listed(lang, "date.months")[m - 1],
              "{month_short}": listed(lang, "date.months_short")[m - 1],
              "{month_heading}": listed(lang, "date.months_heading")[m - 1]}
    out = word(lang, pattern)
    for mark, value in values.items():
        out = out.replace(mark, value)
    return out


def long_date(iso: str, lang: str, year: bool = True) -> str:
    return date_text("date.long" if year else "date.long_noyear", iso, lang)


def short_date(iso: str, lang: str) -> str:
    return date_text("date.short", iso, lang)


def month_name(iso: str, lang: str) -> str:
    return date_text("date.heading", iso, lang)


def minutes_label(n: int, lang: str) -> str:
    """"4 min read", in the plural form the language takes for n."""
    return S.choose(word(lang, "blog.minutes"), S.plural(lang, n)).replace("{n}", str(n))


def first_sentence(text: str) -> str:
    """The opening sentence, for a short card: up to the first full stop
    after a word of two letters or more (so "z. B." and "e.g." do not end
    it) that is followed by a word that starts a sentence: with a letter
    that is not lower case (a capital, or a letter of a script without
    case, as Korean) or as tTerm does, perhaps after an opening quote or ¿;
    or up to a full stop of Chinese or Japanese, which needs no space after
    it. A question inside a sentence, as in "asked Continue? (Y/n), there
    was", does not end it."""
    for match in re.finditer(r"(\w{2,}|\))[.!?](?=\s+[«„“‘¿¡]*(\w)(\w?))|[。！？](?=.)", text):
        nxt, then = match.group(2), match.group(3)
        if nxt is None or (nxt.isalpha() and (not nxt.islower() or then.isupper())):
            return text[: match.end()]
    return text


def reading_time(entry: Entry, pages: dict | None = None) -> None:
    """Minutes to read a post, counted from its page: the words inside
    <article class="post">, tags and what this script writes into it (the
    date, the minutes) left out. `pages` holds pages not written yet, by
    file: the build counts what it is about to write."""
    for lang in LANGS:
        page = page_file(entry.path, lang)
        if pages is not None and page in pages:
            source = pages[page]
        elif page.exists():
            source = page.read_text(encoding="utf-8")
        else:
            fail(f"{entry.date}: {entry.path} has no page {page.relative_to(ROOT)}.")
        source = re.sub(r"<!-- updates:([a-z]+) -->.*?<!-- /updates:\1 -->", "", source, flags=re.S)
        found = re.search(r'<article class="post(?: [^"]*)?">(.*?)</article>', source, re.S)
        if not found:
            fail(f"{page.relative_to(ROOT)}: no <article class=\"post\"> to count.")
        text = html.unescape(re.sub(r"<[^>]+>", " ", found.group(1)))
        # Chinese and Japanese have no spaces: their pace is in characters,
        # and a word in Latin letters among them (a name, a command) counts
        # as one.
        pace, unit = word(lang, "blog.pace").partition(" ")[::2]
        if unit == "characters":
            count = (len(re.findall(r"[\u3040-\u30ff\u3400-\u9fff\uf900-\ufaff]", text))
                     + len(re.findall(r"\w+", re.sub(f"[{CJK}]", " ", text))))
        else:
            count = len(re.findall(r"\w+", text))
        entry.minutes[lang] = max(1, round(count / int(pace)))


def tag_html(entry: Entry, lang: str) -> str:
    return f'<span class="tag tag-{entry.tag}">{esc(word(lang, "blog.tag." + entry.tag))}</span>'


PIN = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 4h6l-1 6 4 4H6l4-4-1-6z"/>'
       '<path d="M12 14v6"/></svg>')


def pin_html(entry: Entry, lang: str) -> str:
    """On the post that leads the blog while newer ones follow it."""
    return f'<span class="pin">{PIN}{word(lang, "blog.pinned")}</span>' if entry.pinned else ""


def meta_html(entry: Entry, lang: str, pin: bool = False) -> str:
    parts = [f'<time datetime="{entry.date}">{long_date(entry.date, lang)}</time>']
    if entry.path:
        parts.append(f"<span>{minutes_label(entry.minutes[lang], lang)}</span>")
    return (f'<p class="post-meta">{pin_html(entry, lang) if pin else ""}{tag_html(entry, lang)}'
            + '<span class="sep" aria-hidden="true">·</span>'.join(parts) + "</p>")


def mini_html(entry: Entry, lang: str, card: bool = False) -> str:
    """A short card: date and tag, title, the opening sentence."""
    klass = "post-mini post-mini-card" if card else "post-mini"
    return (
        f'<a class="{klass}" href="{url(entry, lang)}">\n'
        f'        <span class="post-mini-meta"><time datetime="{entry.date}">'
        f'{short_date(entry.date, lang)}</time> · {esc(word(lang, "blog.tag." + entry.tag))}</span>\n'
        f'        <span class="post-mini-title">{esc(entry.title[lang])}</span>\n'
        f'        <span class="post-mini-text">{esc(first_sentence(entry.text[lang]))}</span>\n'
        f'      </a>'
    )


# ------------------------------------------------------------------ regions


def featured_of(entries: list[Entry]) -> Entry | None:
    """The post on top: the one pinned, or else the newest with a page."""
    return (next((e for e in entries if e.pinned), None)
            or next((e for e in entries if e.path), None))


def render_main(entries: list[Entry], lang: str) -> str:
    """The main page: the post on top, three other entries."""
    top = featured_of(entries)
    short = [e for e in entries if e is not top][:3]
    out = ['<div class="blog-grid">']
    if top:
        out.append(
            f'  <a class="post-feature" href="{url(top, lang)}">\n'
            f'      {COVER}\n'
            f'      <div class="post-feature-body">\n'
            f'        {meta_html(top, lang, pin=True)}\n'
            f'        <h3 class="post-feature-title">{esc(top.title[lang])}</h3>\n'
            f'        <p class="post-feature-lead">{esc(top.text[lang])}</p>\n'
            f'      </div>\n'
            f'    </a>')
    out.append('  <div class="post-stack">')
    out.extend(f"      {mini_html(e, lang)}" for e in short)
    out.append("  </div>")
    out.append("</div>")
    return "\n".join(out)


def render_featured(entries: list[Entry], lang: str) -> str:
    """The blog page: the post on top, large."""
    top = featured_of(entries)
    if not top:
        return ""
    return (
        f'<a class="post-hero" href="{url(top, lang)}">\n'
        f'      <div class="post-hero-cover">\n'
        f'      {COVER}\n'
        f'      </div>\n'
        f'      <div class="post-hero-body">\n'
        f'        {meta_html(top, lang, pin=True)}\n'
        f'        <h2 class="post-hero-title">{esc(top.title[lang])}</h2>\n'
        f'        <p class="post-hero-lead">{esc(top.text[lang])}</p>\n'
        f'        <span class="btn btn-primary">{word(lang, "blog.read")}</span>\n'
        f'      </div>\n'
        f'    </a>'
    )


def render_list(entries: list[Entry], lang: str) -> str:
    """The blog page: every other entry, month by month, in full."""
    top = featured_of(entries)
    rest = [e for e in entries if e is not top]
    older = top is None or all(e.date < top.date for e in rest)
    out = [f'<h2 class="list-title">{word(lang, "blog.earlier" if older else "blog.more")}</h2>',
           '    <div class="timeline">']
    months: dict[str, list[Entry]] = {}
    for entry in rest:
        months.setdefault(entry.date[:7], []).append(entry)
    for group in months.values():
        out.append('      <section class="month">')
        out.append(f'        <h3 class="month-name">{month_name(group[0].date, lang)}</h3>')
        out.append('        <div class="month-entries">')
        for entry in group:
            title = esc(entry.title[lang])
            if entry.path:
                title = f'<a href="{url(entry, lang)}">{title}</a>'
            out.append(f'          <article class="entry" id="{entry.date}">')
            out.append(f'            <p class="entry-meta"><time datetime="{entry.date}">'
                       f'{long_date(entry.date, lang, year=False)}</time>{tag_html(entry, lang)}</p>')
            out.append(f'            <h4 class="entry-title">{title}</h4>')
            out.append(f'            <p class="entry-text">{esc(entry.text[lang])}</p>')
            if entry.path:
                out.append(f'            <p class="entry-more"><a href="{url(entry, lang)}">'
                           f'{word(lang, "blog.read")}</a></p>')
            out.append("          </article>")
        out.append("        </div>")
        out.append("      </section>")
    out.append("    </div>")
    return "\n".join(out)


def render_more(entries: list[Entry], lang: str, path: str) -> str:
    """Under a post: the three newest other entries."""
    others = [e for e in entries if e.path != path][:3]
    out = ['<div class="more-grid">']
    out.extend(f"      {mini_html(e, lang, card=True)}" for e in others)
    out.append("    </div>")
    return "\n".join(out)


def entry_at(entries: list[Entry], path: str) -> Entry:
    for entry in entries:
        if entry.path == path:
            return entry
    fail(f"{path} has a page but no entry in updates.md.")
    raise AssertionError


def render_ld(entry: Entry, lang: str) -> str:
    """A post's structured data, so a search engine knows its date."""
    data = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": entry.title[lang],
        "description": entry.text[lang],
        "datePublished": entry.date,
        "inLanguage": lang,
        "url": f"https://tterm.net{url(entry, lang)}",
        "image": "https://tterm.net/assets/og-cloud.png",
        "author": {"@type": "Organization", "name": "tTerm", "url": "https://tterm.net"},
        "publisher": {"@type": "Organization", "name": "tTerm",
                      "logo": {"@type": "ImageObject",
                               "url": "https://tterm.net/assets/logo.svg"}},
    }
    body = json.dumps(data, ensure_ascii=False, indent=2).replace("</", "<\\/")
    return f'<script type="application/ld+json">\n{body}\n</script>'


# ------------------------------------------------------------------- pages


def language_of(page) -> str:
    return S.language_of(page)[0].code


def post_path_of(page) -> str:
    return S.language_of(page)[1]


def same_as_post(entry: Entry) -> None:
    """A post's preview title and description (post.<name>.og_title and
    .description in i18n/) are its entry's title and text, in every
    language: change one, change the other."""
    name = entry.path.strip("/").split("/")[-1]
    for lang in LANGS:
        own = S.strings(lang)
        for part, key, what in ((entry.title, "og_title", "title"), (entry.text, "description", "text")):
            value = own.get(f"post.{name}.{key}")
            if value is None:
                fail(f"{entry.date}: i18n/{lang}.txt has no post.{name}.{key}.")
            if html.unescape(value) != part[lang]:
                fail(f"{entry.date}: the {what} for {lang} in updates.md is not post.{name}.{key} "
                     f"in i18n/{lang}.txt; the two must be the same.")


def load(pages: dict | None = None) -> list[Entry]:
    """The entries, checked, with the reading time of every post."""
    entries = parse(SOURCE.read_text(encoding="utf-8"))
    for entry in entries:
        if entry.path:
            same_as_post(entry)
            reading_time(entry, pages)
    return entries


def fill(text: str, page, entries: list[Entry]) -> str:
    """A page with its blog blocks written in."""
    lang = language_of(page)

    def block(match: re.Match[str]) -> str:
        name = match.group(1)
        if name == "main":
            body = render_main(entries, lang)
        elif name == "featured":
            body = render_featured(entries, lang)
        elif name == "list":
            body = render_list(entries, lang)
        elif name == "more":
            body = render_more(entries, lang, post_path_of(page))
        elif name == "meta":
            body = meta_html(entry_at(entries, post_path_of(page)), lang)
        elif name == "ld":
            body = render_ld(entry_at(entries, post_path_of(page)), lang)
        else:
            fail(f"{page.relative_to(ROOT)}: unknown block '{name}'.")
        return f"<!-- updates:{name} -->\n    {body}\n    <!-- /updates:{name} -->"

    return re.sub(r"<!-- updates:([a-z]+) -->.*?<!-- /updates:\1 -->", block, text, flags=re.S)


#: Folders of the repository that hold no pages of the site.
NOT_PAGES = {".git", "node_modules", "templates", "i18n", "tools", "preview", ".wrangler"}


def site_pages() -> list:
    return sorted(p for p in ROOT.rglob("index.html")
                  if p.relative_to(ROOT).parts[0] not in NOT_PAGES)


def main() -> None:
    entries = load()
    posts = sum(1 for e in entries if e.path)
    print(f"tterm.net — {len(entries)} blog entries, {posts} with a page")
    for page in site_pages():
        text = page.read_text(encoding="utf-8")
        if "<!-- updates:" not in text:
            continue
        page.write_text(fill(text, page, entries), encoding="utf-8")
        print(f"  {page.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
