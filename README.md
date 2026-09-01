# tterm.net

**Version 1.3.0.** The number lives in `VERSION` and in a `<meta>` tag on
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

Bump `VERSION` and the `<meta name="version">` tag on both pages in the same
commit. One version, one set of files — the same rule as the bot: never ship
two different things under one number.

## Deploy

Pushing to `main` publishes the site. Cloudflare builds it as a Worker that
serves static assets; `wrangler.jsonc` says which directory to serve and
`.assetsignore` keeps the build scripts and notes out of it.

There is no build step — the site is plain HTML and CSS.

## Pages

`/` and `/ru/` are the landing page, `/donate/` and `/ru/donate/` hold the
donation addresses.

`build_donate.py` writes both donation pages from one template — the addresses
live in that script and nowhere else, so the two languages cannot drift apart.

`build_qr.py` regenerates the QR codes in `assets/`. It parses every file as
XML before writing it: an earlier version painted the modules by adding a
second `fill` attribute beside the one the library emits, which browsers
reject outright and show as a broken image.

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
