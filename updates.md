# Updates for tterm.net: the blog.
#
# One entry per release worth telling about, not per version. The site
# builds the blog in every language from here, so they cannot drift apart.
#
# An entry:
#
#   ## 2026-10-07 bot              date, then what it is about: web, mac,
#                                  docs, bot or site
#   ## 2026-10-18 web /blog/x/     a path after that: the entry has a page of
#                                  its own, /blog/x/ in every language
#                                  (templates/blog/x.html), and the text below
#                                  is its lead
#   ## 2026-10-18 web /blog/x/ pinned
#                                  that page leads the blog even when newer
#                                  entries come after it: one at most
#   @en Title in English           a language, then the entry's title
#   Text in English.
#   @ru Заголовок по-русски
#   Текст по-русски.
#   ...                            and so on, every language of the site
#
# Newest first. Dates in ISO form, one entry per date; the pages format them
# per language. The text is shown as plain text: no markup, no code style.

## 2026-11-03 web /blog/logs/

@en Logs: we now create a log for every machine automatically
A machine's log records every command: who ran it, when and how it ended.
The records are kept for a year. You can leave a note on a command, and
erase a password that got into one by mistake.

@ru Логи: теперь мы автоматически создаём логи для каждой машины
В логе машины записана каждая команда: кто её запустил, когда и чем она
закончилась. Записи хранятся год. К команде можно оставить заметку, а
пароль, случайно попавший в команду, стереть.

@de Logs: Wir legen jetzt für jede Maschine automatisch ein Log an
Das Log einer Maschine hält jeden Befehl fest: wer ihn ausgeführt hat, wann
und wie er ausging. Die Einträge werden ein Jahr lang aufbewahrt. Du kannst
zu einem Befehl eine Notiz hinterlassen und ein Passwort schwärzen, das
versehentlich hineingeraten ist.

@es Bitácoras: ahora creamos automáticamente una bitácora para cada máquina
La bitácora de una máquina registra cada comando: quién lo ejecutó, cuándo y
cómo terminó. Las entradas se guardan durante un año. Puedes dejar una nota
en un comando y borrar una contraseña que se coló en él por error.

@fr Journaux : nous créons désormais automatiquement un journal pour chaque machine
Le journal d’une machine enregistre chaque commande : qui l’a lancée, quand
et comment elle s’est terminée. Les entrées sont conservées un an. Vous
pouvez laisser une note sur une commande et effacer un mot de passe qui s’y
est glissé par erreur.

@it Log: ora creiamo automaticamente un log per ogni macchina
Il log di una macchina registra ogni comando: chi l'ha eseguito, quando e
com'è finito. Le voci vengono conservate per un anno. Puoi lasciare una nota
su un comando e oscurare una password che ci è finita dentro per errore.

@pl Logi: teraz automatycznie tworzymy log dla każdej maszyny
Log maszyny zapisuje każde polecenie: kto je uruchomił, kiedy i jak się
zakończyło. Wpisy są przechowywane przez rok. Do polecenia możesz dodać
notatkę, a hasło, które trafiło do niego przez pomyłkę, wymazać.

@pt-BR Logs: agora criamos automaticamente um log para cada máquina
O log de uma máquina registra cada comando: quem o executou, quando e como
terminou. Os registros ficam guardados por um ano. Você pode deixar uma nota
num comando e apagar uma senha que foi parar nele por engano.

@tr Loglar: artık her makine için otomatik olarak bir log oluşturuyoruz
Bir makinenin logu her komutu kaydeder: kim çalıştırdı, ne zaman ve nasıl
sonuçlandı. Kayıtlar bir yıl boyunca saklanır. Bir komuta not bırakabilir,
yanlışlıkla komuta karışan bir parolayı da silebilirsin.

@ja ログ：マシンごとにログを自動で作成するようになりました
マシンのログには、すべてのコマンドについて、誰がいつ実行し、どう終わったかが記録されます。保存期間は 1 年間です。コマンドにノートを残したり、うっかり入り込んだパスワードを墨消ししたりできます。

@ko 로그: 이제 머신마다 로그를 자동으로 만들어요
머신 로그에는 모든 명령이 누가, 언제 실행했고 어떻게 끝났는지와 함께 기록돼요. 보관 기간은 1년이에요. 명령에 노트를 남길 수 있고,
실수로 들어간 비밀번호는 지울 수 있어요.

@zh-CN 日志：现在我们会自动为每台机器创建日志
机器的日志会记录每一条命令：谁运行的、什么时候运行的、结果如何。记录保留一年。你可以给命令留下笔记，也可以抹除不小心混进命令里的密码。

## 2026-11-02 docs /blog/docs/

@en tTerm now has documentation
At docs.tterm.net you'll find how tTerm works, from your first command to
how access is set up. 19 pages in all 12 languages, with screenshots in the
light and the dark theme.

@ru У tTerm появилась документация
На docs.tterm.net описано, как работает tTerm: от первой команды до того,
как устроен доступ. 19 страниц на всех 12 языках, со снимками экрана в
светлой и тёмной теме.

@de tTerm hat jetzt eine Dokumentation
Auf docs.tterm.net erfährst du, wie tTerm funktioniert: von deinem ersten
Befehl bis dazu, wie der Zugriff aufgebaut ist. Insgesamt 19 Seiten in allen
12 Sprachen, mit Screenshots im hellen und im dunklen Design.

@es tTerm ya tiene documentación
En docs.tterm.net te explicamos cómo funciona tTerm, desde tu primer comando
hasta cómo está organizado el acceso. En total, 19 páginas en los 12
idiomas, con capturas de pantalla en el tema claro y en el oscuro.

@fr tTerm a désormais sa documentation
Sur docs.tterm.net, découvrez comment fonctionne tTerm, de votre première
commande à l’organisation des accès. Au total, 19 pages dans chacune des 12
langues, avec des captures d’écran en thème clair et en thème sombre.

@it tTerm ora ha la sua documentazione
Su docs.tterm.net scopri come funziona tTerm, dal tuo primo comando a come è
organizzato l'accesso. Sono 19 pagine in tutte le 12 lingue, con screenshot
nel tema chiaro e in quello scuro.

@pl tTerm ma teraz dokumentację
Na docs.tterm.net dowiesz się, jak działa tTerm: od pierwszego polecenia po
organizację dostępu. W sumie 19 stron we wszystkich 12 językach, ze zrzutami
ekranu w jasnym i ciemnym motywie.

@pt-BR O tTerm agora tem documentação
Em docs.tterm.net você descobre como o tTerm funciona, do seu primeiro
comando até a organização do acesso. São 19 páginas em todos os 12 idiomas,
com capturas de tela no tema claro e no escuro.

