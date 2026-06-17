"""
CARE Runtime v23.16.1 — UX Patch Candidate / Simple Review Mode
==============================================================
LOCAL CANDIDATE ONLY. INBOX / REVIEW / UNKNOWN -> HOLD.

UX patch on top of v23.16 (v23.16 is kept byte-untouched as rollback).
This is a UX frontdoor for testpersoner / sagsbehandlere / first-time visitors.

It does NOT change CARE-core. It does NOT change authority rules.
It does NOT change the meaning of PASS / HOLD. There is no FAIL state here.
It is observer-only and produces only a review-completeness signal (PASS / HOLD).

Locked CARE core (display only — never altered here):
  No proof -> no bind -> no effect-capable path -> no effect.
  UNKNOWN -> HOLD.
  No bind -> no human consequence.
  PASS is not permission.
  HOLD is not failure.
  Visibility is not authority.
  Review is not authority.
  Claude is not authority.

vNEXT858 remains baseline. vNEXT859 remains NOT CREATED / HOLD.
No approval / certification / compliance / medical / clinical claim is made anywhere.
The word "Allow" is intentionally NOT used anywhere in this UI.
"""

import streamlit as st

# ----------------------------------------------------------------------------
# Constants (display-only; this app never grants authority)
# ----------------------------------------------------------------------------
APP_VERSION = "CARE Runtime v23.16.1 · UX Patch Candidate · Simple Review Mode"
STAGE = "Public demo / observer-only prototype · candidate (local)"
FULL_RUNTIME_URL = "https://careruntime.streamlit.app"  # Full Audit Runtime (v23.15 public)

CORE_LINES = [
    "No proof -> no bind -> no effect-capable path -> no effect.",
    "UNKNOWN -> HOLD.",
    "No bind -> no human consequence.",
    "PASS is not permission.",
    "HOLD is not failure.",
    "Visibility is not authority.",
    "Review is not authority.",
    "Claude is not authority.",
]

# Boundary chips — always shown clearly near the top (canonical English terms).
BOUNDARY_CHIPS = [
    "PASS is not permission",
    "Visibility is not authority",
    "Observer-only / not authority",
    "UNKNOWN -> HOLD",
]

