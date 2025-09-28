// Open-Meteo client + geração de sugestão de comida

const weather = {
  /**
   * Assinatura compatível com o WeatherTipBanner:
   * onRequestWeather({ latitude, longitude }) => Promise<{ tempC: number|null, tip: string }>
   */
  async getSuggestionByCoords({ latitude, longitude }) {
    try {
      const url = new URL("https://api.open-meteo.com/v1/forecast");
      url.searchParams.set("latitude", latitude);
      url.searchParams.set("longitude", longitude);
      url.searchParams.set("current", "temperature_2m");
      url.searchParams.set("temperature_unit", "celsius");
      url.searchParams.set("timezone", "auto");

      const res = await fetch(url.toString());
      if (!res.ok) throw new Error("Falha ao buscar dados do clima");

      const data = await res.json();
      const tempC = data?.current?.temperature_2m;

      // Sugestão baseada na temperatura
      let tip =
        "Sugestão do dia: mantenha-se hidratado e aposte em comidas leves, como frutas ou uma salada."; // fallback
      if (typeof tempC === "number") {
        const t = Math.round(tempC);
        if (t <= 0) {
          tip = `Hoje está ${t}°C. Que tal uma sopa bem quente para se aquecer?`;
        } else if (t <= 10) {
          tip = `Hoje está ${t}°C. Experimente caldos e pratos quentes para espantar o frio.`;
        } else if (t <= 20) {
          tip = `Hoje está ${t}°C. Um prato de massa ou legumes salteados pode cair muito bem.`;
        } else if (t <= 28) {
          tip = `Hoje está ${t}°C. Mantenha-se hidratado e aproveite frutas frescas.`;
        } else {
          tip = `Hoje está ${t}°C. Hidrate-se bem e prefira comidas leves, como uma salada.`;
        }
      }

      return { tempC, tip };
    } catch (err) {
      console.error("Erro em weather.getSuggestionByCoords:", err);
      // Em erro de rede/API, devolve fallback genérico para o banner exibir algo útil
      return {
        tempC: null,
        tip:
          "Sugestão do dia: mantenha-se hidratado e aposte em comidas leves, como frutas ou uma salada.",
      };
    }
  },
};

export default weather;
