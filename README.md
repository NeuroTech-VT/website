# NeuroTech@VT Website Repository

This repository contains the source code for the official [NeuroTech@VT](https://neurotechatvt.org/) website. 

## Directory Structure

```text
.
├── index.html              # Main landing page
├── index.css               # Styles specific to the landing page
├── styles.css              # Global stylesheet
├── script.js               # Main client-side JavaScript logic
├── research.html           # Research overview page
├── research.css            # Styles for the research overview page
├── team.html               # Team members page
├── team.css                # Styles for the team page
├── blog.html               # Blog/updates page
├── blog.css                # Styles for the blog page
├── sponsors.html           # Sponsors page
├── sponsors.css            # Styles for the sponsors page
├── research/               # Sub-directory for detailed research project pages
│   ├── drone-swarm.html    # Drone Swarm project details
│   ├── eeg-wheelchair.html # EEG Wheelchair project overview
│   ├── eeg-wheelchair-hardware.html
│   ├── eeg-wheelchair-software.html
│   └── project.css         # Styles used within research project pages
├── crop_svg.py             # Utility script for processing SVG assets
├── NeuroTech_VT.svg        # Original logo asset
├── NeuroTech_VT_cropped.svg # Cropped logo asset used in navigation
└── [images/assets]         # Various images (e.g., group_photo.jpg)
```

## Notes

- **Styling:** The site uses a modular CSS approach where each major page has its own CSS file alongside a global `styles.css`.
- **Assets:** Use `crop_svg.py` for any transformations required for SVG assets.
- **Deployment:** [Insert deployment instructions here, e.g., "Push to main to trigger GitHub Pages/Vercel deployment."]