@tr tTerm'in artık belgeleri var
docs.tterm.net, ilk komutundan erişimin nasıl sağlandığına kadar tTerm'in
nasıl çalıştığını anlatıyor. Toplam 19 sayfa, 12 dilin hepsinde, açık ve
koyu temada ekran görüntüleriyle.

@ja tTerm にドキュメントができました
docs.tterm.net では、最初のコマンドからアクセスの仕組みまで、tTerm がどう動くのかを説明しています。19 ページを 12 言語すべてで用意し、ライトテーマとダークテーマのスクリーンショットも載せています。

@ko tTerm에 문서가 생겼어요
docs.tterm.net에서 첫 명령부터 접근 방식까지, tTerm이 어떻게 작동하는지 알아볼 수 있어요. 총 19개 페이지를 12개
언어 모두로 제공하고, 라이트 테마와 다크 테마 스크린샷도 담았어요.

@zh-CN tTerm 现在有文档了
docs.tterm.net 介绍了 tTerm 的工作方式：从你的第一条命令，到访问如何运作。全部 19 个页面都有 12 种语言版本，并配有浅色和深色主题的截图。

## 2026-10-31 mac /blog/tterm-for-mac/ pinned

@en tTerm for Mac: a local terminal with the cloud inside
tTerm now has an app for the Mac. It opens your computer's shells in blocks
and works without an account, and once you sign in, your servers from the
cloud appear in the same window. Free, macOS 11 or later.

@ru tTerm для Mac: локальный терминал с облаком внутри
У tTerm появилось приложение для Mac. Оно открывает шеллы твоего компьютера
блоками и работает без аккаунта, а после входа в том же окне появляются твои
серверы из облака. Бесплатно, macOS 11 и новее.

@de tTerm für Mac: ein lokales Terminal mit der Cloud an Bord
tTerm gibt es jetzt als App für den Mac. Die App öffnet die Shells deines
Computers in Blöcken und funktioniert ohne Konto. Nach der Anmeldung
erscheinen deine Server aus der Cloud im selben Fenster. Kostenlos, macOS 11
oder neuer.

@es tTerm para Mac: una terminal local con la nube dentro
tTerm ya tiene una aplicación para Mac. Abre los shells de tu computadora en
bloques, funciona sin cuenta y, cuando inicias sesión, muestra en la misma
ventana tus servidores de la nube. Gratis, macOS 11 o posterior.

@fr tTerm pour Mac : un terminal local avec le cloud intégré
tTerm a désormais une application pour Mac. Elle ouvre les shells de votre
ordinateur sous forme de blocs et fonctionne sans compte. Une fois connecté,
vous retrouvez vos serveurs du cloud dans la même fenêtre. Gratuit, macOS 11
ou version ultérieure.

@it tTerm per Mac: un terminale locale con dentro il cloud
tTerm ora ha un'app per Mac. Apre le shell del tuo computer a blocchi,
funziona senza account e, dopo l'accesso, mostra nella stessa finestra i
tuoi server dal cloud. Gratis, macOS 11 o successivo.

@pl tTerm dla Maca: lokalny terminal z chmurą w środku
tTerm ma teraz aplikację na Maca. Otwiera powłoki twojego komputera w
blokach i działa bez konta, a po zalogowaniu w tym samym oknie pojawiają się
twoje serwery z chmury. Za darmo, macOS 11 lub nowszy.

@pt-BR tTerm para Mac: um terminal local com a nuvem dentro
O tTerm agora tem um app para Mac. Ele abre os shells do seu computador em
blocos, funciona sem conta e, depois que você entra, mostra os seus
servidores da nuvem na mesma janela. Grátis, macOS 11 ou posterior.

@tr Mac için tTerm: bulutu içinde taşıyan yerel bir terminal
tTerm'in artık bir Mac uygulaması var. Bilgisayarının kabuklarını bloklar
halinde açar ve hesap olmadan çalışır, giriş yaptığında da buluttaki
sunucuların aynı pencerede belirir. Ücretsiz, macOS 11 veya üstü.

@ja Mac 版 tTerm：クラウドを内蔵したローカルターミナル
tTerm に Mac 版アプリが加わりました。お使いの Mac のシェルをブロックで開き、アカウントがなくても使えます。サインインすると、同じウィンドウにクラウドのサーバーも表示されます。無料、macOS 11 以降に対応。

@ko Mac용 tTerm: 클라우드가 들어 있는 로컬 터미널
tTerm에 Mac용 앱이 생겼어요. 컴퓨터의 셸을 블록으로 열고 계정 없이도 작동하며, 로그인하면 클라우드의 서버가 같은 창에
나타나요. 무료, macOS 11 이상.

@zh-CN tTerm Mac 版：内置云端的本地终端
tTerm 推出了 Mac 应用。它以块的形式打开你电脑上的 shell，没有账号也能使用；登录后，你在云端的服务器也会出现在同一个窗口里。免费，支持 macOS 11 或更高版本。

## 2026-10-25 web /blog/open-source/

@en Why tTerm's code is open, even though paid plans are coming
All of tTerm's code is now under AGPL v3 instead of MIT, and paid plans are
coming soon. Here is why one does not get in the way of the other, and why we
opened even the server.

@ru Почему код tTerm открыт, хотя будут платные тарифы
Весь код tTerm теперь под лицензией AGPL v3 вместо MIT, а скоро появятся
платные тарифы. Рассказываем, почему одно другому не мешает и зачем мы
открыли даже сервер.

@de Warum der Code von tTerm offen ist, obwohl kostenpflichtige Tarife kommen
Der gesamte Code von tTerm steht jetzt unter AGPL v3 statt MIT, und bald
kommen kostenpflichtige Tarife. Hier erklären wir, warum das eine dem
anderen nicht im Weg steht und warum sogar der Server offen ist.

@es Por qué el código de tTerm es abierto, aunque habrá planes de pago
Todo el código de tTerm está ahora bajo AGPL v3 en lugar de MIT, y pronto
llegarán los planes de pago. Te contamos por qué una cosa no impide la otra
y por qué abrimos incluso el servidor.

@fr Pourquoi le code de tTerm est ouvert, alors que des offres payantes arrivent
Tout le code de tTerm est désormais sous AGPL v3 au lieu de MIT, et des
offres payantes arrivent bientôt. Voici pourquoi l’un n’empêche pas l’autre,
et pourquoi nous avons ouvert jusqu’au serveur.

@it Perché il codice di tTerm è aperto, anche se arrivano i piani a pagamento
Tutto il codice di tTerm ora è sotto licenza AGPL v3 invece che MIT, e
presto arriveranno i piani a pagamento. Ecco perché una cosa non ostacola
l'altra, e perché abbiamo aperto anche il server.

