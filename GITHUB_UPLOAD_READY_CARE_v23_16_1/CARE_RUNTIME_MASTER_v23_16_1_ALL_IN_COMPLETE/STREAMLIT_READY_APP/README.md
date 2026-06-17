# CARE Runtime v23.16.1 — UX Patch Candidate / Simple Review Mode

**Status:** LOCAL CANDIDATE ONLY · INBOX / REVIEW / UNKNOWN -> HOLD
**Date:** 2026-06-17
**Built from:** v23.16 UX Candidate (v23.16 kept byte-untouched as rollback)

This is a **UX-only patch** on top of v23.16. It is a separate, self-contained Streamlit app. It does NOT touch CARE-core, the authority rules, or the existing v23.15 / v23.0 runtimes — those are preserved untouched as reference and rollback. It does NOT change the meaning of PASS / HOLD, and there is no FAIL state.

## What changed in v23.16.1 (UX patches)
1. **Simpler first 2 minutes** — plain-language start explainer: *CARE asks whether review can continue or must HOLD. CARE does not approve / does not give permission / does not replace human judgment.*
2. **Clear first action** — explicit 5-step flow (Step 1 describe → Step 2 documentation → Step 3 review completeness → Step 4 PASS/HOLD explanation → Step 5 feedback), shown up top and used as the section headers.
3. **More human checklist** — short, test-person-friendly labels (Evidence is present / current; Authority source identified / still valid; Current state verified; Source/custody checked; Unknown items are marked HOLD). Anything missing/unknown → HOLD.
4. **Result card** — only `PASS — review can continue` or `HOLD — missing, invalid, or unverified evidence`, with a "What do PASS and HOLD mean?" explainer (PASS may continue · PASS is not permission · PASS does not approve action · HOLD = stop until resolved). The word "Allow" is never used.
5. **Progress = "Review completeness"** (not approval/certification/compliance), with explanation: *shows how much review input is present; it does not show approval.*
6. **Mobile UX** — mobile tips (use simple mode first; advanced docs read better on desktop; rotate/scroll wide tables) + nav: Start simple review · Open full audit runtime · Open advanced documentation · Back to top.
7. **Tables** — card-style summary (3 metrics) instead of a wide table in simple mode; full per-item status is behind a `Show full table` expander with a rotate/scroll mobile note.
8. **Download clutter** — kept in an `Advanced downloads / archive` expander with note: *Most test users do not need these files for first review.* Nothing removed; all audit material preserved.
9. **Feedback pointer** — closing feedback section: *Feedback is not approval. Feedback helps improve clarity, usability, and review flow.* Asks what was clear / confusing / simpler, and phone-vs-desktop. Demo feedback stays local.
10. **Privacy / data note** — *Do not enter private, medical, or sensitive personal data unless this is a controlled test context.* + *Nothing in this demo should be treated as official approval or decision-making.*
11. **Boundary chips** — always visible: PASS is not permission · Visibility is not authority · Observer-only / not authority · UNKNOWN -> HOLD.

## What it is NOT
Not CARE-core · not vNEXT859 · not approval / certification / compliance / medical / clinical · not deployed · not moved to 03_APPROVED. No domain/email created.

## Run locally
```
cd STREAMLIT_READY_APP
py -m pip install -r requirements.txt
py -m streamlit run app.py --server.address 0.0.0.0 --server.port 8510
```
(Use port 8510 so it does not clash with v23.16 on 8509 or v23.15 on 8508.)

## Boundaries
PASS is not permission. Visibility is not authority. Observer-only / not authority. UNKNOWN -> HOLD. Only Nick can approve.

vNEXT858 remains baseline. vNEXT859 remains HOLD.

*Tryghed før tempo. Mennesket først. Kontinuitet altid.*
