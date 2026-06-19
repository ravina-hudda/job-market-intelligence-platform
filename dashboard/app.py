# dashboard/app.py

import streamlit as st

st.set_page_config(
    page_title="Job Market Intelligence Platform",
    layout="wide"
)

st.title(
    "📊 Job Market Intelligence Platform"
)

st.markdown(
    """
    End-to-End Data Engineering Project

    Source: Adzuna API
    Warehouse: Snowflake
    Processing: PySpark
    Dashboard: Streamlit
    """
)