async function predire(texte, apiUrl, apiKey) {
    try {
        const reponse = await fetch(`${apiUrl}/v1/predict`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-API-Key": apiKey
            },
            body: JSON.stringify({ text: texte })
        });
        const corps = await reponse.json();
        if (reponse.ok) {
            return { ok: true, label: corps.label, score: corps.score };
        }
        return { ok: false, code: corps.erreur?.code || "ERREUR", message: corps.erreur?.message };
    } catch (e) {
        return { ok: false, code: "INJOIGNABLE", message: "API injoignable" };
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const bouton = document.getElementById("analyser");
    bouton.addEventListener("click", async () => {
        const texte = document.getElementById("avis").value;
        const apiUrl = document.getElementById("api-url").value;
        const apiKey = document.getElementById("api-key").value;
        const resultat = document.getElementById("resultat");

        resultat.innerHTML = "<em>Analyse en cours...</em>";
        resultat.className = "";

        const r = await predire(texte, apiUrl, apiKey);

        if (r.ok) {
            if (r.label === "INDETERMINE") {
                resultat.className = "warn";
                resultat.innerHTML = `<strong>Je ne sais pas : à faire vérifier par un humain</strong><br>Confiance : ${(r.score*100).toFixed(0)}%`;
            } else {
                resultat.className = "ok";
                const nom = r.label === "POSITIVE" ? "Avis positif" : "Avis négatif";
                resultat.innerHTML = `<strong>${nom}</strong><br>Confiance : ${(r.score*100).toFixed(0)}%`;
            }
        } else {
            resultat.className = "err";
            resultat.innerHTML = `<strong>Erreur</strong> : ${r.message}`;
        }
    });
});
