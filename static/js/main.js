// Auto-prepend https:// if missing
document.addEventListener('DOMContentLoaded', function () {

    // ── Floating Particles ──
    const container = document.getElementById('particles');
    if (container) {
        for (let i = 0; i < 40; i++) {
            const p = document.createElement('div');
            p.className = 'particle';
            p.style.left = Math.random() * 100 + '%';
            p.style.animationDuration = (8 + Math.random() * 12) + 's';
            p.style.animationDelay = Math.random() * 10 + 's';
            p.style.width = p.style.height = (2 + Math.random() * 3) + 'px';
            p.style.opacity = (0.3 + Math.random() * 0.7);
            const colors = ['#7c3aed', '#00bcd4', '#00e676', '#a855f7'];
            p.style.background = colors[Math.floor(Math.random() * colors.length)];
            container.appendChild(p);
        }
    }

    // ── Form submit: auto-prepend scheme + show loader ──
    const form = document.getElementById('analyze-form');
    const btn = document.getElementById('analyze-btn');
    const loader = document.getElementById('btn-loader');
    const btnText = btn ? btn.querySelector('.btn-text') : null;
    const btnIcon = btn ? btn.querySelector('.btn-icon') : null;

    if (form) {
        form.addEventListener('submit', function (e) {
            const urlInput = document.getElementById('url-input');
            let val = urlInput.value.trim();

            if (val && !val.startsWith('http://') && !val.startsWith('https://')) {
                urlInput.value = 'https://' + val;
            }

            // Show loading state
            if (loader && btnText && btnIcon) {
                btnText.textContent = 'Analyzing...';
                btnIcon.style.display = 'none';
                loader.style.display = 'block';
                btn.style.opacity = '0.8';
                btn.style.pointerEvents = 'none';
            }
        });
    }

    // ── Input: live character count or visual feedback ──
    const urlInput = document.getElementById('url-input');
    if (urlInput) {
        urlInput.addEventListener('input', function () {
            const val = this.value;
            if (val.length > 0) {
                this.style.borderColor = 'rgba(124,58,237,0.5)';
            } else {
                this.style.borderColor = '';
            }
        });

        // Focus input on load
        urlInput.focus();
    }
});
