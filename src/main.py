from fastapi import FastAPI
from src.database import get_engine
import pandas as pd

app = FastAPI(title="LinkedIn Agent Analytics API")

engine = get_engine()


@app.get("/")
def home():
    return {
        "message": "LinkedIn Agent Analytics API is running"
    }


@app.get("/leads")
def get_leads():
    df = pd.read_sql(
        "SELECT * FROM linkedin_leads ORDER BY id",
        engine
    )

    df = df.where(pd.notna(df), None)

    return df.to_dict(orient="records")


@app.get("/analytics")
def get_analytics():
    df = pd.read_sql(
        "SELECT * FROM linkedin_leads",
        engine
    )

    return {
        "total_leads": len(df),
        "connected_leads": int(
            df["connected_at"].notna().sum()
        ),
        "missing_company": int(
            df["company"].isna().sum()
        ),
        "missing_industry": int(
            df["industry"].isna().sum()
        ),
        "top_industries": (
            df["industry"]
            .value_counts()
            .head(10)
            .to_dict()
        ),
        "top_locations": (
            df["location"]
            .value_counts()
            .head(10)
            .to_dict()
        )
    }