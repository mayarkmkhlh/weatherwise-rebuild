const API_BASE = import.meta.env.VITE_API_BASE_URL;

export type HealthResponse = {
    status: string;
  };

  export async function getHealth(): Promise<HealthResponse> {
    const res = await fetch(`${API_BASE}/health`);
  
    if (!res.ok) {
      throw new Error(`Health request failed: ${res.status}`);
    }
  
    return res.json();
  }

  export type PredictRequest = {
    temperature: number;
    rain: boolean;
  };
  
  export type PredictResponse = {
    umbrella: boolean;
    clothing: string;
    advice: string;
  };
  
  export async function getPrediction(
    body: PredictRequest
  ): Promise<PredictResponse> {
    const res = await fetch(`${API_BASE}/predict`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });
  
    if (!res.ok) {
      throw new Error(`Prediction failed: ${res.status}`);
    }
  
    return res.json();
  }