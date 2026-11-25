#!/usr/bin/env bash
# Stage the public-only deployment artifact into ./_site and verify its contents.
# Used by .github/workflows/pages.yml and runnable locally: bash tools/stage_site.sh
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf _site && mkdir _site
cp -r index.html 404.html about research projects insights contact css js assets _site/
cp robots.txt sitemap.xml llms.txt manifest.webmanifest favicon.svg favicon.ico apple-touch-icon.png .nojekyll _site/
# Not needed by any page: the preserved original and two unused 1024 px logo derivatives stay in the repository only.
rm -rf _site/assets/brand/original
rm -f _site/assets/brand/sidera-mark-light-transparent-1024.png _site/assets/brand/sidera-mark-original-colors-transparent-1024.png

# Verify: nothing internal may be present, and the required public files must exist.
bad=0
for p in src tools data documentation .github .git assets/brand/original build.py README.md .gitignore; do
  if [ -e "_site/$p" ]; then echo "FORBIDDEN in _site: $p"; bad=1; fi
done
if find _site \( -name '*.py' -o -name '*.sh' -o -name '*.md' -o -name '.env*' -o -name '*.pyc' -o -name '*.zip' -o -name '*.log' -o -name '*.tmp' -o -name '*~' \) | grep -q .; then
  echo "FORBIDDEN file types in _site:"; find _site \( -name '*.py' -o -name '*.sh' -o -name '*.md' -o -name '.env*' -o -name '*.pyc' -o -name '*.zip' -o -name '*.log' -o -name '*.tmp' -o -name '*~' \); bad=1
fi
for p in index.html 404.html about/index.html research/index.html projects/index.html insights/index.html contact/index.html \
         css/site.css js/site.js sitemap.xml robots.txt manifest.webmanifest favicon.svg favicon.ico .nojekyll \
         assets/images/og-sidera-labs.png assets/brand/sidera-mark-512.png; do
  [ -e "_site/$p" ] || { echo "MISSING in _site: $p"; bad=1; }
done
[ "$bad" = 0 ] || exit 1
echo "_site OK: $(find _site -type f | wc -l) files"
