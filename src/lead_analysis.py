import pandas as pd
from src.database import get_engine

engine = get_engine()

df = pd.read_sql("""
    SELECT
        name,
        job_title,
        company,
        industry,
        location,
        added_on,
        last_contacted,
        connected_at
    FROM linkedin_leads
""", engine)

for col in ["added_on", "last_contacted", "connected_at"]:
    df[col] = pd.to_datetime(df[col], errors="coerce")

print("\n========== LEAD SEGMENT ANALYSIS ==========\n")

print(f"Total Leads: {len(df)}")

print("\n--- Top Companies ---")
print(
    df["company"]
    .value_counts()
    .head(15)
)

print("\n--- Industries ---")
print(
    df["industry"]
    .value_counts()
    .head(15)
)

print("\n--- Locations ---")
print(
    df["location"]
    .value_counts()
    .head(15)
)

print("\n--- Job Titles ---")
print(
    df["job_title"]
    .value_counts()
    .head(15)
)

print("\n--- Missing Company ---")
print(
    f"{df['company'].isna().sum()} of {len(df)} leads "
    "have no company information."
)

print("\n--- Missing Industry ---")
print(
    f"{df['industry'].isna().sum()} of {len(df)} leads "
    "have no industry information."
)