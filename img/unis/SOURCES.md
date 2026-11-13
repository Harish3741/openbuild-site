# Uni logos

Used in the drawing at the top of partners.html (`<!--UNI:slug x y w h-->` in the page, inlined by `build.py`). Black parts use `currentColor`, so they follow the page ink and turn light in dark mode; brand colours stay. Pulled 14 Nov 2026.

| File | Source | How |
|---|---|---|
| unsw.svg | unsw.edu.au header PNG (`/content/dam/images/graphics/logos/unsw/unsw_0.png`, 330 px) | No official vector on the site: the crest is embedded as a WebP; "UNSW SYDNEY" is the PNG's alpha used as a mask over `currentColor` |
| usyd.svg | sydney.edu.au `/content/dam/icons/logos/logo-usyd-dark.svg` | Official vector; #141414 → currentColor |
| uts.svg | uts.edu.au footer SVG (`restricteduts-logofooter.svg`) | Official vector; white → currentColor |
| macquarie.svg | en.wikipedia.org "Logotype of Macquarie University.svg" (mq.edu.au sits behind a bot check) | Vector; reds, grey and white lighthouse kept, black text → currentColor |
