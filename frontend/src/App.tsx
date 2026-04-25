import { useEffect, useState } from "react";
import { getPrediction } from "./services/api";

function App() {
  const [result, setResult] = useState<string>("No prediction yet");

  const handleClick = async () => {
    try {
      const data = await getPrediction({
        temperature: 15,
        rain: true,
      });

      setResult(data.advice);
    } catch (err) {
      console.error(err);
      setResult("Error calling backend");
    }
  };

  return (
    <div>
      <h1>WeatherWise</h1>

      <button onClick={handleClick}>Get Recommendation</button>

      <p>{result}</p>
    </div>
  );
}

export default App;
