import { useEffect, useState } from "react";
import "./WeatherTipBanner.css";

/**
 * Componente que mostra uma sugestão de comida baseada no clima.
 *
 * Props:
 * - onRequestWeather: função ({ latitude, longitude }) => Promise<{ tempC, tip }>
 */
export default function WeatherTipBanner({ onRequestWeather }) {
  const [status, setStatus] = useState("locating"); // locating | loading | ready | denied | error
  const [temperature, setTemperature] = useState(null);
  const [tip, setTip] = useState("");

  // fallback para quando usuário nega geolocalização
  const fallbackTip =
    "Sugestão do dia: mantenha-se hidratado e aposte em comidas leves, como frutas ou uma salada.";

  useEffect(() => {
    let cancelled = false;

    if (!("geolocation" in navigator)) {
      setStatus("denied");
      setTip(fallbackTip);
      return;
    }

    navigator.geolocation.getCurrentPosition(
      async (pos) => {
        if (cancelled) return;
        const { latitude, longitude } = pos.coords;

        if (typeof onRequestWeather !== "function") {
          setStatus("denied");
          setTip(fallbackTip);
          return;
        }

        try {
          setStatus("loading");
          const data = await onRequestWeather({ latitude, longitude });
          if (cancelled) return;

          setTemperature(
            data && typeof data.tempC === "number" ? Math.round(data.tempC) : null
          );
          setTip(data?.tip || fallbackTip);
          setStatus("ready");
        } catch (err) {
          console.error("Erro ao buscar sugestão de clima:", err);
          setStatus("error");
          setTip(fallbackTip);
        }
      },
      () => {
        if (!cancelled) {
          setStatus("denied");
          setTip(fallbackTip);
        }
      },
      { enableHighAccuracy: false, timeout: 8000, maximumAge: 5 * 60 * 1000 }
    );

    return () => {
      cancelled = true;
    };
  }, [onRequestWeather]);

  return (
    <div className="weather-banner-container" aria-live="polite" aria-atomic="true">
      <div className="weather-banner-card">
        {status === "ready" && temperature != null && (
          <span className="weather-banner-temp">{`~${temperature}°C`}</span>
        )}

        <div className="weather-banner-tip">
          {status === "locating" && <span>Localizando clima próximo…</span>}
          {status === "loading" && <span>Carregando sugestão…</span>}
          {(status === "denied" || status === "error") && <span>{tip}</span>}
          {status === "ready" && <span>{tip}</span>}

          {(status === "locating" || status === "loading") && (
            <small className="weather-banner-muted">Pode levar alguns segundos.</small>
          )}
          {(status === "denied" || status === "error") && (
            <small className="weather-banner-muted">
              Sem localização — exibindo sugestão genérica.
            </small>
          )}
        </div>
      </div>
    </div>
  );
}