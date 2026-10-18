# Updates for tterm.net: the blog.
#
# One entry per release worth telling about, not per version. The site
# builds the blog in both languages from here, so the two cannot drift apart.
#
# An entry:
#
#   ## 2026-10-07 bot              date, then what it is about: web, bot or site
#   ## 2026-10-18 web /blog/x/     a path after that: the entry has a page of
#                                  its own, /blog/x/ and /ru/blog/x/, and the
#                                  text below is its lead
#   @en Title in English           a language, then the entry's title
#   Text in English.
#   @ru Заголовок по-русски
#   Текст по-русски.
#
# Newest first. Dates in ISO form, one entry per date; the pages format them
# per language. The text is shown as plain text: no markup, no code style.

## 2026-10-18 web /blog/tterm-web/

@en tTerm now works in the browser
All your servers and computers in one tab, every command in a block of its
own, and no keys on your device. What tTerm Web can do today, how to connect
a machine and what comes next.

@ru tTerm теперь работает в браузере
Все серверы и компьютеры в одной вкладке, каждая команда отдельным блоком,
и никаких ключей на устройстве. Что уже умеет tTerm Web, как подключить
машину и что будет дальше.

## 2026-10-07 bot

@en Independent windows on a computer
Terminal windows on a computer with the agent are now independent: each one
has its own shell, as on a server, and cd in one no longer moves the others.
To get this, update the agent by running the install again from
/addhost → Computer. The window buttons now sit at the bottom of the list
and stay put when you switch. A computer no longer shows as offline after
the agent reconnects quickly.

@ru Независимые окна на компьютере
Окна на компьютере с агентом теперь независимы: у каждого свой шелл, как
на сервере, и cd в одном больше не двигает остальные. Для этого обновите
агента, повторив установку через /addhost → Computer. Кнопки окна стоят
внизу списка и не прыгают при переключении. Компьютер больше не
показывается offline после быстрого переподключения агента.

## 2026-09-30 bot

@en Answer a command as it runs
You can now answer a command while it runs: whatever you type goes to its
input, the way it would in a terminal. Yes/no questions are recognised even
with a spinner turning below them. A computer with the agent no longer drops
out of the list after half an hour without commands.

@ru Ответ команде на ходу
Команде теперь можно ответить, пока она работает: всё, что вы пишете, уходит
ей на ввод, как в обычном терминале. Вопросы «да или нет» распознаются, даже
если под ними крутится индикатор. Компьютер с агентом больше не выпадает
из списка после получаса без команд.

## 2026-09-17 bot

@en Your own shell
The agent now runs your own shell, bash or zsh, so the environment and the
paths are the ones you see in a normal terminal. Commands that leave nothing
to fix ask for confirmation. The server's key is checked on every connection.
Long output arrives with a summary instead of its last few lines.

@ru Ваш собственный шелл
Агент запускает ваш собственный шелл – bash или zsh, – так что окружение
и пути те же, что в обычном терминале. Команды, после которых нечего чинить,
спрашивают подтверждение. Ключ сервера сверяется при каждом подключении.
Длинный вывод приходит со сводкой вместо хвоста.

## 2026-09-01 bot

@en Several terminals on one machine
A machine can now hold several terminals, the way you keep more than one
window open on a server. Output appears as it arrives, with a Stop button,
and a command waiting for an answer says so instead of hanging silently. The
git branch sits above the prompt, and longer output stays in the chat
instead of turning into a file.

@ru Несколько терминалов на одной машине
На одной машине теперь можно держать несколько терминалов, как несколько
окон на сервере. Вывод появляется по мере готовности, с кнопкой Stop,
а команда, которая ждёт ответа, говорит об этом, а не висит молча. Ветка git
встала над приглашением, и длинный вывод остаётся в чате, а не уходит файлом.

## 2026-08-30 site

@en The site and the channel
tterm.net is live, along with the channel where changes get announced. The
bot and the agent are open source.

@ru Сайт и канал
Заработал сайт tterm.net и канал, где мы рассказываем об изменениях.
Исходники бота и агента открыты.

## 2026-08-28 bot

@en The bot on its own server
The bot moved to its own server and no longer depends on a laptop being
open. Source for the bot and the agent is public.

@ru Бот на своём сервере
Бот переехал на свой сервер и больше не зависит от того, открыт ли ноутбук.
Исходники бота и агента открыты.

## 2026-08-26 bot

@en Buttons in messages
Machine list, menus and confirmations moved to buttons inside messages. A
machine that cannot be reached is greyed out instead of leading to an error.

@ru Кнопки в сообщениях
Список машин, меню и подтверждения переехали на кнопки внутри сообщений.
Машина не на связи теперь серая, а не ведёт в ошибку.

## 2026-08-25 bot

@en Access with a time limit
Shared access with time limits. Expired access closes itself and both sides
are told. Owners can export the full command history as a file.

@ru Доступ со сроком
Доступ для других со сроком. Истёкший закрывается сам, и обоим приходит
уведомление. Всю историю команд можно выгрузить файлом.

## 2026-08-23 bot

@en Computers through an agent
Computers can be connected too, through a small agent that dials out. macOS
and Linux for now.

@ru Компьютеры через агента
Подключаются и компьютеры: через маленький агент, который сам держит связь.
Пока macOS и Linux.
