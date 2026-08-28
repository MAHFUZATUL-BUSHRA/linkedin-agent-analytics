import pandas as pd
from src.database import get_engine

CSV_FILE = "data/raw/newton-leads-all-156-2026-08-26.csv"

df = pd.read_csv(CSV_FILE)

engine = get_engine()

df.columns = [
    "name",
    "job_title",
    "company",
    "industry",
    "location",
    "agent",
    "sdr_status",
    "comment_status",
    "hot_score",
    "source",
    "prioritized",
    "linkedin_url",
    "added_on",
    "last_contacted",
    "invite_sent_at",
    "connected_at"
]

date_columns = [
    "added_on",
    "last_contacted",
    "invite_sent_at",
    "connected_at"
]

for column in date_columns:
    df[column] = pd.to_datetime(df[column], errors="coerce")

df.to_sql(
    "linkedin_leads",
    engine,
    if_exists="append",
    index=False,
    method="multi"
)

print(f"Successfully loaded {len(df)} leads into PostgreSQL.")