@pl Dlaczego kod tTerma jest otwarty, choć będą płatne plany
Cały kod tTerma jest teraz na licencji AGPL v3 zamiast MIT, a wkrótce
pojawią się płatne plany. Wyjaśniamy, dlaczego jedno nie przeszkadza
drugiemu i dlaczego otworzyliśmy nawet serwer.

@pt-BR Por que o código do tTerm é aberto, mesmo com planos pagos a caminho
Todo o código do tTerm agora está sob a AGPL v3 em vez da licença MIT, e os
planos pagos chegam em breve. Explicamos por que uma coisa não atrapalha a
outra e por que abrimos até o servidor.

@tr Ücretli planlar yolda olsa da tTerm'in kodu neden açık
tTerm'in tüm kodu artık MIT yerine AGPL v3 lisansıyla yayımlanıyor ve
yakında ücretli planlar geliyor. Bunların neden birbirine engel olmadığını
ve neden sunucuyu bile açtığımızı anlatıyoruz.

@ja 有料プランを予定していても tTerm のコードを公開する理由
tTerm のコードはすべて、MIT に代わって AGPL v3 で公開されるようになりました。有料プランもまもなく始まります。この
2 つが両立する理由と、サーバーまで公開した理由を説明します。

@ko 유료 요금제가 나오는데도 tTerm의 코드를 공개하는 이유
이제 tTerm의 모든 코드는 MIT 대신 AGPL v3로 공개되고, 곧 유료 요금제도
나와요. 이 둘이 왜 서로 부딪히지 않는지, 그리고 왜 서버까지 공개했는지
설명할게요.

@zh-CN 付费方案即将推出，为何仍开源
tTerm 的全部代码现在采用 AGPL v3，而不再是 MIT，付费方案也即将推出。下面说说为什么两者并不冲突，以及我们为什么连服务器都开源了。

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

@de Notizen, farbige Projekte und Namen für Terminals
Runbooks, Checklisten und Notizen zu Zugängen liegen jetzt direkt neben den
Maschinen, um die es geht. Du kannst eigene Projekte anlegen und jedem eine
Farbe geben, deine Terminals benennen und Maschinen und Notizen von einem
Projekt in ein anderes verschieben. Das hat tTerm Web in seinen ersten Tagen
gelernt.

@es Notas, proyectos con color y nombres de terminales
Los runbooks, las listas de verificación y las notas sobre accesos ahora
viven junto a las máquinas a las que se refieren. Puedes crear tus propios
proyectos y darle a cada uno un color, poner nombre a tus terminales y mover
máquinas y notas de un proyecto a otro. Esto es lo que tTerm Web aprendió a
hacer en sus primeros días.

@fr Notes, projets en couleur et noms de terminaux
Runbooks, check-lists et notes sur les accès sont désormais rangés à côté
des machines qu’ils concernent. Vous pouvez créer vos propres projets et
donner à chacun sa couleur, nommer vos terminaux, et déplacer machines et
notes d’un projet à l’autre. Voici ce que tTerm Web a appris à faire dans
ses premiers jours.

@it Note, progetti a colori e nomi dei terminali
Runbook, checklist e note sugli accessi ora stanno accanto alle macchine a
cui si riferiscono. Puoi creare i tuoi progetti e assegnare a ognuno un
colore, dare un nome ai terminali e spostare macchine e note da un progetto
all'altro. Ecco cosa ha imparato tTerm Web nei suoi primi giorni.

@pl Notatki, kolorowe projekty i nazwy terminali
Runbooki, checklisty i notatki o dostępach są teraz tuż obok maszyn, których
dotyczą. Możesz tworzyć własne projekty i nadawać każdemu kolor, nazywać
terminale oraz przenosić maszyny i notatki między projektami. Tego tTerm Web
nauczył się w pierwszych dniach.

@pt-BR Notas, projetos coloridos e nomes de terminais
Runbooks, checklists e notas sobre acessos agora ficam ao lado das máquinas
a que se referem. Você pode criar projetos próprios, cada um com a sua cor,
dar nomes aos seus terminais e mover máquinas e notas de um projeto para
outro. Veja o que o tTerm Web aprendeu a fazer nos primeiros dias.

@tr Notlar, renkli projeler ve terminal adları
Runbook'lar, kontrol listeleri ve erişim notları artık ait oldukları
makinelerin yanında duruyor. Kendi projelerini oluşturup her birine bir renk
verebilir, terminallerine ad koyabilir, makineleri ve notları bir projeden
ötekine taşıyabilirsin. İşte tTerm Web'in ilk günlerinde öğrendikleri.

@ja ノート、色分けされたプロジェクト、ターミナルの名前
手順書、チェックリスト、アクセス情報などのノートを、対象のマシンのすぐそばに置けるようになりました。プロジェクトを自分で作って色を付けたり、ターミナルに名前を付けたり、マシンやノートを別のプロジェクトへ移したりもできます。公開から最初の数日で
tTerm Web に加わった機能を紹介します。

@ko 노트, 프로젝트 색상, 터미널 이름
런북, 체크리스트, 접속 정보 노트가 이제 관련된 머신 바로 옆에 있어요.
프로젝트를 직접 만들어 색을 정하고, 터미널에 이름을 붙이고, 머신과 노트를
다른 프로젝트로 옮길 수 있어요. 출시 후 첫 며칠 동안 tTerm Web에 새로 생긴
것들이에요.

@zh-CN 笔记、彩色项目和终端名称
运维手册、检查清单和访问说明，现在就放在相关机器的旁边。你可以创建自己的项目并为每个项目设定颜色，给终端命名，还能把机器和笔记从一个项目移到另一个项目。以下是
tTerm Web 上线头几天新增的功能。

## 2026-10-18 web /blog/tterm-web/

@en tTerm now works in the browser
All your servers and computers in one tab, every command in a block of its
own, and no keys on your device. What tTerm Web can do today, how to connect
a machine and what comes next.

@ru tTerm теперь работает в браузере
Все серверы и компьютеры в одной вкладке, каждая команда отдельным блоком,
и никаких ключей на устройстве. Что уже умеет tTerm Web, как подключить
машину и что будет дальше.

@de tTerm funktioniert jetzt im Browser
Alle deine Server und Computer in einem Tab, jeder Befehl in einem eigenen
Block und keine Schlüssel auf deinem Gerät. Was tTerm Web heute kann, wie du
eine Maschine verbindest und wie es weitergeht.

@es tTerm ya funciona en el navegador
Todos tus servidores y computadoras en una pestaña, cada comando en su
propio bloque y ninguna clave en tu dispositivo. Lo que tTerm Web ya sabe
hacer, cómo conectar una máquina y lo que viene después.

