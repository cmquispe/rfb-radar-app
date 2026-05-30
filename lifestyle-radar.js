const lifestyleData = {
  "Ford": [4, 3, 4, 2, 2, 3],
  "Subaru": [4, 3, 5, 2, 2, 3],
  "Nissan": [3, 4, 3, 2, 2, 4],
  "Honda": [4, 4, 3, 2, 2, 4],
  "Chevrolet": [4, 3, 4, 2, 3, 3],
  "Volkswagen": [3, 4, 3, 3, 3, 3],
  "Toyota": [5, 4, 3, 2, 2, 4],
  "Hyundai": [3, 4, 3, 4, 3, 3],
  "Kia": [3, 4, 3, 4, 3, 3],
  "Tesla": [2, 4, 2, 5, 3, 2],
  "BYD": [3, 4, 3, 4, 3, 3],
  "BMW": [2, 4, 2, 3, 5, 2],
  "Mercedes": [2, 4, 2, 3, 5, 2]
};


document.getElementById("generateBtn").onclick = async () => {
  const brand = document.getElementById("brandSelect").value;

  if (!brand) {
    alert("Please select a brand");
    return;
  }

  const criteria = ["Family", "Commuter", "Outdoor", "Tech‑Focused", "Luxury", "Budget"];
  const values = lifestyleData[brand];

  const payload = {
    criteria: criteria,
    entities: {
      [brand]: values
    }
  };

  const response = await fetch("https://rfb-radar-app.onrender.com/radar", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });

  const data = await response.json();

  document.getElementById("insightsResult").innerHTML =
    `<h3>Insights</h3><ul>${data.insights.map(i => `<li>${i}</li>`).join("")}</ul>`;

  document.getElementById("radarResult").innerHTML =
    `<img src="https://rfb-radar-app.onrender.com/radar-image?${Date.now()}" style="max-width:500px;">`;
};
