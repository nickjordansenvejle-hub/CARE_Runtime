# Upload-vejledning til Nick — CARE Runtime v23.16.1 UX Patch (GitHub web upload)

**Rolig og enkel. Ingen terminal. Ingen kommandoer. Du gør det hele i browseren.**

Tryghed før tempo. Du kan stoppe når som helst. HOLD is not failure.

> **Intet er pushet eller deployet.** Dette er kun en lokal upload-klar mappe. Du bestemmer selv hvornår (og om) noget går online. Only Nick can approve.

---

## Hvad du har her
En upload-klar mappe (samme mønster som v23.15):

```
GITHUB_UPLOAD_READY_CARE_v23_16_1/
└── CARE_RUNTIME_MASTER_v23_16_1_ALL_IN_COMPLETE/
    └── STREAMLIT_READY_APP/
        ├── app.py            (v23.16.1 UX Patch — verificeret)
        ├── requirements.txt  (streamlit + reportlab — uændret)
        ├── README.md
        └── .streamlit/
            └── config.toml   (dark theme + headless — overført fra v23.15)
```

`app.py` SHA256: `acd09e940cadc933653d75849154486bcd47b908323298eb727318597f1f3199`
Du skal ikke ændre noget i filerne.

---

## VIGTIGT — hvorfor dette IKKE ændrer den offentlige app automatisk
Vi bruger **samme sikre mønster som v23.15: én ny mappe pr. version + manuel skift af "Main file path".**

- Når du uploader v23.16.1-mappen til GitHub, ligger den bare som en **ny mappe** ved siden af de gamle.
- Streamlit viser stadig den mappe, som appens **Main file path** peger på (lige nu v23.15/v23.0).
- **Den offentlige app skifter FØRST**, når DU manuelt ændrer Main file path i Streamlit-indstillingerne (DEL 2).
- Så: upload alene = ingen offentlig ændring. Du har den fulde kontrol.

**Bekræft før upload:**
1. ✅ Repo bekræftet (skærmbillede 17-06): `nickjordansenvejle-hub/CARE_Runtime` (underscore) · Public · branch `main` · hver version er sin egen top-mappe (v18/v20/v22/v23.0/v23.15 ligger der allerede).
2. Den live Streamlit-URL nævnes både som `careruntime.streamlit.app` og `care-runtime.streamlit.app`. Linket inde i app'en peger på `careruntime.streamlit.app` — ret det bagefter hvis den live slug er en anden.

---

## DEL 1 — Læg filerne op på GitHub (ændrer IKKE den offentlige app)

1. Gå til dit repo (bekræftet): **https://github.com/nickjordansenvejle-hub/CARE_Runtime**
2. Tjek at du står på branch **main** (øverst til venstre over fillisten).
3. Tryk **"Add file"** → **"Upload files"**.
4. Åbn et filvindue og find mappen:
   `C:\Users\carer\Desktop\CARE\GITHUB_UPLOAD_READY_CARE_v23_16_1\`
5. **Træk hele mappen** `CARE_RUNTIME_MASTER_v23_16_1_ALL_IN_COMPLETE`
   ind i feltet "Drag files here". GitHub beholder mappe-strukturen (`STREAMLIT_READY_APP` og `.streamlit` følger med).
   - Upload IKKE `UPLOAD_INSTRUCTIONS_FOR_NICK.md` — den er kun til dig.
6. Commit message: `Add CARE Runtime v23.16.1 UX Patch folder (not live yet)`
7. Tryk **"Commit changes"**.

✅ Nu ligger v23.16.1 i en NY mappe. v23.15 og v23.0 er ikke rørt. **Den offentlige app er uændret.**

---

## DEL 2 — (KUN når du selv vil gå live) Peg Streamlit på den nye mappe

> Gør først dette når du har besluttet at v23.16.1 skal være offentlig. Dette er det skridt der ændrer careruntime.streamlit.app.

8. Gå til **https://share.streamlit.io**
9. Åbn din nuværende CARE-app.
10. Åbn appens **Settings** (tre prikker → Settings / "Edit").
11. Skift **Main file path** til præcis:
    ```
    CARE_RUNTIME_MASTER_v23_16_1_ALL_IN_COMPLETE/STREAMLIT_READY_APP/app.py
    ```
    (Repo og branch `main` forbliver de samme.)
12. Tryk **Save** og derefter **Reboot** / **Deploy**.
13. Vent til appen er bygget, og åbn det offentlige link for at teste.

---

## TJEK efter (kun hvis du har gjort DEL 2)
- [ ] Forsiden / Simple Review Mode loader.
- [ ] Titlen/versionen viser **v23.16.1**.
- [ ] 5-trins flow (Step 1–5) synligt; "Review completeness" vises.
- [ ] Resultat kun **PASS — review can continue** / **HOLD — missing, invalid, or unverified evidence**.
- [ ] Boundary chips: PASS is not permission · Visibility is not authority · Observer-only / not authority · UNKNOWN -> HOLD.
- [ ] Ingen "Allow" i UI. Ingen private data synlig.

## ROLLBACK (helt sikkert)
Skift bare **Main file path** tilbage til den gamle og tryk Save + Reboot:
```
CARE_RUNTIME_MASTER_v23_15_ALL_IN_COMPLETE/STREAMLIT_READY_APP/app.py
```
Så er du tilbage på v23.15 med det samme. Intet er tabt.

---

## VIGTIGT
- v23.15- og v23.0-mapperne må IKKE røres, slettes eller ændres.
- Du uploader kun den nye v23.16.1-mappe.
- Det er DIG der trykker upload, commit og (evt.) deploy — i din egen browser, med dit eget login.

*Mennesket først. Kontinuitet altid. Tryghed før tempo.*

No approval created. No CARE-core change. No vNEXT859 created. No GitHub push performed. No Streamlit deploy performed. No token used. No credential stored. v23.15 preserved. Only Nick can approve. UNKNOWN -> HOLD.
