# MedInfo Assist

A working prototype for Scenario 3 (Pharma | Medical information), built for the Ankura AI by Design graduate exercise. All companies, products, documents and enquiries are fictional or synthetic.

## Open and test
- **Simplest:** open `index.html` in any modern browser. Everything runs locally: no install, no back end, and nothing is stored (it resets on reload).
- **Guided walkthrough:** see the *How it works* tab in the app.
- **Automated tests:** `node tests/run-tests.js` runs the 22-case synthetic test set against the core logic. The same results appear in the app's *Test results* tab.

## Structure
- `src/core.js` – redaction, triage rules, BM25 retrieval over approved sources, extractive drafting, grounding check, test set
- `src/ui.js`, `src/template.html` – interface
- `build.py` – combines the sources into the single-file `index.html`

## Optional LLM mode
The draft panel can call an Anthropic model with your own API key. Only the redacted enquiry and the retrieved approved passages are sent, and the output must pass the same grounding check. This works when `index.html` is opened locally or served from GitHub Pages.
