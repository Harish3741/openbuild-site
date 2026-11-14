# Partner logos

Brand-colour SVGs. Brand colours are fixed; parts that are black in the original use `currentColor`, so they follow the page ink and turn light in dark mode (how most brands do their dark versions). `build.py` inlines them and sizes each by aspect ratio. Pulled 11 Nov 2026 from each organisation's own site.

| File | Source | How |
|---|---|---|
| builders-world.svg | thebuilders.world site icon (1024 px PNG) + header | Three-piece mark traced as vectors with its pink, blue and green gradients (the soft highlight is left out); "Buildersworld" set in Inter Bold, as their header does. Added 14 Nov 2026 |
| base44.svg | base44.com header SVG | Official vector; orange kept |
| notion.svg | notion.com footer wordmark SVG | Official vector; white cube with black lines kept |
| web-directions.svg | webdirections.org/wp-content/themes/wd/images/wdlogo.svg | Official vector (their logo is all black) |
| stone-chalk.svg | stoneandchalk.com.au/_nuxt/logo.DwoXkII7.svg | Official vector; purples kept |
| wix.svg | wix.com header SVG | Official vector (their logo is all black) |
| crucible-ventures.svg | crucibleventures.vc header (`assets/mark.svg` + name) | Official CV mark (blue V #4F6AED kept); "Crucible Ventures" set in Schibsted Grotesk 600, their site font |
| unsw-founders.svg | unswfounders.com header PNG (1500 px) | Traced; yellow #FCDC10 box with black UNSW |
| collage.svg | collageapp.com.au wordmark PNG (993 px) | Traced; brand periwinkle #A0BCFC |
| mlai.svg | mlai.au kangaroo badge + `text_logo.png` | Kangaroo is an illustration, embedded as a 192 px WebP; "MLAI" letters traced |
| a1zap.svg | a1zap.com header (app icon + name) | App Store icon embedded as a 192 px WebP; "A1Zap" set in Inter SemiBold, as their header does |
| arrayah.svg | arrayah's Luma calendar avatar (1536 px) | Cream "A" mark traced onto their night navy; "arrayah" set in Lato Bold, their site font |

To swap one: drop an SVG with a tight viewBox here (keep the file name; use `currentColor` for any black parts), then run `python build.py`. Adjust its optical weight in `PARTNERS` in build.py if it looks heavy or light next to the others.
