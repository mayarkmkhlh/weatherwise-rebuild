from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.data import df

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5173", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

class PredictRequest(BaseModel):
    temperature: float
    rain: bool

@app.post("/predict")
def predict(data: PredictRequest):

    # 🔹 Step 1: Filter rain condition
    if data.rain:
        df_filtered = df[df["precipitation_mm"] > 0]
    else:
        df_filtered = df[df["precipitation_mm"] == 0]

    # 🔹 Step 2: If empty, fallback to full dataset
    if df_filtered.empty:
        df_filtered = df

    # 🔹 Step 3: Compute temperature difference
    df_filtered = df_filtered.copy()  # avoid warning
    df_filtered["temp_diff"] = abs(df_filtered["temperature_c"] - data.temperature)

    # 🔹 Step 4: Sort by closest temperature
    df_filtered = df_filtered.sort_values(by="temp_diff")

    # 🔹 Step 5: Pick best match
    row = df_filtered.iloc[0]

    return {
        "umbrella": bool(row["umbrella_needed"]),
        "clothing": row["clothing_recommendation"],
        "advice": row["recommendation_text"],
    }