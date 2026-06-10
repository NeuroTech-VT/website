# NeuroTech@VT Website Repository

This repository contains the source code for the [NeuroTech@VT](https://neurotechatvt.org/) website.

## TODO

The following pages are placeholders awaiting content:

- **alumni-network.html** — Alumni network page
- **arxiv.html** — arXiv publications page
- **sponsors-onboarding.html** — Sponsor onboarding flow

## Directory Structure

```
.
├── index.html              # Main landing page
├── index.css               # Landing page specific styles
├── styles.css              # Global stylesheet (CSS variables, layout, components)
├── script.js               # Client-side JavaScript (theme, halftone, filters, effects)
├── research.html           # Research overview page
├── research.css            # Research page styles
├── team.html               # Team members page
├── team.css                # Team page styles
├── blog.html               # Blog/updates page
├── blog.css                # Blog page styles
├── sponsors.html           # Sponsors page
├── sponsors.css            # Sponsors page styles
├── alumni-network.html     # Alumni network page (placeholder)
├── arxiv.html              # arXiv page (placeholder)
├── sponsors-onboarding.html # Sponsor onboarding page (placeholder)
├── research/               # Detailed research project pages
│   ├── drone-swarm.html    # Drone Swarm project details
│   ├── eeg-wheelchair.html # EEG Wheelchair project overview
│   ├── eeg-wheelchair-hardware.html
│   ├── eeg-wheelchair-software.html
│   └── project.css         # Shared styles for research project pages
├── assets/                 # Image assets
│   ├── NeuroTech_VT.svg           # Original logo
│   ├── NeuroTech_VT_cropped.svg   # Cropped logo for nav
│   ├── group_photo.jpg
│   ├── group_photo_hero_cropped.png
│   ├── group_photo_main_img.png
│   └── volunteering_img.png
├── docs/                   # Documentation
│   └── contact-fallback-feature.md
├── AGENTS.md               # Agent-specific instructions for working on this project
└── CNAME                   # Domain configuration
```

## Running Locally

This is a static site — open any HTML file directly in a browser, or serve locally:

```bash
python3 -m http.server 8000
# Then visit http://localhost:8000
```

## Deployment

Push changes to the main branch to trigger deployment via GitHub Pages. The site is hosted at https://neurotechatvt.org/.

## Technologies

- **HTML**: Modular pages with duplicated layout (no templating)
- **CSS**: Modular CSS with CSS variables for theming (dark/light mode)
- **JavaScript**: Client-side features including theme toggle, halftone animation, blog filtering, content alignment toggle, and text scramble effects
- **Fonts**: IBM Plex Mono (primary) + IBM Plex Serif (headings) via Google Fonts

