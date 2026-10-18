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
   lang="ru", home="/ru/", blog="/ru/blog/", other="/donate/", other_lang="en",
   other_label="EN", other_name="English",
   skip="Перейти к содержанию", beta="бета", home_label="tTerm, на главную",
   nav_label="Разделы", menu="Меню",
   nav=[("#how", "Как это работает"), ("#features", "Возможности"),
        ("#security", "Безопасность"), ("#pricing", "Тарифы"), ("#faq", "Вопросы")],
   blog_label="Блог", signin="Войти", start="Начать бесплатно",
   title="Поддержать",
   desc="Адреса для пожертвований. USDT в сетях TRON и Ethereum.",
   h1="Поддержать проект",
   lede=("tTerm бесплатный и останется таким. Пожертвования идут "
         "на хостинг и дальнейшее развитие сервиса."),
   copy="Скопировать",
   only_tron="Только сеть TRON. Из другой сети не дойдёт.",
   only_eth="Только сеть Ethereum. Из другой сети не дойдёт.",
   thanks_h="Спасибо",
   thanks=("Даже небольшой перевод покрывает день работы сервера. "
           "А если переводить нечего, просто пользуйся, это тоже помогает: "
           "по замечаниям видно, что чинить дальше."),
   back="На главную",
   foot_label="Ссылки",
   foot=[("/ru/blog/", "Блог"), ("https://t.me/tTermNetBot", "Бот в Telegram"),
         ("/terms/", "Условия использования"), ("https://github.com/tterm-net", "Исходники"),
         ("https://t.me/tTermBlog", "Канал в Telegram"),
         ("/privacy/", "Политика конфиденциальности")],
   license="Лицензия AGPL-3.0 · 2026 · v{v}",
 ),
 "en": dict(
   lang="en", home="/", blog="/blog/", other="/ru/donate/", other_lang="ru",
   other_label="RU", other_name="Русский",
   skip="Skip to content", beta="beta", home_label="tTerm, home",
   nav_label="Sections", menu="Menu",
   nav=[("#how", "How it works"), ("#features", "Features"), ("#security", "Security"),
        ("#pricing", "Pricing"), ("#faq", "FAQ")],
   blog_label="Blog", signin="Sign in", start="Start for free",
   title="Donate",
   desc="Donation addresses. USDT on TRON and Ethereum.",
   h1="Donate",
   lede=("tTerm is free and will stay that way. Donations go to hosting "
         "and further development of the service."),
   copy="Copy",
   only_tron="TRON network only. Sent from another, it will not arrive.",
   only_eth="Ethereum network only. Sent from another, it will not arrive.",
   thanks_h="Thank you",
   thanks=("Even a small transfer covers a day of server time. And if there "
           "is nothing to send, just use it, that helps too: what you run "
           "into tells us what to fix next."),
   back="Home",
   foot_label="Links",
   foot=[("/blog/", "Blog"), ("https://t.me/tTermNetBot", "Telegram bot"),
         ("/terms/", "Terms of Service"), ("https://github.com/tterm-net", "Source code"),
         ("https://t.me/tTermBlog", "Telegram channel"), ("/privacy/", "Privacy Policy")],
   license="AGPL-3.0 licensed · 2026 · v{v}",
 ),
}

MENU_OPEN = ('<svg class="menu-open" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
             'stroke-width="2" stroke-linecap="round" aria-hidden="true">'
             '<path d="M4 7h16M4 12h16M4 17h16"/></svg>')
MENU_CLOSE = ('<svg class="menu-close" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
              'stroke-width="2" stroke-linecap="round" aria-hidden="true">'
              '<path d="M6 6l12 12M18 6L6 18"/></svg>')


def wallet(icon, network, note, only, address, qr, copy_label):
    return f"""      <div class="wallet">
        <div class="wallet-head">
          {icon}
          <div>
            <h3>{network}</h3>
            <p>{note}</p>
          </div>
        </div>
        <div class="wallet-body">
          <img class="qr" src="/assets/{qr}" alt="" width="128" height="128">
          <div class="wallet-addr">
            <code>{address}</code>
            <p class="only">{only}</p>
            <button class="btn btn-ghost copy" type="button"
                    data-copy="{address}">{copy_label}</button>
          </div>
        </div>
      </div>"""


