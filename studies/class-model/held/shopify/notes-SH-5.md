# SH-5: a role's permissions that the permission tree holds, placed by script

**What the batch is.** 110 entries of Shopify's `admin-role-permissions`: the permissions of the role the store `ctcbwa-r1` answered with (`data.organization.accessRole.permissions`), each a handle and its access level (ALLOW or DENY). An entry stands for one handle at one level. Its handle is a permission that the permission tree holds and that SH-3 or SH-4 placed.

**How it was placed.** The coordinator placed it by script (`method/held_role_permissions.py`), not by an agent. The rule is mechanical, and the tree's lines are already checked.
- **A role's permission takes its permission's line** (the rule after SH-4): the same capability, support, scope and filler as the tree's line for the same id. A permission the tree splits over two lines (S4, M-6) gives two.
- **Its terms are the handle,** the entry's own words. The tree's title and filler stay with the tree's line, which the reading cites by batch, line and entry.
- **The access level is the role's own setting,** in `reading`. A DENY denies one role a permission the platform has, so it changes no line.
- **A handle the tree holds twice with lines that differ,** or not at all, is left. It goes to SH-6 and SH-7.

**The cut.** The structure's 358 entries were cut again:
- SH-5 holds the 110 that take a tree line, in 127 lines;
- SH-6 and SH-7 hold the other 248, 124 each, in their order.

  Most of these are the POS role's permissions (cash tracking, offline payments, the cash drawer, saved carts), which the tree doesn't hold.

**What the checker prints.**
- **Cell changes:** CM-ONB-004, by the Home permission, as SH-3's line made it.
- **Notes:** the tree's lines' own.

The checker's last line, for SH-5: `110 of 110 entries placed; 0 problems` (after this file was written).

## The coordinator's check (31 October 2026, after the batch)

- Placed by the coordinator, as above. Its cost is the coordinator's few requests, against about 12 million for an agent's batch of these repeats.
