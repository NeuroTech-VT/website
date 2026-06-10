# Responsiveness Audit & Plan

## Current State Summary

The site has **9 HTML pages** across root + `research/` subdirectory. There are bare-minimum responsive breakpoints at `900px` and `600px` in `styles.css`, plus some page-specific ones, but **many layout problems are unaddressed**. The site is essentially built for desktop-first and adapted via `!important` overrides in `index.css` and `blog.css`.

---

## Key Issues Found

### 1. **Top bar** (`styles.css`)
- At `600px`, `topbar-left span:not(:first-child)` hides — but the left side is empty on all pages anyway. The right side (GitHub, arXiv, Contact, theme toggle) has **no responsive treatment** beyond the empty left-side rule.
- **Problem**: On narrow screens (< 400px), the topbar items overflow.

### 2. **Navigation bar** (`styles.css`)
- At `900px`, nav-right is hidden, nav-links get `overflow-x: auto`. This works but the nav-links items (Research, Team, Blog, Sponsors) have fixed padding (`padding: 0 14px`) — on very narrow screens they'll squeeze.
- **Problem**: No hamburger/mobile menu pattern. The links just scroll horizontally which is fine for 4 items but could be improved.

### 3. **Hero section** — major issue across all pages
- **`index.html`**: The hero uses `display: flex; flex-direction: row` with `!important` (in `index.css`). The image and text sit side-by-side. At `768px` they stack, with the image coming first via `order`. This is fragile.
- **All other pages**: The hero uses `<canvas id="halftone-hero">` positioned absolutely + a gradient overlay. The hero text has `max-width: 520px`. On mobile, the canvas covers the full hero but it's just decorative — the real problem is **padding and font sizes**.
- `hero-title` goes from `30px` → `22px` at 600px, but the `hero-desc` max-width stays at `520px` which is wider than most phone screens.

### 4. **Project description section** (index.html)
- `.project-desc-inner` has `max-width: 800px; margin: 0 auto` — fine for desktop but no responsive padding adjustments on mobile beyond the default `padding: 32px 20px`.

### 5. **Research page** (`research.css`)
- Project rows use `grid-template-columns: 56px 1fr 32px`. At 600px they shrink to `40px 1fr 28px` — okay, but the title (`font-size: 17px`) and description (`font-size: 11px`) don't adjust further.
- Filter bar (`height: 34px` on desktop) goes to `height: auto` with wrapping at 600px — good, but could use better spacing.

### 6. **Team page** (`team.css`)
- `member-card-grid` uses `grid-template-columns: repeat(3, 200px)` with `gap: 40px`. The **fixed column width** of 200px with 40px gap means it **overflows** on screens narrower than ~720px (3×200 + 2×40 + padding).
- No responsive breakpoints for the member card grid at all.
- `.member-row` uses `grid-template-columns: 48px 220px 130px 1fr` — will break badly on mobile.
- The filmstrip gallery's `frame-inner` is `width: 280px; height: 300px` with 3px border. On small screens this overflows.

### 7. **Blog page** (`blog.css`)
- The `blog-card` width override (`33.3333%` via flex) and breakpoints at `900px` (50%) and `600px` (100%) work — but **the blog-card height=120px** image section has no responsive adjustment.
- Search input (`width: 140px`) doesn't grow on mobile — the filter bar wraps but the search stays narrow.

### 8. **Sponsors page** (`sponsors.css`)
- `.sponsors-about-photo` has `min-height: 360px` — at 900px it collapses to `flex-direction: column` but `min-height: 220px` is still large on phone.
- `.sponsors-cta-title` is `font-size: 38px` — no mobile breakpoint for this.
- CTA button padding is `10px 28px` — appropriate, but `font-size: 12px` is small.

### 9. **Project subpages** (`project.css`)
- `metrics-row` has responsive at 900px (3 cols) and 600px (2 cols) — good.
- `project-col` max-width 800px with no mobile padding adjustment beyond `padding: 16px 14px` at 600px.
- `align-control-bar` is `position: absolute; right: -120px` — on mobile this would be off-screen or overlapping.
- `stack-grid` uses `repeat(auto-fill, minmax(160px, 1fr))` — fine for mobile since it collapses to 1 column.
- `project-tabs` padding `8px 18px` — on small screens tabs might overflow.

### 10. **Physics/Viewport gaps**
- `html, body { height: 100%; }` in `blog.css` with `!important` is fine for the blog's sticky-footer trick, but `blog-card-img { height: 120px }` is too tall on mobile (wastes vertical space).
- The filmstrip gallery's `film-row { height: 420px }` is fixed — will overflow on small screens.

