# tterm.net

**Version 1.1.1.** The number lives in `VERSION` and in a `<meta>` tag on
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

The list on the page is the user-facing changelog: two lines per entry about
what changed for the reader, not for us. The same entries go to
[@tTermBlog](https://t.me/tTermBlog).
