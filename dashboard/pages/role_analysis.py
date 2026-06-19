# dashboard/pages/role_analysis.py

import streamlit as st
import plotly.express as px


import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from snowflake_reader import get_roles_df

st.set_page_config(
    page_title="Role Analysis",
    layout="wide"
)

st.title("📈 Top Hiring Roles")

df = get_roles_df()

total_roles = len(df)
total_jobs = int(df["TOTAL_JOBS"].sum())

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Unique Roles",
        total_roles
    )

with col2:
    st.metric(
        "Total Jobs",
        total_jobs
    )

st.subheader("Role Hiring Distribution")

fig = px.bar(
    df,
    x="ROLE",
    y="TOTAL_JOBS",
    title="Jobs by Role"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("Role Data")

st.dataframe(
    df,
    use_container_width=True
)