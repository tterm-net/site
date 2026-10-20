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
#   ## 2026-10-18 web /blog/x/ pinned
#                                  that page leads the blog even when newer
#                                  entries come after it: one at most
#   @en Title in English           a language, then the entry's title
#   Text in English.
#   @ru Заголовок по-русски
#   Текст по-русски.
#
# Newest first. Dates in ISO form, one entry per date; the pages format them
# per language. The text is shown as plain text: no markup, no code style.

## 2026-10-20 web /blog/notes-and-projects/

@en Notes, colored projects and terminal names
Runbooks, checklists and notes on access now live next to the machines they
are about. You can make projects of your own and give each a color, name
your terminals, and move machines and notes from one project to another.
Here is what tTerm Web learned in its first days.

@ru Заметки, проекты в цвете и имена терминалов
Ранбуки, чек-листы и заметки о доступах теперь живут рядом с машинами, к
которым относятся. Проекты можно заводить свои и красить в свой цвет,
терминалам давать имена, а машины и заметки переносить из проекта в проект.
Вот что появилось в tTerm Web за первые дни после запуска.

## 2026-10-18 web /blog/tterm-web/ pinned

@en tTerm now works in the browser
All your servers and computers in one tab, every command in a block of its
own, and no keys on your device. What tTerm Web can do today, how to connect
a machine and what comes next.

@ru tTerm теперь работает в браузере
Все серверы и компьютеры в одной вкладке, каждая команда отдельным блоком,
и никаких ключей на устройстве. Что уже умеет tTerm Web, как подключить
машину и что будет дальше.

## 2026-10-07 bot /blog/independent-windows/

@en Windows on a computer are now independent
On a server, every window has always been a terminal of its own. On a
computer with the agent, all windows shared one shell: a cd in one moved the
others too, and while a program ran in one window, the rest had to wait. Now
each window gets its own shell, the same as on a server. You can keep a dev
server running in one window and work in another.

@ru Окна на компьютере теперь независимы
На сервере каждое окно всегда было отдельным терминалом. На компьютере с
агентом все окна делили один шелл: cd в одном переносил и остальные, а пока
в одном работала программа, другие ждали. Теперь у каждого окна свой шелл,
как на сервере. Можно держать сервер разработки в одном окне и работать в
другом.

## 2026-09-30 bot /blog/answer-while-it-runs/

@en You can answer a command while it runs
When a program asked Continue? (Y/n), there used to be no way to reply: your
message would not send until the command was over. Now whatever you type
while a command is running goes to its input, the way it would in a
terminal. The bot marks such a message with 👌.

@ru Команде можно ответить, пока она работает
Раньше, если программа спрашивала Continue? (Y/n), ответить было нельзя:
сообщение не отправлялось, пока команда не закончится. Теперь всё, что ты
пишешь, пока команда работает, уходит ей на ввод, как в обычном терминале.
Бот отмечает такое сообщение реакцией 👌.

## 2026-09-17 bot /blog/your-shell/

@en The agent now runs your shell: bash or zsh
It used to start bash no matter what. On macOS, where zsh has been the
default since 2019, that meant somebody else's environment: half of what you
had installed could not be found.

@ru Агент запускает твой шелл: bash или zsh
Раньше агент запускал bash, что бы ни было. На macOS, где zsh стоит по
умолчанию с 2019 года, это означало чужое окружение: половина того, что у
тебя установлено, не находилась.

## 2026-09-03 site /blog/verified-on-github/

@en tTerm is now a verified organisation on GitHub
github.com/tterm-net carries a Verified badge: GitHub confirmed that the
organisation and tterm.net are the same people.

@ru tTerm теперь проверенная организация на GitHub
У github.com/tterm-net теперь есть галочка Verified: GitHub подтвердил, что
за организацией и tterm.net стоят одни и те же люди.

## 2026-09-01 bot /blog/several-terminals/

@en Several terminals per machine
You can now keep more than one terminal open on the same server – one
tailing a log, another doing the work. They show up as separate lines in
/use, each with its own shell: a cd in one leaves the other where it was.

@ru Несколько терминалов на одной машине
Теперь на одном сервере можно держать открытыми несколько терминалов: в
одном идёт лог, в другом ты работаешь. В /use они видны отдельными строками,
и у каждого свой шелл: cd в одном не сдвигает другой.

## 2026-08-31 bot /blog/tterm-is-live/

@en tTerm is live
A terminal for your servers, right here in Telegram. Type a command – it
runs on your machine, and the reply comes back as a message with the exit
code, the working directory and the git branch. The shell remembers where
you left off.

@ru tTerm запущен
Терминал для твоих серверов прямо в Telegram. Пишешь команду, она
выполняется на машине, а ответ приходит сообщением: код возврата, рабочий
каталог и ветка git. Шелл помнит, где ты остановился.

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
