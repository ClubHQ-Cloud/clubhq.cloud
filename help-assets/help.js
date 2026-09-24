/* Install article: show the guide for the reader's browser, in the orientation they
   are holding the phone.

   Without JavaScript every guide stays visible in portrait, which is a long page but
   a complete one. With it, one guide shows at a time:

   - the browser comes from ?browser= (the app links here with the one it detected),
     else from the user agent — the same rules as the app's pwa/browser.ts;
   - the orientation follows the device and keeps following it on rotation, until the
     reader picks one themselves. */

(function () {
    const guides = document.querySelectorAll('.help-guide');
    if (!guides.length) return;

    const controls = document.querySelector('.help-controls');
    const chips = document.querySelectorAll('.help-chip');
    const orientationBox = document.querySelector('.help-orientation');
    const orientationButtons = document.querySelectorAll('.help-segmented button');
    const known = new Set([...guides].map(g => g.dataset.browser));

    function detect() {
        const ua = navigator.userAgent;
        const ios = /iPad|iPhone|iPod/.test(ua) || (/Macintosh/.test(ua) && navigator.maxTouchPoints > 1);
        if (ios) {
            if (/CriOS|FxiOS|EdgiOS|OPiOS|GSA\//.test(ua)) return 'ios-other';
            const version = Number((/Version\/(\d+)/.exec(ua) || [])[1] || 0);
            // Since iOS 26 the OS version in the user agent is frozen at 18_x;
            // Safari's own version still moves, so that is what tells the toolbars apart.
            if (version >= 27) return 'ios-safari-27';
            return version >= 26 ? 'ios-safari' : 'ios-safari-legacy';
        }
        if (/Android/i.test(ua)) {
            if (/SamsungBrowser/.test(ua)) return 'android-samsung';
            if (/EdgA\//.test(ua)) return 'android-edge';
            if (/Firefox\//.test(ua)) return 'android-firefox';
            if (/Chrome\//.test(ua) && !/OPR\/|YaBrowser|wv\)/.test(ua)) return 'android-chrome';
            return 'android-other';
        }
        return 'desktop';
    }

    const params = new URLSearchParams(location.search);
    let browser = known.has(params.get('browser')) ? params.get('browser') : detect();

    const landscapeQuery = window.matchMedia('(orientation: landscape)');
    let orientation = landscapeQuery.matches && browser !== 'desktop' ? 'landscape' : 'portrait';
    let orientationChosen = false;

    function render() {
        let oriented = false;
        guides.forEach(g => {
            const active = g.dataset.browser === browser;
            g.hidden = !active;
            if (active) oriented = g.hasAttribute('data-oriented');
        });
        chips.forEach(c => c.setAttribute('aria-pressed', String(c.dataset.browser === browser)));
        orientationBox.hidden = !oriented;
        orientationButtons.forEach(b => b.setAttribute('aria-pressed', String(b.dataset.orientation === orientation)));
        document.body.classList.toggle('help-landscape', orientation === 'landscape');
    }

    chips.forEach(chip => chip.addEventListener('click', () => {
        browser = chip.dataset.browser;
        const url = new URL(location.href);
        url.searchParams.set('browser', browser);
        history.replaceState(null, '', url);
        render();
    }));

    orientationButtons.forEach(button => button.addEventListener('click', () => {
        orientation = button.dataset.orientation;
        orientationChosen = true;
        render();
    }));

    landscapeQuery.addEventListener('change', e => {
        if (orientationChosen) return;
        orientation = e.matches ? 'landscape' : 'portrait';
        render();
    });

    document.body.classList.add('help-js');
    controls.hidden = false;
    render();
})();
