#!/usr/bin/env bash
# Runs the end-to-end scenario in headless Chrome with a fake Claude runtime (no API key needed).
# Usage: bash tests/run_headless.sh   (from the repo root; needs google-chrome or chromium)
set -e
cd "$(dirname "$0")/.."
python3 - <<'PY'
h = open('index.html', encoding='utf-8').read()
pre = open('tests/fake_claude_runtime.js', encoding='utf-8').read()
post = open('tests/scenario.js', encoding='utf-8').read()
h = h.replace('<script>\n"use strict";', '<script>' + pre + '</script>\n<script>\n"use strict";', 1).replace('</body>', '<script>' + post + '</script></body>')
open('tests/_test.html', 'w', encoding='utf-8').write(h)
PY
CHROME=$(command -v google-chrome || command -v chromium || command -v chromium-browser)
"$CHROME" --headless=new --no-sandbox --disable-gpu --virtual-time-budget=20000 --dump-dom "file://$PWD/tests/_test.html" 2>/dev/null \
 | python3 -c "import sys,re,html; d=sys.stdin.read(); m=re.search(r'<pre id=\"TESTOUT\">(.*?)</pre>', d, re.S); print(html.unescape(m.group(1)) if m else 'no output')"
