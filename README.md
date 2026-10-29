# NCE Statement Builder

A website for preparing the financial statements of non-corporate entities (proprietorships, partnership firms, LLPs, HUFs, trusts and societies) in the format of the ICAI Guidance Note on Financial Statements of Non-Corporate Entities.

You enter figures only in the notes, schedules and party lists. The Balance Sheet and the Statement of Profit and Loss are built from them automatically.

## What it does

- **Notes 1 to 27**, numbered in the order the items appear on the Balance Sheet and the Statement of Profit and Loss.
- **Partners' capital account**: opening balance, additions, withdrawals, interest, remuneration and profit share by ratio, with a previous-year line.
- **Fixed assets** on the written down value method: rate-wise blocks, with half-rate depreciation on additions used for less than 180 days.
- **Long-term and short-term borrowings** listed lender by lender (secured and unsecured), each with terms of borrowing.
- **Debtors and creditors** listed party by party, with ageing and MSME status. You can paste a list straight from Excel or Tally.
- **Checks**: whether the Balance Sheet tallies, whether profit-sharing ratios add up to 100%, whether opening balances agree with last year, and whether stock agrees between notes.
- **Export**:
  - **Excel**: separate sheets for the Balance Sheet, P&L, Notes, Capital Account, Fixed Assets, Debtors and Creditors, laid out for A4 and printed at 100%.
  - **PDF**: the same layout. **Export PDF** opens the print dialog; choose *Save as PDF*.
- **Backup / Restore** as a file, and several entities in one browser.

## Your data

Figures are stored only in the browser you use (local storage). Nothing is sent to a server. Use **Backup** to keep a copy or to move to another device, and **Restore** to load it there.

## Use it on iPhone or Android

Open the website in Safari (iPhone) or Chrome (Android), then choose **Share → Add to Home Screen**. It opens full screen like an app and keeps working offline.

## Project layout

| File | Purpose |
|---|---|
| `src/app.html` | The application: markup, styles and script |
| `build.py` | Wraps `src/app.html` into `index.html` with the page metadata and offline support |
| `index.html` | The built page that GitHub Pages serves |
| `sw.js` | Service worker for offline use |
| `manifest.webmanifest`, `icon-*.png` | Home-screen app name and icons |

To change the app, edit `src/app.html`, run `python3 build.py`, and commit both files.

## Hosting on GitHub Pages

In the repository settings, open **Pages** and set *Source* to **Deploy from a branch**, branch `main`, folder `/ (root)`. The site is published at `https://<user>.github.io/<repository>/`.