@fr tTerm fonctionne désormais dans le navigateur
Tous vos serveurs et ordinateurs dans un seul onglet, chaque commande dans
son propre bloc, et aucune clé sur votre appareil. Ce que tTerm Web sait
faire aujourd’hui, comment connecter une machine et ce qui arrive ensuite.

@it tTerm ora funziona nel browser
Tutti i tuoi server e computer in una scheda, ogni comando in un blocco a sé
e nessuna chiave sul tuo dispositivo. Cosa sa fare oggi tTerm Web, come
collegare una macchina e cosa viene dopo.

@pl tTerm działa teraz w przeglądarce
Wszystkie twoje serwery i komputery w jednej karcie, każde polecenie
w osobnym bloku i żadnych kluczy na twoim urządzeniu. Co tTerm Web potrafi
już dziś, jak podłączyć maszynę i co będzie dalej.

@pt-BR O tTerm agora funciona no navegador
Todos os seus servidores e computadores em uma aba, cada comando em um bloco
próprio e nenhuma chave no seu dispositivo. O que o tTerm Web já faz, como
conectar uma máquina e o que vem a seguir.

@tr tTerm artık tarayıcıda çalışıyor
Tüm sunucuların ve bilgisayarların tek bir sekmede, her komut ayrı bir
blokta, cihazında da hiç anahtar yok. İşte tTerm Web'in bugün neler
yapabildiği, bir makinenin nasıl bağlanacağı ve sırada ne olduğu.

@ja tTerm がブラウザーで使えるようになりました
すべてのサーバーとコンピューターを 1 つのタブで。コマンドはそれぞれ独立したブロックになり、デバイスに鍵を置く必要もありません。tTerm Web
で今できること、マシンの接続方法、今後の予定を紹介します。

@ko tTerm, 이제 브라우저에서
모든 서버와 컴퓨터를 탭 하나에서, 명령은 하나하나 별도의 블록으로, 기기에는
키 없이. tTerm Web이 지금 할 수 있는 일, 머신 연결 방법, 앞으로의 계획을
소개해요.

@zh-CN tTerm 现在能在浏览器里用了
所有服务器和电脑都在一个标签页中，每条命令自成一个块，设备上无需任何密钥。tTerm Web 现在能做什么、如何连接机器，以及接下来的计划。

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

@de Fenster auf einem Computer sind jetzt unabhängig
Auf einem Server war jedes Fenster schon immer ein eigenes Terminal. Auf
einem Computer mit dem Agenten teilten sich alle Fenster eine Shell: Ein cd
in einem Fenster galt auch für die anderen, und während in einem Fenster ein
Programm lief, mussten die übrigen warten. Jetzt bekommt jedes Fenster seine
eigene Shell, genau wie auf einem Server. Du kannst in einem Fenster einen
Dev-Server laufen lassen und in einem anderen arbeiten.

@es Las ventanas en una computadora ya son independientes
En un servidor, cada ventana siempre ha sido una terminal independiente. En
una computadora con el agente, todas las ventanas compartían un mismo shell:
un cd en una movía también a las demás, y mientras un programa se ejecutaba
en una ventana, el resto tenía que esperar. Ahora cada ventana tiene su
propio shell, igual que en un servidor. Puedes tener un servidor de
desarrollo en marcha en una ventana y trabajar en otra.

@fr Sur un ordinateur, les fenêtres sont désormais indépendantes
Sur un serveur, chaque fenêtre a toujours été un terminal à part entière.
Sur un ordinateur équipé de l’agent, toutes les fenêtres partageaient un
seul shell : un cd dans l’une déplaçait aussi les autres, et tant qu’un
programme tournait dans une fenêtre, les autres devaient attendre.
Désormais, chaque fenêtre a son propre shell, comme sur un serveur. Vous
pouvez laisser tourner un serveur de développement dans une fenêtre et
travailler dans une autre.

@it Le finestre su un computer ora sono indipendenti
Su un server ogni finestra è sempre stata un terminale a sé. Su un computer
con l'agente, invece, tutte le finestre condividevano un'unica shell: un cd
in una spostava anche le altre, e mentre in una finestra girava un
programma, le altre dovevano aspettare. Ora ogni finestra ha la sua shell,
proprio come su un server. Puoi lasciare un server di sviluppo in esecuzione
in una finestra e lavorare in un'altra.

@pl Okna na komputerze są teraz niezależne
Na serwerze każde okno zawsze było osobnym terminalem. Na komputerze
z agentem wszystkie okna dzieliły jedną powłokę: cd w jednym przenosiło też
pozostałe, a gdy w jednym oknie działał program, reszta musiała czekać.
Teraz każde okno ma własną powłokę, tak jak na serwerze. Możesz mieć
w jednym oknie uruchomiony serwer deweloperski i pracować w drugim.

@pt-BR As janelas no computador agora são independentes
Num servidor, cada janela sempre foi um terminal à parte. Num computador com
o agente, todas as janelas compartilhavam um único shell: um cd em uma delas
movia as outras também, e, enquanto um programa rodava numa janela, as
demais tinham que esperar. Agora cada janela tem o seu próprio shell, como
num servidor. Você pode deixar um servidor de desenvolvimento rodando numa
janela e trabalhar em outra.

@tr Bilgisayardaki pencereler artık birbirinden bağımsız
Sunucuda her pencere baştan beri ayrı bir terminaldi. Ajan kurulu bir
bilgisayarda ise tüm pencereler tek bir kabuğu paylaşıyordu: birinde
yaptığın cd ötekilerin de dizinini değiştiriyordu, bir pencerede program
çalışırken diğerleri beklemek zorundaydı. Artık her pencerenin, sunucuda
olduğu gibi, kendi kabuğu var. Bir pencerede geliştirme sunucusunu çalışır
halde tutup diğerinde çalışabilirsin.

@ja コンピューターのウィンドウが互いに独立しました
サーバーでは以前から、ウィンドウはそれぞれ独立したターミナルでした。一方、エージェントを入れたコンピューターでは、すべてのウィンドウが
1 つのシェルを共有していました。1 つのウィンドウで cd
するとほかのウィンドウのディレクトリも変わり、どこかでプログラムが動いているあいだ、ほかのウィンドウは待たされていました。今後は、サーバーと同じく、ウィンドウごとに専用のシェルが割り当てられます。あるウィンドウで開発サーバーを動かしたまま、別のウィンドウで作業できます。

