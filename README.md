# tterm.net

**Version 2.1.0.** The number lives in `VERSION` and in a `<meta>` tag on
each page, so you can tell what is deployed by viewing source.

The site of [tTerm](https://github.com/tterm-net): tTerm Web, a terminal in
your browser for all your servers and computers, and the Telegram bot it
grew out of.

Static HTML and CSS with one small script, `assets/site.js`. Nothing is built
on Cloudflare: the scripts below run on your machine, and what they write is
committed like any other page.

## Local preview

```bash
python3 -m http.server 4000 --bind 127.0.0.1
```

Then open <http://localhost:4000>. The pages link with absolute paths
(`/style.css`, `/ru/blog/`), so open them through the server, not as files.
`--bind` keeps the server to this machine: without it the folder is open to
the whole network, and macOS asks whether to let Python accept connections.

## Releasing

Bump `VERSION`, the `<meta name="version">` tag and the number in the footer
on every page in the same commit: the two main pages, the two blog pages, the
posts, the Terms, the Policy and the 404 page. The donation pages take it
from `VERSION` when `build_donate.py` runs. One version, one set of files:
the same rule as the bot, never ship two different things under one number.

## Pages

`/` and `/ru/` are the main page. Its first screen is the product itself: a
live demo of tTerm Web, drawn by `assets/site.js`.

`/blog/` and `/ru/blog/` are the blog: what we shipped and what changed. A
post with a page of its own lives at `/blog/<name>/` and `/ru/blog/<name>/`.

`/terms/` and `/privacy/` hold the Terms of Service and the Privacy Policy, in
English only: one binding text, linked from the sign-up box of tTerm Web and
from every footer. They are written by hand, laid out like Todoist's: a list
of sections at the top, numbered clauses with a bold label, no tables.

`/donate/` and `/ru/donate/` hold the donation addresses for the bot. Since
2.0.0 the site does not link to them; they stay for links from the bot and
from earlier posts. `build_donate.py` writes both from one template. The
addresses live in that script and nowhere else, so the two languages cannot
drift apart.

`build_qr.py` regenerates the QR codes in `assets/`. It parses every file as
XML before writing it: an earlier version painted the modules by adding a
second `fill` attribute beside the one the library emits, which browsers
reject outright and show as a broken image.

Every page has the same header and footer, written out in each file: a page
must work without any script. On a narrow screen the header's links fold into
a `<details>` menu, and the language button is a `<details>` too: both open
without a script, `site.js` only closes them after a tap.

## The demo

`assets/site.js` draws tTerm Web at work into every `[data-demo]` element:
the sidebar with projects, machines and their terminals, tabs, blocks of
output, the input line, the Cmd+K palette. The interface is in English, as in
the product. It stands still until half of it is on screen, then plays, and
pauses again once it leaves the screen or the tab is hidden. Visitors who
asked their system for less motion get one still frame.

The first screen of the main page ends about a third of the way into the
demo on any window: the text above it takes the height that is left, within
limits (`.hero-text` in `style.css`).

## Search engines

`build_seo.py` writes `robots.txt` and `sitemap.xml`. Run it after adding a
page, or the page will not be in the sitemap and Google will not hear about
it. Posts are taken from `updates.md`, so a new post needs nothing there.

`lastmod` comes from `updates.md`, not from file times: the deploy rewrites
every file, and a site claiming everything changed on every push gets
discounted.

`assets/og-web.png` is the preview card shown when a link is shared: the
designer's `assets/og.png` with the line under the name changed from
"Terminal in Telegram" to "Terminal in your browser". Keep `og.png` as it is,
never regenerate or replace it by accident: an earlier archive overwrote it
three times with a placeholder.

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
beside them.

## Languages

`/` is English, `/ru/` is Russian, and so is every page under them. Both are
hand-written, not translated strings: the copy differs where the language
calls for it. The header of each page has a button with the page's language
that opens both; on phones the two sit in the menu. The Terms and the Policy
are in English only, so their Russian leads to the Russian main page.

## The blog

`updates.md` is the only place an entry is written. `build_updates.py` puts it
everywhere it shows: the block on both main pages, the lists on both blog
pages, and on each post's page its date, reading time and "more from the
blog". Those parts sit between `<!-- updates:NAME -->` comments, and editing
them by hand is pointless: the next run overwrites them.

An entry starts with its date and what it is about (`web`, `bot` or `site`),
then a title and text in every language:

```
## 2026-10-07 bot

@en Independent windows on a computer
Terminal windows on a computer with the agent are now independent...

@ru Независимые окна на компьютере
Окна на компьютере с агентом теперь независимы...
```

An entry with a page of its own adds the page's path after the tag
(`## 2026-10-18 web /blog/tterm-web/`); its text is then the post's lead, and
the post itself is written by hand in `blog/<name>/index.html` and
`ru/blog/<name>/index.html`. The newest such post leads the blog. The date
lives in `updates.md` only: change it there and run the script.

An entry needs a title and text in every language or the build stops. That is
the whole point of the file: written twice by hand, the two lists drift apart
within a month and nothing says which one is right.

One entry per release worth telling about, not per version. Five versions can
be one entry: a reader does not need three attempts at the same fix.

After changing `updates.md`:

```bash
python3 build_updates.py && python3 build_seo.py
```

Posting to [@tTermBlog](https://t.me/tTermBlog) stays manual. Deciding what is
worth telling is a judgement call, and a script would post everything.
