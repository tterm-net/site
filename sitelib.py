"""
sitelib.py — what the build scripts share.

The languages of the site, their strings, the switches, the version, and the
parts every page has: the links between languages in <head>, the header and
the footer. They live here and in `templates/`, once, so that the header of
every page changes in one file and a new language is a line in LANGUAGES and
a file in `i18n/`.

Templates are plain HTML with a few marks:

    {{key}}               a string of the page's language, from i18n/<code>.txt
    {{json:key}}          the same string escaped for JSON
    {{$name}}             a value the build knows: $base, $home, $version, ...
    {{>header}}           another template, here templates/_header.html
    {{#if mac}}…{{/if}}   a part shown only while a switch is on
    {{#unless mac}}…{{/unless}}

A string may hold marks too, `{{$base}}` in a link most often: the Russian
"/ru/blog/" and the English "/blog/" are one string with `{{$base}}/blog/`.

Every language has every string, or the build stops: a page that quietly
shows English in the middle of a Russian one is the thing this prevents.
"""
from __future__ import annotations

import functools
import html
import json
import pathlib
import re
from dataclasses import dataclass

ROOT = pathlib.Path(__file__).parent
SITE = "https://tterm.net"
TEMPLATES = ROOT / "templates"
I18N = ROOT / "i18n"


@dataclass(frozen=True)
class Language:
    code: str       # as in <html lang> and hreflang: "en", "ru", "pt-BR"
    name: str       # its own name, in the language menu: "English", "Русский"
    short: str      # on the language button: "EN", "RU"
    prefix: str     # the folder its pages live in: "" for English, "ru"
    locale: str     # for og:locale: "en_US", "ru_RU"
    dir: str = "ltr"


#: The languages of the site, in the order of the language menu. English is
#: first: it lives at the root, and search engines are sent to it when they
#: know no better (x-default).
LANGUAGES = [
    Language("en", "English", "EN", "", "en_US"),
    Language("de", "Deutsch", "DE", "de", "de_DE"),
    Language("es", "Español", "ES", "es", "es_ES"),
    Language("fr", "Français", "FR", "fr", "fr_FR"),
    Language("it", "Italiano", "IT", "it", "it_IT"),
    Language("pl", "Polski", "PL", "pl", "pl_PL"),
    Language("pt-BR", "Português", "PT", "pt", "pt_BR"),
    Language("tr", "Türkçe", "TR", "tr", "tr_TR"),
    Language("ru", "Русский", "RU", "ru", "ru_RU"),
    Language("ja", "日本語", "JA", "ja", "ja_JP"),
    Language("ko", "한국어", "KO", "ko", "ko_KR"),
    Language("zh-CN", "简体中文", "ZH", "zh", "zh_CN"),
]
ENGLISH = LANGUAGES[0]

#: Parts of the site that wait for something outside it. Off, a part is not
#: on any page and its pages are not built (an earlier build's are removed).
FLAGS = {
    # tTerm for Mac: the item in the header, the section and the buttons on
    # the main page, the download page. On since 2.6.0, with app 0.5.0. The
    # app is signed with tTerm's own certificate, not an Apple Developer ID,
    # so the download page says how to open it the first time
    # (download.first.*); with a Developer ID and notarization that goes.
    "mac": True,
}

#: Where the download button takes you: the .dmg of the latest release of the
#: app. A stable name in every release keeps this address the same, so the
#: site does not change with each version of the app.
MAC_DOWNLOAD = "https://github.com/tterm-net/tterm-app/releases/latest/download/tTerm.dmg"


def fail(message: str) -> None:
    raise SystemExit(f"  {message}")


def version() -> str:
    return (ROOT / "VERSION").read_text(encoding="utf-8").strip()


def language(code: str) -> Language:
    for lang in LANGUAGES:
        if lang.code == code:
            return lang
    fail(f"no language {code!r}; the site has {', '.join(l.code for l in LANGUAGES)}.")
    raise AssertionError


def base(lang: Language) -> str:
    """What a link to a page of the language starts with: "" or "/ru"."""
    return f"/{lang.prefix}" if lang.prefix else ""


def page_url(lang: Language, path: str) -> str:
    """The address of a page in a language: "/blog/" and Russian give "/ru/blog/"."""
    return base(lang) + path


