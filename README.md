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
- **"Sydney's best builders are students" drawings** (14 Nov, redrawn as one matched set in the clean-up pass): one inline SVG per point, all flat fills on the same 320×132 box, ground line and figure size: a row of people with a magnifying glass on one (searching), two chain links locked together, society ink and partner lavender (steady; Harish picked this on 14 Nov over hands, fists and a handshake, and prefers bold objects to people here), and two gears turning, a large ink one and a small lavender one (together; Harish picked this on 14 Nov over blocks, a laptop, a jigsaw, bricks, tools and an arch). Harish wants drawings simple, not cluttered. Classes `.d-glass`, `.d-lens`, `.d-lk`, `.d-hole`.
- **Clean-up pass (14 Nov):** every drawn door now opens the way the logo's does (leaf hinged left, swinging toward you) and has the same proportions; drawing labels share one baseline and grow on phones (`@media (max-width:560px){.draw text}`); the partners "What you get" cards lost their captions to match the societies page; "Societies we've built with" shows the four uni logos (undone the same evening: Harish wanted the society logo carousel back); team placeholders use the site's own figure (`#d-pawn`).
- **No partner filter**: the "By event" filter on the logo wall was removed on 11 Nov (Harish: too complex). The wall is a plain grid again.
- **No "Find your match"**: the optional matcher beside the contact form was removed on 12 Nov (unchecked data, sat above the form on phones). The contact section is now one form per audience page (see the 14 Nov evening round).
- **No students card** (Harish, 14 Nov). Student sign-up is the email field in the Next up card.
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
- **Next up card:** names no event for now ("We're planning the next one." + an email field with a "Get event news" button). Random Hacks of Kindness is kept off the whole site while it is still being organised (Harish, 11 Nov). The old card is saved in `notes/next-up-rhok.html`; putting it back also needs the countdown lines (`const start=new Date('2026-12-04T18:00:00+11:00')` … `cd.textContent`) and dropping the `tba` class.
- **Track record:** H4H (170 checked in), HealthHack (126), Debugged on the page. Base44 Workshop / Build Your Life (45 registered) and the Notion workshop were run too but are not shown. Labelled as run through NCS before Open Build was named.
- **Photos:** hero strip is H4H (`img/h4h-*.jpg`, from `Societies/Hack for Humanity/Photos`); event panels use `img/ev-*.jpg` from the portfolio's `img/personal/` (hack-for-humanity-2, healthack-2, debugged-hacking-2).
- **Forms:** partner (partners page), society (societies page) and the Next up email field (home). They're UI only; submit shows a "preview, not connected" note.

## To do

1. Harish picks direction A or B (or a mix).
2. Open Build Luma calendar: Harish will add the link. The footer's Events / Instagram / LinkedIn links are **hidden since 15 Nov** (Harish) until those accounts exist: they sit between `<!--HIDDEN-->` markers in `src/parts/footer.html` (`build.py` now strips HIDDEN blocks from parts too). Put the real links in, delete the two marker lines, and swap the Luma link into, once it has events, the Next up card.
3. Wire the forms: Tally/Formspree, or a Supabase table.
4. Instagram and LinkedIn handles go in the footer.
5. Buy **openbuild.club** at Porkbun (US$4.12 first year, US$15.96/yr renewal, checked 10 Nov 2026), then deploy (Vercel or Cloudflare Pages) and point DNS.
6. Get partner name sign-offs (see above).

## 12 Nov evening changes