@ko 독립된 창, 이제 컴퓨터에서도
서버에서는 원래부터 창 하나하나가 별도의 터미널이었어요. 에이전트를 쓰는
컴퓨터에서는 모든 창이 셸 하나를 함께 썼어요. 한 창에서 cd를 하면 다른 창도
같이 이동했고, 한 창에서 프로그램이 실행되는 동안 나머지 창은 기다려야
했어요. 이제는 서버와 똑같이 창마다 자기 셸이 있어요. 한 창에서 개발 서버를
띄워 두고 다른 창에서 작업할 수 있어요.

@zh-CN 电脑上的窗口现在彼此独立
在服务器上，每个窗口一直都是独立的终端。而在装有代理的电脑上，所有窗口共用一个 shell：在一个窗口里
cd，其他窗口也会跟着切换目录；一个窗口里有程序在运行时，其余窗口只能等待。现在每个窗口都有自己的
shell，和服务器上一样。你可以在一个窗口里运行开发服务器，同时在另一个窗口里工作。

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

@de Du kannst einem Befehl antworten, während er läuft
Wenn ein Programm Continue? (Y/n) fragte, konntest du bisher nicht
antworten: Deine Nachricht ging erst raus, wenn der Befehl fertig war. Jetzt
geht alles, was du tippst, während ein Befehl läuft, direkt an dessen
Eingabe, so wie in einem Terminal. Der Bot markiert so eine Nachricht mit 👌.

@es Puedes responder a un comando mientras se ejecuta
Cuando un programa preguntaba «Continue? (Y/n)», no había forma de
responder: tu mensaje no se enviaba hasta que terminaba el comando. Ahora
todo lo que escribes mientras un comando se ejecuta va a su entrada, igual
que en una terminal. El bot marca esos mensajes con 👌.

@fr Vous pouvez répondre à une commande en cours d’exécution
Quand un programme demandait Continue? (Y/n), il n’y avait aucun moyen de
répondre : votre message ne partait qu’à la fin de la commande. Désormais,
tout ce que vous tapez pendant qu’une commande s’exécute est envoyé à son
entrée, comme dans un terminal. Le bot marque un tel message d’un 👌.

@it Puoi rispondere a un comando mentre è in esecuzione
Quando un programma chiedeva Continue? (Y/n), non c'era modo di rispondere:
il tuo messaggio non partiva finché il comando non era finito. Ora tutto
quello che scrivi mentre un comando è in esecuzione gli arriva in input,
come succederebbe in un terminale. Il bot segna questi messaggi con 👌.

@pl Możesz odpowiedzieć działającemu poleceniu
Wcześniej, gdy program pytał Continue? (Y/n), nie było jak odpowiedzieć:
wiadomość czekała, aż polecenie się skończy. Teraz wszystko, co piszesz
w trakcie działania polecenia, trafia na jego wejście, tak jak w terminalu.
Bot oznacza taką wiadomość reakcją 👌.

@pt-BR Você pode responder a um comando enquanto ele roda
Quando um programa perguntava Continue? (Y/n), não havia como responder: a
sua mensagem só era enviada depois que o comando terminava. Agora, tudo o
que você digita enquanto um comando está rodando vai para a entrada dele,
como aconteceria num terminal. O bot marca essas mensagens com 👌.

@tr Komut çalışırken ona yanıt verebilirsin
Eskiden bir program Continue? (Y/n) diye sorduğunda yanıt vermenin yolu
yoktu: komut bitene kadar mesajın gönderilmiyordu. Artık komut çalışırken
yazdığın her şey, terminalde olduğu gibi komutun girişine gidiyor. Bot böyle
bir mesajı 👌 ile işaretliyor.

@ja 実行中のコマンドに応答できるようになりました
これまでは、プログラムに Continue? (Y/n)
と聞かれても、答える方法がありませんでした。コマンドが終わるまでメッセージが送信されなかったためです。今後は、コマンドの実行中に入力した内容が、普通のターミナルと同じようにそのコマンドへの入力として渡されます。ボットはそうしたメッセージに
👌 のリアクションを付けます。

@ko 실행 중인 명령에 답하기
예전에는 프로그램이 Continue? (Y/n) 같은 질문을 해도 답할 방법이 없었어요.
명령이 끝날 때까지 메시지가 전송되지 않았거든요. 이제는 명령이 실행되는 동안
입력한 내용이 터미널에서처럼 그 명령의 입력으로 들어가요. 봇은 이런 메시지에
👌 반응을 남겨요.

@zh-CN 命令运行时也能回复它了
以前程序询问 Continue? (Y/n)
时，你没法回复：命令结束之前，你的消息发不出去。现在，命令运行期间你输入的任何内容都会作为它的输入，就像在终端里一样。机器人会用 👌 标记这样的消息。

## 2026-09-17 bot /blog/your-shell/

@en The agent now runs your shell: bash or zsh
It used to start bash no matter what. On macOS, where zsh has been the
default since 2019, that meant somebody else's environment: half of what you
had installed could not be found.

@ru Агент запускает твой шелл: bash или zsh
Раньше агент запускал bash, что бы ни было. На macOS, где zsh стоит по
умолчанию с 2019 года, это означало чужое окружение: половина того, что у
тебя установлено, не находилась.

@de Der Agent startet jetzt deine Shell: bash oder zsh
Bisher startete der Agent in jedem Fall bash. Auf macOS, wo zsh seit 2019
Standard ist, bedeutete das eine fremde Umgebung: Die Hälfte dessen, was
du installiert hattest, wurde nicht gefunden.

@es El agente ahora ejecuta tu shell: bash o zsh
Antes, el agente iniciaba bash pasara lo que pasara. En macOS, donde zsh es
el shell predeterminado desde 2019, eso significaba un entorno ajeno: la
mitad de lo que tenías instalado no se encontraba.

@fr L’agent lance désormais votre shell : bash ou zsh
Auparavant, l’agent lançait bash quoi qu’il arrive. Sur macOS, où zsh est le
shell par défaut depuis 2019, cela voulait dire un environnement qui n’était
pas le vôtre : la moitié de ce que vous aviez installé restait introuvable.

@it Ora l'agente avvia la tua shell: bash o zsh
Prima l'agente avviava bash in ogni caso. Su macOS, dove zsh è la shell
predefinita dal 2019, questo significava un ambiente che non era il tuo:
metà di ciò che avevi installato risultava introvabile.

@pl Agent uruchamia teraz twoją powłokę: bash lub zsh
Wcześniej agent zawsze uruchamiał bash, bez względu na wszystko. Na macOS,
gdzie od 2019 roku domyślną powłoką jest zsh, oznaczało to cudze środowisko:
nie było widać połowy tego, co masz zainstalowane.

