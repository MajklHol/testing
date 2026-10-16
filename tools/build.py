"""Builds index.html from src/template.html and data/map-paths.json.

The template is written as an Artifact fragment (no <html>/<head>/<body>), so this
wraps it into a standalone page that also works on GitHub Pages or from disk.
"""
import json, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
geo = json.loads((root / "data/map-paths.json").read_text())
tpl = (root / "src/template.html").read_text()
page = tpl.replace("__BORDER__", geo["border"]).replace("__RIVERS__", geo["rivers"])
head, body = page.split("</style>", 1)
html = (
    '<!doctype html>\n<html lang="sk">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    + head + "</style>\n</head>\n<body>\n" + body.strip() + "\n</body>\n</html>\n"
)
(root / "index.html").write_text(html)
print("wrote index.html", len(html), "bytes")