- **Section order:** hero → who we work with → events we've run → committees → societies → partners → contact. Societies sit right above the partner wall.
- **Society names: only in "Societies we've built with"** (Harish, 14 Nov, corrected the same day). That section on the societies page is the logo carousel of all nine societies (`.socs`, `img/societies/`), and he wants it kept. Everywhere else stays generic: the committees diagram uses Society A/B/C, team members show only their uni, events carry no society names or society-specific stats, and photos don't show society names on screens.
- **Round of 14 Nov, evening (Harish):**
  - "Who we are" is **off the site for launch**. Its markup stays in `src/pages/home.html` between `<!--HIDDEN ...-->` and `<!--/HIDDEN-->`, which `build.py` leaves out; delete the two marker lines to bring it back.
  - **No contact section on home.** Each audience page ends on its own form only (no tabs, no student form): `contact.html` holds both forms between `<!--partner-->` / `<!--society-->` markers and `build.py` keeps the page's one. "Get in touch" and the footer's "soon" links use `{{CONTACT}}`: `#join` on the audience pages, `#who` (the two audience buttons) on home.
  - **Next up card** now has its own email field (`.next-form`), since the student form it used to open is gone.
  - **"What you get" and "How it works" are one section** on both audience pages (Harish, later the same night): "How it works." is three photo cards on a timeline (`ol.shots.rail`). The rail starts at a tick, has a numbered dot above the middle of each photo and ends in an arrowhead; each stretch draws in with its card. On phones it runs down the left with the dots beside the photos. The old benefit lines were folded into the step text.
  - **Headlines:** partners "One door to every uni.", societies "One door to every sponsor." (14 Nov; were "Every uni through one contact." / "Sponsors and speakers through one contact.") (the cold-emails line and its two-door drawing were too confusing). The societies drawing now mirrors the partners one: sponsors, speakers, judges and co-hosts → the door → You.
  - Other ways to draw "We keep it steady" and "We build together" were sent to Harish as an options sheet (S1-S3, T1-T3); the generator is not in the repo. Nothing changes on the site until he picks.
- **"We make it easy." maze on the societies page** (Harish, 15 Nov): the societies page's answer to the partners page's committee timeline, placed after "How it works." so both audience pages run hero → How it works → diagram section → logos → form (moved there the same day for consistency). Three grey routes set off from You together and each hits a dead end, the maze fades back, then the lavender Open Build line goes straight through to a company building (labelled Sponsor), which turns lavender. About 3.7s, plays once per stage like everything else. Turned down on the way there: rows of each company's "way in", a row of grey doors (too many doors on the site already: logo, home hero, home buttons and both audience heroes), a before/after list, and an "Ask once" ripple to sponsors/speakers/judges/co-hosts (repeats the hero drawing). The maze walls and routes were generated from a seeded maze (seed 6, 7×6 cells of 40px); the generator is not in the repo, so redraw walls and routes together.
- **Events:** the Partners / Societies / Where list is gone from every event. On desktop all panels share one grid cell and closed ones stay laid out but invisible, so the box is always as tall as the tallest event.


## 13 Nov changes

- Home: the two audience cards are plain buttons (`.door-btn`); "Who we are" is a carousel of placeholder portraits (`.stack`, `.face`, script in `site.js`).
- Societies and companies pages: a drawing in the page head (`.draw`, figures `#d-pawn` and `#d-env` in `sprite.svg.html`), a "What you get" section and event blurbs with photos (`.shots`). Photo sources are in `img/PHOTOS.md`.
- Pages open at the top at once: smooth scrolling waits for `html.ready`, and leaving a page fades out and resets the scroll first (`site.js`, top of the file).
- Choices, other options and what needs Harish's call: `notes/ROUND-13-NOV.md`.
- Publishing: send `door.html` to the artifact with `societies.html`, `partners.html` and any new `img/` files as extra files.

**Societies head drawing (14 Nov, late):** each of the four figures now shows what it is: sponsor with a coin, speaker with a speech bubble, judge holding up a "10" score card, co-hosts as a pair (ink + lavender, `.d-halo` separates them). Symbols inside the props use `.draw text.d-sym`.

**Partners carousel (14 Nov, late):** "Who we've worked with." is now the same carousel as the societies, in two rows (`ul.socs.plogos`, second row `.rev` runs the other way). `logo_wall()` in build.py splits `PARTNERS` in half, so adding a partner is one line there plus its SVG in `img/logos/`. The "Partner with us" grid cell became the link under the rows. site.js repeats each row until it covers the widest screen. Builders World (thebuilders.world) added, 12 partners. Societies drawing badges are ink only, one per figure, so lavender stays for "You".

**Societies drawing icons (14 Nov, late):** the four left-hand figures are gone; each row is one ink icon and its label (coin, speech bubble, "10" score card, microphone for co-hosts). Harish's call.

**One page colour (14 Nov, late):** no section has its own tint any more. "Committees change" on the partners page lost its `--paper-2` band (and the hidden team section would too), so every page is the page colour until the dark form and footer, like the home page. Sections after the first use `padding-top:0`, so the gaps match.

**Phone pass (14 Nov, late):** the hero door keeps a door's proportions at every width (`--dh` on `.doorway` sets the frame and the light on the floor; it used to go square on phones), less gap under the heading, nav and footer links have 38px+ tap areas, and the societies drawing's icons and labels are bigger (labels grow again under 560px). Checked at 320, 390, 768, 1000 and 1280px: no sideways scroll.