@pt-BR O agente agora roda o seu shell: bash ou zsh
Antes, o agente iniciava sempre o bash. No macOS, onde o zsh é o padrão
desde 2019, isso significava um ambiente que não era o seu: metade do que
você tinha instalado não era encontrada.

@tr Ajan artık senin kabuğunu çalıştırıyor: bash ya da zsh
Eskiden ajan ne olursa olsun bash başlatıyordu. Varsayılan kabuğun 2019'dan
beri zsh olduğu macOS'te bu, başka birinin ortamı demekti: kurduğun şeylerin
yarısı bulunamıyordu.

@ja エージェントがいつものシェルを起動するようになりました：bash でも zsh でも
これまでエージェントは、ユーザーのシェルにかかわらず常に bash を起動していました。2019年から zsh が標準になっている macOS
では、それは他人の環境で作業するのと同じことで、インストールしたもののうち半分は見つかりませんでした。

@ko 이제 에이전트가 bash든 zsh든 내 셸을 실행해요
예전에는 에이전트가 무조건 bash를 실행했어요. 2019년부터 기본 셸이 zsh인
macOS에서는 남의 환경이나 마찬가지였어요. 설치해 둔 것의 절반을 찾지
못했으니까요.

@zh-CN 代理现在运行你的 bash 或 zsh
以前它不管怎样都启动 bash。在 macOS 上，zsh 从 2019年起就是默认
shell，这意味着你用的是别人的环境：你装过的东西，有一半都找不到。

## 2026-09-03 site /blog/verified-on-github/

@en tTerm is now a verified organisation on GitHub
github.com/tterm-net carries a Verified badge: GitHub confirmed that the
organisation and tterm.net are the same people.

@ru tTerm теперь проверенная организация на GitHub
У github.com/tterm-net теперь есть галочка Verified: GitHub подтвердил, что
за организацией и tterm.net стоят одни и те же люди.

@de tTerm ist jetzt eine verifizierte Organisation auf GitHub
github.com/tterm-net trägt jetzt das Verified-Badge: GitHub hat bestätigt,
dass hinter der Organisation und tterm.net dieselben Leute stehen.

@es tTerm ya es una organización verificada en GitHub
github.com/tterm-net tiene la insignia Verified: GitHub confirma que detrás
de la organización y de tterm.net están las mismas personas.

@fr tTerm est désormais une organisation vérifiée sur GitHub
github.com/tterm-net porte le badge Verified : GitHub a confirmé que
derrière l’organisation et tterm.net se trouvent les mêmes personnes.

@it tTerm ora è un'organizzazione verificata su GitHub
github.com/tterm-net ha il badge Verified: GitHub ha confermato che dietro
l'organizzazione e dietro tterm.net ci sono le stesse persone.

@pl tTerm jest teraz zweryfikowaną organizacją na GitHubie
github.com/tterm-net ma odznakę Verified: GitHub potwierdził, że za
organizacją i tterm.net stoją ci sami ludzie.

@pt-BR O tTerm agora é uma organização verificada no GitHub
O github.com/tterm-net tem o selo Verified: o GitHub confirmou que por trás
da organização e do tterm.net estão as mesmas pessoas.

@tr tTerm artık GitHub'da doğrulanmış bir organizasyon
github.com/tterm-net artık Verified rozeti taşıyor: GitHub, organizasyonun
ve tterm.net sitesinin arkasında aynı insanların olduğunu doğruladı.

@ja tTerm が GitHub の検証済み組織になりました
github.com/tterm-net に Verified バッジが付きました。この組織と tterm.net
の運営者が同じであることを、GitHub が確認しました。

@ko GitHub 인증 조직이 된 tTerm
github.com/tterm-net에 Verified 배지가 붙었어요. GitHub가 이 조직과
tterm.net을 같은 사람들이 운영한다는 걸 확인했어요.

@zh-CN tTerm 成为 GitHub 认证组织
github.com/tterm-net 带有 Verified 徽章：GitHub 已确认，这个组织和 tterm.net 背后是同一批人。

## 2026-09-01 bot /blog/several-terminals/

@en Several terminals per machine
You can now keep more than one terminal open on the same server – one
tailing a log, another doing the work. They show up as separate lines in
/use, each with its own shell: a cd in one leaves the other where it was.

@ru Несколько терминалов на одной машине
Теперь на одном сервере можно держать открытыми несколько терминалов: в
одном идёт лог, в другом ты работаешь. В /use они видны отдельными строками,
и у каждого свой шелл: cd в одном не сдвигает другой.

@de Mehrere Terminals pro Maschine
Du kannst jetzt mehr als ein Terminal auf demselben Server offen halten: In
einem läuft ein Log mit, im anderen arbeitest du. Sie erscheinen als eigene
Zeilen in /use, jedes mit seiner eigenen Shell: Ein cd im einen lässt das
andere, wo es war.

@es Varias terminales por máquina
Ahora puedes tener más de una terminal abierta en el mismo servidor: en una
sigues un log y en la otra trabajas. Aparecen como líneas separadas en /use,
cada una con su propio shell: un cd en una deja la otra donde estaba.

@fr Plusieurs terminaux par machine
Vous pouvez désormais garder plusieurs terminaux ouverts sur le même
serveur : l’un qui suit un journal, l’autre pour travailler. Ils
apparaissent comme des lignes distinctes dans /use, chacun avec son propre
shell : un cd dans l’un laisse l’autre là où il était.

@it Più terminali per macchina
Ora puoi tenere aperti più terminali sullo stesso server: in uno scorre un
log, nell'altro lavori. In /use compaiono come righe separate, ognuno con la
sua shell: un cd in uno lascia l'altro dov'era.

@pl Kilka terminali na jednej maszynie
Na jednym serwerze możesz teraz mieć otwartych kilka terminali: w jednym
śledzisz log, w drugim pracujesz. W /use widać je jako osobne wiersze, każdy
z własną powłoką: cd w jednym zostawia drugi tam, gdzie był.

@pt-BR Vários terminais por máquina
Agora você pode manter mais de um terminal aberto no mesmo servidor: um
acompanhando um log, outro fazendo o trabalho. Eles aparecem como linhas
separadas em /use, cada um com o seu próprio shell: um cd num deles deixa o
outro onde estava.

@tr Bir makinede birden fazla terminal
Artık aynı sunucuda birden fazla terminali açık tutabilirsin: birinde log
akarken diğerinde işini yaparsın. Her biri /use komutunda ayrı bir satırda
görünür ve kendi kabuğuna sahiptir: birinde yaptığın cd diğerini olduğu
yerde bırakır.

@ja 1 台のマシンで複数のターミナル
同じサーバーで、複数のターミナルを開いておけるようになりました。1 つでログを追い、もう 1 つで作業する、といった使い方ができます。/use
では別々の行として表示され、それぞれが専用のシェルを持ちます。片方で cd しても、もう片方のディレクトリは変わりません。

