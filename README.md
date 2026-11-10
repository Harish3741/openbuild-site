# Open Build website

Draft site for Open Build (Harish + Varun's Sydney go-between for uni societies and companies/communities). Background: `~/Documents/Societies/Open Build/ABOUT.md`. Research behind the design: `~/Documents/Societies/Open Build/Research/website/` (README.md is the summary).

## Status (10 Nov 2026)

**Decision (10 Nov):** go with A ("The Door") for everything, but use B's opening-doorway hero animation. `src/door.html` is now that merged version and is the main site. `src/after-hours.html` is kept for reference only.

| Direction | Source | Live preview (private artifact) |
|---|---|---|
| A, "The Door": light, editorial, follows the system theme | `src/door.html` | https://claude.ai/artifact/D6ZtBxnj4FDkUa7dMMVq5m |
| B, "After Hours": dark night-event poster, doorway of light | `src/after-hours.html` | https://claude.ai/artifact/FU8as8bP1RsWwMvcSrjz2T |

To republish from another session, pass the artifact URL as `url` and publish the built file with `files` for `img/h4h-room.jpg`, `img/h4h-tables.jpg` and `img/h4h-pitch.jpg`.

## Build

`python3 build.py` injects `sprite.svg.html` (logo mark + wordmark from the brand kit) into `src/*.html` and writes:
- `door.html` / `after-hours.html`: artifact bodies with no doctype, since the Artifact tool adds the skeleton
- `preview/*.html`: full documents to open locally

Always edit `src/`, never the built files.

## Content decisions

- **Societies shown** (every society that co-hosted an NCS event, per the Luma hosts and NCS records):
  - UNSW: No-Code Society, Enactus UNSW, AISoc, RAPSOC
  - USYD: SoftSoc, WIT USYD
  - UTS: TechSoc
  - Macquarie: MQAIS
- **Left out:**
  - EPIS × DevSoc: they invited NCS to a Shark Tank workshop, but there's no record it ran.
  - MSA MedSoc: listed as a HealthHack partner, but its uni is unclear.
- **Partners named:** MLAI, Base44, Web Directions, UNSW Founders, Notion, A1Zap, Wix (judge), Crucible Ventures, Stone & Chalk, Collage. **Confirm each is OK being named before the site goes public.**
- **Next up card:** Random Hacks of Kindness (MLAI × Web Directions, 4–5 Dec, Stone & Chalk). It links to luma.com/n6q3mp7y, where Open Build is a supporting community. The countdown is computed in JS.
- **Track record:** H4H (170 checked in), HealthHack (126), Base44 Workshop (45 registered), Debugged, Notion workshop. Labelled as run through NCS before Open Build was named.
- **Photos:** H4H only (`img/`, from `Societies/Hack for Humanity/Photos`).
- **Forms:** partner and society. They're UI only; submit shows a "preview, not connected" note.

## To do

1. Harish picks direction A or B (or a mix).
2. Open Build Luma calendar: Harish will add the link. Swap it into the footer "Luma soon" links and, once it has events, the Next up card.
3. Wire the forms: Tally/Formspree, or a Supabase table.
4. Instagram and LinkedIn handles go in the footer.
5. Buy **openbuild.club** at Porkbun (US$4.12 first year, US$15.96/yr renewal, checked 10 Nov 2026), then deploy (Vercel or Cloudflare Pages) and point DNS.
6. Get partner name sign-offs (see above).
