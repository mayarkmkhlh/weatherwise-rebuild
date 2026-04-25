from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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
    if data.rain:
        return {
            "umbrella": True,
            "clothing": "light_jacket",
            "advice": "Rain expected — take an umbrella."
        }
    else:
        return {
            "umbrella": False,
            "clothing": "t_shirt",
            "advice": "Weather is clear — light clothing is fine."
        }