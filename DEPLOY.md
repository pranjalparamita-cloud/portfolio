# Deploy to Streamlit Community Cloud

This folder is deployment-ready. No API keys, secrets or environment variables are required.

## 1. Push to GitHub

From this folder:

```bash
git init
git add .
git commit -m "Cinematic Streamlit portfolio"
git remote add origin https://github.com/<YOUR_USERNAME>/<YOUR_REPO>.git
git branch -M main
git push -u origin main
```

If you already have a repo, skip `git init` and just replace the remote line.

> The repository already contains a local commit, so if you cloned/downloaded this exact folder you only need to add the remote and push.

## 2. Deploy on Streamlit Community Cloud

1. Open <https://share.streamlit.io/> and sign in with **GitHub**.
2. Click **New app**.
3. Select:
   - **Repository:** `<YOUR_USERNAME>/<YOUR_REPO>`
   - **Branch:** `main`
   - **Main file path:** `app.py`
4. Leave **Advanced settings** empty. There are no secrets to add.
5. Click **Deploy**.

Streamlit will install `streamlit>=1.67,<2` from `requirements.txt` and start the app. The first build usually takes 1–3 minutes.

## 3. Your live URL

After deployment you'll get a URL like:

```text
https://<your-app-name>-<hash>.streamlit.app
```

You can customise it under **App settings → App URL** if the name is available.

## Why it works on Community Cloud

- `app.py` is the only entry point.
- `portfolio_builder.py` reads files relative to `__file__`, so it works from any working directory.
- All images and PDFs are embedded as data URIs at runtime — nothing depends on local absolute paths or external CDNs.
- `height="content"` on `st.iframe` lets the page grow naturally.
- No database, no ports, no credentials, no extra services.

## Quick checks before deploying

```bash
pip install -r requirements.txt
streamlit run app.py
```

If the local app opens correctly, the Cloud deployment will behave the same way.

## Troubleshooting

| Issue | Fix |
|---|---|
| Blank page | Confirm `requirements.txt` pins `streamlit>=1.67`; older versions lack `st.iframe(height="content")`. |
| Slow first load | The generated HTML embeds your résumé and 10 PDFs (~8 MB). First load after a cold start can take a few seconds. |
| 404 on certificates | None — certificate PDFs are embedded in the HTML, not served from the filesystem. |
| App sleeps | Free Streamlit apps sleep after inactivity. Opening the URL wakes them; the first wake takes ~20–40 seconds. |

---

Built with Python, CSS, and an unreasonable amount of chai. ☕
