/* tTerm site: the header menu on narrow screens, and the demo of tTerm Web
   on the main page and in posts. No dependencies, nothing loaded from
   anywhere else: the Privacy Policy promises the pages load nothing from
   third parties. */
(function () {
  'use strict';

  /* ------------------------------------------------------------- menu */

  // The menu is a <details>, so it opens with no script at all. Here it only
  // closes: after a tap on one of its links, on Escape, on a tap elsewhere.
  function initMenu(menu) {
    var summary = menu.querySelector('summary');
    menu.addEventListener('click', function (event) {
      if (event.target.closest && event.target.closest('.menu-panel a')) menu.open = false;
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

  // tTerm Web at work: a pull, a build and a restart on web-01, then Cmd+K
  // opens a terminal on api-prod in another project. The interface is in
  // English, as in the product. One tick is 70 ms; the story loops in about
  // half a minute.

  var DIM = 'dim', OK = 'ok', INK = 'ink';
  var STORY = [
    { tab: 'web', cmd: 'git pull', time: '1.4 s', out: [
      ['Updating 3f2c1a9..8d4e7b2', DIM],
      ['Fast-forward', DIM],
      [' src/server.ts | 12 +++++++-----', DIM],
      [' src/routes.ts |  4 ++--', DIM],
      [' 2 files changed, 9 insertions(+), 7 deletions(-)', DIM]] },
    { tab: 'web', cmd: 'npm run build', time: '4.2 s', out: [
      ['> app@2.4.0 build', DIM],
      ['> vite build', DIM],
      ['vite v7.1.4 building for production...', DIM],
      ['✓ 412 modules transformed.', OK],
      ['dist/index.html                0.46 kB', DIM],
      ['dist/assets/index.js         184.20 kB', DIM],
      ['✓ built in 3.81s', OK]] },
    { tab: 'web', cmd: 'sudo systemctl restart app', time: '0.9 s', out: [] },
    { tab: 'web', cmd: 'systemctl is-active app', time: '0.0 s', out: [['active', OK]] },
    { palette: 'api' },
    { tab: 'api', cmd: 'docker compose ps', time: '0.3 s', out: [
      ['NAME        IMAGE            STATUS', DIM],
      ['api-web-1   acme/api:2.4.0   Up 23 days', INK],
      ['api-db-1    postgres:17      Up 23 days (healthy)', INK]] }
  ];

  // Ticks: a typed character, the pause before Enter, an output line, the
  // pause after a command; the palette opening, a character, the pick.
  var TYPE = 2, ENTER = 6, LINE = 3, AFTER = 18, END = 60;
  var P_OPEN = 8, P_CHAR = 4, P_PICK = 12;

  var SPANS = [];
  var TOTAL = 0;
  STORY.forEach(function (step) {
    var length = step.palette
      ? P_OPEN + step.palette.length * P_CHAR + P_PICK
      : step.cmd.length * TYPE + ENTER + step.out.length * LINE + AFTER;
    SPANS.push({ start: TOTAL, end: TOTAL + length });
    TOTAL += length;
  });
  TOTAL += END;

  // For visitors who asked for less motion: one still frame, the build has
  // just finished.
  var STILL = SPANS[1].end - 1;

  var WHERE = { web: { cwd: '~/app', branch: 'main' }, api: { cwd: '~/acme', branch: 'main' } };

  // What is on screen at a given tick.
  function frame(tick) {
    var t = tick % TOTAL;
    var feeds = {
      web: [
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
    var s = { tab: 'web', typed: '', palette: false, query: '', picked: false };

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

    s.feed = feeds[s.tab].slice(-4);
    s.busy = { web: feeds.web.some(running), api: feeds.api.some(running) };
    // The terminal on api-prod exists once it is picked in the palette.
    s.apiOpen = s.tab === 'api' || s.picked;
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
    lock: svg('<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>')
  };

  function dot(busy) { return busy ? '<b class="dot busy"></b>' : '<b class="dot"></b>'; }

  // The sidebar: projects, their machines, and under each machine its
  // terminals. The current terminal is lit; a running command spins.
  function treeHtml(s) {
    var current = s.tab === 'web' ? 'web1' : 'api1';
    function term(id, n, busy) {
      return '<div class="dm-term' + (id === current ? ' on' : '') + '">' + dot(busy) +
        'terminal ' + n + '</div>';
    }
    var projects = [
      { code: 'P', name: 'Personal', role: 'Owner', badge: '', machines: [
        { name: 'web-01', icon: 'server', terms: term('web1', 1, s.busy.web) + term('web2', 2, false) },
        { name: 'db-01', icon: 'server', terms: '' },
        { name: 'MacBook', icon: 'computer', terms: term('mac1', 1, false) }
      ] },
      { code: 'A', name: 'Acme', role: 'Admin', badge: ' amber', machines: [
        { name: 'api-prod', icon: 'server', terms: s.apiOpen ? term('api1', 1, s.busy.api) : '' },
        { name: 'staging', icon: 'server', terms: '' }
      ] }
    ];
    return projects.map(function (p) {
      return '<div class="dm-project"><div class="dm-project-row">' + ICON.chevron +
        '<span class="dm-badge' + p.badge + '">' + p.code + '</span>' +
        '<span class="dm-project-name">' + p.name + '</span>' +
        '<span class="dm-role">' + p.role + '</span></div>' +
        p.machines.map(function (m) {
          return '<div class="dm-machine"><div class="dm-machine-row">' + ICON[m.icon] +
            '<span>' + m.name + '</span></div>' + m.terms + '</div>';
        }).join('') + '</div>';
    }).join('');
  }

  // Tabs as the real tab bar labels them: P/web-01 · 2 for a second
  // terminal on the same machine.
  function tabsHtml(s) {
    var tabs = [
      { code: 'P', name: 'web-01', on: s.tab === 'web', busy: s.busy.web },
      { code: 'P', name: 'web-01 · 2' },
      { code: 'P', name: 'MacBook' }
    ];
    if (s.apiOpen) tabs.push({ code: 'A', name: 'api-prod', on: s.tab === 'api', busy: s.busy.api });
    return tabs.map(function (tab) {
      return '<span class="dm-tab' + (tab.on ? ' on' : '') + '">' + dot(tab.busy) +
        '<span><em>' + tab.code + '/</em>' + esc(tab.name) + '</span></span>';
    }).join('');
  }

  function feedHtml(s) {
    var where = WHERE[s.tab];
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

  function chipsHtml(s) {
    var where = WHERE[s.tab];
    return '<span>' + where.cwd + '</span><span class="dm-branch-chip">' + where.branch + '</span>';
  }

  // The palette, as Jump to shows it: open terminals, then a new terminal
  // on any machine.
  var OPEN_TERMINALS = [['P', 'web-01', 'terminal'], ['P', 'web-01 · 2', 'terminal'],
    ['P', 'MacBook', 'terminal']];
  var MACHINES = [['P', 'web-01', 'server'], ['P', 'db-01', 'server'], ['P', 'MacBook', 'computer'],
    ['A', 'api-prod', 'server'], ['A', 'staging', 'server']];

  function paletteHtml(s) {
    var query = s.query;
    var first = query.length > 0;
    function items(list, hint) {
      return list.filter(function (x) {
        return !query || x[1].toLowerCase().indexOf(query) !== -1;
      }).slice(0, 4).map(function (x) {
        var lit = first;
        first = false;
        return '<div class="dm-item' + (lit ? (s.picked ? ' lit picked' : ' lit') : '') + '">' +
          ICON[x[2]] + '<span><em>' + x[0] + '/</em>' + esc(x[1]) + '</span>' +
          (lit ? '<span class="dm-hint">' + hint + '</span>' : '') + '</div>';
      }).join('');
    }
    var groups = [['Terminals', items(OPEN_TERMINALS, 'Go to')],
      ['New terminal', items(MACHINES, 'Open a terminal')]];
    return '<div class="dm-pal"><div class="dm-pal-q">' + ICON.search +
      '<span class="dm-q">' + esc(query) + '</span><span class="dm-pal-caret"></span>' +
      (query ? '' : '<span class="dm-ph">A terminal, a machine or something to do</span>') +
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
        '<div class="dm-feed"></div>' +
        '<div class="dm-input"><div class="dm-chips"></div>' +
          '<div class="dm-line"><em>❯</em><span class="dm-typed"></span><span class="dm-caret"></span></div></div>' +
        '<div class="dm-palette" hidden></div>' +
      '</div>' +
    '</div>';

  function initDemo(root) {
    root.innerHTML = '<div class="dm" aria-hidden="true">' + SKELETON + '</div>';
    var el = {};
    ['tree', 'tabs', 'feed', 'chips', 'typed', 'palette'].forEach(function (name) {
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
      put('tree', treeHtml(s));
      put('tabs', tabsHtml(s));
      put('feed', feedHtml(s));
      put('chips', chipsHtml(s));
      if (el.typed.textContent !== s.typed) el.typed.textContent = s.typed;
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

  Array.prototype.forEach.call(document.querySelectorAll('details.menu'), initMenu);
  Array.prototype.forEach.call(document.querySelectorAll('[data-demo]'), initDemo);
})();
