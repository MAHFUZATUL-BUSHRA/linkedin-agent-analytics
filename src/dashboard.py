import streamlit as st
import pandas as pd
from database import get_engine
st.set_page_config(
    page_title="LinkedIn Agent Analytics",
    page_icon="📊",
    layout="wide"
)

engine = get_engine()

df = pd.read_sql(
    "SELECT * FROM linkedin_leads",
    engine
)

# -------------------------
# Title
# -------------------------

st.title("📊 LinkedIn Agent Analytics")
st.caption("Lead intelligence and outreach monitoring dashboard")

# -------------------------
# KPI Metrics
# -------------------------

total_leads = len(df)
connected = df["connected_at"].notna().sum()
missing_company = df["company"].isna().sum()
missing_industry = df["industry"].isna().sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Leads", total_leads)
col2.metric("Connected", connected)
col3.metric("Missing Company", missing_company)
col4.metric("Missing Industry", missing_industry)

st.divider()

# -------------------------
# Industry Analysis
# -------------------------

col1, col2 = st.columns(2)

with col1:
    st.subheader("Top Industries")

    industry_counts = (
        df["industry"]
        .fillna("Unknown")
        .value_counts()
        .head(10)
    )

    st.bar_chart(industry_counts)

with col2:
    st.subheader("Top Locations")

    location_counts = (
        df["location"]
        .fillna("Unknown")
        .value_counts()
        .head(10)
    )

    st.bar_chart(location_counts)

# -------------------------
# Lead Table
# -------------------------

st.divider()

st.subheader("Lead Database")

search = st.text_input(
    "Search by name, company or job title"
)

filtered_df = df.copy()

if search:
    mask = (
        filtered_df["name"].str.contains(
            search, case=False, na=False
        )
        |
        filtered_df["company"].fillna("").str.contains(
            search, case=False, na=False
        )
        |
        filtered_df["job_title"].fillna("").str.contains(
            search, case=False, na=False
        )
    )

    filtered_df = filtered_df[mask]

st.dataframe(
    filtered_df[
        [
            "name",
            "job_title",
            "company",
            "industry",
            "location",
            "sdr_status",
            "last_contacted",
            "linkedin_url"
        ]
    ],
    use_container_width=True,
    hide_index=True
)