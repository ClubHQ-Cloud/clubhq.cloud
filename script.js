let currentLang = 'pl';

/* Language ------------------------------------------------------------------
   Only the body class changes. The stylesheet hides the inactive language, so
   nothing here has to know which `display` value any given element wants. */

function setLang(lang) {
    currentLang = lang;

    document.body.classList.remove('lang-pl', 'lang-en');
    document.body.classList.add('lang-' + lang);
    document.documentElement.lang = lang;

    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.setAttribute('aria-pressed', String(btn.id === 'btn-' + lang));
    });

    // The preview's theme buttons are icon-only, so they can't be duplicated
    // per language the way visible copy is — their labels are swapped instead.
    document.querySelectorAll('#preview-theme button').forEach(btn => {
        const label = btn.getAttribute('data-label-' + lang);
        if (label) {
            btn.setAttribute('title', label);
            btn.setAttribute('aria-label', label);
        }
    });
}

function initLanguage() {
    const userLang = navigator.language || navigator.userLanguage;
    if (userLang && userLang.toLowerCase().startsWith('pl')) {
        setLang('pl');
    } else {
        setLang('en');
    }

    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.addEventListener('click', () => setLang(btn.id.replace('btn-', '')));
    });
}

/* Preview dates -------------------------------------------------------------
   The balances widget shows payment deadlines, so they can't be hard-coded: a
   fixed date drifts, and a screenshot claiming a payment is overdue while
   naming a date next month reads as a bug. Each <time data-day-offset> is
   filled relative to today — the overdue deadline sits 14 days back, and the
   pending one falls due today.

   Each element takes its format from its own [lang] ancestor, so the Polish
   and English copies are both correct and neither needs redoing when the
   visitor switches language. */

function initPreviewDates() {
    const FORMATS = {
        pl: { day: '2-digit', month: '2-digit' },   // 16.07
        en: { day: '2-digit', month: 'short' }      // 16 Jul
    };
    const LOCALES = { pl: 'pl-PL', en: 'en-GB' };

    document.querySelectorAll('time[data-day-offset]').forEach(el => {
        const offset = parseInt(el.getAttribute('data-day-offset'), 10);
        if (Number.isNaN(offset)) return;

        const date = new Date();
        date.setDate(date.getDate() + offset);

        const host = el.closest('[lang]');
        const hostLang = host ? host.getAttribute('lang') : null;
        const lang = FORMATS[hostLang] ? hostLang : 'pl';

        // Built from local parts — toISOString() is UTC and can land a day off.
        el.setAttribute('datetime', [
            date.getFullYear(),
            String(date.getMonth() + 1).padStart(2, '0'),
            String(date.getDate()).padStart(2, '0')
        ].join('-'));

        el.textContent = new Intl.DateTimeFormat(LOCALES[lang], FORMATS[lang]).format(date);
    });
}

/* Product preview tabs ------------------------------------------------------
   Three screens behind one slot: the week's sessions, who has confirmed, and
   what the club is owed. Home page only. */

function initPreviewTabs() {
    const tabs = Array.from(document.querySelectorAll('#preview-tabs [role="tab"]'));
    if (!tabs.length) return;

    function select(tab, moveFocus) {
        tabs.forEach(t => {
            const on = t === tab;
            t.setAttribute('aria-selected', String(on));
            t.tabIndex = on ? 0 : -1;
            document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
        });
        if (moveFocus) tab.focus();
    }

    tabs.forEach(tab => {
        tab.addEventListener('click', () => select(tab, false));

        tab.addEventListener('keydown', e => {
            const i = tabs.indexOf(tab);
            let next = null;
            if (e.key === 'ArrowRight') next = tabs[(i + 1) % tabs.length];
            else if (e.key === 'ArrowLeft') next = tabs[(i - 1 + tabs.length) % tabs.length];
            else if (e.key === 'Home') next = tabs[0];
            else if (e.key === 'End') next = tabs[tabs.length - 1];
            if (next) {
                e.preventDefault();
                select(next, true);
            }
        });
    });
}

/* Product preview theme -----------------------------------------------------
   Mirrors the app's own ThemeSwitcher: the preview shows the product, and the
   product is themeable, so the preview demonstrates it. Home page only. */

function initPreviewTheme() {
    const preview = document.getElementById('preview');
    const buttons = document.querySelectorAll('#preview-theme button');
    if (!preview || !buttons.length) return;

    buttons.forEach(btn => {
        btn.addEventListener('click', () => {
            const theme = btn.getAttribute('data-preview-set');
            preview.setAttribute('data-preview-theme', theme);
            buttons.forEach(b => {
                b.setAttribute('aria-pressed', String(b.getAttribute('data-preview-set') === theme));
            });
        });
    });
}

initLanguage();
initPreviewDates();
initPreviewTabs();
initPreviewTheme();
