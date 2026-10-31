# SH-91: the admin's plan page, its frame, placed by script

**What the batch is.** The last 75 entries of Shopify's `plan-page-admin`: ibx5bt-xy's plan page as it rendered in a settings dialog, its items read from `<body>`, so they hold the admin's own frame beside the page's last plan items.

**The rule** (SH-89's R89.9, kept by its check; `method/held_plan_frame.py`):
- **`out`, the admin's frame:** the main navigation (items lines 8 to 23), a repeat of what `admin-main-nav` holds and places for ibx5bt-xy; the keyboard shortcuts (lines 27 to 87) and their group headings, each shortcut naming another place as a key's target; and the UI strings (the drag hint, the dialog's Close).
- **The trial banner** ('Trial ends in 2 days', 'Subscribe for $1', Select a plan) takes SH-3's line 9: CM-PLN-001 `core`, the store's days left its own.
- **'Plus+'** is the Plus card's title, with an aria-hidden '+': SH-89's line 69.
Any other entry would have stopped the script, for an agent; none did.

## The coordinator's check (31 October 2026, the script's batch)

- **The checker passes** on all 75 entries: 71 `out`, 4 on CM-PLN-001.
- **R89.9's veto, not used:** the other reading would give each navigation item and shortcut that names a section that section's line, about 65 lines repeating `admin-main-nav`'s, and change no cell. A page's own frame is `out`, as the built-in feature pages' and the mobile app's frames are.
- **Cost:** the script, no agent.
