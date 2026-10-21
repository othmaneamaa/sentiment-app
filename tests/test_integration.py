"""Tests d'intÃ©gration : l'API telle qu'elle tourne vraiment (TP4, Ã©tape D)."""
from pathlib import Path

import pytest

MODELE = Path(__file__).resolve().parents[1] / "models" / "sentiment.joblib"
pytestmark = pytest.mark.skipif(not MODELE.exists(), reason="modÃ¨le non produit : python src/train.py")


def test_demarrage_reel_charge_le_modele():
    """D.1 : un client ouvert par Â« with Â» exÃ©cute le lifespan."""
    from fastapi.testclient import TestClient
    from api.main import app

    with TestClient(app) as client:
        reponse = client.get("/health")
    assert reponse.status_code == 200
    assert "TP2" in reponse.json()["model"]


def test_modele_absent_refuse_de_demarrer(monkeypatch, tmp_path):
    """D.2 : chemin du modÃ¨le redirigÃ©, cache vidÃ©, l'API refuse de dÃ©marrer."""
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
    import predict as predict_module

    from fastapi.testclient import TestClient
    from api.main import app

    monkeypatch.setattr(predict_module, "MODELE", tmp_path / "inexistant.joblib")
    if hasattr(predict_module, "charger_modele"):
        predict_module.charger_modele.cache_clear()

    with pytest.raises(FileNotFoundError):
        with TestClient(app):
            pass


def test_modele_non_charge_renvoie_503():
    """D.3 : modÃ¨le retirÃ© de app.state : 503 sur /health et /predict."""
    from fastapi.testclient import TestClient
    from api.main import app

    with TestClient(app) as client:
        app.state.classifier = None
        assert client.get("/health").status_code == 503
        assert client.post("/predict", json={"text": "Livraison rapide"}).status_code == 503


@pytest.mark.parametrize("exception", [RuntimeError("panne gÃ©nÃ©rique"), ValueError("bug interne")])
def test_modele_en_panne_renvoie_500_sans_message_interne(monkeypatch, exception):
    """D.4 : predict() lÃ¨ve une exception : 500, sans message interne."""
    from fastapi.testclient import TestClient
    from api.main import app

    with TestClient(app) as client:
        classifier = app.state.classifier
        monkeypatch.setattr(classifier, "predict", lambda text: (_ for _ in ()).throw(exception))
        reponse = client.post("/predict", json={"text": "Livraison rapide"})

    assert reponse.status_code == 500
    detail = reponse.json()["detail"]
    assert "panne gÃ©nÃ©rique" not in detail
    assert "bug interne" not in detail


def test_etiquettes_inconnues_renvoient_500(monkeypatch):
    """D.5 : predict() renvoie un label hors contrat : 500, pas de label inconnu au client."""
    from fastapi.testclient import TestClient

    from api.main import app

    # raise_server_exceptions=False : les exceptions serveur deviennent des réponses 500
    with TestClient(app, raise_server_exceptions=False) as client:
        classifier = app.state.classifier
        monkeypatch.setattr(
            classifier,
            "predict",
            lambda text: {"label": "PEUT_ETRE", "score": 0.5, "text": text[:100]},
        )
        reponse = client.post("/predict", json={"text": "Livraison rapide"})

    assert reponse.status_code == 500