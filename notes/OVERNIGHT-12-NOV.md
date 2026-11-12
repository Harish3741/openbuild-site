# Overnight build, 12 Nov 2026: what I chose and what else we could do

Site: https://claude.ai/artifact/D6ZtBxnj4FDkUa7dMMVq5m (version 17, everything below is live there and pushed to GitHub).

The site is now three pages. Home is for everyone. Two cards on home open a page for societies and a page for companies and communities.

## What's on each page

**Home (for everyone)**
1. Hero: "Doors open. Bring an idea." and the door. The paragraph under the headline is gone.
2. Next up card and the three Hack for Humanity photos.
3. What we're trying to do: "Sydney's best builders are students." plus three lines from Julia's LinkedIn draft (we do the searching, we keep it steady, we build together).
4. Who we work with: the societies card and the companies card. Clicking either opens its page. The students strip sits under them.
5. Events we've run: the same three events, same height.
6. Who we are: six first names with their society, next to the team photo from Hack for Humanity.
7. Contact form and footer.

**Societies page**
1. "Sponsors and speakers, without the cold emails." with what a society gets and an "Add your society" button.
2. How it works, in three steps.
3. Societies we've built with: the carousel, nine societies.
4. What we've run together: the three events with which societies were in each.
5. Contact form, opened on the society tab.

**Companies page**
1. "Every Sydney uni, through one contact." with what a partner gets and a "Start a collab" button.
2. How it works, in three steps.
3. "Committees change. We don't." with the timeline.
4. What we've run with partners: the three events with which partners were in each.
5. Who we've worked with: the logo wall.
6. Contact form, opened on the company tab.

## Things that need your call

- **Team names and photo.** The link is public ("anyone with the link"). Six first names and a photo of four of the team are now on it. Get everyone's OK before you share the link. A message you can send is at the bottom.
- **The three-step "How it works" on both pages is my wording.** I took it from `ABOUT.md` and the form fields. Check you're happy to promise "your society is in the room" and "we're still your contact next year".
- **"Nine societies"** counts RAPSOC and MedSoc. Take either out if they shouldn't be there and I'll change the number.
- **MedSoc.** You said to add "MSA MedSoc". It is the UNSW Medical Society: its crest is on the HealthHack poster on the NCS site. The card says "MedSoc, UNSW".
- **Students strip.** You described two audiences, but I kept the students strip on home so students still have a way in. Say the word and I'll remove it.
- **da goats** haven't replied yet about big events to show.

## Choices I made, and the other options

| # | What | What I chose | Other options |
|---|---|---|---|
| 1 | Site shape | Three pages: home, societies, companies | (a) One page with a societies/companies switch. (b) Four pages, with events on their own page. (c) A fourth page for students |
| 2 | Home order | What we do → who we work with → events → who we are | (a) Events straight after the hero, as proof first. (b) Who we are before events |
| 3 | Hero | Headline and door only | (a) One short line under the headline. (b) Two buttons in the hero, "For societies" and "For companies" |
| 4 | What we do | Julia's three lines | (a) The two problems from `ABOUT.md` (companies lack young talent, societies reset every year). (b) A row of numbers: 9 societies, 4 unis, 3 events |
| 5 | The two cards | Whole card is the link to its page | (a) Keep the cards as they were and add a separate "Learn more" link. (b) Make them bigger with a photo each |
| 6 | Who we are | One team photo and six first names with their society | (a) A headshot for each person (needs six photos). (b) Founders only, you and Varun, with a short story. (c) Photo only, no names. (d) A LinkedIn link per person |
| 7 | Societies list | Carousel that scrolls on its own and pauses on hover | (a) Arrows and swipe, no auto-scroll. (b) Grouped by uni with a heading each. (c) The equal grid from earlier tonight. (d) Two rows of logos only, moving in opposite directions |
| 8 | Carousel speed | About 4 seconds per society | Faster or slower: it's one number, `n*4` in `src/parts/site.js` |
| 9 | Committees timeline | On the companies page only, as you asked | Also on the societies page, since the handover is their problem too |
| 10 | Event proof on the two pages | Three short blurbs naming the societies or partners in each event | (a) Leave it off and only link to home. (b) Full case studies with a quote from a partner |
| 11 | Menu | Events, Societies, Partners. On phones the three links sit in a second row | (a) A hamburger menu on phones. (b) Rename to "For societies" and "For companies" |
| 12 | Contact form | Same form on all three pages, opened on the right tab | A shorter form on each page with only that audience's fields |
| 13 | Pricing | Only the "Free through 2026" line in the contact section | A small "what it costs" block: free in 2026, flagship event in 2027 |

## Fixed along the way

- Clicking a card halfway down home opened the next page halfway down. Every page now opens at the top. I checked this on the live link.
- Enactus now uses a sharper logo (from their Linktree).
- On phones the menu links were hidden, which would have left no way between pages. They now show.

## Still not done

- The forms don't send anywhere yet.
- Footer links (Luma, Instagram, LinkedIn) still say "soon".
- The "Free through 2026" wording is still an open question.
- Partner names and society logos still need sign-off before the site goes public.

## Message for da goats (not sent)

> for the site's who we are bit can everyone send a photo of themselves they're happy to have up
>
> and lmk if you're cool with your first name + society being on there

## Working on it from the PC

- Folder: `Projects\openbuild-site` (same repo, `Harish3741/openbuild-site`).
- Edit `src/pages/` (one file per page) and `src/parts/` (styles, header, contact form, footer, script). Then run `python build.py`.
- On the PC, `build.py` writes CRLF line endings, so run `sed -i 's/\r$//'` on the built `.html` files after.
- To update the link, publish `door.html` to the artifact URL above with `societies.html`, `partners.html` and any new images as extra files.
