"""Builds the donation page in both languages from one template.

The addresses live here and nowhere else, so the two languages
cannot drift apart.
"""
import pathlib

TRC = "TPv5SQVhjczDR3fBPvGKBu9Ekn8gcziQTX"
ERC = "0xBc0B9cB860A6c789F7cB13DC59E6b5cf12Ab1fa0"

# Network marks in their own brand colours: TRON red, Ethereum blue-violet.
# Drawn here rather than pulled in, so the page stays a single static file
# and depends on nobody else's CDN.
TRON = (
    '<svg viewBox="0 0 64 64" width="26" height="26" aria-hidden="true">'
    '<circle cx="32" cy="32" r="32" fill="#EF0027"/>'
    '<g transform="translate(9 12) scale(0.72)">'
    '<path fill="#fff" d="M61.55 19.28c-3-2.77-7.15-7-10.53-10l-.2-.14a3.82 '
    '3.82 0 0 0-1.11-.62l0 0C41.55 7 3.63-.09 2.89 0a1.4 1.4 0 0 0-.58.22'
    'L2.12.37a2.23 2.23 0 0 0-.52.84l-.05.13v.71l0 .11C5.82 14.05 22.68 53 '
    '26 62.14c.2.62.58 1.8 1.29 1.86h.16c.38 0 2-2.14 2-2.14S58.72 26.72 '
    '61.63 23a9.06 9.06 0 0 0 1-1.51 2.46 2.46 0 0 0-1.08-2.21ZM36.88 '
    '23.37 49.24 13.12l7.25 6.68Zm-4.8-.67L10.8 5.26l34.43 6.35ZM34 '
    '27.19l23.83-3.84-27.23 32.8ZM7.91 7 30.3 26l-4.06 33.1Z"/>'
    '</g></svg>')
ETH = (
    '<svg viewBox="0 0 32 32" width="26" height="26" aria-hidden="true">'
    '<circle cx="16" cy="16" r="16" fill="#627EEA"/>'
    '<path d="M16.5 4v8.9l7.5 3.3-7.5-12.2z" fill="#fff" fill-opacity=".6"/>'
    '<path d="M16.5 4 9 16.2l7.5-3.3V4z" fill="#fff"/>'
    '<path d="M16.5 21.9v6.1L24 17.6l-7.5 4.3z" fill="#fff" fill-opacity=".6"/>'
    '<path d="M16.5 28v-6.1L9 17.6l7.5 10.4z" fill="#fff"/>'
    '<path d="M16.5 20.5 24 16.2l-7.5-3.3v7.6z" fill="#fff" fill-opacity=".2"/>'
    '<path d="M9 16.2l7.5 4.3v-7.6L9 16.2z" fill="#fff" fill-opacity=".6"/>'
    '</svg>')

T = {
 "ru": dict(
   lang="ru", home="/ru/", other="/donate/", other_lang="en",
   other_label="English", self_label="Русский", label="RU",
   title="Поддержать",
   desc="Адреса для пожертвований. USDT в сетях TRON и Ethereum.",
   nav=[("Исходники", "https://github.com/tterm-net"),
        ("Новости", "https://t.me/tTermBlog")],
   support="Поддержать",
   h1="Поддержать проект",
   lede=("tTerm бесплатный и останется таким. Пожертвования идут "
         "на хостинг и дальнейшее развитие сервиса."),
   copy="Скопировать",
   only_tron="Только сеть TRON. Из другой сети не дойдёт.",
   only_eth="Только сеть Ethereum. Из другой сети не дойдёт.",
   thanks_h="Спасибо",
   thanks=("Даже небольшой перевод покрывает день работы сервера. "
           "А если переводить нечего — просто пользуйся, это тоже помогает: "
           "по замечаниям видно, что чинить дальше."),
   back="← На главную",
   foot=[("Бот", "https://t.me/tTermNetBot"),
         ("Новости", "https://t.me/tTermBlog"),
         ("Исходники", "https://github.com/tterm-net")],
   license="Лицензия MIT · 2026 · v{v}",
 ),
 "en": dict(
   lang="en", home="/", other="/ru/donate/", other_lang="ru",
   other_label="Русский", self_label="English", label="EN",
   title="Donate",
   desc="Donation addresses. USDT on TRON and Ethereum.",
   nav=[("Source", "https://github.com/tterm-net"),
        ("News", "https://t.me/tTermBlog")],
   support="Donate",
   h1="Donate",
   lede=("tTerm is free and will stay that way. Donations go to hosting "
         "and further development of the service."),
   copy="Copy",
   only_tron="TRON network only. Sent from another, it will not arrive.",
   only_eth="Ethereum network only. Sent from another, it will not arrive.",
   thanks_h="Thank you",
   thanks=("Even a small transfer covers a day of server time. And if there "
           "is nothing to send, just use it — that helps too: what you run "
           "into tells us what to fix next."),
   back="← Back home",
   foot=[("Bot", "https://t.me/tTermNetBot"),
         ("News", "https://t.me/tTermBlog"),
         ("Source", "https://github.com/tterm-net")],
   license="MIT licensed · 2026 · v{v}",
 ),
}

