"""Build: inject the logo sprite and the partner logo wall into src/*.html.
Outputs <name>.html (artifact body, no skeleton) and preview/<name>.html (full document for local viewing)."""
import math, pathlib, re
root = pathlib.Path(__file__).parent
sprite = (root / 'sprite.svg.html').read_text(encoding='utf8')

# Partner logos: brand-colour SVGs in img/logos (sources in img/logos/SOURCES.md); black parts use currentColor so they follow the page ink.
# Each logo is sized by its aspect ratio so wide wordmarks and compact marks carry about equal weight.
# The number is an optical weight: <1 for logos that read heavy (solid blocks), >1 for light ones.
PARTNERS = [
    ('base44', 'Base44', 'https://base44.com', 1.0),
    ('mlai', 'MLAI', 'https://mlai.au', 1.15),
    ('web-directions', 'Web Directions', 'https://webdirections.org', 1.05),
    ('unsw-founders', 'UNSW Founders', 'https://unswfounders.com', .95),
    ('notion', 'Notion', 'https://www.notion.com', 1.0),
    ('wix', 'Wix', 'https://www.wix.com', .74),
    ('a1zap', 'A1Zap', 'https://www.a1zap.com', 1.1),
    ('crucible-ventures', 'Crucible Ventures', 'https://www.crucibleventures.vc', 1.28),
    ('arrayah', 'arrayah', 'https://arrayah.city', 1.1),
    ('stone-chalk', 'Stone & Chalk', 'https://www.stoneandchalk.com.au', 1.0),
    ('collage', 'Collage', 'https://www.collageapp.com.au', .95),
]
H0, K = 52, .4  # height = H0 * aspect^-K: wide wordmarks shrink less than pure equal-area would

def logo_wall():
    items = []
    for slug, name, url, weight in PARTNERS:
        svg = (root / 'img' / 'logos' / f'{slug}.svg').read_text(encoding='utf8').strip()
        w, h = map(float, re.search(r'viewBox="[-\d.]+ [-\d.]+ ([\d.]+) ([\d.]+)"', svg).groups())
        r = w / h
        hh = min(H0 * r ** -K, 44) * weight
        svg = svg.replace('<svg ', f'<svg aria-hidden="true" focusable="false" style="--h:{hh:.1f}px;--r:{r:.3f}" ', 1)
        items.append(f'<li><a href="{url}" target="_blank" rel="noopener" aria-label="{name.replace("&", "&amp;")}">{svg}</a></li>')
    # Fill the last grid row with an invitation rather than leaving a hole
    items.append('<li class="add"><a href="#join" data-tab="partner">Partner with us <span class="arr" aria-hidden="true">→</span></a></li>')
    return '<ul class="logos" data-reveal>' + ''.join(items) + '</ul>'

(root / 'preview').mkdir(exist_ok=True)
for src in sorted((root / 'src').glob('*.html')):
    body = src.read_text(encoding='utf8').replace('<!--SPRITE-->', sprite)
    if '<!--PARTNERS-->' in body:
        body = body.replace('<!--PARTNERS-->', logo_wall())
    (root / src.name).write_text(body, encoding='utf8')
    head, _, rest = body.partition('</style>')
    doc = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
           '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
           + head + '</style></head><body>' + rest + '</body></html>')
    (root / 'preview' / src.name).write_text(doc.replace('src="img/', 'src="../img/'), encoding='utf8')
    print('built', src.name)