def page_file(lang: Language, path: str) -> pathlib.Path:
    """The file of a page: "/blog/" in Russian is ru/blog/index.html."""
    folder = ROOT / lang.prefix if lang.prefix else ROOT
    name = path.strip("/")
    if name.endswith(".html"):
        return folder / name
    return (folder / name / "index.html") if name else folder / "index.html"


def language_of(file: pathlib.Path) -> tuple[Language, str]:
    """The language and the path of a page from where its file lies."""
    parts = file.relative_to(ROOT).parts
    lang = ENGLISH
    for other in LANGUAGES[1:]:
        if parts and parts[0] == other.prefix:
            lang, parts = other, parts[1:]
            break
    if parts[-1] == "index.html":
        path = "/" + "/".join(parts[:-1]) + ("/" if len(parts) > 1 else "")
    else:
        path = "/" + "/".join(parts)
    return lang, path


# ------------------------------------------------------------------ strings

LINE = re.compile(r"([a-z0-9][a-z0-9_.-]*) =(?: (.*))?")


def unescape(value: str) -> str:
    """`\\n` is a line break, `\\\\` a backslash; any other backslash is text."""
    return re.sub(r"\\([n\\])", lambda m: "\n" if m.group(1) == "n" else "\\", value)


@functools.lru_cache(maxsize=None)
def strings(code: str) -> dict[str, str]:
    """i18n/<code>.txt: one string a line, `key = text`; `\\n` is a line
    break inside a string, lines starting with # are comments."""
    path = I18N / f"{code}.txt"
    if not path.exists():
        fail(f"i18n/{code}.txt: no strings for {code}.")
    out: dict[str, str] = {}
    for n, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip() or raw.startswith("#"):
            continue
        match = LINE.fullmatch(raw)
        if not match:
            fail(f"i18n/{code}.txt:{n}: expected 'key = text', found {raw[:70]!r}.")
        key, value = match.group(1), match.group(2) or ""
        if key in out:
            fail(f"i18n/{code}.txt:{n}: {key} is there twice.")
        out[key] = unescape(value)
    return out


#: The plural forms each language has, by Unicode CLDR: blog.minutes must
#: have exactly these.
PLURAL_FORMS = {
    "en": {"one", "other"}, "de": {"one", "other"}, "es": {"one", "other"},
    "it": {"one", "other"}, "tr": {"one", "other"}, "fr": {"one", "other"},
    "pt": {"one", "other"}, "ru": {"one", "few", "many"}, "uk": {"one", "few", "many"},
    "pl": {"one", "few", "many"}, "ja": {"other"}, "ko": {"other"}, "zh": {"other"},
}


def attribute_keys() -> set[str]:
    """Strings the templates put inside a tag (content="", aria-label=""):
    there they may hold no markup and no straight quote."""
    keys = set()
    for path in TEMPLATES.glob("**/*.html"):
        for tag in re.findall(r"<[^<>]*\{\{[^<>]*>", path.read_text(encoding="utf-8")):
            keys.update(k for k in re.findall(r"\{\{(?:json:)?([a-z0-9][a-z0-9_.-]*)\}\}", tag))
    return keys


def check_strings() -> None:
    """Every language has the strings English has, and no others, none of
    them empty where English is not; no string has a straight double quote
    in its text, where it would end an attribute halfway (quotes are the
    language's own, “ ”, « », „ “, 「 」); strings that go into a tag hold no
    markup; the months are twelve, the plural forms the language's, the
    pace a number."""
    english = strings(ENGLISH.code)
    in_tags = attribute_keys()
    for lang in LANGUAGES:
        own = strings(lang.code)
        name = f"i18n/{lang.code}.txt"
        missing = [k for k in english if k not in own]
        extra = [k for k in own if k not in english]
        if missing:
            fail(f"{name} lacks {len(missing)} strings: {', '.join(missing[:8])}.")
        if extra:
            fail(f"{name} has strings English does not: {', '.join(extra[:8])}.")
        for key, value in own.items():
            text = re.sub(r"<[^>]*>", "", value)
            if '"' in text:
                fail(f'{name}: {key} has a straight " in its text.')
            if english[key].strip() and not value.strip():
                fail(f"{name}: {key} is empty.")
            if key in in_tags and re.search(r'[<>"]', value):
                fail(f"{name}: {key} goes into a tag, so it can hold no markup and no straight quote.")
        for key in ("date.months", "date.months_heading", "date.months_short"):
            if len(own[key].split(" | ")) != 12:
                fail(f"{name}: {key} must list twelve months, separated by ' | '.")
        forms = set(forms_of(own["blog.minutes"]))
        expected = PLURAL_FORMS.get(lang.code.split("-")[0])
        if expected and forms != expected:
            fail(f"{name}: blog.minutes has the forms {sorted(forms)}, the language has {sorted(expected)}.")
        if not re.fullmatch(r"\d+(?: characters)?", own["blog.pace"]):
            fail(f"{name}: blog.pace is words a minute ('220') or characters a minute ('500 characters').")


