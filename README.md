# tterm.net

**Version 2.5.0.** The number lives in `VERSION`; the build puts it in a
`<meta>` tag and the footer of every page, so you can tell what is deployed
by viewing source.

The site of [tTerm](https://github.com/tterm-net): tTerm Web, a terminal in
your browser for all your servers and computers, and the Telegram bot it
grew out of.

Static HTML and CSS with one small script, `assets/site.js`. Nothing is built
on Cloudflare: the scripts below run on your machine, and what they write is
committed like any other page.

## Building

```bash
python3 build_site.py
```

One command builds everything: the pages from `templates/` in every
language, the header and the footer of the pages written by hand, the blog
from `updates.md` and the sitemap. It needs Python 3 and nothing else, and
it stops with a line saying what is wrong when a string, a page or an entry
is missing. Every page is made in memory first and the files are written
only when all of them came out, so a failed build leaves the site as it was.
Run it after any change and commit what it writes; a second run changes
nothing.

## Local preview

```bash
python3 -m http.server 4000 --bind 127.0.0.1
```

Then open <http://localhost:4000>. The pages link with absolute paths
(`/style.css`, `/ru/blog/`), so open them through the server, not as files.
`--bind` keeps the server to this machine: without it the folder is open to
the whole network, and macOS asks whether to let Python accept connections.

## Releasing

Bump `VERSION` and run `build_site.py`: every page then carries the new
number, in its `<meta name="version">` and its footer. The donation pages
take it when `build_donate.py` runs. One version, one set of files: the same
rule as the bot, never ship two different things under one number.

## Pages

`/` is the main page, in English; every other language has the same pages
in a folder of its own (`/ru/`, `/de/blog/`; see Languages). The main page's
first screen is the product itself: a live demo of tTerm Web, drawn by
`assets/site.js`.

`/blog/` is the blog: what we shipped and what changed. A post with a page of
its own lives at `/blog/<name>/`.

`/download/` is tTerm for Mac, the local terminal: what it is, how it fits
with the cloud, how to install it, and the button that downloads it. Built
only while tTerm for Mac is switched on (see below).

`/404.html` and the `404.html` of each language's folder answer for any
address that is not there: Cloudflare serves the nearest one.

`/terms/` and `/privacy/` hold the Terms of Service and the Privacy Policy, in
English only: one binding text, linked from the sign-up box of tTerm Web and
from every footer. They are written by hand, laid out like Todoist's: a list
of sections at the top, numbered clauses with a bold label, no tables.

`/donate/` and `/ru/donate/` hold the donation addresses for the bot, in
English and Russian only. Since
2.0.0 the site does not link to them; they stay for links from the bot and
from earlier posts. `build_donate.py` writes both from one template. The
addresses live in that script and nowhere else, so the two languages cannot
drift apart.

`build_qr.py` regenerates the QR codes in `assets/`. It parses every file as
XML before writing it: an earlier version painted the modules by adding a
second `fill` attribute beside the one the library emits, which browsers
reject outright and show as a broken image.

Every page has the same header and footer, `templates/_header.html` and
`templates/_footer.html`, written out into each page by the build: a page
must work without any script. The header: Features, Security and Pricing on
the main page, Resources (the blog, the questions, the Telegram channel, the
code) and, while it is switched on, the local terminal. The buttons are only
Sign in and Start for free. The footer: the name and one line on what tTerm
is, three columns of links (Product, Resources, Legal), the year, the version
and the language. On a narrow screen the header's links fold into a
`<details>` menu; Resources and the language button are `<details>` too. All
open without a script, `site.js` only closes them after a tap, on Escape or
when another opens, and leaves the menu open while the language opens inside
it.

The header shows its links above 1240px, and at 1241px, with the local
terminal, its line has about 25px to spare in French and Russian, the
longest: a new item goes in only after measuring it in every language of
the site.

## Templates and strings

The pages written once for every language live in `templates/`: the main
page (`index.html`), the blog page (`blog.html`), the posts
(`blog/<name>.html`), the 404 page and the download page. Their words are in
`i18n/<language>.txt`, one string a line:

```
index.hero.4 = Start for free
```

Every language has every string of English, or the build stops. A string can
hold markup, and `{{$base}}` in a link: the language's folder, "" in English
and "/ru" in Russian. A string that goes into an attribute (a title, a
description) holds neither markup nor a straight quote, and `\n` in a string
is a line break. In a template, `{{key}}` is a string, `{{$name}}` a value
of the build, `{{>name}}` the template `_name.html`, and `{{#if mac}}…{{/if}}`
a part shown while a switch is on (sitelib.py has the full list).

The Terms, the Policy and the donation pages are written by hand; the build
only writes their header, footer and version.

## tTerm for Mac

A switch, `FLAGS["mac"]` in `sitelib.py`, with `MAC_DOWNLOAD` beside it: the
address of the .dmg. Off, nothing about the app is on the site and
`/download/` is not built. On, the header gets the local terminal, the main
page a second button on the first screen, a section about the app after the
features, lines in the steps, security, pricing and questions, and a button
in its last block; `/download/` is built in every language, and the
footer lists tTerm for Mac. Switch it on with the first release signed with
Developer ID and notarized, the link going to that release's dmg. With the
switch on and no link, the build stops. While it is off, every build still
makes the switched-off parts and throws them away: a typo there stops the
build today, not on the day of the release.

## The demo

`assets/site.js` draws tTerm Web at work into every `[data-demo]` element:
the sidebar with projects in their colors, machines with their terminals and
notes in folders, tabs, blocks of output, the input line, a note with a
checklist being ticked off, the Cmd+K palette. The interface is in English, as in
the product. The terminal starts with a few commands behind it, so the window
is full from the first frame. It stands still until half of it is on screen,
then plays, and pauses again once it leaves the screen or the tab is hidden.
Visitors who asked their system for less motion get one still frame.

The first screen of the main page ends about a third of the way into the
demo on any window: the text above it takes the height that is left, within
limits (`.hero-text` in `style.css`).

On the main page the demo stands on a stage, `[data-stage]`: it leans back,
its top edge away from you, and stands up as the page scrolls. `site.js` sets
`--e` from 0 to 1 by the scroll position and `style.css` turns it into the
tilt, 20° on a computer, 16° on a tablet and 12° on a phone. With less motion
asked for, the window is upright from the start; without the script it stays
leaning, which still reads as a picture.

A post can show tTerm Web standing still, as the post on the license does:
the demo's own markup written out in the page, in a `.demo-still` without
`data-demo`, so `site.js` leaves it as it is. What its terminal prints is
what the commands print, checked in a real clone. Leading spaces of a line
sit in `.dm-indent`, which a narrow screen drops so the line fits whole.

Behind the first screen is the sky, `.sky`: the amber of the brand in the
middle and the colors of projects in tTerm around it, drifting slowly, with
grain on top so the gradients do not band. Further down the page the same
colors glow quieter behind features, security, teams and pricing. Cards carry
a hairline of light and a long soft shadow, and with a mouse a warm light
follows the pointer across features and steps.

## Search engines

`build_seo.py` writes `robots.txt` and `sitemap.xml`, and `build_site.py`
runs it. Posts are taken from `updates.md`, the pinned one too, so a new post
needs nothing there; a new page written by hand needs its line in `PAGES` in
`build_seo.py`, or it will not be in the sitemap and Google will not hear
about it.

`lastmod` comes from `updates.md`, not from file times: the deploy rewrites
every file, and a site claiming everything changed on every push gets
discounted.

`assets/og-cloud.png` is the preview card shown when a link is shared: the
designer's `assets/og.png` with the line under the name changed from
"Terminal in Telegram" to "The cloud terminal", in JetBrains Mono at the size
and color of the original, the picture moved to keep it centered. Keep
`og.png` as it is, never regenerate or replace it by accident: an earlier
archive overwrote it three times with a placeholder. `og-web.png`, the card
with "Terminal in your browser" from 2.1.0 to 2.3.0, stays for previews that
still point at it. A new card gets a new file name: Telegram, Slack and the
rest keep a picture they have seen under its address. After a change, ask
@WebpageBot in Telegram to refresh the links.

No page's `og:title` carries the name: a preview already shows it above,
from `og:site_name`. The main pages' preview title is the headline, the
blog's is "Blog: what's new", a post's is its title alone. The `<title>`
keeps the name ("tTerm: …", "… · tTerm blog"), since a browser tab has
nothing else to say whose page it is.

The donation pages carry `noindex` and are excluded in `robots.txt`: a page of
wallet addresses is not what anyone should arrive at from a search.

## Deploy

Pushing to `main` publishes the site. Cloudflare builds it as a Worker that
serves static assets; `wrangler.jsonc` says which directory to serve and
`.assetsignore` keeps the build scripts and notes out of it.

## Fonts

Manrope and JetBrains Mono are served from `assets/fonts`, not from Google
Fonts: the Privacy Policy says the pages load nothing from third parties, and
a font request hands the visitor's address to whoever serves it. The files
are the variable fontsource builds tterm-web uses, with their OFL licenses
beside them. Chinese, Japanese and Korean take the rest of their letters
from the system's fonts, chosen by the page's language (`:lang()` in
`style.css`): Manrope has none of them, and a web font for them weighs
megabytes.

## Languages

Twelve since 2.5.0: English at `/`, then Deutsch `/de/`, Español `/es/`,
Français `/fr/`, Italiano `/it/`, Polski `/pl/`, Português (Brasil) `/pt/`,
Türkçe `/tr/`, Русский `/ru/`, 日本語 `/ja/`, 한국어 `/ko/` and 简体中文 `/zh/`,
every page under them in that language. Each is a line in `LANGUAGES` in
`sitelib.py`, in the order of the language menu, and a file in `i18n/`; the
path of a page is the same in every language (`/de/download/`). A new one is
a copy of `i18n/en.txt` translated, its line, and its title and text in
every entry of `updates.md`. The copy is written for the language, not word
for word: a string is a whole sentence or paragraph, and it may say a thing
differently.

Beyond the copy, a language has its own forms: `blog.minutes` takes its
plural forms (Unicode CLDR), dates follow its patterns (`date.*`, with
`date.day_one` for the first of a month: "1er" in French), and `blog.pace` is
set so a post takes as many minutes as in English, from the words of all
posts in the language against the English at 220 (Chinese and Japanese
count characters).

The language menu is the same in the header, the footer and the phone menu:
a list, so it takes any number of languages. A page that is not in a
language leads to that language's main page: the Terms and the Policy are in
English only, one binding text.

## The blog

`updates.md` is the only place an entry is written. `build_updates.py` puts it
everywhere it shows: the block on every main page, the list on every blog
page, and on each post's page its date, reading time and "more from the
blog". Those parts sit between `<!-- updates:NAME -->` comments, and editing
them by hand is pointless: the next run overwrites them. The reading time
counts the post's own text, not those parts.

An entry starts with its date and what it is about (`web`, `bot` or `site`),
then a title and text in every language (the words around them, "Read the
post", the months, "4 min read", are strings in `i18n/`, under `blog.` and
`date.`):

```
## 2026-10-07 bot

@en Independent windows on a computer
Terminal windows on a computer with the agent are now independent...

@ru Независимые окна на компьютере
Окна на компьютере с агентом теперь независимы...

@de ...
```

An entry with a page of its own adds the page's path after the tag
(`## 2026-10-18 web /blog/tterm-web/`); its text is then the post's lead, and
the post itself is a template, `templates/blog/<name>.html`, with its strings
`post.<name>.*` in every language: its `title` ends in " · tTerm blog" in the
language's words, and its `og_title` and `description` are the entry's
title and text (the build stops when they differ). The newest such post leads the blog. The date
lives in `updates.md` only: change it there and run the script.

To keep a post on top while newer entries come out, write `pinned` after its
path (`## 2026-10-18 web /blog/tterm-web/ pinned`). It then leads the blog
page and the block on every main page with a "Pinned" mark, and the newer
entries follow it. One entry at most can be pinned; take the word off to let
the newest post lead again.

An entry needs a title and text in every language or the build stops. That is
the whole point of the file: written by hand in each language, the lists
drift apart within a month and nothing says which one is right.

One entry per release worth telling about, not per version. Five versions can
be one entry: a reader does not need three attempts at the same fix.

After changing `updates.md`, build the site (`build_site.py` runs both
`build_updates.py` and `build_seo.py`):

```bash
python3 build_site.py
```

Posting to [@tTermBlog](https://t.me/tTermBlog) stays manual. Deciding what is
worth telling is a judgement call, and a script would post everything.

## License

AGPL-3.0, like the rest of tTerm. The pages say so in their footer since
1.8.1, and `LICENSE` holds the text since 2.3.3: the same file, byte for
byte, as in the other repositories, the copyright holder on its first line.
It stays in the repository: `.assetsignore` keeps it off the site.
