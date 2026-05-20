# Contact Button Fallback Feature

## Problem

When users click the **Contact** link (`mailto:neurotechatvt@proton.me`), the browser attempts to open the system's default email client. If the user:
- Has no email client configured, or
- Cancels the "Open Pick An App?" / "Choose an application" popup

...the action fails silently and the user is left without a way to contact the team.

## Goal

If the user cancels the email-client popup, display the email address directly on the page so they can copy it manually.
