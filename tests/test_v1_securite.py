"""Tests des routes /v1 et de l'authentification par clé d'API.

Les routes /v1 et api/securite.py n'avaient pas de tests Python : la couverture de api/
tombait à 76 %, sous le seuil de 95 % exigé par la CI.
"""
from pathlib import Path

import pytest

from api.securite import charger_cles

MODELE = Path(__file__).resolve().parents[1] / "models" / "sentiment.joblib"
avec_modele = pytest.mark.skipif(not MODELE.exists(), reason="modèle non produit : python src/train.py")

CLE_CLIENT = "cle-client-0123456789"
CLE_ADMIN = "cle-admin-0123456789ab"
CLE_INCONNUE = "cle-inconnue-0123456789"


# --- charger_cles : lecture de API_KEYS, sans serveur ---------------------------------------

def test_charger_cles_lit_cles_et_roles():
    assert charger_cles(f"{CLE_CLIENT}:client, {CLE_ADMIN}:admin") == {
        CLE_CLIENT: "client",
        CLE_ADMIN: "admin",
    }


def test_charger_cles_vide_ferme_par_defaut():
    assert charger_cles("") == {}
    assert charger_cles(" , ,") == {}


def test_charger_cles_lit_la_variable_d_environnement(monkeypatch):
    monkeypatch.setenv("API_KEYS", f"{CLE_CLIENT}:client")
    assert charger_cles() == {CLE_CLIENT: "client"}


def test_charger_cles_refuse_un_role_inconnu():
    with pytest.raises(ValueError, match="role inconnu"):
        charger_cles(f"{CLE_CLIENT}:superuser")


def test_charger_cles_refuse_une_cle_trop_courte():
    with pytest.raises(ValueError, match="trop courte"):
        charger_cles("courte:client")


def test_dotenv_est_lu_sans_ecraser_l_environnement(monkeypatch, tmp_path):
    import api.securite as securite

    faux_module = tmp_path / "api" / "securite.py"
    faux_module.parent.mkdir()
    faux_module.touch()
    (tmp_path / ".env").write_text(
        "# commentaire\n\nSANS_EGAL\nVAR_TEST_A='valeur a'\nVAR_TEST_B=\"nouvelle\"\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(securite, "__file__", str(faux_module))
    monkeypatch.delenv("VAR_TEST_A", raising=False)
    monkeypatch.setenv("VAR_TEST_B", "deja-la")
    securite._charger_dotenv()
    assert securite.os.environ["VAR_TEST_A"] == "valeur a"
    assert securite.os.environ["VAR_TEST_B"] == "deja-la"  # l'environnement gagne sur .env
    monkeypatch.delenv("VAR_TEST_A")


def test_dotenv_absent_ne_fait_rien(monkeypatch, tmp_path):
    import api.securite as securite

    faux_module = tmp_path / "api" / "securite.py"
    monkeypatch.setattr(securite, "__file__", str(faux_module))
    securite._charger_dotenv()  # aucun .env : aucune erreur


# --- Les routes /v1, via TestClient ------------------------------------------------------------

@pytest.fixture()
def client(monkeypatch):
    from fastapi.testclient import TestClient

    from api.main import app

    monkeypatch.setenv("API_KEYS", f"{CLE_CLIENT}:client,{CLE_ADMIN}:admin")
    with TestClient(app) as c:
        yield c


def _predire(client, cle=None, texte="Livraison rapide, produit conforme, très satisfait"):
    entetes = {"X-API-Key": cle} if cle else {}
    return client.post("/v1/predict", json={"text": texte}, headers=entetes)


@avec_modele
def test_v1_health_est_public(client):
    r = client.get("/v1/health")
    assert r.status_code == 200
    assert r.json()["status"] == "OK"


@avec_modele
def test_v1_predict_sans_cle_401(client):
    r = _predire(client)
    assert r.status_code == 401
    assert r.headers["WWW-Authenticate"] == "ApiKey"


@avec_modele
def test_v1_predict_cle_inconnue_401(client):
    assert _predire(client, CLE_INCONNUE).status_code == 401


@avec_modele
@pytest.mark.parametrize("cle", [CLE_CLIENT, CLE_ADMIN])
def test_v1_predict_client_et_admin_acceptes(client, cle):
    r = _predire(client, cle)
    assert r.status_code == 200
    assert r.json()["label"] == "POSITIVE"


@avec_modele
def test_v1_predict_texte_vide_422(client):
    assert _predire(client, CLE_CLIENT, texte="   ").status_code == 422


def test_role_non_autorise_403():
    from fastapi import HTTPException

    from api.securite import exiger

    verifier = exiger("admin")
    assert verifier("admin") == "admin"
    with pytest.raises(HTTPException) as erreur:
        verifier("client")
    assert erreur.value.status_code == 403


@avec_modele
def test_v1_modele_non_charge_503(client):
    from api.main import app

    sauvegarde = app.state.classifier
    app.state.classifier = None
    try:
        assert client.get("/v1/health").status_code == 503
    finally:
        app.state.classifier = sauvegarde


@avec_modele
def test_v1_predict_panne_500_sans_message_interne(client, monkeypatch):
    from api.main import app

    def en_panne(texte):
        raise RuntimeError("secret interne")

    monkeypatch.setattr(app.state.classifier, "predict", en_panne)
    r = _predire(client, CLE_CLIENT)
    assert r.status_code == 500
    assert "secret interne" not in r.text
