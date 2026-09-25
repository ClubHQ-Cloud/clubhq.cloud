#!/usr/bin/env python3
"""Builds the help pages: /pomoc/ and /help/, and the install article in each.

    python3 tools/help/build.py                       # pages only
    python3 tools/help/build.py --shots <dir>         # also re-import screenshots

The site has no build step, so the output is committed like any hand-written page;
this script only exists so the two languages and the per-browser guides can't drift.
Edit `content.py`, re-run, commit both.

Screenshots come from real devices driven by automation (iOS Simulator via XCUITest,
Android emulator via adb): `<dir>/<set>-<lang>/<orientation>-<n>.png` plus
`<orientation>.json` holding the tapped control's box as window fractions. Importing
converts them to WebP under help-assets/install/ and records the boxes in
targets.json, which is what the highlight rings are drawn from.
"""
import argparse
import html
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
from content import GUIDES, TEXT, icon  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
ASSETS = os.path.join(ROOT, 'help-assets', 'install')
TARGETS = os.path.join(ASSETS, 'targets.json')
URLS = {
    'pl': {'index': '/pomoc/', 'install': '/pomoc/instalacja-aplikacji/'},
    'en': {'index': '/help/', 'install': '/help/install-app/'},
}
SITE = 'https://sportmatch.pl'
APP = 'https://app.sportmatch.pl'

# The home-screen result, cut out of the last portrait capture: the icon and a bit of
# wallpaper, as fractions of the screenshot (x, y, w, h). The capture's home screen
# also holds the test runner's own icon, which is why it is cropped rather than shown.
HOME_CROP = {
    'ios-27': (0.0, 0.322, 0.29, 0.125),
    'ios-26': (0.0, 0.322, 0.29, 0.125),
    'ios-17': (0.245, 0.205, 0.255, 0.12),
}


# --------------------------------------------------------------------------- import

def magick(*args):
    subprocess.run(['magick', *args], check=True)


def import_shots(src):
    targets = {}
    os.makedirs(ASSETS, exist_ok=True)
    for entry in sorted(os.listdir(src)):
        m = re.fullmatch(r'(android|ios-\d+)-(en|pl)', entry)
        if not m:
            continue
        shot_set, lang = m.groups()
        folder = os.path.join(src, entry)
        out = os.path.join(ASSETS, lang)
        os.makedirs(out, exist_ok=True)
        for orientation in ('portrait', 'landscape'):
            boxes_file = os.path.join(folder, f'{orientation}.json')
            boxes = json.load(open(boxes_file)) if os.path.exists(boxes_file) else {}
            shots = sorted(
                (f for f in os.listdir(folder) if re.fullmatch(rf'{orientation}-\d+\.png', f)),
                key=lambda f: int(re.search(r'\d+', f).group()),
            )
            for f in shots:
                n = int(re.search(r'\d+', f).group())
                name = f'{shot_set}-{orientation}-{n}'
                width = 560 if orientation == 'portrait' else 1120
                magick(os.path.join(folder, f), '-auto-orient', '-strip', '-resize', f'{width}x',
                       '-quality', '82', os.path.join(out, f'{name}.webp'))
                box = boxes.get(f'{orientation}-{n}')
                if box:
                    targets[f'{lang}/{name}'] = {k: round(v, 4) for k, v in box.items()}
            if orientation == 'portrait' and shots and shot_set in HOME_CROP:
                x, y, w, h = HOME_CROP[shot_set]
                last = os.path.join(folder, shots[-1])
                size = subprocess.run(['magick', 'identify', '-format', '%w %h', last],
                                      capture_output=True, text=True, check=True).stdout.split()
                W, H = int(size[0]), int(size[1])
                magick(last, '-auto-orient', '-strip',
                       '-crop', f'{int(W * w)}x{int(H * h)}+{int(W * x)}+{int(H * y)}', '+repage',
                       '-resize', '480x', '-quality', '82', os.path.join(out, f'{shot_set}-home.webp'))
    with open(TARGETS, 'w') as fh:
        json.dump(targets, fh, indent=1, sort_keys=True)
        fh.write('\n')


# --------------------------------------------------------------------------- pages

def image_size(path):
    out = subprocess.run(['magick', 'identify', '-format', '%w %h', path],
                         capture_output=True, text=True, check=True).stdout.split()
    return int(out[0]), int(out[1])


