# Run 20261010T051708Z-community-clients

Thirteen public GitHub repositories cited in the Yemen notes, copied at their latest commit on 10 October 2026. Ten are community-written clients for Yemeni wallet and bank payment APIs: Kuraimi E-Pay, Al-Qutaibi Bank, Aden Bank, Cash Pay, Floosak, Jawali and SabaCash. They are the main public record of how those APIs behave. The other three are a Yemen payments project, a financial tracker and a list of Yemeni open-source projects.

- **Fetched from:** a Claude Code cloud container outside Yemen, by anonymous shallow `git clone` (read-only).
- **Not copied:** each repository's `.git` folder, plus `node_modules` and `vendor` if present.
- **Credentials:** a pattern search for credentials found only placeholders, in example code.

`clients.tsv` lists, for each repository:

- its address and branch;
- the commit copied, and that commit's date;
- the folder it was copied to, with file count and size;
- the cited addresses that point into it;
- where each is cited.

Every commit is dated December 2023 or later, so none falls under the pre-2023 historical rule. A client shows how its author called the API at that commit. It is not the provider's own documentation.
