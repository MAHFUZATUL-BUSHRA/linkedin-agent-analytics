import pandas as pd

FILE_PATH = "data/raw/newton-leads-all-156-2026-08-26.csv"

df = pd.read_csv(FILE_PATH)

print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isna().sum())