#!/usr/bin/env python3
"""Regression test: check_site.py must pass when the project sits beneath a parent directory
named 'data' (for example /mnt/data/...). A substring match on '/data' used to skip every page there.
Usage: python3 tools/test_check_site.py"""
import os, shutil, subprocess, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP = shutil.ignore_patterns('.git', '_site', '__pycache__')
with tempfile.TemporaryDirectory() as tmp:
    dest = os.path.join(tmp, 'mnt', 'data', 'src', 'project')
    shutil.copytree(ROOT, dest, ignore=SKIP)
    r = subprocess.run([sys.executable, os.path.join(dest, 'tools', 'check_site.py')], capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip().splitlines()
    last = out[-1] if out else ''
    pages = int(last.split()[0]) if last and last.split()[0].isdigit() else 0
    if r.returncode != 0 or pages < 1:
        print('FAIL: checker did not pass under', dest); print('\n'.join(out)); sys.exit(1)
    print(f'PASS: checker ran under a parent path containing "data" and "src": {last}')
