# 13 Nov 2026: plain buttons, photos, team carousel, drawings

Site: https://claude.ai/artifact/D6ZtBxnj4FDkUa7dMMVq5m (version 18, everything below is live there).

## What changed

**Home**
- The two "Who we work with" cards are now plain buttons: "Societies" and "Companies and communities", each with a small drawing and an arrow. The headline and the three bullets moved to each page.
- "Who we are" is a carousel: a stack of photo cards with the name under it, arrows, and the six names as buttons. Swipe works on a phone. It steps on by itself every 4.5 seconds until someone moves it.
- The photos in the carousel are placeholders (a silhouette and the first letter). The team photo from Hack for Humanity is off the page for now.

**Societies page and companies page**
- The top of each page has a drawing next to the headline instead of the three bullets.
- New "What you get" section: the three bullets, each with a photo of that thing happening.
- "What we've run together / with partners": each of the three events has a photo.

**Moving between pages**
- A new page now opens at the top straight away. Before, it opened where the last page was left and then slid up. The page you leave fades out first.

## Photos (12 new, all from Google Drive)

Sources and Drive file names are in `img/PHOTOS.md`.

| Page | Where | Photo |
|---|---|---|
| Societies | Companies that want to back student events | HealthHack opening slide with the backers' logos |
| Societies | Judges, mentors and speakers | Three people working through a build at Hack for Humanity |
| Societies | Societies at other unis | "The organising societies" slide at Hack for Humanity |
| Societies | Hack for Humanity | Full room on day one |
| Societies | HealthHack Sydney | UNSW MedSoc speaking |
| Societies | Debugged | Kick-off at UNSW Founders |
| Companies | We pick the societies | Packed room at Hack for Humanity |
| Companies | We help run the day | Crucible Ventures' pitching workshop |
| Companies | You meet students who build | Bipolar Australia with a team |
| Companies | Hack for Humanity | The judges' row during final pitches |
| Companies | HealthHack Sydney | StatDoctor speaking at Stone & Chalk |
| Companies | Debugged | A speaker at UNSW Founders |

## Things that need your call

- **People in the photos.** These are event photos from the shared Drive folders, and the link is public. The close-up ones (the three people at the laptop, the Bipolar Australia photo, the StatDoctor and Crucible Ventures speakers) show faces clearly. Swap any you'd rather not use.
- **Captions name Crucible Ventures, Bipolar Australia and StatDoctor.** Their names were already on the site, but check they're fine next to a photo.
- **Team photos.** Send a photo per person and each placeholder becomes a real one (see below). The message for da goats in `OVERNIGHT-12-NOV.md` still stands.
- **Students strip.** Still on home under the two buttons. It now has more text than the buttons above it. Say if you want it cut down to match.

## Choices I made, and the other options

| # | What | What I chose | Other options |
|---|---|---|---|
| 1 | The two buttons | Name, small drawing, arrow | (a) Name and arrow only. (b) One line under each name |
| 2 | Where the bullets went | "What you get" on each page, with a photo each | Keep them as a list at the top of each page |
| 3 | Team carousel | Stack of cards, names as buttons, arrows, auto-step until touched | (a) No auto-step. (b) A row of six cards you scroll sideways. (c) A short quote per person, like Scorify |
| 4 | Placeholders | Silhouette and first letter, three colours | (a) Crops from the Hack for Humanity team photo (only four of the six are in it). (b) Initials only |
| 5 | Drawings | Two: shut door with cold emails vs open door (societies), four unis into one door (companies) | More: one per "How it works" step, one on home under "Sydney's best builders are students" |
| 6 | Page change | Fade out, open at the top | No fade, just the jump to the top |

## Swapping in a real team photo

In `src/pages/home.html`, each person is one `<figure class="face …">` with an `<svg>` inside. Replace the `<svg>…</svg>` with `<img src="img/team-harish.jpg" alt="Harish">` and run `python3 build.py`. Portrait photos (4:5) fit best.