def lockup():
    return '''<a href="/" class="lockup tone-auto">
                    <svg viewBox="0 0 100 100" role="img" aria-label="Sport Match">
                        <path d="M12 56 H24 L36 28 L50 70" fill="none" stroke="currentColor" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>
                        <path d="M50 70 L64 28 L76 56 H88" fill="none" stroke="var(--chq-mark-accent)" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    <span class="lockup-word">Sport <span>Match</span></span>
                </a>'''


def footer():
    """The legal pages' footer, with its links made root-relative for pages that live
    in a subdirectory."""
    source = open(os.path.join(ROOT, 'regulamin.html'), encoding='utf-8').read()
    block = source[source.index('    <footer'):source.index('</footer>') + len('</footer>')]
    block = re.sub(r'href="(?!https?:|mailto:|tel:|/|#)', 'href="/', block)
    return block.replace('href="/index.html#', 'href="/#').replace('href="/index.html"', 'href="/"')


def page(lang, key, title, description, body, extra_head=''):
    other = 'en' if lang == 'pl' else 'pl'
    here, there = URLS[lang][key], URLS[other][key]
    login = 'Zaloguj się' if lang == 'pl' else 'Log in'
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(title)}</title>
    <meta name="description" content="{html.escape(description)}">
    <link rel="canonical" href="{SITE}{here}">
    <link rel="alternate" hreflang="{lang}" href="{SITE}{here}">
    <link rel="alternate" hreflang="{other}" href="{SITE}{there}">
    <link rel="alternate" hreflang="x-default" href="{SITE}{URLS['pl'][key]}">
    <meta name="theme-color" content="#1a1d29">
    <link rel="icon" href="/favicon.ico" type="image/x-icon">
    <link rel="preload" href="/fonts/space-grotesk-300-700-latin.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="stylesheet" href="/style.css">
    <script src="/script.js" defer></script>{extra_head}
</head>
<body class="lang-{lang}">
    <!-- Generated by tools/help/build.py from tools/help/content.py — edit those, not this file. -->
    <header class="site-header">
        <div class="container">
            <div class="topbar">
                {lockup()}

                <div class="topbar-actions">
                    <div class="lang-switch">
                        <a class="lang-btn" href="{URLS['pl'][key]}" hreflang="pl"{' aria-current="page"' if lang == 'pl' else ''}>PL</a>
                        <a class="lang-btn" href="{URLS['en'][key]}" hreflang="en"{' aria-current="page"' if lang == 'en' else ''}>EN</a>
                    </div>

                    <a href="{APP}" class="btn btn-sm btn-ghost">{login}</a>
                </div>
            </div>
        </div>
    </header>

{body}