# Bilingual copy (kept light; Danish + English)
T = {
    "EN": {
        "lang_label": "Language / Sprog",
        "tagline": "See AI consequence before it reaches a human.",
        "intro_lines": [
            "CARE asks whether review can continue or must HOLD.",
            "CARE does not approve.",
            "CARE does not give permission.",
            "CARE does not replace human judgment.",
        ],
        "ask": "CARE asks: Is there enough verified grounding for review to continue? "
               "If not: HOLD.",
        "how_title": "How it works (5 steps)",
        "steps": [
            "Step 1 — Describe what is being reviewed",
            "Step 2 — Check documentation status",
            "Step 3 — Review completeness",
            "Step 4 — PASS/HOLD explanation",
            "Step 5 — Give feedback",
        ],
        "start_simple": "Start simple review",
        "go_full": "Open full audit runtime",
        "open_adv": "Open advanced documentation",
        "back_top": "Back to top",
        "case_header": "Step 1 — Describe what is being reviewed",
        "case_name": "Case name / short description",
        "case_what": "What is being reviewed?",
        "case_notes": "Notes / context",
        "privacy": "⚠️ Do not enter private, medical, or sensitive personal data "
                   "unless this is a controlled test context.",
        "privacy_extra": "Nothing in this demo should be treated as official approval "
                         "or decision-making.",
        "check_header": "Step 2 — Check documentation status",
        "check_help": "If anything is missing or unknown, the result is HOLD.",
        "progress_header": "Step 3 — Review completeness",
        "progress_label": "Review completeness",
        "progress_expl": "Review completeness shows how much of the review input is "
                         "present. It does not show approval.",
        "summary_title": "Review summary",
        "metric_completeness": "Review completeness",
        "metric_checked": "Items checked",
        "metric_signal": "Current signal",
        "show_full_table": "Show full table",
        "table_summary": "Card summary above. Full per-item status is in the table below.",
        "col_item": "Item",
        "col_status": "Status",
        "status_checked": "Checked",
        "status_hold": "HOLD",
        "table_mobile_note": "Rotate screen or scroll horizontally to view all columns.",
        "result_header": "Step 4 — PASS/HOLD explanation",
        "pass_label": "PASS — review can continue",
        "hold_label": "HOLD — missing, invalid, or unverified evidence",
        "result_expl": [
            "PASS means review may continue.",
            "PASS is not permission.",
            "PASS does not approve action.",
            "HOLD means review should stop until missing or invalid conditions are resolved.",
        ],
        "meaning_title": "What do PASS and HOLD mean?",
        "hold_details_title": "HOLD details",
        "adv_header": "Full Audit Runtime / Advanced",
        "adv_note": "The full runtime, all documentation, downloads and audit material "
                    "are preserved. Nothing was removed — only made less noisy here.",
        "downloads_header": "Advanced downloads / archive",
        "downloads_note": "Most test users do not need these files for first review.",
        "mobile_header": "Mobile tips",
        "mobile_lines": [
            "On mobile, use the simple mode first.",
            "Advanced documentation may be easier to read on desktop.",
            "For wide tables, rotate screen or scroll horizontally.",
        ],
        "feedback_header": "Step 5 — Give feedback",
        "feedback_note": "Feedback is not approval. Feedback helps improve clarity, "
                         "usability, and review flow.",
        "fb_clear": "What was clear?",
        "fb_confusing": "What was confusing?",
        "fb_simpler": "What should be simpler?",
        "fb_device": "Were you using phone or desktop?",
        "device_options": ["Phone", "Desktop"],
        "feedback_local_note": "This demo feedback stays local. Nothing is sent or "
                               "stored as a decision.",
        "no_decide": "CARE does not decide outcomes. CARE does not approve people, "
                     "institutions, documents, systems, or actions. CARE only preserves "
                     "a boundary: No proof -> no bind -> no effect.",
        "core_title": "CARE core (locked — display only)",
        "footer": "Observer-only / not authority · Review is not approval · "
                  "Only Nick can approve · UNKNOWN -> HOLD",
    },
    "DA": {
        "lang_label": "Language / Sprog",
        "tagline": "Se AI-konsekvens, før den når et menneske.",
        "intro_lines": [
            "CARE spørger, om en gennemgang kan fortsætte eller skal HOLDE.",
            "CARE godkender ikke.",
            "CARE giver ikke tilladelse.",
            "CARE erstatter ikke menneskelig dømmekraft.",
        ],
        "ask": "CARE spørger: Er der nok verificeret grundlag til, at gennemgangen kan "
               "fortsætte? Hvis ikke: HOLD.",
        "how_title": "Sådan virker det (5 trin)",
        "steps": [
            "Trin 1 — Beskriv hvad der gennemgås",
            "Trin 2 — Tjek dokumentationsstatus",
            "Trin 3 — Gennemgangs-fuldstændighed",
            "Trin 4 — PASS/HOLD-forklaring",
            "Trin 5 — Giv feedback",
        ],
        "start_simple": "Start simpel gennemgang",
        "go_full": "Åbn fuld audit-runtime",
        "open_adv": "Åbn avanceret dokumentation",
        "back_top": "Til toppen",
        "case_header": "Trin 1 — Beskriv hvad der gennemgås",
        "case_name": "Sagsnavn / kort beskrivelse",
        "case_what": "Hvad gennemgås?",
        "case_notes": "Noter / kontekst",
        "privacy": "⚠️ Indtast ikke private, medicinske eller følsomme personoplysninger, "
                   "medmindre dette er en kontrolleret testkontekst.",
        "privacy_extra": "Intet i denne demo må behandles som officiel godkendelse eller "
                         "beslutningstagning.",
        "check_header": "Trin 2 — Tjek dokumentationsstatus",
        "check_help": "Hvis noget mangler eller er ukendt, er resultatet HOLD.",
        "progress_header": "Trin 3 — Gennemgangs-fuldstændighed",
        "progress_label": "Gennemgangs-fuldstændighed",
        "progress_expl": "Gennemgangs-fuldstændighed viser, hvor meget af gennemgangs-"
                         "input der er til stede. Den viser ikke godkendelse.",
        "summary_title": "Gennemgangs-oversigt",
        "metric_completeness": "Gennemgangs-fuldstændighed",
        "metric_checked": "Punkter afkrydset",
        "metric_signal": "Aktuelt signal",
        "show_full_table": "Vis fuld tabel",
        "table_summary": "Kort-oversigt ovenfor. Fuld status pr. punkt er i tabellen herunder.",
        "col_item": "Punkt",
        "col_status": "Status",
        "status_checked": "Afkrydset",
        "status_hold": "HOLD",
        "table_mobile_note": "Drej skærmen eller scroll vandret for at se alle kolonner.",
        "result_header": "Trin 4 — PASS/HOLD-forklaring",
        "pass_label": "PASS — gennemgang kan fortsætte",
        "hold_label": "HOLD — manglende, ugyldigt eller uverificeret grundlag",
        "result_expl": [
            "PASS betyder, at gennemgangen må fortsætte.",
            "PASS er ikke tilladelse.",
            "PASS godkender ikke handling.",
            "HOLD betyder, at gennemgangen bør stoppe, indtil manglende eller ugyldige "
            "forhold er løst.",
        ],
        "meaning_title": "Hvad betyder PASS og HOLD?",
        "hold_details_title": "HOLD-detaljer",
        "adv_header": "Fuld Audit-Runtime / Avanceret",
        "adv_note": "Den fulde runtime, al dokumentation, downloads og auditmateriale er "
                    "bevaret. Intet er fjernet — kun gjort mindre forstyrrende her.",
        "downloads_header": "Avancerede downloads / arkiv",
        "downloads_note": "De fleste testpersoner har ikke brug for disse filer til en "
                          "første gennemgang.",
        "mobile_header": "Mobil-tips",
        "mobile_lines": [
            "På mobil: brug den simple tilstand først.",
            "Avanceret dokumentation er ofte nemmere at læse på en computer.",
            "For brede tabeller: drej skærmen eller scroll vandret.",
        ],
        "feedback_header": "Trin 5 — Giv feedback",
        "feedback_note": "Feedback er ikke godkendelse. Feedback hjælper med at forbedre "
                         "klarhed, brugervenlighed og gennemgangs-flow.",
        "fb_clear": "Hvad var tydeligt?",
        "fb_confusing": "Hvad var forvirrende?",
        "fb_simpler": "Hvad bør være enklere?",
        "fb_device": "Brugte du telefon eller computer?",
        "device_options": ["Telefon", "Computer"],
        "feedback_local_note": "Denne demo-feedback forbliver lokal. Intet sendes eller "
                               "gemmes som en beslutning.",
        "no_decide": "CARE afgør ikke udfald. CARE godkender ikke mennesker, "
                     "institutioner, dokumenter, systemer eller handlinger. CARE bevarer "
                     "kun en grænse: No proof -> no bind -> no effect.",
        "core_title": "CARE core (låst — kun visning)",
        "footer": "Observer-only / not authority · Review is not approval · "
                  "Only Nick can approve · UNKNOWN -> HOLD",
    },
}

