"""Words for the help pages — the install article's guides, in both languages.

A guide is one browser. Its `flows` are the steps per orientation; a step with a
`shot` shows that screenshot (1-based, from the capture) with the tapped control
highlighted, a step without one is text and an icon. Browsers we have no device for
share one flow for both orientations.
"""

GUIDES = [
    {
        'id': 'ios-safari-27',
        'name': {'en': 'Safari · iOS 27', 'pl': 'Safari · iOS 27'},
        'shots': 'ios-27',
        'flows': {
            'portrait': [
                {'shot': 1, 'icon': 'align-left', 'en': 'Tap the page menu button <b>≡</b> at the left end of the address bar, at the bottom of the screen.', 'pl': 'Dotknij przycisku menu strony <b>≡</b> na lewym końcu paska adresu, na dole ekranu.'},
                {'shot': 2, 'icon': 'share', 'en': 'Tap <b>Share</b>.', 'pl': 'Dotknij <b>Udostępnij</b>.'},
                {'shot': 3, 'icon': 'chevron-down', 'en': 'Tap <b>View More</b>.', 'pl': 'Dotknij <b>Pokaż więcej</b>.'},
                {'shot': 4, 'icon': 'square-plus', 'en': 'Tap <b>Add to Home Screen</b>.', 'pl': 'Dotknij <b>Do ekranu głównego</b>.'},
                {'shot': 5, 'icon': 'toggle-right', 'en': 'Leave <b>Open as Web App</b> switched on and tap <b>Add</b>.', 'pl': 'Zostaw włączony przełącznik <b>Otwórz jako aplikację www</b> i dotknij <b>Dodaj</b>.'},
                {'shot': 'home', 'icon': 'house', 'en': 'Sport Match is on your home screen. Open it from there from now on.', 'pl': 'Sport Match jest na ekranie głównym. Od teraz otwieraj ją stamtąd.'},
            ],
            'landscape': [
                {'shot': 1, 'icon': 'share', 'en': 'Tap <b>Share</b> in the toolbar at the top of the screen.', 'pl': 'Dotknij <b>Udostępnij</b> na pasku narzędzi u góry ekranu.'},
                {'shot': 2, 'icon': 'square-plus', 'en': 'Tap <b>Add to Home Screen</b>.', 'pl': 'Dotknij <b>Do ekranu głównego</b>.'},
                {'shot': 3, 'icon': 'check', 'en': 'Tap <b>Add</b> in the top-right corner. (<b>Open as Web App</b>, hidden under the keyboard here, is on by default — leave it on.)', 'pl': 'Dotknij <b>Dodaj</b> w prawym górnym rogu. (Przełącznik <b>Otwórz jako aplikację www</b>, tu schowany pod klawiaturą, jest domyślnie włączony — zostaw go tak.)'},
                {'shot': 'home', 'icon': 'house', 'en': 'Sport Match is on your home screen. Open it from there from now on.', 'pl': 'Sport Match jest na ekranie głównym. Od teraz otwieraj ją stamtąd.'},
            ],
        },
    },
    {
        'id': 'ios-safari',
        'name': {'en': 'Safari · iOS 26', 'pl': 'Safari · iOS 26'},
        'shots': 'ios-26',
        'flows': {
            'portrait': [
                {'shot': 1, 'icon': 'ellipsis', 'en': 'Tap <b>⋯</b> at the bottom right of the screen.', 'pl': 'Dotknij <b>⋯</b> w prawym dolnym rogu ekranu.'},
                {'shot': 2, 'icon': 'share', 'en': 'Tap <b>Share</b>.', 'pl': 'Dotknij <b>Udostępnij</b>.'},
                {'shot': 3, 'icon': 'chevron-down', 'en': 'Tap <b>View More</b>.', 'pl': 'Dotknij <b>Pokaż więcej</b>.'},
                {'shot': 4, 'icon': 'square-plus', 'en': 'Tap <b>Add to Home Screen</b>.', 'pl': 'Dotknij <b>Do ekranu głównego</b>.'},
                {'shot': 5, 'icon': 'toggle-right', 'en': 'Leave <b>Open as Web App</b> switched on and tap <b>Add</b>.', 'pl': 'Zostaw włączony przełącznik <b>Otwórz jako aplikację www</b> i dotknij <b>Dodaj</b>.'},
                {'shot': 'home', 'icon': 'house', 'en': 'Sport Match is on your home screen. Open it from there from now on.', 'pl': 'Sport Match jest na ekranie głównym. Od teraz otwieraj ją stamtąd.'},
            ],
            'landscape': [
                {'shot': 1, 'icon': 'share', 'en': 'Tap <b>Share</b> in the toolbar at the top of the screen.', 'pl': 'Dotknij <b>Udostępnij</b> na pasku narzędzi u góry ekranu.'},
                {'shot': 2, 'icon': 'square-plus', 'en': 'Tap <b>Add to Home Screen</b>.', 'pl': 'Dotknij <b>Do ekranu głównego</b>.'},
                {'shot': 3, 'icon': 'check', 'en': 'Tap <b>Add</b> in the top-right corner. (<b>Open as Web App</b>, hidden under the keyboard here, is on by default — leave it on.)', 'pl': 'Dotknij <b>Dodaj</b> w prawym górnym rogu. (Przełącznik <b>Otwórz jako aplikację www</b>, tu schowany pod klawiaturą, jest domyślnie włączony — zostaw go tak.)'},
                {'shot': 'home', 'icon': 'house', 'en': 'Sport Match is on your home screen. Open it from there from now on.', 'pl': 'Sport Match jest na ekranie głównym. Od teraz otwieraj ją stamtąd.'},
            ],
        },
    },
    {
        'id': 'ios-safari-legacy',
        'name': {'en': 'Safari · iOS 18 and older', 'pl': 'Safari · iOS 18 i starszy'},
        'shots': 'ios-17',
        'flows': {
            'portrait': [
                {'shot': 1, 'icon': 'share', 'en': 'Tap <b>Share</b> in the toolbar at the bottom of the screen.', 'pl': 'Dotknij <b>Udostępnij</b> na pasku narzędzi na dole ekranu.'},
                {'shot': 2, 'icon': 'square-plus', 'en': 'Scroll down and tap <b>Add to Home Screen</b>.', 'pl': 'Przewiń w dół i dotknij <b>Do ekranu początkowego</b>.'},
                {'shot': 3, 'icon': 'check', 'en': 'Tap <b>Add</b> in the top-right corner.', 'pl': 'Dotknij <b>Dodaj</b> w prawym górnym rogu.'},
                {'shot': 'home', 'icon': 'house', 'en': 'Sport Match is on your home screen. Open it from there from now on.', 'pl': 'Sport Match jest na ekranie głównym. Od teraz otwieraj ją stamtąd.'},
            ],
            'landscape': [
                {'shot': 1, 'icon': 'share', 'en': 'Tap <b>Share</b> in the toolbar at the top of the screen.', 'pl': 'Dotknij <b>Udostępnij</b> na pasku narzędzi u góry ekranu.'},
                {'shot': 2, 'icon': 'square-plus', 'en': 'Scroll down and tap <b>Add to Home Screen</b>.', 'pl': 'Przewiń w dół i dotknij <b>Do ekranu początkowego</b>.'},
                {'shot': 3, 'icon': 'check', 'en': 'Tap <b>Add</b> in the top-right corner.', 'pl': 'Dotknij <b>Dodaj</b> w prawym górnym rogu.'},
                {'shot': 'home', 'icon': 'house', 'en': 'Sport Match is on your home screen. Open it from there from now on.', 'pl': 'Sport Match jest na ekranie głównym. Od teraz otwieraj ją stamtąd.'},
            ],
        },
    },
    {
        'id': 'ios-other',
        'name': {'en': 'Chrome, Edge or Firefox · iPhone', 'pl': 'Chrome, Edge lub Firefox · iPhone'},
        'flows': {
            'any': [
                {'icon': 'share', 'en': 'Tap <b>Share</b>. In Chrome it is at the right end of the address bar; in Edge and Firefox open the menu first.', 'pl': 'Dotknij <b>Udostępnij</b>. W Chrome jest na prawym końcu paska adresu; w Edge i Firefoksie najpierw otwórz menu.'},
                {'icon': 'square-plus', 'en': 'Tap <b>Add to Home Screen</b> — under <b>View More</b> if you don’t see it.', 'pl': 'Dotknij <b>Do ekranu głównego</b> (w starszych iOS: <b>Do ekranu początkowego</b>) — pod <b>Pokaż więcej</b>, jeśli go nie widać.'},
                {'icon': 'check', 'en': 'Tap <b>Add</b>.', 'pl': 'Dotknij <b>Dodaj</b>.'},
            ],
        },
    },
    {
        'id': 'android-chrome',
        'name': {'en': 'Chrome · Android', 'pl': 'Chrome · Android'},
        'shots': 'android',
        'flows': {
            'portrait': [
                {'shot': 1, 'icon': 'ellipsis-vertical', 'en': 'Tap <b>⋮</b> in the top-right corner.', 'pl': 'Dotknij <b>⋮</b> w prawym górnym rogu.'},
                {'shot': 2, 'icon': 'square-plus', 'en': 'Tap <b>Add to Home screen</b>.', 'pl': 'Dotknij <b>Dodaj do ekranu głównego</b>.'},
                {'shot': 3, 'icon': 'download', 'en': 'Choose <b>Install</b> — it installs Sport Match as an app, not just a shortcut.', 'pl': 'Wybierz <b>Zainstaluj</b> — Sport Match zainstaluje się jako aplikacja, a nie tylko skrót.'},
                {'shot': 4, 'icon': 'check', 'en': 'Confirm with <b>Install</b>. The icon appears on your home screen and in the app list.', 'pl': 'Potwierdź, dotykając <b>Zainstaluj</b>. Ikona pojawi się na ekranie głównym i na liście aplikacji.'},
            ],
            'landscape': [
                {'shot': 1, 'icon': 'ellipsis-vertical', 'en': 'Tap <b>⋮</b> in the top-right corner.', 'pl': 'Dotknij <b>⋮</b> w prawym górnym rogu.'},
                {'shot': 2, 'icon': 'square-plus', 'en': 'Scroll the menu down and tap <b>Add to Home screen</b>.', 'pl': 'Przewiń menu w dół i dotknij <b>Dodaj do ekranu głównego</b>.'},
                {'shot': 3, 'icon': 'download', 'en': 'Choose <b>Install</b> — it installs Sport Match as an app, not just a shortcut.', 'pl': 'Wybierz <b>Zainstaluj</b> — Sport Match zainstaluje się jako aplikacja, a nie tylko skrót.'},
                {'shot': 4, 'icon': 'check', 'en': 'Confirm with <b>Install</b>. The icon appears on your home screen and in the app list.', 'pl': 'Potwierdź, dotykając <b>Zainstaluj</b>. Ikona pojawi się na ekranie głównym i na liście aplikacji.'},
            ],
        },
    },
    {
        'id': 'android-samsung',
        'name': {'en': 'Samsung Internet', 'pl': 'Samsung Internet'},
        'flows': {
            'any': [
                {'icon': 'menu', 'en': 'Tap <b>≡</b> in the toolbar at the bottom.', 'pl': 'Dotknij <b>≡</b> na pasku na dole.'},
                {'icon': 'square-plus', 'en': 'Tap <b>Add page to</b>.', 'pl': 'Dotknij <b>Dodaj stronę do</b>.'},
                {'icon': 'house', 'en': 'Choose <b>Home screen</b> and tap <b>Add</b>.', 'pl': 'Wybierz <b>Ekran startowy</b> i dotknij <b>Dodaj</b>.'},
            ],
        },
    },
    {
        'id': 'android-firefox',
        'name': {'en': 'Firefox · Android', 'pl': 'Firefox · Android'},
        'flows': {
            'any': [
                {'icon': 'ellipsis-vertical', 'en': 'Tap <b>⋮</b> next to the address bar.', 'pl': 'Dotknij <b>⋮</b> obok paska adresu.'},
                {'icon': 'square-plus', 'en': 'Tap <b>Add app to Home screen</b>.', 'pl': 'Dotknij <b>Dodaj aplikację do ekranu głównego</b>.'},
                {'icon': 'check', 'en': 'Tap <b>Add</b>.', 'pl': 'Dotknij <b>Dodaj</b>.'},
            ],
        },
    },
    {
        'id': 'android-edge',
        'name': {'en': 'Edge · Android', 'pl': 'Edge · Android'},
        'flows': {
            'any': [
                {'icon': 'ellipsis', 'en': 'Tap <b>⋯</b> in the toolbar at the bottom.', 'pl': 'Dotknij <b>⋯</b> na pasku na dole.'},
                {'icon': 'smartphone', 'en': 'Tap <b>Add to phone</b>.', 'pl': 'Dotknij <b>Dodaj do telefonu</b>.'},
                {'icon': 'check', 'en': 'Tap <b>Install</b>.', 'pl': 'Dotknij <b>Zainstaluj</b>.'},
            ],
        },
    },
    {
        'id': 'android-other',
        'name': {'en': 'Another browser', 'pl': 'Inna przeglądarka'},
        'flows': {
            'any': [
                {'icon': 'ellipsis-vertical', 'en': 'Open your browser’s menu — usually <b>⋮</b> or <b>≡</b> next to the address bar.', 'pl': 'Otwórz menu przeglądarki — zwykle <b>⋮</b> albo <b>≡</b> obok paska adresu.'},
                {'icon': 'square-plus', 'en': 'Look for <b>Install app</b> or <b>Add to Home screen</b>.', 'pl': 'Poszukaj pozycji <b>Zainstaluj aplikację</b> albo <b>Dodaj do ekranu głównego</b>.'},
                {'icon': 'check', 'en': 'Confirm. If there is no such option, open the page in Chrome and follow its guide.', 'pl': 'Potwierdź. Jeśli takiej opcji nie ma, otwórz stronę w Chrome i skorzystaj z instrukcji dla Chrome.'},
            ],
        },
    },
    {
        'id': 'desktop',
        'name': {'en': 'Computer', 'pl': 'Komputer'},
        'flows': {
            'any': [
                {'icon': 'download', 'en': 'In Chrome or Edge, click the install icon at the right end of the address bar.', 'pl': 'W Chrome lub Edge kliknij ikonę instalacji na prawym końcu paska adresu.'},
                {'icon': 'check', 'en': 'Click <b>Install</b>. Sport Match opens in its own window.', 'pl': 'Kliknij <b>Zainstaluj</b>. Sport Match otworzy się we własnym oknie.'},
                {'icon': 'smartphone', 'en': 'The app is at its best on a phone, though — open <b>app.clubhq.cloud</b> there and pick your phone’s browser above.', 'pl': 'Najlepiej sprawdza się jednak na telefonie — otwórz tam <b>app.clubhq.cloud</b> i wybierz powyżej przeglądarkę telefonu.'},
            ],
        },
    },
]

