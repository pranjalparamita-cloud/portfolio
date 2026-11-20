"""Build the self-contained portfolio HTML from the local template and assets."""
from __future__ import annotations

import base64
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"

CERT_KEYS = (
    "cttc",
    "deloitte",
    "tata",
    "jpmorgan",
    "nptel_ds",
    "nptel_dm",
    "adobe",
    "eduskill",
    "eduskill_intern",
    "unified_mentor",
)


def _mime(path: Path) -> str:
    return {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".svg": "image/svg+xml",
    }.get(path.suffix.lower(), "application/octet-stream")


def data_uri(path: Path) -> str:
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{_mime(path)};base64,{encoded}"


@lru_cache(maxsize=1)
def build_html() -> str:
    """Return the complete, offline-ready portfolio HTML string."""
    html = (ASSETS / "template.html").read_text(encoding="utf-8")
    replacements: dict[str, str] = {
        "PHOTO": data_uri(ASSETS / "photo.jpg"),
        "RESUME_PDF": data_uri(ASSETS / "resume.pdf"),
    }
    for key in CERT_KEYS:
        replacements[f"CERT_{key.upper()}_IMG"] = data_uri(ASSETS / "certs" / f"{key}.jpg")
        replacements[f"CERT_{key.upper()}_PDF"] = data_uri(ASSETS / "certs" / f"{key}.pdf")

    for token, value in replacements.items():
        html = html.replace(f"__{token}__", value)
    return html


if __name__ == "__main__":
    out = ROOT / "portfolio.html"
    out.write_text(build_html(), encoding="utf-8")
    print(f"Wrote {out} ({out.stat().st_size / 1024 / 1024:.1f} MB)")
