import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

import streamlit as st
import plotly.express as px

from snowflake_reader import get_companies_df


st.set_page_config(
    page_title="Company Analysis",
    layout="wide"
)

st.title("🏢 Top Hiring Companies")

df = get_companies_df()

total_companies = len(df)
total_jobs = int(df["TOTAL_JOBS"].sum())

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Unique Companies",
        total_companies
    )

with col2:
    st.metric(
        "Total Jobs",
        total_jobs
    )

st.subheader(
    "Company Hiring Distribution"
)

fig = px.bar(
    df.head(20),
    x="COMPANY_NAME",
    y="TOTAL_JOBS",
    title="Top Companies by Job Count"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("Company Data")

st.dataframe(
    df,
    use_container_width=True
)