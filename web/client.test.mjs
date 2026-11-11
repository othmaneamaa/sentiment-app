import test from "node:test";
import assert from "node:assert/strict";

async function predire(texte, apiUrl, apiKey, fetchFn = fetch) {
    try {
        const reponse = await fetchFn(`${apiUrl}/v1/predict`, {
            method: "POST",
            headers: { "Content-Type": "application/json", "X-API-Key": apiKey },
            body: JSON.stringify({ text: texte })
        });
        const corps = await reponse.json();
        if (reponse.ok) return { ok: true, label: corps.label, score: corps.score };
        return { ok: false, code: corps.erreur?.code || "ERREUR", message: corps.erreur?.message };
    } catch (e) {
        return { ok: false, code: "INJOIGNABLE", message: "API injoignable" };
    }
}

test("réponse OK renvoie label et score", async () => {
    const fakeFetch = async () => ({ ok: true, json: async () => ({ label: "POSITIVE", score: 0.9 }) });
    const r = await predire("test", "http://api", "cle", fakeFetch);
    assert.equal(r.ok, true); assert.equal(r.label, "POSITIVE"); assert.equal(r.score, 0.9);
});

test("401 renvoie NON_AUTHENTIFIE", async () => {
    const fakeFetch = async () => ({ ok: false, json: async () => ({ erreur: { code: "NON_AUTHENTIFIE", message: "Clé manquante" } }) });
    const r = await predire("test", "http://api", "", fakeFetch);
    assert.equal(r.ok, false); assert.equal(r.code, "NON_AUTHENTIFIE");
});

test("422 renvoie ENTREE_INVALIDE", async () => {
    const fakeFetch = async () => ({ ok: false, json: async () => ({ erreur: { code: "ENTREE_INVALIDE", message: "Texte vide" } }) });
    const r = await predire("", "http://api", "cle", fakeFetch);
    assert.equal(r.code, "ENTREE_INVALIDE");
});

test("403 renvoie ACCES_REFUSE", async () => {
    const fakeFetch = async () => ({ ok: false, json: async () => ({ erreur: { code: "ACCES_REFUSE", message: "Rôle insuffisant" } }) });
    const r = await predire("test", "http://api", "cle-client", fakeFetch);
    assert.equal(r.code, "ACCES_REFUSE");
});

test("503 renvoie MODELE_INDISPONIBLE", async () => {
    const fakeFetch = async () => ({ ok: false, json: async () => ({ erreur: { code: "MODELE_INDISPONIBLE", message: "Modèle non chargé" } }) });
    const r = await predire("test", "http://api", "cle", fakeFetch);
    assert.equal(r.code, "MODELE_INDISPONIBLE");
});

test("500 renvoie ERREUR_INTERNE", async () => {
    const fakeFetch = async () => ({ ok: false, json: async () => ({ erreur: { code: "ERREUR_INTERNE", message: "Erreur" } }) });
    const r = await predire("test", "http://api", "cle", fakeFetch);
    assert.equal(r.code, "ERREUR_INTERNE");
});

test("API injoignable renvoie INJOIGNABLE", async () => {
    const fakeFetch = async () => { throw new Error("réseau"); };
    const r = await predire("test", "http://api", "cle", fakeFetch);
    assert.equal(r.code, "INJOIGNABLE");
});

test("texte vide renvoie INJOIGNABLE sans planter", async () => {
    const fakeFetch = async () => { throw new Error("réseau"); };
    const r = await predire("", "http://api", "cle", fakeFetch);
    assert.equal(r.ok, false);
});

test("score 0.5 est bien un nombre", async () => {
    const fakeFetch = async () => ({ ok: true, json: async () => ({ label: "NEGATIVE", score: 0.5 }) });
    const r = await predire("test", "http://api", "cle", fakeFetch);
    assert.equal(typeof r.score, "number");
});

test("label INDETERMINE est accepté", async () => {
    const fakeFetch = async () => ({ ok: true, json: async () => ({ label: "INDETERMINE", score: 0.55 }) });
    const r = await predire("test", "http://api", "cle", fakeFetch);
    assert.equal(r.label, "INDETERMINE");
});

test("apiUrl est bien utilisé", async () => {
    let url = "";
    const fakeFetch = async (u) => { url = u; return { ok: true, json: async () => ({ label: "POSITIVE", score: 0.9 }) }; };
    await predire("test", "http://mon-api", "cle", fakeFetch);
    assert.equal(url, "http://mon-api/v1/predict");
});

test("apiKey est bien transmise dans l'en-tête", async () => {
    let entete = "";
    const fakeFetch = async (u, opts) => { entete = opts.headers["X-API-Key"]; return { ok: true, json: async () => ({ label: "POSITIVE", score: 0.9 }) }; };
    await predire("test", "http://api", "ma-cle-secrete", fakeFetch);
    assert.equal(entete, "ma-cle-secrete");
});
