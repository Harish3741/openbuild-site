"""Save the next event on Open Build's Luma calendar to next-event.json, for the home page's Next up card.

Run every few hours by .github/workflows/next-event.yml, which commits the file when it changes.
It reads the calendar's public ICS feed (the one Luma gives for "Subscribe"), so no Luma API key is needed.
With no calendar set, no upcoming event, or Luma not answering, the card says "We're planning the next one."
"""
import json, re, sys, urllib.request
from datetime import datetime, timezone
from pathlib import Path

# Open Build's Luma calendar (luma.com/openbuildorg, on admin@open-build.org): its link or its id (cal-…). The id doesn't change if the link does.
LUMA = 'cal-sRW1HTbUigrclhW'

OUT = Path(__file__).resolve().parent.parent / 'next-event.json'
UA = {'User-Agent': 'Mozilla/5.0 (open-build.org next event)'}

def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
        return r.read().decode('utf8')

def calendar_id():
    if LUMA.startswith('cal-'):
        return LUMA
    page = get(LUMA)
    m = re.search(r'"calendar_api_id":"(cal-\w+)"', page) or re.search(r'"api_id":"(cal-\w+)"', page)
    if not m:
        raise SystemExit(f'No Luma calendar id found on {LUMA}')
    return m.group(1)

def events(ics):
    # Unfold continuation lines, then read each VEVENT's fields (DTSTART;TZID=… keeps only the name before the ;)
    ics = re.sub(r'\r?\n[ \t]', '', ics)
    for block in re.findall(r'BEGIN:VEVENT(.*?)END:VEVENT', ics, re.S):
        f = {}
        for line in block.splitlines():
            if ':' in line:
                k, v = line.split(':', 1)
                f[k.split(';')[0]] = re.sub(r'\\([,;\\])', r'\1', v).replace('\\n', '\n')
        yield f

def when(v):
    return datetime.strptime(v, '%Y%m%dT%H%M%SZ').replace(tzinfo=timezone.utc)

def next_event():
    if not LUMA:
        return {}
    now, best = datetime.now(timezone.utc), None
    for f in events(get(f'https://api.lu.ma/ics/get?entity=calendar&id={calendar_id()}')):
        if f.get('STATUS') == 'CANCELLED' or not f.get('DTSTART', '').endswith('Z'):
            continue
        start, end = when(f['DTSTART']), when(f.get('DTEND', f['DTSTART']))
        link = re.search(r'https://(?:luma\.com|lu\.ma)/[\w-]+', f.get('DESCRIPTION', '') + ' ' + f.get('URL', ''))
        if end > now and link and (best is None or start < best[0]):
            # Only the venue name, not the full street address. A hidden or unset venue comes through as a Luma link: left blank.
            where = f.get('LOCATION', '').split(',')[0].strip()
            best = (start, {'name': f.get('SUMMARY', '').strip(), 'start': start.isoformat(), 'end': end.isoformat(),
                            'where': '' if where.startswith('http') else where, 'url': link.group(0)})
    return best[1] if best else {}

if __name__ == '__main__':
    try:
        ev = next_event()
    except Exception as e:
        # Keep whatever was saved last rather than blanking the card on a bad fetch. A warning, not a failure,
        # so a Luma hiccup doesn't email a failed-run notice every few hours (the page hides a past event anyway).
        print(f'::warning::Luma fetch failed, kept next-event.json as it was: {e}')
        sys.exit(0)
    text = json.dumps(ev, indent=1, ensure_ascii=False) + '\n'
    if not OUT.exists() or OUT.read_text(encoding='utf8') != text:
        OUT.write_text(text, encoding='utf8')
    print(text, end='')
