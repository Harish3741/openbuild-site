"""Build the site from src/parts (shared head, header, contact, footer, script) and src/pages (one body per page).
Outputs door.html (the main page, an artifact body with no skeleton), index.html (the same page as a whole document, for GitHub Pages), societies.html and partners.html (whole documents
published beside it) and preview/<name>.html (whole documents for local viewing)."""
import math, pathlib, re
root = pathlib.Path(__file__).parent
sprite = (root / 'sprite.svg.html').read_text(encoding='utf8')

# Partner logos: brand-colour SVGs in img/logos (sources in img/logos/SOURCES.md); black parts use currentColor so they follow the page ink.
# Each logo is sized by its aspect ratio so wide wordmarks and compact marks carry about equal weight.
# The number is an optical weight: <1 for logos that read heavy (solid blocks), >1 for light ones.
PARTNERS = [
    ('base44', 'Base44', 'https://base44.com', 1.0),
    ('mlai', 'MLAI', 'https://mlai.au', 1.15),
    ('builders-world', 'Builders World', 'https://thebuilders.world', 1.0),
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
    """Two carousel rows of partner logos, the second running the other way. Add a partner to PARTNERS and it joins a row."""
    items = []
    for slug, name, url, weight in PARTNERS:
        svg = (root / 'img' / 'logos' / f'{slug}.svg').read_text(encoding='utf8').strip()
        w, h = map(float, re.search(r'viewBox="[-\d.]+ [-\d.]+ ([\d.]+) ([\d.]+)"', svg).groups())
        r = w / h
        hh = min(H0 * r ** -K, 44) * weight
        svg = svg.replace('<svg ', f'<svg aria-hidden="true" focusable="false" style="--h:{hh:.1f}px;--r:{r:.3f}" ', 1)
        items.append(f'<li><a href="{url}" target="_blank" rel="noopener" aria-label="{name.replace("&", "&amp;")}">{svg}</a></li>')
    half = math.ceil(len(items) / 2)
    rows = [('', items[:half]), (' rev', items[half:])]
    return '\n'.join(f'<div class="socs-rail" data-reveal role="region" aria-label="Partners, row {i}"><ul class="socs plogos{cls}">{"".join(row)}</ul></div>'
                     for i, (cls, row) in enumerate(rows, 1))

# Uni logos for the drawings: <!--UNI:slug x y w h--> becomes img/unis/<slug>.svg nested at that box, left-aligned and centred vertically.
def uni_logo(m):
    slug, x, y, w, h = m.group(1), *m.group(2).split()
    svg = (root / 'img' / 'unis' / f'{slug}.svg').read_text(encoding='utf8').strip()
    svg = re.sub(r' xmlns="[^"]*"', '', svg, count=1)
    return svg.replace('<svg ', f'<svg class="d-uni" x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="xMinYMid meet" ', 1)

# The site is three pages built from shared parts (src/parts) and one body each (src/pages).
# (output name, page body, <title>, description, which contact form the page carries; the home page has none)
PAGES = [
    ('door', 'home', 'Open Build',
     "Open Build connects Sydney's uni societies with the companies and communities who want to build with them.", None),
    ('societies', 'societies', 'Open Build Societies',
     'For uni societies: sponsors, speakers and co-hosts through Open Build, and the societies we have built with.', 'society'),
    ('partners', 'partners', 'Open Build Partners',
     'For companies and communities: every uni through one contact, and who we have worked with.', 'partner'),
]
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800'
         '&family=Figtree:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap">\n')
# What the Artifact tool wraps the main page in; the other pages and the previews are whole documents, so they carry it themselves.
SKELETON = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
            '<style>:root{color-scheme:light;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);'
            'padding-bottom:env(safe-area-inset-bottom,0px)}html{scroll-padding-top:env(safe-area-inset-top,0px)}'
            'body{margin:0}img{max-width:100%}</style>\n')

def part(name):
    return (root / 'src' / 'parts' / name).read_text(encoding='utf8')

def page(out, body_name, title, desc, tab, home):
    """Return (head, body). `home` is the link back to the main page ('' on the main page itself)."""
    head = (f'<title>{title}</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n'
            f'<meta name="description" content="{desc}">\n' + FONTS
            + '<style>\n' + part('style.css') + '</style>\n'
            "<script>document.documentElement.classList.add('js');if(!location.hash){try{history.scrollRestoration='manual'}catch(e){}scrollTo(0,0)}</script>\n")
    header = part('header.html').replace(f'href="{out}.html"', f'href="{out}.html" aria-current="page"')
    main = (root / 'src' / 'pages' / f'{body_name}.html').read_text(encoding='utf8')
    # Anything between <!--HIDDEN ...--> and <!--/HIDDEN--> is left out of the built page
    main = re.sub(r'<!--HIDDEN.*?<!--/HIDDEN-->\n?', '', main, flags=re.S)
    # Each audience page ends on its own contact form; the other audience's form is cut
    contact = re.sub(r'<!--(\w+)-->\n(.*?)<!--/\1-->\n', lambda m: m.group(2) if m.group(1) == tab else '', part('contact.html'), flags=re.S) if tab else ''
    body = ('\n' + sprite + '\n' + header + '\n<main>\n' + main + '\n\n'
            + contact + '</main>\n\n' + part('footer.html')
            + '\n<script>\n' + part('site.js') + '</script>\n')
    # "Get in touch" goes to the page's form, or on the home page to the two audience buttons
    body = body.replace('{{CONTACT}}', '#join' if tab else '#who')
    body = body.replace('<!--PARTNERS-->', logo_wall() if '<!--PARTNERS-->' in body else '')
    body = re.sub(r'<!--UNI:(\S+) ([\d. ]+)-->', uni_logo, body)
    return head, body.replace('{{HOME}}', home)

(root / 'preview').mkdir(exist_ok=True)
for out, body_name, title, desc, tab in PAGES:
    main_page = out == 'door'
    # Published: the main page is index.html in the artifact, the others sit beside it
    head, body = page(out, body_name, title, desc, tab, '' if main_page else 'index.html')
    (root / f'{out}.html').write_text(head + body if main_page else SKELETON + head + '</head><body>' + body + '</body></html>\n', encoding='utf8')
    # GitHub Pages: the main page again as a whole document at index.html
    if main_page:
        (root / 'index.html').write_text(SKELETON + head + '</head><body>' + body + '</body></html>\n', encoding='utf8')
    # Local preview: whole documents in preview/, where the main page is door.html
    head, body = page(out, body_name, title, desc, tab, '' if main_page else 'door.html')
    doc = SKELETON + head + '</head><body>' + body + '</body></html>\n'
    (root / 'preview' / f'{out}.html').write_text(doc.replace('src="img/', 'src="../img/'), encoding='utf8')
    print('built', f'{out}.html')

# Direction B ("After Hours") is one self-contained file, kept for reference
for src in sorted((root / 'src').glob('*.html')):
    body = src.read_text(encoding='utf8').replace('<!--SPRITE-->', sprite)
    (root / src.name).write_text(body, encoding='utf8')
    head, _, rest = body.partition('</style>')
    doc = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
           '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
           + head + '</style></head><body>' + rest + '</body></html>')
    (root / 'preview' / src.name).write_text(doc.replace('src="img/', 'src="../img/'), encoding='utf8')
    print('built', src.name)
