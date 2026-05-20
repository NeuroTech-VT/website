# Contact Button Fallback Feature

## Problem

When users click the **Contact** link (`mailto:neurotechatvt@proton.me`), the browser attempts to open the system's default email client. If the user:
- Has no email client configured, or
- Cancels the "Open Pick An App?" / "Choose an application" popup

...the action fails silently and the user is left without a way to contact the team.

## Goal

If the user cancels the email-client popup, display the email address directly on the page so they can copy it manually.

## Proposed Solution

Replace the `<a href="mailto:...">` link with a **button** that:
1. Attempts to open the email client via `mailto:` link
2. Also opens a small **modal/popup** that displays the email address with a "Copy" button

This ensures that:
- Users with a working email client can still use the mailto flow
- Users without an email client (or who cancel) can still see/copy the email

## Implementation Plan

### 1. Modify HTML
Replace:
```html
<a href="mailto:neurotechatvt@proton.me">Contact</a>
```
with:
```html
<button class="contact-btn" id="contactBtn">Contact</button>
```

### 2. Add Modal HTML
Add a modal to `index.html` (or in a shared component if using one):
```html
<div id="contactModal" class="modal hidden">
  <div class="modal-content">
    <span class="close-btn">&times;</span>
    <h3>Contact Us</h3>
    <p>Email: <a href="mailto:neurotechatvt@proton.me">neurotechatvt@proton.me</a></p>
    <button id="copyEmailBtn" class="btn-small">Copy Email</button>
  </div>
</div>
```

### 3. Add CSS
Style the modal (centered overlay, hidden by default). Use existing site colors.

### 4. Add JavaScript
In `script.js`, add:
```javascript
const contactBtn = document.getElementById('contactBtn');
const modal = document.getElementById('contactModal');
const closeBtn = document.querySelector('.close-btn');
const copyBtn = document.getElementById('copyEmailBtn');

// Open modal on click
contactBtn.addEventListener('click', () => {
  modal.classList.remove('hidden');
});

// Close modal
closeBtn.addEventListener('click', () => {
  modal.classList.add('hidden');
});

// Close on outside click
window.addEventListener('click', (e) => {
  if (e.target === modal) {
    modal.classList.add('hidden');
  }
});

// Copy email to clipboard
copyBtn.addEventListener('click', () => {
  navigator.clipboard.writeText('neurotechatvt@proton.me')
    .then(() => alert('Email copied!'))
    .catch(() => alert('Failed to copy. Please copy manually.'));
});
```

### 5. Apply to All Pages
Update the Contact link/button on all pages:
- `index.html`
- `blog.html`
- `research.html`
- `team.html`
- `sponsors.html`
- `research/*.html` (drone-swarm, eeg-wheelchair, etc.)

Add the modal HTML to each page, or (better) use a shared JavaScript function to inject the modal dynamically if the site uses a modular structure.

### 6. Testing
- Click Contact → verify modal appears
- Click "Copy Email" → verify clipboard works
- Click close (×) / outside → verify modal closes
- Verify mailto still works for users with email clients

## Files to Modify

- `index.html`, `blog.html`, `research.html`, `team.html`, `sponsors.html`
- `research/drone-swarm.html`, `research/eeg-wheelchair.html`, `research/eeg-wheelchair-hardware.html`, `research/eeg-wheelchair-software.html`
- `script.js` (add modal logic)
- `styles.css` or `index.css` (add modal styles)

## Estimated Effort

- HTML changes: ~10–15 min
- CSS: ~10 min
- JavaScript: ~15 min
- Testing: ~10 min

**Total: ~45 min**