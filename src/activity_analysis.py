import pandas as pd
from src.database import get_engine

engine = get_engine()

df = pd.read_sql("""
    SELECT
        name,
        company,
        added_on,
        last_contacted,
        connected_at
    FROM linkedin_leads
""", engine)

for col in ["added_on", "last_contacted", "connected_at"]:
    df[col] = pd.to_datetime(df[col], errors="coerce")

# Time from lead added to first/last contact
df["contact_delay_minutes"] = (
    df["last_contacted"] - df["added_on"]
).dt.total_seconds() / 60

# Time between contact and connection
df["connection_delay_minutes"] = (
    df["connected_at"] - df["last_contacted"]
).dt.total_seconds() / 60

print("\n========== CONTACT ACTIVITY ==========\n")

print(f"Total Leads: {len(df)}")

print("\n--- Contact Delay ---")
print(f"Average: {df['contact_delay_minutes'].mean():.2f} minutes")
print(f"Minimum: {df['contact_delay_minutes'].min():.2f} minutes")
print(f"Maximum: {df['contact_delay_minutes'].max():.2f} minutes")

print("\n--- Connection Delay ---")
print(f"Average: {df['connection_delay_minutes'].mean():.2f} minutes")
print(f"Minimum: {df['connection_delay_minutes'].min():.2f} minutes")
print(f"Maximum: {df['connection_delay_minutes'].max():.2f} minutes")

print("\n--- Contact Activity by Hour ---")

df["contact_hour"] = df["last_contacted"].dt.hour

print(
    df["contact_hour"]
    .value_counts()
    .sort_index()
)

print("\n--- Most Recent Contacts ---")

print(
    df[
        ["name", "company", "last_contacted", "connected_at"]
    ]
    .sort_values("last_contacted", ascending=False)
    .head(10)
    .to_string(index=False)
)