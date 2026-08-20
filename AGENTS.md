# AGENTS.md — NeuroTech@VT Website

> IMPORTANT: This is my actual desktop where my entire life is based on (it contains important documents, photos, financial information, work projects, etc), not a sandbox or container environment. Do not mess with system settings, and always use bash one command at a time so that human-in-the-loop authorizations are more granular. Use venv instead of adding packages to system python. 

## Project Overview

This is the official website for **NeuroTech@VT** (https://neurotechatvt.org/), a student organization at Virginia Tech building applied brain-computer interface (BCI) systems. The site is a static HTML/CSS/JS website that showcases research projects, team members, blog updates, and sponsors.

### Current Focus
The primary research project is an **EEG-powered wheelchair add-on** that translates imagined motion (motor imagery) into wheelchair movement. The team is split into hardware and software subteams.

---

## Directory Structure

```
.
├── index.html                # Main landing page
├── index.css                 # Landing page specific styles
├── styles.css                # Global stylesheet (CSS variables, layout, components)
├── script.js                 # Client-side JavaScript (theme, halftone, filters, effects)
├── research.html             # Research overview page
├── research.css              # Research page styles
├── team.html                 # Team members page
├── team.css                  # Team page styles
├── blog.html                 # Blog/updates page
├── blog.css                  # Blog page styles
├── sponsors.html             # Sponsors page
├── sponsors.css              # Sponsors page styles
├── alumni-network.html       # Alumni network page (placeholder)
├── arxiv.html                # arXiv publications page (placeholder)
├── CNAME                     # Domain config (www.neurotechvt.org)
├── research/                 # Detailed research project pages
│   ├── drone-swarm.html     # Drone Swarm project details
│   ├── eeg-wheelchair.html  # EEG Wheelchair project overview
│   ├── eeg-wheelchair-hardware.html
│   ├── eeg-wheelchair-software.html
│   └── project.css          # Shared styles for research project pages
├── assets/                   # Image assets
│   ├── NeuroTech_VT.svg           # Original logo
│   ├── NeuroTech_VT_cropped.svg   # Cropped logo for nav
│   ├── group_photo.jpg
│   ├── group_photo_hero_cropped.png
│   ├── group_photo_main_img.png
│   └── volunteering_img.png
└── docs/                     # Documentation
    ├── contact-fallback-feature.md  # Email client fallback feature design
    └── responsive-mobile-plan.md    # Responsiveness audit & improvement plan
```

### Placeholder Pages

The following pages exist but contain only minimal placeholder content:
- **`alumni-network.html`** — Alumni network page
- **`arxiv.html`** — arXiv publications page

---

## Key Technologies & Patterns

### HTML Structure
- **Modular pages**: Each major section (research, team, blog, sponsors) has its own HTML file
- **Shared layout**: Top bar, navigation, and footer are duplicated across pages (no templating)
- **Data attributes**: Used extensively for filtering (e.g., `data-category` on blog cards)

### CSS Architecture
- **CSS Variables**: Defined in `:root` for theming (dark/light mode)
- **Modular CSS**: Global `styles.css` + page-specific CSS files
- **Theme support**: `.light` class toggles CSS variable overrides
- **Typography**: IBM Plex Mono (primary) + IBM Plex Serif (headings)

### JavaScript (`script.js`)
The script handles multiple independent features:

1. **Theme Toggle** — Light/dark mode with localStorage persistence
2. **Halftone Hero** — Canvas-based halftone animation on the hero section
3. **Blog Filter** — Category filtering and search functionality
4. **Content Alignment** — Left/center text alignment toggle (persisted in localStorage)
5. **Scramble Effect** — Text scrambling animation on hover for nav links

---

## Common Tasks

### Running the Site
This is a static site — open any HTML file directly in a browser, or serve locally:
```bash
python3 -m http.server 8000
# Then visit http://localhost:8000
```

### Adding a New Blog Post
1. Open `blog.html`
2. Add a new `<article class="blog-card" data-category="...">` block
3. Include title, date, excerpt, and link
4. Use appropriate category: `update`, `research`, `event`, `recruiting`

### Modifying the Theme
1. **Colors**: Edit CSS variables in `styles.css` (`:root` and `.light`)
2. **Toggle behavior**: Modify `initTheme()` and `toggleTheme()` in `script.js`

### Adding a New Research Project Page
1. Create new HTML file in `research/` directory
2. Link from `research.html`
3. Use `project.css` for consistent styling
4. Add content alignment toggle if needed (the script auto-generates it for `.project-col`)

### Updating Team Information
1. Edit `team.html`
2. Add/edit member cards in the appropriate section
3. Update the filmstrip gallery if needed

### Placeholder Pages — Not for Agents
Pages like `alumni-network.html` and `arxiv.html` contain minimal placeholder content waiting for real project information. Agents should **not** write content for these pages — they require input from team members with project knowledge.

### Working on Responsive Design
1. See `docs/responsive-mobile-plan.md` for a full audit and phased improvement plan
2. Key breakpoints: `900px`, `768px`, `600px`, `400px`
3. Touch targets should be at least 44px (Apple HIG) or 48px (Material Design)
4. The team page `.member-card-grid` and filmstrip gallery are the most broken elements on mobile

---

## Code Conventions

- **CSS**: Use the existing CSS variables (`--bg`, `--fg`, `--accent`, etc.) rather than hardcoding colors
- **JavaScript**: All scripts run on page load; wrap feature code in IIFEs to avoid polluting global scope
- **Links**: Use relative paths (e.g., `research.html`, not `/research.html`)
- **Images**: Place images in root directory or create an `assets/` folder
- **External resources**: Font is loaded from Google Fonts (IBM Plex Mono/Serif)

---

## Deployment

Push changes to the main branch to trigger deployment via **GitHub Pages**. The site is hosted at https://neurotechatvt.org/ (configured via `CNAME` file with `www.neurotechvt.org`).

---

## Notes for Agents

- This is a **static site** with no build step or framework
- Changes to HTML require manual updates to all pages (no templating)
- The `script.js` handles multiple unrelated features — be careful when modifying
- The halftone canvas animation is performance-sensitive; test on various screen sizes
- Blog filtering works with both category buttons and search input
- The content alignment toggle uses `localStorage` key `content-align`
- The theme toggle uses `localStorage` key `theme`
- When asked about elements that exist throughout many pages (e.g., nav links, buttons), always check the `research/` subpages in addition to the root-level HTML files — for example, the arXiv link in the top bar exists on 9 pages: index.html, research.html, team.html, blog.html, sponsors.html, and research/{eeg-wheelchair.html, eeg-wheelchair-hardware.html, eeg-wheelchair-software.html, drone-swarm.html}
- **Placeholder pages** (alumni-network.html, arxiv.html) are minimal — they link from other pages but have no real content yet. Agents must **not** write page content for these — they require team members with project knowledge
- **Contact button** uses `mailto:neurotechatvt@proton.me` — see `docs/contact-fallback-feature.md` for the planned fallback behavior if no email client is configured
- **Responsive design** is a work in progress — see `docs/responsive-mobile-plan.md` for the full audit. Several phases have been completed (touch targets, grid layout, spacing, global consistency) but advanced features (hamburger menu) remain TODO
- **CSS breakpoints**: Site uses 900px, 768px, 600px, and 400px breakpoints. Responsive rules are spread across `styles.css` and page-specific CSS files
- **CNAME**: The file `CNAME` contains `www.neurotechvt.org` for GitHub Pages custom domain
- **Assets**: There are image assets in the root directory (not all in `assets/` folder) — e.g., `group_photo.jpg`, `group_photo_hero_cropped.png`, `group_photo_main_img.png`, `volunteering_img.png`