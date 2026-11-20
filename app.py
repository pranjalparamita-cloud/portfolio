"""Streamlit entry point for Pranjal Paramita Sahu's portfolio.

Deploy on Streamlit Community Cloud with this file as the main script.
"""
from __future__ import annotations

import streamlit as st

from portfolio_builder import build_html

st.set_page_config(
    page_title="Pranjal Paramita Sahu · Data & Business Analyst",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit chrome so the embedded portfolio owns the viewport.
st.html(
    """
    <style>
      [data-testid="stHeader"], [data-testid="stToolbar"],
      [data-testid="stDecoration"], [data-testid="stStatusWidget"],
      [data-testid="stSidebar"], .stDeployButton { display: none !important; }
      .block-container { padding: 0 !important; max-width: none !important; }
      .main, .main .block-container { background: #050506 !important; }
      iframe[title="Pranjal Paramita Sahu portfolio"] { display: block; }
      footer { visibility: hidden; }
    </style>
    """
)

st.iframe(
    build_html(),
    height="content",
    alt="Pranjal Paramita Sahu portfolio",
)