@ko 머신 하나에 터미널 여러 개
이제 같은 서버에서 터미널을 여러 개 열어 둘 수 있어요. 하나로는 로그를
지켜보고, 다른 하나로는 작업하는 식이에요. /use에서는 각각 별도의 줄로
보이고, 저마다 자기 셸이 있어요. 한 터미널에서 cd를 해도 다른 터미널은 원래
위치에 그대로 있어요.

@zh-CN 一台机器可以开多个终端了
现在，同一台服务器上可以同时打开多个终端：一个用来跟踪日志，另一个用来干活。它们在 /use 中显示为单独的行，各有自己的 shell：在一个终端里
cd，另一个仍停在原处。

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

@de tTerm ist gestartet
Ein Terminal für deine Server, direkt hier in Telegram. Tipp einen Befehl:
Er läuft auf deiner Maschine, und die Antwort kommt als Nachricht zurück,
mit Exit-Code, Arbeitsverzeichnis und git-Branch. Die Shell merkt sich, wo
du aufgehört hast.

@es tTerm ya está disponible
Una terminal para tus servidores, aquí mismo, en Telegram. Escribe un
comando: se ejecuta en tu máquina y la respuesta llega como un mensaje con
el código de salida, el directorio de trabajo y la rama de git. El shell
recuerda dónde lo dejaste.

@fr tTerm est en ligne
Un terminal pour vos serveurs, directement dans Telegram. Tapez une
commande, elle s’exécute sur votre machine, et la réponse revient sous forme
de message avec le code de retour, le répertoire de travail et la branche
git. Le shell se souvient de l’endroit où vous vous étiez arrêté.

@it tTerm è online
Un terminale per i tuoi server, proprio qui su Telegram. Scrivi un comando:
viene eseguito sulla tua macchina e la risposta torna come messaggio, con il
codice di uscita, la directory di lavoro e il branch git. La shell ricorda
dove eri rimasto.

@pl tTerm wystartował
Terminal dla twoich serwerów, prosto w Telegramie. Wpisz polecenie: wykona
się na twojej maszynie, a odpowiedź przyjdzie jako wiadomość z kodem
wyjścia, katalogiem roboczym i gałęzią Gita. Powłoka pamięta, na czym
stanęło.

@pt-BR O tTerm está no ar
Um terminal para os seus servidores, aqui mesmo no Telegram. Digite um
comando: ele roda na sua máquina, e a resposta volta como uma mensagem com o
código de retorno, o diretório de trabalho e a branch do git. O shell lembra
onde você parou.

@tr tTerm yayında
Sunucuların için bir terminal, tam burada, Telegram'da. Bir komut yaz:
makinende çalışır, yanıt da çıkış kodu, çalışma dizini ve git dalıyla
birlikte mesaj olarak gelir. Kabuk kaldığın yeri hatırlar.

@ja tTerm を公開しました
サーバーのためのターミナルを、ここ Telegram で。コマンドを入力するとマシン上で実行され、終了コード、作業ディレクトリ、git
のブランチを添えたメッセージで結果が返ってきます。シェルは、前回作業を終えたところを覚えています。

@ko tTerm 출시
서버를 위한 터미널을 바로 이곳 Telegram에서 쓸 수 있어요. 명령을 입력하면 내
머신에서 실행되고, 종료 코드, 작업 디렉터리, git 브랜치가 담긴 메시지로
결과가 돌아와요. 셸은 마지막으로 작업하던 위치를 기억해요.

@zh-CN tTerm 上线了
为你的服务器准备的终端，就在 Telegram 里。输入一条命令，它会在你的机器上运行，结果以消息形式返回，附带退出码、工作目录和 git
分支。shell 会记住你上次停在哪里。

## 2026-08-28 bot

@en The bot on its own server
The bot moved to its own server and no longer depends on a laptop being
open. Source for the bot and the agent is public.

@ru Бот на своём сервере
Бот переехал на свой сервер и больше не зависит от того, открыт ли ноутбук.
Исходники бота и агента открыты.

@de Der Bot auf eigenem Server
Der Bot ist auf einen eigenen Server umgezogen und hängt nicht mehr davon
ab, ob ein Laptop aufgeklappt ist. Der Quellcode von Bot und Agent ist
öffentlich.

@es El bot, en su propio servidor
El bot se mudó a su propio servidor y ya no depende de que haya un portátil
abierto. El código fuente del bot y del agente es público.

@fr Le bot sur son propre serveur
Le bot tourne désormais sur son propre serveur et ne dépend plus d’un
ordinateur portable resté ouvert. Le code source du bot et de l’agent est
public.

@it Il bot su un server tutto suo
Il bot si è trasferito su un server tutto suo e non dipende più da un
portatile rimasto aperto. Il codice sorgente del bot e dell'agente è
pubblico.

@pl Bot na własnym serwerze
Bot przeniósł się na własny serwer i nie zależy już od tego, czy laptop jest
otwarty. Kod źródłowy bota i agenta jest publicznie dostępny.

@pt-BR O bot em servidor próprio
O bot se mudou para um servidor próprio e não depende mais de um notebook
aberto. O código-fonte do bot e do agente é público.

@tr Bot kendi sunucusunda
Bot kendi sunucusuna taşındı ve artık bir dizüstünün açık olmasına bağlı
değil. Botun ve ajanın kaynak kodu herkese açık.

@ja ボットを専用サーバーへ移行
ボットは専用のサーバーに移り、ノートパソコンが開いているかどうかに左右されなくなりました。ボットとエージェントのソースコードは公開されています。

@ko 전용 서버로 옮긴 봇
봇이 전용 서버로 옮겨서, 이제 노트북이 열려 있지 않아도 작동해요. 봇과
에이전트의 소스 코드는 공개되어 있어요.

@zh-CN 机器人有了自己的服务器
机器人已迁移到自己的服务器上，不再依赖某台笔记本是否开着。机器人和代理的源代码已经公开。

## 2026-08-26 bot

@en Buttons in messages
Machine list, menus and confirmations moved to buttons inside messages. A
machine that cannot be reached is greyed out instead of leading to an error.

@ru Кнопки в сообщениях
Список машин, меню и подтверждения переехали на кнопки внутри сообщений.
Машина не на связи теперь серая, а не ведёт в ошибку.

@de Buttons in Nachrichten
Maschinenliste, Menüs und Bestätigungen laufen jetzt über Buttons direkt in
den Nachrichten. Eine Maschine, die nicht erreichbar ist, wird ausgegraut,
statt zu einem Fehler zu führen.

