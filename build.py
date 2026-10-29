"""Build index.html for GitHub Pages from src/app.html.

src/app.html is the page body as written (title, styles and scripts first, then the app markup).
This wraps it in a full HTML document, adds the home-screen metadata, and registers the
offline service worker.
"""
from pathlib import Path

ROOT = Path(__file__).parent
src = (ROOT / "src" / "app.html").read_text(encoding="utf-8")

# everything before the app header belongs in <head>
split = src.index('<header class="top">')
head_part, body_part = src[:split], src[split:]

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Prepare the Balance Sheet, Statement of Profit and Loss and notes for non-corporate entities in the ICAI format. Export to Excel and PDF.">
<meta name="theme-color" content="#1d5b47">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="NCE Statements">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" sizes="192x192" href="icon-192.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<style>
:root { padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px); color-scheme: light; }
body { margin: 0; font: 14px/1.45 system-ui, -apple-system, "Segoe UI", sans-serif; }
img { max-width: 100%; }
[hidden] { display: none !important; }
</style>
"""

SW = """<script>
if ("serviceWorker" in navigator) addEventListener("load", () => navigator.serviceWorker.register("sw.js").catch(() => {}));
</script>
"""

out = HEAD + head_part + "</head>\n<body>\n" + body_part + SW + "</body>\n</html>\n"
(ROOT / "index.html").write_text(out, encoding="utf-8")
print(f"index.html written ({len(out):,} bytes)")
