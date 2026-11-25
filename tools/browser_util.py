"""Shared browser discovery for the optional QA tools (not used by the static build).

Order: BROWSER_EXECUTABLE environment variable, common Chrome/Chromium locations and
names on PATH, then Playwright's own managed Chromium. Returns launch kwargs for
playwright.chromium.launch(), or exits with a clear message."""
import os, shutil, sys

CANDIDATES = [
    '/usr/bin/google-chrome', '/usr/bin/google-chrome-stable', '/usr/bin/chromium', '/usr/bin/chromium-browser',
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/Applications/Chromium.app/Contents/MacOS/Chromium',
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
]
NAMES = ['google-chrome', 'google-chrome-stable', 'chromium', 'chromium-browser', 'chrome']

def launch_args(extra=None):
    args = ['--no-sandbox'] + list(extra or [])
    exe = os.environ.get('BROWSER_EXECUTABLE')
    if exe:
        if not os.path.exists(exe):
            sys.exit(f'BROWSER_EXECUTABLE is set to {exe!r}, which does not exist. Browser QA was not run.')
        return dict(executable_path=exe, args=args)
    for c in CANDIDATES:
        if os.path.exists(c): return dict(executable_path=c, args=args)
    for n in NAMES:
        w = shutil.which(n)
        if w: return dict(executable_path=w, args=args)
    return dict(args=args)  # fall back to Playwright-managed Chromium

def launch(p, tool, extra=None):
    """Launch Chromium; on failure print which optional test could not run and exit 2."""
    try:
        return p.chromium.launch(**launch_args(extra))
    except Exception as e:
        sys.exit(f'{tool}: no usable browser found ({str(e).splitlines()[0]}).\n'
                 f'This optional browser test was NOT run. Install Chrome/Chromium, set BROWSER_EXECUTABLE, '
                 f'or run "playwright install chromium". The static build and tools/check_site.py do not need a browser.')