TEXT = {
    'en': {
        'help': 'Help',
        'help_title': 'Help — Sport Match',
        'help_lead': 'Guides for getting the most out of Sport Match.',
        'title': 'Install Sport Match on your phone',
        'page_title': 'Install the app — Sport Match help',
        'description': 'How to add Sport Match to your phone’s home screen — step by step with screenshots for Safari on iPhone and Chrome on Android.',
        'lead': 'Sport Match works in the browser, but installed on your home screen it opens full screen with one tap — and on iPhone, notifications only work in the installed app. It takes under a minute and needs no app store.',
        'browser': 'Your browser',
        'detected': 'Detected automatically — pick another if it’s wrong.',
        'orientation': 'Screen',
        'portrait': 'Portrait',
        'landscape': 'Landscape',
        'step': 'Step',
        'shot_alt': 'Screenshot: {text}',
        'faq': 'Something’s not right?',
        'back': '← All help articles',
        'open_app': 'Open Sport Match',
        'faqs': [
            ('I don’t see “Add to Home Screen”',
             'You are probably in an app’s built-in browser — links opened from Facebook, Instagram, Messenger or an email app often are. Open the page in Safari (iPhone) or Chrome (Android) first: the built-in browser’s menu usually has <b>Open in browser</b>.'),
            ('Notifications don’t arrive on my iPhone',
             'An iPhone only delivers notifications to the installed app (iOS 16.4 or newer). Open Sport Match from its home screen icon, not from Safari, and switch notifications on in your settings there.'),
            ('How do I know it worked?',
             'Sport Match has its own icon on the home screen and opens without the browser’s address bar.'),
            ('How do I remove it?',
             'Touch and hold the icon, then choose <b>Remove App</b> (iPhone) or <b>Uninstall</b> (Android). Your account and club data stay as they are.'),
        ],
    },
    'pl': {
        'help': 'Pomoc',
        'help_title': 'Pomoc — Sport Match',
        'help_lead': 'Instrukcje, które pomogą Ci wygodnie korzystać ze Sport Match.',
        'title': 'Zainstaluj Sport Match na telefonie',
        'page_title': 'Instalacja aplikacji — pomoc Sport Match',
        'description': 'Jak dodać Sport Match do ekranu głównego telefonu — krok po kroku, ze zrzutami ekranu dla Safari na iPhonie i Chrome na Androidzie.',
        'lead': 'Sport Match działa w przeglądarce, ale zainstalowana na ekranie głównym otwiera się jednym dotknięciem na pełnym ekranie — a na iPhonie powiadomienia działają tylko w zainstalowanej aplikacji. Zajmuje to niecałą minutę i nie wymaga sklepu z aplikacjami.',
        'browser': 'Twoja przeglądarka',
        'detected': 'Wykryta automatycznie — wybierz inną, jeśli się nie zgadza.',
        'orientation': 'Ekran',
        'portrait': 'Pionowo',
        'landscape': 'Poziomo',
        'step': 'Krok',
        'shot_alt': 'Zrzut ekranu: {text}',
        'faq': 'Coś nie działa?',
        'back': '← Wszystkie artykuły pomocy',
        'open_app': 'Otwórz Sport Match',
        'faqs': [
            ('Nie widzę „Do ekranu głównego”',
             'Najpewniej jesteś we wbudowanej przeglądarce innej aplikacji — tak otwierają się linki z Facebooka, Instagrama, Messengera czy aplikacji pocztowej. Najpierw otwórz stronę w Safari (iPhone) albo Chrome (Android): menu wbudowanej przeglądarki zwykle ma pozycję <b>Otwórz w przeglądarce</b>.'),
            ('Na iPhonie nie przychodzą powiadomienia',
             'iPhone dostarcza powiadomienia tylko do zainstalowanej aplikacji (iOS 16.4 lub nowszy). Otwórz Sport Match z ikony na ekranie głównym, a nie z Safari, i tam włącz powiadomienia w ustawieniach.'),
            ('Skąd mam wiedzieć, że się udało?',
             'Sport Match ma własną ikonę na ekranie głównym i otwiera się bez paska adresu przeglądarki.'),
            ('Jak ją usunąć?',
             'Przytrzymaj ikonę i wybierz <b>Usuń aplikację</b> (iPhone) albo <b>Odinstaluj</b> (Android). Twoje konto i dane klubu pozostaną bez zmian.'),
        ],
    },
}

