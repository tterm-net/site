/* tTerm site: the menus in the header (the one on narrow screens and the
   language), the demo of tTerm Web on the main page and in posts, its
   window standing up as the main page scrolls, and a soft light under the
   pointer on cards. No dependencies, nothing loaded from anywhere else: the
   Privacy Policy promises the pages load nothing from third parties. */
(function () {
  'use strict';

  /* ------------------------------------------------------------ menus */

  // Both menus are <details>, so they open with no script at all. Here they
  // only close: after a tap on one of their links, on Escape, on a tap
  // elsewhere, and when the other one opens.
  var menus = [];

  function initMenu(menu) {
    var summary = menu.querySelector('summary');
    menus.push(menu);
    menu.addEventListener('toggle', function () {
      if (!menu.open) return;
      menus.forEach(function (other) { if (other !== menu) other.open = false; });
    });
    menu.addEventListener('click', function (event) {
      if (event.target.closest && event.target.closest('.menu-panel a, .lang-menu a')) menu.open = false;
    });
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && menu.open) {
        menu.open = false;
        summary.focus();
      }
    });
    document.addEventListener('click', function (event) {
      if (menu.open && !menu.contains(event.target)) menu.open = false;
    });
  }

  /* ------------------------------------------------------------- demo */

  // tTerm Web at work, as in 0.1.2: a deploy on web-01 in Client X, with its
  // release checklist ticked off in a note beside it, then Cmd+K opens a
  // terminal on api-prod in Acme. Every project in its color, the whole
  // block tinted, as the account page lets you choose. The interface is in
  // English, as in the product. One tick is 70 ms; the story loops in about
  // 35 seconds.

  var DIM = 'dim', OK = 'ok', INK = 'ink';
  var STORY = [
    { tab: 'deploy', cmd: 'git pull', time: '1.4 s', out: [
      ['Updating 3f2c1a9..8d4e7b2', DIM],
      ['Fast-forward', DIM],
      [' src/server.ts | 12 +++++++-----', DIM],
      [' src/routes.ts |  4 ++--', DIM],
      [' 2 files changed, 9 insertions(+), 7 deletions(-)', DIM]] },
    { tab: 'deploy', cmd: 'npm run build', time: '4.2 s', out: [
      ['> app@2.4.0 build', DIM],
      ['> vite build', DIM],
      ['vite v7.1.4 building for production...', DIM],
      ['✓ 412 modules transformed.', OK],
      ['dist/index.html                0.46 kB', DIM],
      ['dist/assets/index.js         184.20 kB', DIM],
      ['✓ built in 3.81s', OK]] },
    { note: 1 },
    { tab: 'deploy', cmd: 'sudo systemctl restart app', time: '0.9 s', out: [] },
    { tab: 'deploy', cmd: 'systemctl is-active app', time: '0.0 s', out: [['active', OK]] },
    { note: 2 },
    { palette: 'api' },
    { tab: 'api', cmd: 'docker compose ps', time: '0.3 s', out: [
      ['NAME        IMAGE            STATUS', DIM],
      ['api-web-1   acme/api:2.4.0   Up 23 days', INK],
      ['api-db-1    postgres:17      Up 23 days (healthy)', INK]] }
  ];

  // The release checklist in Client X: the first item was ticked before
  // the story starts, two more are ticked as the deploy goes.
  var CHECKLIST = [
    ['Freeze merges to main', '10:02'],
    ['Pull and build on web-01', '10:14'],
    ['Restart the service', '10:15'],
    ['Tell the team in #releases', '']
  ];

  // Ticks: a typed character, the pause before Enter, an output line, the
  // pause after a command; the palette opening, a character, the pick; a
  // note in front before its item is ticked, and after.
  var TYPE = 2, ENTER = 6, LINE = 3, AFTER = 18, END = 60;
  var P_OPEN = 8, P_CHAR = 4, P_PICK = 12;
  var N_TICK = 14, N_HOLD = 26;

  var SPANS = [];
  var TOTAL = 0;
  STORY.forEach(function (step) {
    var length = step.palette ? P_OPEN + step.palette.length * P_CHAR + P_PICK
      : step.note !== undefined ? N_TICK + N_HOLD
      : step.cmd.length * TYPE + ENTER + step.out.length * LINE + AFTER;
    SPANS.push({ start: TOTAL, end: TOTAL + length });
    TOTAL += length;
  });
  TOTAL += END;

  // For visitors who asked for less motion: one still frame, the note in
  // front just after its second item was ticked.
  var STILL = SPANS[2].end - 1;

  var WHERE = { deploy: { cwd: '~/app', branch: 'main' }, api: { cwd: '~/acme', branch: 'main' } };

  // What is on screen at a given tick. The terminal on web-01 already has a
  // few commands behind it, so the window is full from the first frame: on
  // the main page only its top is on the first screen.
  function frame(tick) {
    var t = tick % TOTAL;
    var feeds = {
      deploy: [
        { cmd: 'uptime', meta: '0.0 s', run: false,
          lines: [[' 10:01:58 up 41 days,  2:13,  1 user,  load average: 0.08, 0.12, 0.10', DIM]] },
        { cmd: 'git log --oneline -3', meta: '0.0 s', run: false,
          lines: [['3f2c1a9 Retry the webhook on 502', DIM],
                  ['b81e0d4 Cache the pricing table', DIM],
                  ['9c4a7f2 Bump vite to 7.1', DIM]] },
        { cmd: 'df -h /', meta: '0.0 s', run: false,
          lines: [['Filesystem      Size  Used Avail Use% Mounted on', DIM],
                  ['/dev/vda1        78G   31G   47G  40% /', DIM]] },
        { cmd: 'ls', meta: '0.0 s', run: false,
          lines: [['README.md  docker-compose.yml  package.json  src', DIM]] },
        { cmd: 'git status -sb', meta: '0.1 s', run: false,
          lines: [['## main...origin/main [behind 2]', DIM]] }
      ],
      api: [
        { cmd: 'uptime', meta: '0.0 s', run: false,
          lines: [[' 09:41:12 up 23 days,  4:02,  1 user,  load average: 0.21, 0.18', DIM]] }
      ]
    };
    var s = { tab: 'deploy', typed: '', palette: false, query: '', picked: false,
      ticked: [true, false, false, false], fresh: -1 };

    STORY.forEach(function (step, i) {
      var span = SPANS[i];
      if (t < span.start) return;
      var local = t - span.start;
      if (step.palette) {
        if (t >= span.end) { s.tab = 'api'; return; }
        s.palette = true;
        if (local >= P_OPEN) {
          s.query = step.palette.slice(0, Math.min(step.palette.length,
            Math.floor((local - P_OPEN) / P_CHAR) + 1));
        }
        s.picked = local >= P_OPEN + step.palette.length * P_CHAR;
        return;
      }
      if (step.note !== undefined) {
        s.tab = 'note';
        if (local >= N_TICK) s.ticked[step.note] = true;
        if (local >= N_TICK && t < span.end) s.fresh = step.note;
        return;
      }
      s.tab = step.tab;
      s.typed = '';
      var typeEnd = step.cmd.length * TYPE;
      var runStart = typeEnd + ENTER;
      var outEnd = runStart + step.out.length * LINE;
      if (local < typeEnd) { s.typed = step.cmd.slice(0, Math.floor(local / TYPE)); return; }
      if (local < runStart) { s.typed = step.cmd; return; }
      var done = local >= outEnd + 2;
      var shown = done ? step.out.length
        : Math.min(step.out.length, Math.floor((local - runStart) / LINE));
      feeds[step.tab].push({ cmd: step.cmd, meta: done ? step.time : 'running', run: !done,
        lines: step.out.slice(0, shown) });
    });

    // The terminal in front, or the one the note was opened beside.
    s.term = s.tab === 'api' ? 'api' : 'deploy';
    s.feed = feeds[s.term].slice(-5);
    s.busy = { deploy: feeds.deploy.some(running), api: feeds.api.some(running) };
    // The terminal on api-prod exists once it is picked in the palette.
    s.apiOpen = s.tab === 'api' || s.picked;
    s.done = s.ticked.filter(Boolean).length;
    return s;
  }

  function running(block) { return block.run; }

  var ESCAPES = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' };
  function esc(text) {
    return String(text).replace(/[&<>"]/g, function (c) { return ESCAPES[c]; });
  }

  function svg(paths) { return '<svg viewBox="0 0 24 24" aria-hidden="true">' + paths + '</svg>'; }
  var ICON = {
    server: svg('<rect x="3" y="4" width="18" height="7" rx="2"/><rect x="3" y="13" width="18" height="7" rx="2"/>'),
    computer: svg('<rect x="4" y="5" width="16" height="11" rx="2"/><path d="M2 19h20"/>'),
    terminal: svg('<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 9l3 3-3 3M12 15h5"/>'),
    chevron: svg('<path d="M6 9l6 6 6-6"/>'),
    search: svg('<circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/>'),
    plus: svg('<path d="M12 5v14M5 12h14"/>'),
    lock: svg('<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>'),
    folder: svg('<path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>'),
    folderOpen: svg('<path d="M3 7a2 2 0 0 1 2-2h4l2 2h7a2 2 0 0 1 2 2v1"/><path d="M3 7v10a2 2 0 0 0 2 2h12.5a2 2 0 0 0 1.9-1.4L21 12a1.5 1.5 0 0 0-1.4-2H8.3a2 2 0 0 0-1.9 1.4L3 19"/>'),
    doc: svg('<path d="M7 3h7l5 5v11a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2z"/><path d="M14 3v5h5M9 13h6M9 17h4"/>'),
    list: svg('<path d="M4 6l1.5 1.5L8 5M4 12l1.5 1.5L8 11M4 18l1.5 1.5L8 17M11 6.5h9M11 12.5h9M11 18.5h9"/>'),
    check: svg('<path d="M5 12.5l4.2 4.2L19 7"/>'),
    copy: svg('<rect x="9" y="9" width="11" height="11" rx="2"/><path d="M5 15V6a2 2 0 0 1 2-2h9"/>')
  };

  function dot(busy) { return busy ? '<b class="dot busy"></b>' : '<b class="dot"></b>'; }
  var ME = '<span class="dm-av">DG</span>';

  // The sidebar: each project in its color, with its machines and their
  // terminals, then its notes in folders. What is in front is lit; a
  // running command spins; a checklist shows how much of it is ticked.
  function treeHtml(s) {
    function term(id, name, busy) {
      return '<div class="dm-leaf' + (s.tab === id ? ' on' : '') + '">' + ME +
        '<span class="dm-leaf-name">' + name + '</span>' + (busy ? dot(true) : '') + '</div>';
    }
    function note(id, title, icon, progress) {
      return '<div class="dm-leaf dm-note-leaf' + (s.tab === id ? ' on' : '') + '">' +
        ICON[icon] + '<span class="dm-leaf-name">' + title + '</span>' +
        (progress ? '<span class="dm-prog">' + progress + '</span>' : '') + '</div>';
    }
    function row(icon, name, after) {
      return '<div class="dm-row">' + ICON[icon] + '<span class="dm-row-name">' + name + '</span>' +
        (after || '') + '</div>';
    }
    function label(text) {
      return '<div class="dm-sub"><span>' + text + '</span>' + ICON.plus + '</div>';
    }
    var projects = [
      { code: 'CX', name: 'Client X', color: 'sky', inside:
        label('Machines') +
        '<div class="dm-group-in">' + row('server', 'web-01') +
          term('deploy', 'deploy', s.busy.deploy) + term('logs', 'logs', false) + '</div>' +
        label('Notes') +
        '<div class="dm-group-in">' + row('folderOpen', 'Runbooks') +
          note('note', 'Release checklist', 'list', s.done + '/' + CHECKLIST.length) +
          note('rollback', 'Rollback', 'doc', '') + '</div>' },
      { code: 'A', name: 'Acme', color: 'teal', inside:
        label('Machines') +
        '<div class="dm-group-in">' + row('server', 'api-prod') +
          (s.apiOpen ? term('api', 'terminal 1', s.busy.api) : '') + '</div>' },
      { code: 'P', name: 'Personal', color: 'violet', folded: true, inside: '' }
    ];
    return projects.map(function (p) {
      return '<div class="dm-project pc-' + p.color + (p.folded ? ' folded' : '') + '">' +
        '<div class="dm-project-row">' + ICON.chevron +
        '<span class="dm-badge">' + p.code + '</span>' +
        '<span class="dm-project-name">' + p.name + '</span>' +
        '<span class="dm-role">Owner</span></div>' + p.inside + '</div>';
    }).join('');
  }

  // Tabs as the real tab bar labels them, each with its project's code in
  // the project's color: CX/web-01 · deploy, CX/Release checklist.
  function tabsHtml(s) {
    var tabs = [
      { id: 'deploy', color: 'sky', code: 'CX', name: 'web-01 · deploy', busy: s.busy.deploy },
      { id: 'note', color: 'sky', code: 'CX', name: 'Release checklist', note: true },
      { id: 'logs', color: 'sky', code: 'CX', name: 'web-01 · logs' }
    ];
    if (s.apiOpen) tabs.push({ id: 'api', color: 'teal', code: 'A', name: 'api-prod', busy: s.busy.api });
    return tabs.map(function (tab) {
      return '<span class="dm-tab pc-' + tab.color + (tab.id === s.tab ? ' on' : '') + '">' +
        (tab.note ? ICON.list : dot(tab.busy)) +
        '<span><em>' + tab.code + '/</em>' + esc(tab.name) + '</span></span>';
    }).join('');
  }

  function feedHtml(s) {
    var where = WHERE[s.term];
    return s.feed.map(function (block) {
      return '<div class="dm-block"><div class="dm-meta">' +
        (block.run ? '<b class="dm-run"></b>' : '<b class="dot"></b>') +
        '<span>' + where.cwd + '</span><span class="dm-branch">' + where.branch + '</span>' +
        '<span class="dm-time">' + block.meta + '</span></div>' +
        '<div class="dm-cmd"><em>❯</em> ' + esc(block.cmd) + '</div>' +
        block.lines.map(function (line) {
          return '<div class="dm-out ' + line[1] + '">' + esc(line[0]) + '</div>';
        }).join('') + '</div>';
    }).join('');
  }

  // The note in its tab: where it lives, its title, who wrote it, and the
  // checklist with who ticked each item and when.
  function noteHtml(s) {
    var items = CHECKLIST.map(function (item, i) {
      var done = s.ticked[i];
      return '<div class="dm-todo' + (done ? ' done' : '') + (s.fresh === i ? ' fresh' : '') + '">' +
        '<span class="dm-box">' + (done ? ICON.check : '') + '</span>' +
        '<span class="dm-todo-text">' + esc(item[0]) + '</span>' +
        (done ? '<span class="dm-by">You · ' + item[1] + '</span>' : '') + '</div>';
    }).join('');
    return '<div class="dm-crumb pc-sky"><span class="dm-chip">CX</span><span>Client X</span>' +
      '<span>·</span>' + ICON.folder + '<span>Runbooks</span></div>' +
      '<div class="dm-ntitle">Release checklist</div>' +
      '<div class="dm-nmeta">You edited it 2 min ago · only you see it</div>' +
      '<div class="dm-nh">Release 2.4</div>' + items +
      '<div class="dm-nh">If it goes wrong</div>' +
      '<div class="dm-ncode"><span>git checkout v2.3.9 &amp;&amp; npm run build</span>' +
      '<span class="dm-copy">' + ICON.copy + 'Copy</span></div>';
  }

  function chipsHtml(s) {
    var where = WHERE[s.term];
    return '<span>' + where.cwd + '</span><span class="dm-branch-chip">' + where.branch + '</span>';
  }

  // The palette, as Jump to shows it: open terminals, notes, then a new
  // terminal on any machine.
  var OPEN_TERMINALS = [['CX', 'web-01 · deploy', 'terminal', 'sky'],
    ['CX', 'web-01 · logs', 'terminal', 'sky']];
  var NOTES = [['CX', 'Release checklist', 'list', 'sky'], ['CX', 'Rollback', 'doc', 'sky']];
  var MACHINES = [['CX', 'web-01', 'server', 'sky'], ['A', 'api-prod', 'server', 'teal'],
    ['P', 'MacBook', 'computer', 'violet']];

  function paletteHtml(s) {
    var query = s.query;
    var first = query.length > 0;
    function items(list, hint) {
      return list.filter(function (x) {
        return !query || x[1].toLowerCase().indexOf(query) !== -1;
      }).slice(0, 3).map(function (x) {
        var lit = first;
        first = false;
        return '<div class="dm-item pc-' + x[3] + (lit ? (s.picked ? ' lit picked' : ' lit') : '') + '">' +
          ICON[x[2]] + '<span><em>' + x[0] + '/</em>' + esc(x[1]) + '</span>' +
          (lit ? '<span class="dm-hint">' + hint + '</span>' : '') + '</div>';
      }).join('');
    }
    var groups = [['Terminals', items(OPEN_TERMINALS, 'Go to')],
      ['Notes', items(NOTES, 'Open')],
      ['New terminal', items(MACHINES, 'Open a terminal')]];
    return '<div class="dm-pal"><div class="dm-pal-q">' + ICON.search +
      '<span class="dm-q">' + esc(query) + '</span><span class="dm-pal-caret"></span>' +
      (query ? '' : '<span class="dm-ph">A terminal, a note, a machine or something to do</span>') +
      '<kbd>esc</kbd></div><div class="dm-pal-list">' +
      groups.filter(function (g) { return g[1]; }).map(function (g) {
        return '<div class="dm-group">' + g[0] + '</div>' + g[1];
      }).join('') + '</div></div>';
  }

  var SKELETON =
    '<div class="dm-chrome"><i></i><i></i><i></i><span class="dm-url">' + ICON.lock +
      'app.tterm.net</span></div>' +
    '<div class="dm-body">' +
      '<aside class="dm-side">' +
        '<div class="dm-side-head"><img src="/assets/logo.svg" alt="" width="18" height="18">tTerm</div>' +
        '<div class="dm-tree-wrap"><div class="dm-label">Projects</div><div class="dm-tree"></div>' +
          '<div class="dm-newproj"><span class="dm-dash">' + ICON.plus + '</span>New project</div></div>' +
        '<div class="dm-account"><span class="dm-avatar">DG</span>' +
          '<span class="dm-who"><b>Denis</b><small>Free plan</small></span></div>' +
      '</aside>' +
      '<div class="dm-main">' +
        '<div class="dm-bar"><div class="dm-tabs"></div><span class="dm-plus">' + ICON.plus + '</span>' +
          '<span class="dm-jump">' + ICON.search + 'Jump to<kbd>⌘K</kbd></span></div>' +
        '<div class="dm-term-view">' +
          '<div class="dm-feed"></div>' +
          '<div class="dm-input"><div class="dm-chips"></div>' +
            '<div class="dm-line"><em>❯</em><span class="dm-typed"></span><span class="dm-caret"></span></div></div>' +
        '</div>' +
        '<div class="dm-note-view" hidden><div class="dm-note"></div></div>' +
        '<div class="dm-palette" hidden></div>' +
      '</div>' +
    '</div>';

  function initDemo(root) {
    root.innerHTML = '<div class="dm" aria-hidden="true">' + SKELETON + '</div>';
    var el = {};
    ['tree', 'tabs', 'feed', 'chips', 'typed', 'palette', 'note', 'term-view', 'note-view'].forEach(function (name) {
      el[name] = root.querySelector('.dm-' + name);
    });

    // Each part is rewritten only when it changes, so the caret keeps
    // blinking and the rings keep turning between ticks.
    var last = {};
    function put(name, markup) {
      if (last[name] !== markup) {
        last[name] = markup;
        el[name].innerHTML = markup;
      }
    }
    function draw(tick) {
      var s = frame(tick);
      var inNote = s.tab === 'note';
      put('tree', treeHtml(s));
      put('tabs', tabsHtml(s));
      el['term-view'].hidden = inNote;
      el['note-view'].hidden = !inNote;
      if (inNote) put('note', noteHtml(s));
      else {
        put('feed', feedHtml(s));
        put('chips', chipsHtml(s));
        if (el.typed.textContent !== s.typed) el.typed.textContent = s.typed;
      }
      put('palette', s.palette ? paletteHtml(s) : '');
      el.palette.hidden = !s.palette;
    }

    var calm = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (calm) {
      draw(STILL);
      return;
    }

    // Still until at least half of it is on screen, then it plays; off
    // screen, or in a hidden tab, it pauses.
    var tick = 0;
    var timer = null;
    draw(0);
    function play(on) {
      if (on && !timer) {
        timer = setInterval(function () {
          if (!document.hidden) draw(++tick);
        }, 70);
      } else if (!on && timer) {
        clearInterval(timer);
        timer = null;
      }
    }
    if (!('IntersectionObserver' in window)) {
      play(true);
      return;
    }
    new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.intersectionRatio >= 0.5) play(true);
        else if (!entry.isIntersecting) play(false);
      });
    }, { threshold: [0, 0.5] }).observe(root);
  }

  /* ------------------------------------------------------------ stage */

  // On the main page the window of the demo leans back while its top is in
  // the lower part of the screen, where it sits when the page opens, and is
  // upright once its top has risen to the upper part. --e goes from 0 to 1
  // along a smoothstep, so it starts and lands softly; style.css turns it
  // into the tilt. With less motion asked for, it is upright from the start.
  function initStage(stage) {
    var calm = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (calm) {
      stage.style.setProperty('--e', '1');
      return;
    }
    var queued = false;
    function update() {
      queued = false;
      var top = stage.getBoundingClientRect().top;
      var vh = window.innerHeight || document.documentElement.clientHeight;
      var p = (vh * 0.70 - top) / (vh * 0.56);
      p = p < 0 ? 0 : p > 1 ? 1 : p;
      stage.style.setProperty('--e', (p * p * (3 - 2 * p)).toFixed(4));
    }
    function queue() {
      if (!queued) {
        queued = true;
        window.requestAnimationFrame(update);
      }
    }
    window.addEventListener('scroll', queue, { passive: true });
    window.addEventListener('resize', queue);
    update();
  }

  // A soft warm light follows the pointer across feature cards and steps;
  // style.css draws it at --mx, --my. Only where there is a pointer to
  // follow, and not for those who asked for less motion.
  function initGlow(card) {
    card.addEventListener('pointermove', function (event) {
      var r = card.getBoundingClientRect();
      card.style.setProperty('--mx', (event.clientX - r.left) + 'px');
      card.style.setProperty('--my', (event.clientY - r.top) + 'px');
    });
  }

  Array.prototype.forEach.call(document.querySelectorAll('details.menu, details.lang'), initMenu);
  Array.prototype.forEach.call(document.querySelectorAll('[data-demo]'), initDemo);
  Array.prototype.forEach.call(document.querySelectorAll('[data-stage]'), initStage);
  if (window.matchMedia && window.matchMedia('(hover: hover)').matches &&
      !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    Array.prototype.forEach.call(document.querySelectorAll('.feature, .step'), initGlow);
  }
})();
