# Open Build website

**Read first (13 Nov):** [notes/OVERNIGHT-12-NOV.md](notes/OVERNIGHT-12-NOV.md) has what was built overnight on 12 Nov, the choices made, the other options and what needs Harish's call.

**Since 12 Nov the site is three pages** built from shared parts: `src/pages/home.html`, `societies.html` and `partners.html` (one body each) plus `src/parts/` (`style.css`, `header.html`, `contact.html`, `footer.html`, `site.js`). `python3 build.py` writes `door.html` (the main page, published as the artifact's index), `societies.html` and `partners.html` (whole documents published beside it as artifact files) and `preview/` copies for local viewing. `{{HOME}}` in a part or page is the link back to the main page. Older sections of this README that mention `src/door.html` describe the single-page version.

Draft site for Open Build (Harish + Varun's Sydney go-between for uni societies and companies/communities). Background: `~/Documents/Societies/Open Build/ABOUT.md`. Research behind the design: `~/Documents/Societies/Open Build/Research/website/` (README.md is the summary).

## Status (10 Nov 2026)

**Decision (10 Nov):** go with A ("The Door") for everything, but use B's opening-doorway hero animation. `src/door.html` is now that merged version and is the main site. `src/after-hours.html` is kept for reference only.

| Direction | Source | Live preview (private artifact) |
|---|---|---|
| A, "The Door": light, editorial, follows the system theme | `src/door.html` | https://claude.ai/artifact/D6ZtBxnj4FDkUa7dMMVq5m |
| B, "After Hours": dark night-event poster, doorway of light | `src/after-hours.html` | https://claude.ai/artifact/FU8as8bP1RsWwMvcSrjz2T |

To republish from another session, pass the artifact URL as `url`, publish `door.html` and pass `files` for `societies.html`, `partners.html` and any image that changed (`img/*.jpg`).

## Build

`python3 build.py` injects `sprite.svg.html` (logo mark + wordmark from the brand kit) into `src/*.html` and writes:
- `door.html` / `after-hours.html`: artifact bodies with no doctype, since the Artifact tool adds the skeleton
- `preview/*.html`: full documents to open locally

Always edit `src/`, never the built files.

## Design rules (11 Nov polish pass)

- Mono type is for data only (dates, years, counts). No small all-caps labels above headings.
- Buttons are 10px-radius rectangles. A secondary action is a text link with an arrow, not an outlined button.
- Motion: tokens `--ease-out` / `--ease-in-out` in `:root`, and entrances use ease-out. The hero plays once on load, with every piece starting together. Below it, each `[data-stage]` is one scroll stage: when it scrolls in, every `[data-reveal]`, `.strip` and `.timeline` inside it starts at the same moment. **No stagger, on Harish's instruction, except photo cards (`.shots`): since 14 Nov each card comes in on its own and cards that scroll in together follow one another 0.3s apart (`cardIO` in site.js).** He wants it unhurried: entrances run about 1.3–1.4s. The committee timeline is revealed by one left-to-right sweep (`.tl-cover`). Each committee box is drawn as an SVG outline by `draw()`, with the sides facing a neighbour torn into matching zigzags. The boxes either side of a handover jolt as the sweep reaches it. The sweep length is `--sweep` on `.timeline` (3.6s), which JS reads. The jolt timing inverts `--ease-sweep`, so if you change that curve, change `sweepTime` too. Reduced motion turns all of it off.
- The door's perspective is part of the leaf's own transform (`perspective(900px) rotateY(...)`), because WebKit can flatten a parent's `perspective`.

## Interactive pieces (11 Nov)

- **No audience picker** (12 Nov, Harish): the hero's "What brings you here?" buttons are gone. The hero line now follows the vibe of Julia's first LinkedIn draft ("Sydney's best builders are students…"). The cards below still carry each audience's way in.
- **Door**: scrolling the hero opens the leaf fully and grows `.beam` down onto the Next up card (`through()` and `fitBeam()` in the script). The door no longer follows the cursor (12 Nov).
- **Events live on home only** (Harish, 14 Nov): "Events we've run" is a row of `.shots` photo cards (date, name, one short line) after "Who we work with"; the societies and partners pages no longer have their own events sections. Home order: hero + Next up → Sydney's best builders (drawings) → Who we work with → Events → Who we are → contact.
- **"Sydney's best builders are students" drawings** (14 Nov, simplified the same day on Harish's ask): one inline SVG per point in the `.d-*` style: one row of people with a magnifying glass showing one of them up close (searching), two hands meeting at the fingertips, society ink and partner lavender (steady), and a partner and a student either side of one stack of blocks (together). Classes `.d-glass`, `.d-hand`, `.d-block`. The home photo strip is gone (h4h-room/tables/pitch stay only for after-hours.html).
- **No partner filter**: the "By event" filter on the logo wall was removed on 11 Nov (Harish: too complex). The wall is a plain grid again.
- **No "Find your match"**: the optional matcher beside the contact form was removed on 12 Nov (unchecked data, sat above the form on phones). The contact section is the tabs and the form only.
- **No students card** (Harish, 14 Nov). Student sign-up is the Next up card's "Get event news" button and the student contact tab.
- **Nav "Events"** goes to "Events we've run" (`#past`). The footer's Events link still points at `#events` (the Next up card) until the Luma link arrives.

## Content decisions

- **Societies shown** (every society that co-hosted an NCS event, per the Luma hosts and NCS records):
  - UNSW: No-Code Society, Enactus UNSW, AISoc, RAPSOC
  - USYD: SoftSoc, WIT USYD
  - UTS: TechSoc
  - Macquarie: MQAIS
- **Left out:**
  - EPIS × DevSoc: they invited NCS to a Shark Tank workshop, but there's no record it ran.
  - MSA MedSoc: listed as a HealthHack partner, but its uni is unclear.
- **Partner logo wall (11 Nov):** Base44, MLAI, Web Directions, UNSW Founders, Notion, Wix, A1Zap, Crucible Ventures (crucibleventures.vc, Nandit Shah's Sydney studio, not the US crucibleventures.com), arrayah (arrayah.city), Stone & Chalk, Collage, in brand colours from `img/logos/` (sources in `img/logos/SOURCES.md`). `build.py` inlines them at `<!--PARTNERS-->`, sizes them by aspect ratio and fills the last cell with a "Partner with us" link; edit the `PARTNERS` list there to add, drop or reorder. **Confirm each partner is OK being named before the site goes public.**
- **Next up card:** names no event for now ("We're planning the next one." + a "Get event news" button that opens the student tab). Random Hacks of Kindness is kept off the whole site while it is still being organised (Harish, 11 Nov). The old card is saved in `notes/next-up-rhok.html`; putting it back also needs the countdown lines (`const start=new Date('2026-12-04T18:00:00+11:00')` … `cd.textContent`) and dropping the `tba` class.
- **Track record:** H4H (170 checked in), HealthHack (126), Debugged on the page. Base44 Workshop / Build Your Life (45 registered) and the Notion workshop were run too but are not shown. Labelled as run through NCS before Open Build was named.
- **Photos:** hero strip is H4H (`img/h4h-*.jpg`, from `Societies/Hack for Humanity/Photos`); event panels use `img/ev-*.jpg` from the portfolio's `img/personal/` (hack-for-humanity-2, healthack-2, debugged-hacking-2).
- **Forms:** partner and society. They're UI only; submit shows a "preview, not connected" note.

## To do

1. Harish picks direction A or B (or a mix).
2. Open Build Luma calendar: Harish will add the link. Swap it into the footer "Luma soon" links and, once it has events, the Next up card.
3. Wire the forms: Tally/Formspree, or a Supabase table.
4. Instagram and LinkedIn handles go in the footer.
5. Buy **openbuild.club** at Porkbun (US$4.12 first year, US$15.96/yr renewal, checked 10 Nov 2026), then deploy (Vercel or Cloudflare Pages) and point DNS.
6. Get partner name sign-offs (see above).

## 12 Nov evening changes

- **Section order:** hero → who we work with → events we've run → committees → societies → partners → contact. Societies sit right above the partner wall.
- **No society is named anywhere on the site** (Harish, 14 Nov): no society names, logos or society-specific stats, and photos must not show society names on screens. The societies page says "Nine societies across UNSW, USYD, UTS and Macquarie" with no list; the committees diagram uses Society A/B/C; team members show only their uni. Event stats (builder counts, prizes) were removed too.
- **Events:** the Partners / Societies / Where list is gone from every event. On desktop all panels share one grid cell and closed ones stay laid out but invisible, so the box is always as tall as the tallest event.


## 13 Nov changes

- Home: the two audience cards are plain buttons (`.door-btn`); "Who we are" is a carousel of placeholder portraits (`.stack`, `.face`, script in `site.js`).
- Societies and companies pages: a drawing in the page head (`.draw`, figures `#d-pawn` and `#d-env` in `sprite.svg.html`), a "What you get" section and event blurbs with photos (`.shots`). Photo sources are in `img/PHOTOS.md`.
- Pages open at the top at once: smooth scrolling waits for `html.ready`, and leaving a page fades out and resets the scroll first (`site.js`, top of the file).
- Choices, other options and what needs Harish's call: `notes/ROUND-13-NOV.md`.
- Publishing: send `door.html` to the artifact with `societies.html`, `partners.html` and any new `img/` files as extra files.