{footer()}
</body>
</html>
'''


def shot_figure(lang, shot_set, orientation, step, text, targets):
    if step['shot'] == 'home':
        name = f'{shot_set}-home'
    else:
        name = f'{shot_set}-{orientation}-{step["shot"]}'
    path = os.path.join(ASSETS, lang, f'{name}.webp')
    if not os.path.exists(path):
        return ''
    w, h = image_size(path)
    alt = TEXT[lang]['shot_alt'].format(text=re.sub(r'<[^>]+>', '', text))
    ring = ''
    box = targets.get(f'{lang}/{name}')
    if box:
        # A little air around the control, so the ring frames it instead of touching it.
        pad_x, pad_y = 0.012, 0.012 * w / h
        x, y = max(box['x'] - pad_x, 0), max(box['y'] - pad_y, 0)
        bw, bh = min(box['w'] + 2 * pad_x, 1 - x), min(box['h'] + 2 * pad_y, 1 - y)
        ring = (f'<span class="help-ring" style="left:{x * 100:.2f}%;top:{y * 100:.2f}%;'
                f'width:{bw * 100:.2f}%;height:{bh * 100:.2f}%"></span>')
    img = (f'<img src="/help-assets/install/{lang}/{name}.webp" width="{w}" height="{h}" '
           f'alt="{html.escape(alt)}" loading="lazy">')
    if step['shot'] == 'home':
        return f'''
                        <figure class="help-shot help-shot--home">
                            <div class="help-shot-crop">{img}</div>
                        </figure>'''
    # The screenshot inside a drawn phone, the way the simulator shows it: bezel, screen
    # corners and the camera cut-out the capture itself leaves blank. Drawn in CSS rather
    # than Apple's or Google's device artwork, which come with their own licence terms.
    device = 'pixel' if shot_set == 'android' else 'iphone'
    return f'''
                        <figure class="help-shot help-shot--{orientation}">
                            <div class="help-device help-device--{device} help-device--{orientation}">
                                <div class="help-device-body">
                                    <div class="help-device-screen">
                                        {img}{ring}
                                        <span class="help-device-camera" aria-hidden="true"></span>
                                    </div>
                                </div>
                            </div>
                        </figure>'''


def steps_list(lang, guide, orientation, flow, targets):
    items = []
    for i, step in enumerate(flow, 1):
        text = step[lang]
        figure = shot_figure(lang, guide.get('shots'), orientation, step, text, targets) if 'shot' in step else ''
        items.append(f'''
                    <li class="help-step">
                        <div class="help-step-head">
                            <span class="help-step-num" aria-hidden="true">{i}</span>
                            <p>{text}</p>
                            <span class="help-step-icon">{icon(step['icon'])}</span>
                        </div>{figure}
                    </li>''')
    return f'''
                <ol class="help-steps" data-orientation="{orientation}">{''.join(items)}
                </ol>'''


def install_article(lang, targets):
    t = TEXT[lang]
    chips = '\n'.join(
        f'                    <button type="button" class="help-chip" data-browser="{g["id"]}" aria-pressed="false">{html.escape(g["name"][lang])}</button>'
        for g in GUIDES)
    guides = []
    for g in GUIDES:
        flows = ''.join(
            steps_list(lang, g, orientation, g['flows'][orientation], targets)
            for orientation in ('portrait', 'landscape', 'any') if orientation in g['flows'])
        guides.append(f'''
            <section class="help-guide" data-browser="{g['id']}"{' data-oriented' if 'portrait' in g['flows'] else ''} aria-labelledby="guide-{g['id']}">
                <h2 id="guide-{g['id']}">{html.escape(g['name'][lang])}</h2>{flows}
            </section>''')
    faqs = ''.join(f'''
                <details class="help-faq">
                    <summary>{q}</summary>
                    <p>{a}</p>
                </details>''' for q, a in t['faqs'])
    body = f'''    <main class="help">
        <div class="container">
            <nav class="help-crumbs" aria-label="{t['help']}">
                <a href="{URLS[lang]['index']}">{t['help']}</a>
            </nav>

            <h1>{t['title']}</h1>
            <p class="help-lead">{t['lead']}</p>

            <div class="help-controls" hidden>
                <p class="help-label" id="browser-label">{t['browser']}</p>
                <div class="help-chips" role="group" aria-labelledby="browser-label">
{chips}
                </div>
                <p class="help-hint">{t['detected']}</p>

                <div class="help-orientation">
                    <p class="help-label" id="orientation-label">{t['orientation']}</p>
                    <div class="help-segmented" role="group" aria-labelledby="orientation-label">
                        <button type="button" data-orientation="portrait" aria-pressed="true">{t['portrait']}</button>
                        <button type="button" data-orientation="landscape" aria-pressed="false">{t['landscape']}</button>
                    </div>
                </div>
            </div>
{''.join(guides)}

            <section class="help-faqs">
                <h2>{t['faq']}</h2>{faqs}
            </section>

            <p class="help-actions">
                <a class="btn btn-primary" href="{APP}">{t['open_app']}</a>
                <a class="help-back" href="{URLS[lang]['index']}">{t['back']}</a>
            </p>
        </div>
    </main>'''
    return page(lang, 'install', t['page_title'], t['description'], body,
                '\n    <script src="/help-assets/help.js" defer></script>')


def help_index(lang):
    t = TEXT[lang]
    body = f'''    <main class="help">
        <div class="container">
            <h1>{t['help']}</h1>
            <p class="help-lead">{t['help_lead']}</p>

            <ul class="help-index">
                <li>
                    <a href="{URLS[lang]['install']}">
                        <span class="help-index-icon">{icon('smartphone')}</span>
                        <span>
                            <strong>{t['title']}</strong>
                            <span>{t['description']}</span>
                        </span>
                    </a>
                </li>
            </ul>
        </div>
    </main>'''
    return page(lang, 'index', t['help_title'], t['help_lead'], body)


def write(rel, content):
    path = os.path.join(ROOT, rel.strip('/'), 'index.html')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(content)
    print('wrote', os.path.relpath(path, ROOT))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--shots', help='capture directory to import screenshots from')
    args = parser.parse_args()
    if args.shots:
        import_shots(args.shots)
    targets = json.load(open(TARGETS)) if os.path.exists(TARGETS) else {}
    for lang in ('pl', 'en'):
        write(URLS[lang]['index'], help_index(lang))
        write(URLS[lang]['install'], install_article(lang, targets))


if __name__ == '__main__':
    main()
