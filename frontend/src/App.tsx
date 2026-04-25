import { useEffect, useState } from "react";
import { getHealth } from "./services/api";

function App() {
  const [status, setStatus] = useState<string>("Loading...");

  useEffect(() => {
    getHealth()
      .then((data) => setStatus(data.status))
      .catch((err) => setStatus("Error: " + err.message));
  }, []);

  return (
    <div>
      <h1>WeatherWise</h1>
      <p>Backend status: {status}</p>
    </div>
  );
}

export default App;