### 11. **Touch targets**
- Nav links have `padding: 0 14px` — on mobile, touch targets should be at least 44px (Apple HIG) or 48px (Material Design). Current effective height is 36px (nav height).
- Filter buttons (`.blog-filter-btn`, `.research-filter-btn`) have `padding: 2px 8px` — too small to reliably tap.
- The theme toggle button has `padding: 2px 8px; font-size: 10px` — tiny touch target.

---

## Recommended Plan

### Phase 1: Touch Targets & Typography (Critical) ✅ DONE

| # | File | Change |
|---|------|--------|
| 1 | `styles.css` | Add `@media (max-width: 600px)` rule to increase nav link touch targets: `padding: 0 10px; min-height: 44px` or similar ✅ |
| 2 | `styles.css` | Add mobile rules for `.toggle-btn` to have `padding: 6px 12px; font-size: 12px` for better tappability ✅ |
| 3 | `styles.css` | Reduce `.hero-title` font size further at 400px: `font-size: 20px` ✅ |
| 4 | `blog.css` | Reduce `.blog-card-img` height to `80px` at 600px ✅ |
| 5 | `team.css` | Add responsive for `.member-card-grid` — `grid-template-columns: repeat(auto-fill, minmax(160px, 1fr))` at 768px to prevent card overflow ✅ |

### Phase 2: Grid & Layout Collapse ✅ DONE

| # | File | Change |
|---|------|--------|
| 6 | `team.css` | Add `@media (max-width: 768px)` for `.member-card-grid`: `grid-template-columns: repeat(auto-fill, minmax(160px, 1fr))` and reduce gap from 40px to 16px ✅ |
| 7 | `team.css` | Add `@media (max-width: 600px)` for `.member-row`: collapse from 4-column grid to stacked layout ✅ |
| 8 | `project.css` → `team.html` | Add responsive for `.film-row` height: reduce to `280px` at 600px ✅ |
| 9 | `project.css` → `team.html` | Add responsive for `.frame-inner` width/height: reduce to `200px x 220px` at 600px ✅ |
| 10 | `project.css` | Fix `.align-control-bar` positioning on mobile (move inside content area or hide) ✅ |

**Note:** Items 8 & 9 are implemented in `team.html` inline `<style>` tags rather than in `project.css` as the plan anticipated. This is because the filmstrip gallery (`.film-row`, `.frame-inner`) exists only on the team page, not on any research project pages — so placing them in `project.css` wouldn't make sense. The plan's file assignment was slightly off, but the implementation is correct and functional. Also added related mobile polish: `.filmstrip-meta-bar` stacks vertically at ≤600px, `.filmstrip-meta-title` shrinks to 13px, `.filmstrip-bar` and `.filmstrip-meta-bar` padding reduced.

### Phase 3: Spacing & Padding ✅ DONE

| # | File | Change |
|---|------|--------|
| 11 | `styles.css` | Adjust `.hero-main` padding on mobile: `16px 14px` instead of `24px 20px 20px` ✅ |
| 12 | `sponsors.css` | Add mobile font-size for `.sponsors-cta-title`: `28px` at 600px ✅ |
| 13 | `sponsors.css` | Reduce `.sponsors-about-photo` min-height at 600px: `160px` ✅ |
| 14 | `project.css` | Adjust `.project-section` padding at 600px from `16px 14px` to `12px 12px` for narrower screens ✅ |
| 15 | `project.css` | Adjust `.subpage-header` padding at 600px ✅ |

### Phase 4: Global Consistency ✅ DONE

| # | File | Change |
|---|------|--------|
| 16 | All CSS | Unify responsive breakpoints — some use 900/768/600, some 900/600. Consider adding a 400px breakpoint for very small phones ✅
| 17 | `styles.css` | Consider consolidating all responsive rules into `styles.css` rather than scattering across page-specific files ✅
| 18 | `styles.css` | Add a max-width constraint on the hero description (`max-width: 100%`) on mobile so text doesn't sit at full viewport width ✅ |

### Phase 5: Advanced (Nice-to-have)

| # | Change |
|---|--------|
| 19 | Add a hamburger menu for nav links on very small screens (< 480px) instead of horizontal scroll |
| 20 | Make the halftone canvas resolution-aware (it currently redraws on resize, which is good, but could be throttled) |
| 21 | Add `touch-action: manipulation` to interactive elements to prevent double-tap zoom delays |

---

### Critical Fixes (Quick Wins)

These are the most impactful changes that require minimal code changes:

1. **`.member-card-grid` overflow** on team page — this is *the* most broken thing on mobile
2. **Touch targets** — nav links, filter buttons, toggle button
3. **Filmstrip gallery overflow** — fixed heights and widths that don't scale
4. **Hero padding** — text too close to edges on small phones
5. **Sponsors CTA title** — 38px font on phone looks huge
