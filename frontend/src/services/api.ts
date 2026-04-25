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