import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

import streamlit as st
import plotly.express as px

from snowflake_reader import get_locations_df


st.set_page_config(
    page_title="Location Analysis",
    layout="wide"
)

st.title("📍 Top Hiring Locations")

df = get_locations_df()

total_locations = len(df)
total_jobs = int(df["TOTAL_JOBS"].sum())

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Unique Locations",
        total_locations
    )

with col2:
    st.metric(
        "Total Jobs",
        total_jobs
    )

st.subheader(
    "Location Hiring Distribution"
)

fig = px.bar(
    df.head(20),
    x="LOCATION_NAME",
    y="TOTAL_JOBS",
    title="Top Locations by Job Count"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("Location Data")

st.dataframe(
    df,
    use_container_width=True
)