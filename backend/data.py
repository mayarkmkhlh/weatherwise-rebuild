import pandas as pd
from pathlib import Path

# 🔹 Resolve project root reliably
BASE_DIR = Path(__file__).resolve().parents[1]

# 🔹 Path to your dataset
DATA_PATH = BASE_DIR / "ml" / "data" / "raw" / "hourly_observations.csv"

# 🔹 Load once at import time
df = pd.read_csv(DATA_PATH)

# 🔹 Optional: quick sanity info
print(f"[data] Loaded dataset with shape: {df.shape}")
