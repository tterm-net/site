# tterm.net

**Version 1.9.0.** The number lives in `VERSION` and in a `<meta>` tag on
each page, so you can tell what is deployed by viewing source.

The landing page for [tTerm](https://github.com/tterm-net/tTerm) — Terminal in
Telegram with multi-user access.

Static HTML and CSS, no build step. Cloudflare Pages serves it as is.

## Local preview

```bash
python3 -m http.server 4000
```

Then open <http://localhost:4000>.

For a quick look without a server, `python3 build_preview.py` writes a single
review file holding both languages, with the stylesheet and logo inlined and
the language switch wired to swap them in place. It is build output — edit the
pages, never the preview.

## Releasing

Bump `VERSION`, the `<meta name="version">` tag and the number in the footer
on every page in the same commit; the donation pages take it from `VERSION`
when `build_donate.py` runs. One version, one set of files — the same rule as the bot: never ship
two different things under one number.

## Search engines

`build_seo.py` writes `robots.txt` and `sitemap.xml`. Run it after adding a
page, or the page will not be in the sitemap and Google will not hear about it.

`lastmod` comes from the newest date in `updates.md`, not from file times: the
deploy rewrites every file, and a site claiming everything changed on every
push gets discounted.

`build_og.py` draws `assets/og.png`, the preview card shown when a link is
shared. The page pointed at that file long before it existed, so every shared
link came out with a blank space. Replace it with something drawn properly when
there is one — nothing else needs to change.

The donation pages carry `noindex` and are excluded in `robots.txt`: a page of
wallet addresses is not what anyone should arrive at from a search.

## Deploy

Pushing to `main` publishes the site. Cloudflare builds it as a Worker that
serves static assets; `wrangler.jsonc` says which directory to serve and
`.assetsignore` keeps the build scripts and notes out of it.

There is no build step — the site is plain HTML and CSS.

## Pages

`/` and `/ru/` are the landing page, `/donate/` and `/ru/donate/` hold the
donation addresses.

`/terms/` and `/privacy/` hold the Terms of Service and the Privacy Policy, in
English only: one binding text, linked from the sign-up box of tTerm Web and
from every footer. They are written by hand, laid out like Todoist's: a list
of sections at the top, numbered clauses with a bold label, no tables.

`build_donate.py` writes both donation pages from one template — the addresses
live in that script and nowhere else, so the two languages cannot drift apart.

`build_qr.py` regenerates the QR codes in `assets/`. It parses every file as
XML before writing it: an earlier version painted the modules by adding a
second `fill` attribute beside the one the library emits, which browsers
reject outright and show as a broken image.

## Fonts

Manrope and JetBrains Mono are served from `assets/fonts`, not from Google
Fonts: the Privacy Policy says the pages load nothing from third parties, and
a font request hands the visitor's address to whoever serves it. The files
are the variable fontsource builds tterm-web uses, with their OFL licenses
beside them. `build_preview.py` still links Google Fonts: its output is a
local review file and never deployed.

## Languages

`/` is English, `/ru/` is Russian. Both are hand-written, not translated
strings — the copy differs where the language calls for it. A switcher sits
in the header of each.

## Updates

`updates.md` is the only place an update is written. `build_updates.py` puts
it on both language pages — editing a page's list by hand is pointless, the
next run overwrites it.

An entry needs text in every language or the build stops. That is the whole
point of the file: written twice by hand, the two lists drift apart within a
month and nothing says which one is right.

One entry per release worth telling about, not per version. Five versions can
be one entry — a reader does not need three attempts at the same fix.

Posting to [@tTermBlog](https://t.me/tTermBlog) stays manual. Deciding what is
worth telling is a judgement call, and a script would post everything.
