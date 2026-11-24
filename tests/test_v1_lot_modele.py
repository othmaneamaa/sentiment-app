"""Tests de POST /v1/predict/lot."""
from pathlib import Path

import pytest

MODELE = Path(__file__).resolve().parents[1] / "models" / "sentiment.joblib"
pytestmark = pytest.mark.skipif(not MODELE.exists(), reason="modèle non produit : python src/train.py")

CLE_CLIENT = "cle-client-0123456789"
POSITIF = "Livraison rapide, produit conforme, très satisfait"
NEGATIF = "Produit cassé et service injoignable, à fuir"


@pytest.fixture()
def client(monkeypatch):
    from fastapi.testclient import TestClient

    from api.main import app

    monkeypatch.setenv("API_KEYS", f"{CLE_CLIENT}:client")
    with TestClient(app) as c:
        yield c


def _lot(client, avis, cle=CLE_CLIENT):
    entetes = {"X-API-Key": cle} if cle else {}
    return client.post("/v1/predict/lot", json={"avis": avis}, headers=entetes)


# --- POST /v1/predict/lot ---------------------------------------------------------------------

def test_lot_un_verdict_par_avis_dans_l_ordre(client):
    r = _lot(client, [POSITIF, NEGATIF])
    assert r.status_code == 200
    resultats = r.json()["resultats"]
    assert [x["label"] for x in resultats] == ["POSITIVE", "NEGATIVE"]
    assert resultats[0]["text"] == POSITIF


def test_lot_resume_compte_les_verdicts(client):
    resume = _lot(client, [POSITIF, POSITIF, NEGATIF]).json()["resume"]
    assert resume["total"] == 3
    assert resume["POSITIVE"] == 2
    assert resume["NEGATIVE"] == 1
    assert resume["POSITIVE"] + resume["NEGATIVE"] + resume["INDETERMINE"] == resume["total"]


def test_lot_meme_verdict_que_predict_seul(client):
    seul = client.post("/v1/predict", json={"text": NEGATIF}, headers={"X-API-Key": CLE_CLIENT})
    assert _lot(client, [NEGATIF]).json()["resultats"][0] == seul.json()


def test_lot_sans_cle_401(client):
    assert _lot(client, [POSITIF], cle=None).status_code == 401


@pytest.mark.parametrize(
    "avis",
    [[], [POSITIF, "   "], [POSITIF, "x" * 2001], ["avis"] * 101, "pas une liste"],
    ids=["lot-vide", "avis-blanc", "avis-trop-long", "trop-d-avis", "pas-une-liste"],
)
def test_lot_invalide_422(client, avis):
    assert _lot(client, avis).status_code == 422


def test_lot_panne_500_sans_message_interne(client, monkeypatch):
    from api.main import app

    def en_panne(texte):
        raise RuntimeError("secret interne")

    monkeypatch.setattr(app.state.classifier, "predict", en_panne)
    r = _lot(client, [POSITIF])
    assert r.status_code == 500
    assert "secret interne" not in r.text