def build(key: str, version: str) -> str:
    """The page, in the same header and footer as every other page."""
    d = T[key]
    app = "https://app.tterm.net"
    links = [f'<a href="{d["home"]}{a}">{t}</a>' for a, t in d["nav"]]
    links.append(f'<a href="{d["blog"]}">{d["blog_label"]}</a>')
    nav = "\n".join("      " + x for x in links)
    menu = "\n".join("          " + x for x in links)
    foot = "\n".join(
        f'      <a href="{u}"'
        + (' target="_blank" rel="noopener"' if u.startswith("http") else "")
        + f">{n}</a>" for u, n in d["foot"])
    return f"""<!DOCTYPE html>
<html lang="{d['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{d['title']} · tTerm</title>
<meta name="description" content="{d['desc']}">
<meta name="robots" content="noindex">
<link rel="alternate" hreflang="en" href="https://tterm.net/donate/">
<link rel="alternate" hreflang="ru" href="https://tterm.net/ru/donate/">
<link rel="icon" href="/assets/logo.svg" type="image/svg+xml">
<meta name="version" content="{version}">
<link rel="stylesheet" href="/style.css">
<script src="/assets/site.js" defer></script>
</head>
<body>
<a class="skip" href="#main">{d['skip']}</a>
<div class="page">

<header class="top">
  <div class="top-in">
    <a class="brand" href="{d['home']}" aria-label="{d['home_label']}">
      <img src="/assets/logo.svg" alt="" width="30" height="30">
      <span class="brand-name">tTerm</span>
      <span class="beta">{d['beta']}</span>
    </a>
    <nav class="nav" aria-label="{d['nav_label']}">
{nav}
    </nav>
    <div class="top-actions">
      <a class="lang-link" href="{d['other']}" hreflang="{d['other_lang']}" lang="{d['other_lang']}">{d['other_label']}</a>
      <a class="btn btn-ghost btn-sm" href="{app}">{d['signin']}</a>
      <a class="btn btn-primary btn-sm" href="{app}">{d['start']}</a>
      <details class="menu">
        <summary aria-label="{d['menu']}">{MENU_OPEN}{MENU_CLOSE}</summary>
        <nav class="menu-panel" aria-label="{d['menu']}">
{menu}
          <hr>
          <a class="menu-lang" href="{d['other']}" hreflang="{d['other_lang']}" lang="{d['other_lang']}">{d['other_name']}</a>
          <a class="btn btn-primary" href="{app}">{d['start']}</a>
        </nav>
      </details>
    </div>
  </div>
</header>

<main id="main">
  <section class="donate-head">
    <h1>{d['h1']}</h1>
    <p>{d['lede']}</p>
  </section>

  <section class="donate-body">
    <div class="wallets">
{wallet(TRON, "USDT · TRC-20", "TRON", d["only_tron"], TRC, "qr-trc20.svg", d["copy"])}
{wallet(ETH, "USDT · ERC-20", "Ethereum", d["only_eth"], ERC, "qr-erc20.svg", d["copy"])}
    </div>

    <h2>{d['thanks_h']}</h2>
    <p>{d['thanks']}</p>
    <a class="btn btn-ghost" href="{d['home']}">{d['back']}</a>
  </section>
</main>

<footer class="foot">
  <div class="foot-in">
    <div class="foot-brand">
      <a class="brand" href="{d['home']}" aria-label="{d['home_label']}">
        <img src="/assets/logo.svg" alt="" width="24" height="24">
        <span class="brand-name">tTerm</span>
      </a>
      <p class="foot-note">{d['license'].format(v=version)}</p>
    </div>
    <nav class="foot-links" aria-label="{d['foot_label']}">
{foot}
    </nav>
  </div>
</footer>

</div>

<script>
// Progressive enhancement: the address is always visible and selectable,
// the button only saves a few seconds. Without scripts nothing is lost.
document.querySelectorAll('.copy').forEach(function (b) {{
  b.addEventListener('click', function () {{
    navigator.clipboard.writeText(b.dataset.copy).then(function () {{
      var was = b.textContent;
      b.textContent = '✓';
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
