"""Build: inject the logo sprite into src/*.html.
Outputs <name>.html (artifact body, no skeleton) and preview/<name>.html (full document for local viewing)."""
import pathlib
root = pathlib.Path(__file__).parent
sprite = (root / 'sprite.svg.html').read_text()
(root / 'preview').mkdir(exist_ok=True)
for src in sorted((root / 'src').glob('*.html')):
    body = src.read_text().replace('<!--SPRITE-->', sprite)
    (root / src.name).write_text(body)
    head, _, rest = body.partition('</style>')
    doc = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
           '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
           + head + '</style></head><body>' + rest + '</body></html>')
    (root / 'preview' / src.name).write_text(doc.replace('src="img/', 'src="../img/'))
    print('built', src.name)