CHECKLIST_ITEMS = {
    "EN": [
        "Evidence is present",
        "Evidence is current",
        "Authority source is identified",
        "Authority is still valid",
        "Current state is verified",
        "Source/custody is checked",
        "Unknown items are marked HOLD",
    ],
    "DA": [
        "Grundlag er til stede",
        "Grundlag er aktuelt",
        "Autoritetskilde er identificeret",
        "Autoritet er stadig gyldig",
        "Nuværende tilstand er verificeret",
        "Kilde/custody er tjekket",
        "Ukendte punkter er markeret HOLD",
    ],
}


def boundary_chips():
    """Always-visible boundary chips (canonical English boundary terms)."""
    chips = "".join(f'<span class="care-chip">{c}</span>' for c in BOUNDARY_CHIPS)
    st.markdown(f'<div class="care-chips">{chips}</div>', unsafe_allow_html=True)


def main():
    st.set_page_config(
        page_title="CARE v23.16.1 · Simple Review Mode",
        page_icon="🟢",
        layout="centered",
    )

    # Light, calm styling; mobile-first (centered layout, large tap targets)
    st.markdown(
        """
        <style>
        .stButton button, .stLinkButton a {min-height: 48px; width: 100%;}
        .care-pass {background:#064e3b;color:#d1fae5;padding:16px;border-radius:14px;
                    border:1px solid #34d399;font-weight:700;font-size:1.05rem;}
        .care-hold {background:#3b0a0a;color:#fee2e2;padding:16px;border-radius:14px;
                    border:1px solid #f87171;font-weight:700;font-size:1.05rem;}
        .care-chips {display:flex;flex-wrap:wrap;gap:6px;margin:6px 0 2px 0;}
        .care-chip {background:#1e293b;color:#e2e8f0;border:1px solid #475569;
                    border-radius:999px;padding:4px 10px;font-size:0.78rem;font-weight:600;}
        .care-intro {background:#0f172a;color:#e2e8f0;border:1px solid #334155;
                     border-radius:14px;padding:14px 16px;line-height:1.55;}
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Top anchor
    st.markdown('<a name="top"></a>', unsafe_allow_html=True)

    # Language toggle (single widget — drives all copy)
    lang = st.radio(T["EN"]["lang_label"], ["EN", "DA"], horizontal=True, index=0,
                    key="lang_select")
    t = T[lang]

    # ---- Header + identity + boundaries (always visible) ----
    st.title("CARE")
    st.caption(f"{APP_VERSION} · {STAGE}")
    st.caption("vNEXT858 baseline · vNEXT859 NOT CREATED / HOLD")
    boundary_chips()

    # ---- Plain-language start explainer (first 2 minutes) ----
    st.subheader(t["tagline"])
    st.markdown(
        '<div class="care-intro">'
        + "<br>".join(t["intro_lines"])
        + "</div>",
        unsafe_allow_html=True,
    )
    st.write(t["ask"])

    # ---- How it works (5 steps) ----
    with st.expander(t["how_title"], expanded=True):
        for s in t["steps"]:
            st.markdown(f"- {s}")

    # ---- Navigation buttons / links (mobile-friendly) ----
    n1, n2 = st.columns(2)
    with n1:
        st.link_button(t["go_full"], FULL_RUNTIME_URL)
    with n2:
        st.link_button(t["open_adv"], FULL_RUNTIME_URL)
    st.markdown(f"[{t['start_simple']}](#step1) · [{t['back_top']}](#top)")

    st.divider()

    # ===== Step 1 — Describe what is being reviewed =====
    st.markdown('<a name="step1"></a>', unsafe_allow_html=True)
    st.header(t["case_header"])
    st.warning(t["privacy"])
    st.caption(t["privacy_extra"])
    st.text_input(t["case_name"], key="case_name")
    st.text_area(t["case_what"], key="case_what", height=80)
    st.text_area(t["case_notes"], key="case_notes", height=80)

    st.divider()

    # ===== Step 2 — Check documentation status =====
    st.header(t["check_header"])
    st.caption(t["check_help"])
    items = CHECKLIST_ITEMS[lang]
    checked = []
    for i, item in enumerate(items):
        checked.append(st.checkbox(item, key=f"chk_{i}"))

    total = len(items)
    done = sum(1 for c in checked if c)
    completeness = int(round(100 * done / total)) if total else 0
    all_checked = done == total and total > 0

    st.divider()

    # ===== Step 3 — Review completeness (NOT approval) =====
    st.header(t["progress_header"])
    st.progress(completeness / 100.0, text=f"{t['progress_label']}: {completeness}%")
    st.caption(t["progress_expl"])

    # Card-style summary instead of a wide table in simple mode
    st.markdown(f"#### {t['summary_title']}")
    m1, m2, m3 = st.columns(3)
    m1.metric(t["metric_completeness"], f"{completeness}%")
    m2.metric(t["metric_checked"], f"{done}/{total}")
    m3.metric(t["metric_signal"], "PASS" if all_checked else "HOLD")

    # Full per-item table tucked behind an expander (+ mobile note)
    with st.expander(t["show_full_table"]):
        st.caption(t["table_summary"])
        statuses = [t["status_checked"] if c else t["status_hold"] for c in checked]
        st.table({t["col_item"]: items, t["col_status"]: statuses})
        st.caption(t["table_mobile_note"])

    st.divider()

    # ===== Step 4 — PASS / HOLD explanation =====
    st.header(t["result_header"])
    if all_checked:
        st.markdown(f'<div class="care-pass">🟢 {t["pass_label"]}</div>',
                    unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="care-hold">🔴 {t["hold_label"]}</div>',
                    unsafe_allow_html=True)
        missing = [items[i] for i, c in enumerate(checked) if not c]
        if missing:
            with st.expander(t["hold_details_title"]):
                for m in missing:
                    st.write(f"- {m} → UNKNOWN -> HOLD")

    # Full meaning explanation (always available)
    with st.expander(t["meaning_title"]):
        for line in t["result_expl"]:
            st.markdown(f"- {line}")

    st.divider()

    # ===== Advanced / Full Audit Runtime + download archive =====
    with st.expander(t["adv_header"]):
        st.write(t["adv_note"])
        st.link_button(t["go_full"], FULL_RUNTIME_URL)
        st.markdown(f"#### {t['downloads_header']}")
        st.caption(t["downloads_note"])
        st.caption("PDF / JSON / audit exports → " + FULL_RUNTIME_URL)

    # ===== Mobile tips =====
    with st.expander(t["mobile_header"], expanded=False):
        for line in t["mobile_lines"]:
            st.markdown(f"- {line}")

    st.divider()

    # ===== Step 5 — Give feedback =====
    st.header(t["feedback_header"])
    st.info(t["feedback_note"])
    st.radio(t["fb_device"], t["device_options"], horizontal=True, key="fb_device")
    st.text_area(t["fb_clear"], key="fb_clear", height=70)
    st.text_area(t["fb_confusing"], key="fb_confusing", height=70)
    st.text_area(t["fb_simpler"], key="fb_simpler", height=70)
    st.caption(t["feedback_local_note"])

    st.divider()

    # ===== Core (display only) + closing boundaries =====
    st.write(t["no_decide"])
    with st.expander(t["core_title"]):
        st.code("\n".join(CORE_LINES))

    st.caption(t["footer"])
    st.markdown(f"[{t['back_top']}](#top)")


if __name__ == "__main__":
    main()
