import pandas as pd
from src.database import get_engine

engine = get_engine()

df = pd.read_sql(
    """
    SELECT *
    FROM linkedin_leads
    """,
    engine
)

print("\n========== LINKEDIN LEAD ANALYTICS ==========\n")

print(f"Total Leads: {len(df)}")

print("\n--- SDR Status ---")
print(df["sdr_status"].value_counts(dropna=False))

print("\n--- Leads by Agent ---")
print(df["agent"].value_counts(dropna=False))

print("\n--- Comment Status ---")
print(df["comment_status"].value_counts(dropna=False))

print("\n--- Prioritized ---")
print(df["prioritized"].value_counts(dropna=False))

print("\n--- Source ---")
print(df["source"].value_counts(dropna=False))

print("\n--- Connected Leads ---")
print(
    df["connected_at"]
    .notna()
    .sum()
)

print("\n--- Leads with LinkedIn URL ---")
print(
    df["linkedin_url"]
    .notna()
    .sum()
)