# Lucide (ISC licence) — the same icons the app's install popup shows.
ICONS = {
    'share': '<path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"/><polyline points="16 6 12 2 8 6"/><line x1="12" x2="12" y1="2" y2="15"/>',
    'ellipsis': '<circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/><circle cx="5" cy="12" r="1"/>',
    'ellipsis-vertical': '<circle cx="12" cy="12" r="1"/><circle cx="12" cy="5" r="1"/><circle cx="12" cy="19" r="1"/>',
    'square-plus': '<rect width="18" height="18" x="3" y="3" rx="2"/><path d="M8 12h8"/><path d="M12 8v8"/>',
    'chevron-down': '<path d="m6 9 6 6 6-6"/>',
    'align-left': '<path d="M15 12H3"/><path d="M17 18H3"/><path d="M21 6H3"/>',
    'menu': '<line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/>',
    'house': '<path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/><path d="M3 10a2 2 0 0 1 .709-1.528l7-6a2 2 0 0 1 2.582 0l7 6A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
    'smartphone': '<rect width="14" height="20" x="5" y="2" rx="2" ry="2"/><path d="M12 18h.01"/>',
    'download': '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" x2="12" y1="15" y2="3"/>',
    'toggle-right': '<rect width="20" height="12" x="2" y="6" rx="6" ry="6"/><circle cx="16" cy="12" r="2"/>',
    'check': '<path d="M20 6 9 17l-5-5"/>',
    'external-link': '<path d="M15 3h6v6"/><path d="M10 14 21 3"/><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>',
}


def icon(name, cls='icon'):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')
