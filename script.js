let currentLang = 'pl';

function setLang(lang) {
    currentLang = lang;
    document.body.className = document.body.className.replace(/\blang-\w+\b/g, '').trim();
    document.body.classList.add('lang-' + lang);
    document.querySelectorAll('.lang-btn').forEach(btn => btn.classList.remove('active'));
    const btn = document.getElementById('btn-' + lang);
    if (btn) btn.classList.add('active');
    document.documentElement.lang = lang;
}

function initLanguage() {
    const userLang = navigator.language || navigator.userLanguage;
    if (userLang && userLang.toLowerCase().startsWith('pl')) {
        setLang('pl');
    } else {
        setLang('en');
    }
}

initLanguage();