@es Botones en los mensajes
La lista de máquinas, los menús y las confirmaciones pasaron a botones
dentro de los mensajes. Una máquina sin conexión aparece en gris en lugar de
llevar a un error.

@fr Des boutons dans les messages
La liste des machines, les menus et les confirmations passent désormais par
des boutons dans les messages. Une machine injoignable apparaît en grisé au
lieu de mener à une erreur.

@it Pulsanti nei messaggi
L'elenco delle macchine, i menu e le conferme sono passati a pulsanti dentro
i messaggi. Una macchina non raggiungibile appare in grigio invece di
portare a un errore.

@pl Przyciski w wiadomościach
Lista maszyn, menu i potwierdzenia działają teraz jako przyciski
w wiadomościach. Niedostępna maszyna jest wyszarzona i nie prowadzi już do
błędu.

@pt-BR Botões nas mensagens
A lista de máquinas, os menus e as confirmações passaram para botões dentro
das mensagens. Uma máquina inacessível aparece em cinza, em vez de levar a
um erro.

@tr Mesajlarda düğmeler
Makine listesi, menüler ve onaylar mesajların içindeki düğmelere taşındı.
Ulaşılamayan bir makine artık hataya götürmek yerine gri görünüyor.

@ja メッセージ内のボタン
マシンの一覧、メニュー、確認が、メッセージ内のボタンになりました。接続できないマシンは、エラーになるのではなくグレーで表示されます。

@ko 메시지 속 버튼
머신 목록, 메뉴, 확인 요청이 메시지 안의 버튼으로 옮겨졌어요. 연결할 수 없는
머신은 오류로 이어지지 않고 회색으로 표시돼요.

@zh-CN 消息中的按钮
机器列表、菜单和确认操作都改成了消息里的按钮。无法连接的机器会显示为灰色，不会再点进去就报错。

## 2026-08-25 bot

@en Access with a time limit
Shared access with time limits. Expired access closes itself and both sides
are told. Owners can export the full command history as a file.

@ru Доступ со сроком
Доступ для других со сроком. Истёкший закрывается сам, и обоим приходит
уведомление. Всю историю команд можно выгрузить файлом.

@de Befristeter Zugriff
Geteilter Zugriff mit Zeitlimit. Nach Ablauf endet der Zugriff von selbst,
und beide Seiten werden benachrichtigt. Als Eigentümer kannst du den
gesamten Befehlsverlauf als Datei exportieren.

@es Acceso con límite de tiempo
Acceso compartido con límite de tiempo. El acceso caducado se cierra solo y
se avisa a ambas partes. Los propietarios pueden exportar el historial
completo de comandos a un archivo.

@fr Un accès limité dans le temps
Partage d’accès limité dans le temps. Un accès expiré se ferme de lui-même,
et les deux parties en sont averties. Les propriétaires peuvent exporter
tout l’historique des commandes dans un fichier.

@it Accesso a tempo
Accesso condiviso con scadenza. Quando scade, l'accesso si chiude da solo ed
entrambe le parti ricevono un avviso. I proprietari possono esportare
l'intera cronologia dei comandi in un file.

@pl Dostęp na czas określony
Dostęp dla innych osób z limitem czasu. Wygasły dostęp zamyka się sam,
a obie strony dostają powiadomienie. Właściciele mogą wyeksportować całą
historię poleceń do pliku.

@pt-BR Acesso por tempo limitado
Acesso compartilhado com prazo. Quando o prazo acaba, o acesso se encerra
sozinho, e os dois lados recebem um aviso. Os donos podem exportar todo o
histórico de comandos em um arquivo.

@tr Süreli erişim
Başkalarına süreli erişim verebilirsin. Süresi dolan erişim kendiliğinden
kapanır ve iki tarafa da bildirilir. Makine sahipleri tüm komut geçmişini
dosya olarak dışa aktarabilir.

@ja 期限付きのアクセス
アクセスを共有するときに期限を設定できるようになりました。期限が切れたアクセスは自動的に閉じられ、双方に通知が届きます。オーナーは、コマンド履歴全体をファイルとして書き出せます。

@ko 기한이 있는 접근 권한
다른 사람과 공유하는 접근 권한에 기한을 정할 수 있어요. 기한이 지나면 접근
권한이 자동으로 회수되고, 양쪽 모두에게 알림이 가요. 소유자는 전체 명령
기록을 파일로 내보낼 수 있어요.

@zh-CN 限时访问
共享访问可以设定期限。到期后访问会自动关闭，双方都会收到通知。所有者可以把完整的命令历史导出为文件。

## 2026-08-23 bot

@en Computers through an agent
Computers can be connected too, through a small agent that dials out. macOS
and Linux for now.

@ru Компьютеры через агента
Подключаются и компьютеры: через маленький агент, который сам держит связь.
Пока macOS и Linux.

@de Computer über einen Agenten
Auch Computer lassen sich jetzt verbinden, über einen kleinen Agenten, der
die Verbindung selbst nach außen aufbaut. Vorerst macOS und Linux.

@es Computadoras mediante un agente
También se pueden conectar computadoras, mediante un pequeño agente que
inicia la conexión por sí mismo. Por ahora, macOS y Linux.

@fr Des ordinateurs via un agent
Les ordinateurs peuvent aussi être connectés, grâce à un petit agent qui se
connecte lui-même vers l’extérieur. Pour l’instant, sous macOS et Linux.

@it Computer tramite un agente
Si possono collegare anche i computer, tramite un piccolo agente che apre da
sé la connessione verso l'esterno. Per ora macOS e Linux.

@pl Komputery przez agenta
Można też podłączyć komputery przez niewielkiego agenta, który sam nawiązuje
połączenie. Na razie macOS i Linux.

@pt-BR Computadores por meio de um agente
Também dá para conectar computadores, por meio de um pequeno agente que
inicia a conexão sozinho. Por enquanto, macOS e Linux.

@tr Ajan aracılığıyla bilgisayarlar
Artık bilgisayarlar da bağlanabiliyor: dışarıya kendisi bağlanan küçük bir
ajan aracılığıyla. Şimdilik macOS ve Linux.

@ja エージェント経由でコンピューターも
自分から外へ接続する小さなエージェントを介して、コンピューターも接続できるようになりました。今のところ macOS と Linux に対応しています。

@ko 에이전트로 연결하는 컴퓨터
스스로 밖으로 연결하는 작은 에이전트로 컴퓨터도 연결할 수 있어요. 지금은
macOS와 Linux만 지원해요.

@zh-CN 通过代理连接电脑
现在也可以连接电脑了，方法是安装一个主动向外连接的小型代理。目前支持 macOS 和 Linux。