GLOBE = ('<svg viewBox="0 0 24 24" width="15" height="15" fill="none" '
         'stroke="currentColor" stroke-width="1.7" aria-hidden="true">'
         '<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/>'
         '<path d="M12 3a15 15 0 0 1 0 18a15 15 0 0 1 0-18"/></svg>')


def wallet(icon, network, note, only, address, qr, copy_label, depth):
    return f"""      <div class="wallet">
        <div class="wallet-head">
          {icon}
          <div>
            <h3>{network}</h3>
            <p>{note}</p>
          </div>
        </div>
        <div class="wallet-body">
          <img class="qr" src="{depth}/assets/{qr}" alt="" width="128" height="128">
          <div class="wallet-addr">
            <code>{address}</code>
            <p class="only">{only}</p>
            <button class="btn copy" type="button"
                    data-copy="{address}">{copy_label}</button>
          </div>
        </div>
      </div>"""


def build(key: str, version: str) -> str:
    d = T[key]
    depth = "../.." if key == "ru" else ".."
    # Everything in these two lists points off-site.
    nav = "\n".join(
        f'    <a class="pill pill-ghost" href="{u}" target="_blank"'
        f' rel="noopener">{n}</a>' for n, u in d["nav"])
    foot = "\n".join(f'    <a href="{u}" target="_blank" rel="noopener">{n}</a>'
                     for n, u in d["foot"])
    self_href = "/ru/donate/" if key == "ru" else "/donate/"
    menu = (f'      <a href="/ru/donate/" hreflang="ru" lang="ru">Русский</a>\n'
            f'      <a href="/donate/" hreflang="en" lang="en">English</a>')
    return f"""<!DOCTYPE html>
<html lang="{d['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{d['title']} — tTerm</title>
<meta name="description" content="{d['desc']}">
<meta name="version" content="{version}">
<meta name="robots" content="noindex">
<link rel="icon" href="{depth}/assets/logo.svg" type="image/svg+xml">
<link rel="alternate" hreflang="en" href="https://tterm.net/donate/">
<link rel="alternate" hreflang="ru" href="https://tterm.net/ru/donate/">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{depth}/style.css">
</head>
<body class="donate">

<div class="glow" aria-hidden="true"></div>

<header class="bar">
  <a class="brand" href="{d['home']}">
    <img src="{depth}/assets/logo.svg" alt="" width="30" height="30">
    <span>tTerm</span>
    <span class="beta">\u03b2eta version</span>
  </a>
  <nav class="bar-links">
{nav}
    <a class="pill" href="{self_href}">{d['support']}</a>
    <details class="lang">
      <summary aria-label="Language">{GLOBE}<span>{d['label']}</span></summary>
      <div class="lang-menu">
{menu}
      </div>
    </details>
  </nav>
</header>

<main>
  <section class="hero hero-narrow">
    <h1>{d['h1']}</h1>
    <p class="lede">{d['lede']}</p>
  </section>

  <section class="band">
    <div class="wallets">
{wallet(TRON, "USDT · TRC-20", "TRON", d["only_tron"], TRC,
               "qr-trc20.svg", d["copy"], depth)}
{wallet(ETH, "USDT · ERC-20", "Ethereum", d["only_eth"], ERC,
               "qr-erc20.svg", d["copy"], depth)}
    </div>

  </section>

  <section class="band">
    <h2>{d['thanks_h']}</h2>
    <p class="band-lede">{d['thanks']}</p>
    <p><a class="btn" href="{d['home']}">{d['back']}</a></p>
  </section>
</main>

<footer>
  <div class="foot-brand">
    <img src="{depth}/assets/logo.svg" alt="" width="24" height="24">
    <span>tTerm</span>
  </div>
  <nav class="foot-links">
{foot}
  </nav>
  <p class="foot-note">{d['license'].format(v=version)}</p>
</footer>

<script>
// Progressive enhancement: the address is always visible and selectable,
// the button only saves a few seconds. Without scripts nothing is lost.
document.querySelectorAll('.copy').forEach(function (b) {{
  b.addEventListener('click', function () {{
    navigator.clipboard.writeText(b.dataset.copy).then(function () {{
      var was = b.textContent;
      b.textContent = '\u2713';
      setTimeout(function () {{ b.textContent = was; }}, 1400);
    }});
  }});
}});
</script>
</body>
</html>
"""


if __name__ == "__main__":
    version = pathlib.Path("VERSION").read_text().strip()
    pathlib.Path("donate/index.html").write_text(build("en", version))
    pathlib.Path("ru/donate/index.html").write_text(build("ru", version))
    print("  donate/index.html")
    print("  ru/donate/index.html")