def forms_of(spec: str) -> dict[str, str]:
    """"one: {n} min | other: {n} min" as forms; a string with no form names
    is the one form of a language without plurals."""
    if ": " not in spec.split(" | ")[0] or spec.split(" | ")[0].partition(": ")[0] not in (
            "zero", "one", "two", "few", "many", "other"):
        return {"other": spec}
    forms = {}
    for part in spec.split(" | "):
        name, _, text = part.partition(": ")
        forms[name.strip()] = text
    return forms


def choose(spec: str, form: str) -> str:
    """A string with forms, "one: {n} min | other: {n} min", in one form."""
    forms = forms_of(spec)
    if form in forms:
        return forms[form]
    if list(forms) == ["other"]:
        return forms["other"]
    fail(f"the form {form!r} is missing in {spec!r}.")
    raise AssertionError


def plural(code: str, n: int) -> str:
    """The plural form of n in a language, by the rules of Unicode CLDR for
    the languages the site has or plans."""
    lang = code.split("-")[0]
    if lang in ("ja", "zh", "ko"):
        return "other"
    if lang in ("ru", "uk"):
        if n % 10 == 1 and n % 100 != 11:
            return "one"
        if n % 10 in (2, 3, 4) and n % 100 not in (12, 13, 14):
            return "few"
        return "many"
    if lang == "pl":
        if n == 1:
            return "one"
        if n % 10 in (2, 3, 4) and n % 100 not in (12, 13, 14):
            return "few"
        return "many"
    if lang in ("fr", "pt"):
        return "one" if n in (0, 1) else "other"
    return "one" if n == 1 else "other"


# ---------------------------------------------------------------- templates

CONDITION = re.compile(r"\{\{#(if|unless) ([a-z_]+)\}\}((?:(?!\{\{#(?:if|unless) ).)*?)\{\{/\1\}\}", re.S)
MARK = re.compile(r"\{\{([^{}\s]+)\}\}")


@functools.lru_cache(maxsize=None)
def template(name: str) -> str:
    path = TEMPLATES / name
    if not path.exists():
        fail(f"templates/{name}: no such template.")
    return path.read_text(encoding="utf-8")


def render(text: str, lang: Language, ctx: dict, depth: int = 0) -> str:
    if depth > 8:
        fail("templates include each other in a loop.")

    def condition(m: re.Match[str]) -> str:
        kind, flag, body = m.groups()
        if flag not in ctx:
            fail(f"no switch {flag!r}.")
        on = bool(ctx[flag])
        return body if on == (kind == "if") else ""

    while True:
        text, n = CONDITION.subn(condition, text)
        if not n:
            break

    def value(key: str) -> str:
        own = strings(lang.code)
        if key not in own:
            fail(f"{key}: no such string in i18n/{lang.code}.txt.")
        return render(own[key], lang, ctx, depth + 1)

    def mark(m: re.Match[str]) -> str:
        expr = m.group(1)
        if expr.startswith(">"):
            # Editors end a file with a line break; the page does not want it.
            return render(template(f"_{expr[1:]}.html").rstrip("\n"), lang, ctx, depth + 1)
        if expr.startswith("$"):
            if expr[1:] not in ctx:
                fail(f"{expr}: the build has no such value.")
            return str(ctx[expr[1:]])
        if expr.startswith("json:"):
            return json.dumps(html.unescape(value(expr[5:])), ensure_ascii=False)[1:-1]
        return value(expr)

    out = MARK.sub(mark, text)
    if depth == 0 and "{{" in out:
        bad = out[out.index("{{"):][:60].split("\n")[0]
        fail(f"a mark the build does not know is left in the page: {bad!r}.")
    return out


# ------------------------------------------------------------- page context

CHECK = ('<svg class="lang-check" viewBox="0 0 24 24" aria-hidden="true">'
         '<path d="M5 12.5l4.2 4.2L19 7"/></svg>')


