# ✨ Pranjal Paramita Sahu — Interactive Portfolio

A cinematic, Netflix-inspired single-page portfolio built for **Streamlit Community Cloud**. It is a self-contained HTML/CSS/JS experience with your portrait, résumé, projects, experience and all 10 certificates embedded as data URIs — so it works offline, needs no database, no API keys, and no CDN.

## What's inside

- Animated hero with portrait, live status card and floating badges
- Interactive skill tabs (Languages & Data, AI/ML, BI & Tools, Human Skills)
- Dedicated **Training Program on Machine Learning & Its Concepts** showcase with 4 workshop photos and a full-screen lightbox viewer
- Four project cards with clickable "Project notes" (no arrow clutter)
- Experience + education timeline
- Certificate wall: clicking any certificate opens its PDF; "Quick preview" opens a large on-page preview; "PDF ↓" downloads the original
- Clickable conversation-starter chips and floating hero badges that jump to the right skill/project
- Interview cheat sheet with myth-vs-reality accordion
- Playful extras: brag meter, fun facts, hire-o-meter, confetti, easter egg
- Day/night theme toggle and responsive layouts
- Every résumé button downloads the résumé; email/LinkedIn/GitHub/phone links open directly

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

If the local URL doesn't open automatically, visit `http://localhost:8501`.

## Deploy to Streamlit Community Cloud

1. Create a GitHub repository and push this folder to it.
2. Go to <https://share.streamlit.io/> and sign in with GitHub.
3. Choose **New app** → select your repo and branch.
4. Set **Main file path** to `app.py`.
5. Click **Deploy**. No secrets or environment variables are needed.

> Requires `streamlit>=1.67` (pinned in `requirements.txt`) for `st.iframe(..., height="content")`, which lets the page grow naturally instead of showing a nested scrollbar.

## Also works as a plain HTML file

Run this from the repo root to generate `portfolio.html`:

```bash
python portfolio_builder.py
```

Open `portfolio.html` in any browser. Everything — including images and PDFs — is embedded in the file.

## Project structure

```
app.py                  Streamlit entry point
portfolio_builder.py    Turns template + assets into one self-contained HTML string
requirements.txt        Only dependency: Streamlit
.streamlit/config.toml  Theme / app configuration
assets/
  template.html         The entire website markup, CSS and JS
  photo.jpg             Optimized portrait
  resume.pdf            Downloadable résumé
  certs/                Certificate thumbnails + original PDFs
portfolio.html          Generated standalone version (optional)
```

## Editing content

- **Projects, skills, about text, jokes:** edit `assets/template.html`.
- **Certificates:** add a `key` to `CERT_KEYS` in `portfolio_builder.py`, place `<key>.jpg` and `<key>.pdf` in `assets/certs/`, add its `__CERT_<KEY>_IMG` / `__CERT_<KEY>_PDF` data to the `certs` array inside `template.html`, and add the matching filter category if needed.
- **Portrait / résumé:** replace `assets/photo.jpg` / `assets/resume.pdf`.

The site intentionally uses system fonts, inline SVG and embedded assets — no external requests, so it renders identically in the Streamlit preview and in production.

---

Built with Python, CSS, and an unreasonable amount of chai. ☕