def lang_links(lang: Language, path: str, langs: list[Language], indent: str) -> str:
    """The language menu: every language, the page's own marked. A language
    the page is not in leads to its main page."""
    out = []
    for other in LANGUAGES:
        href = page_url(other, path) if other in langs else page_url(other, "/")
        here = ' aria-current="true"' if other == lang else ""
        mark = CHECK if other == lang else ""
        out.append(f'{indent}<a href="{href}" hreflang="{other.code}" lang="{other.code}"{here}>'
                   f'{other.name}{mark}</a>')
    return "\n".join(out)


def links_html(lang: Language, path: str, langs: list[Language]) -> str:
    """<head>: the page's own address and its versions in other languages."""
    out = [f'<link rel="canonical" href="{SITE}{page_url(lang, path)}">']
    if len(langs) > 1:
        for other in LANGUAGES:
            if other in langs:
                out.append(f'<link rel="alternate" hreflang="{other.code}" href="{SITE}{page_url(other, path)}">')
        out.append(f'<link rel="alternate" hreflang="x-default" href="{SITE}{page_url(ENGLISH, path)}">')
    return "\n".join(out)


def locales_html(lang: Language, langs: list[Language]) -> str:
    out = [f'<meta property="og:locale" content="{lang.locale}">']
    for other in LANGUAGES:
        if other in langs and other != lang:
            out.append(f'<meta property="og:locale:alternate" content="{other.locale}">')
    return "\n".join(out)


def languages_of(path: str) -> list[Language]:
    """The languages a page exists in, by its files."""
    return [lang for lang in LANGUAGES if page_file(lang, path).exists()]


def context(lang: Language, path: str, langs: list[Language] | None = None,
            current: str | None = None, **extra) -> dict:
    """What a page's template can use: $base, $home, its links, the switches."""
    langs = LANGUAGES if langs is None else langs
    ctx = {
        "lang": lang.code,
        "dir": lang.dir,
        "short": lang.short,
        "own": lang.name,
        "base": base(lang),
        "home": page_url(lang, "/"),
        "version": version(),
        "url": page_url(lang, path),
        "canonical": SITE + page_url(lang, path),
        "links": links_html(lang, path, langs),
        "locales": locales_html(lang, langs),
        "lang_links": lang_links(lang, path, langs, "          "),
        "lang_links_row": lang_links(lang, path, langs, "              "),
        "lang_links_foot": lang_links(lang, path, langs, "          "),
        "cur_blog": ' aria-current="page"' if current == "blog" else "",
        "cur_download": ' aria-current="page"' if current == "download" else "",
        "mac_download": MAC_DOWNLOAD,
    }
    ctx.update(FLAGS)
    ctx.update(extra)
    return ctx


# -------------------------------------------------------- hand-written pages

def shell_text(file: pathlib.Path, text: str, current: str | None = None,
               alternates: bool = False) -> str:
    """A page written by hand with the header, the footer and the version of
    every page; a post also with its links to its other languages."""
    lang, path = language_of(file)
    langs = languages_of(path)
    ctx = context(lang, path, langs=langs, current=current)

    def swap(pattern: str, new: str, label: str) -> None:
        nonlocal text
        text, n = re.subn(pattern, lambda m: new, text, count=1, flags=re.S)
        if n != 1:
            fail(f"{file.relative_to(ROOT)}: no {label} to replace.")

    swap(r'<header class="top">.*?</header>', render("{{>header}}", lang, ctx), "header")
    swap(r'<footer class="foot">.*?</footer>', render("{{>footer}}", lang, ctx), "footer")
    swap(r'<meta name="version" content="[^"]*">', f'<meta name="version" content="{version()}">', "version")
    swap(r'<a class="skip" href="#main">[^<]*</a>', render('<a class="skip" href="#main">{{shell.skip}}</a>', lang, ctx), "skip link")
    if alternates:
        swap(r'<link rel="canonical" href="[^"]*">(?:\n<link rel="alternate" hreflang="[^"]*" href="[^"]*">)*',
             ctx["links"], "links to other languages")
        swap(r'<meta property="og:locale" content="[^"]*">(?:\n<meta property="og:locale:alternate" content="[^"]*">)*',
             ctx["locales"], "og:locale")
    return text


def fill_shell(file: pathlib.Path, current: str | None = None, alternates: bool = False) -> None:
    file.write_text(shell_text(file, file.read_text(encoding="utf-8"), current, alternates), encoding="utf-8")
