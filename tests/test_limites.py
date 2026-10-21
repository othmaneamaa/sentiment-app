"""Tests aux limites du contrat d'entrÃ©e (TP4, Ã©tape B).

PredictRequest promet un champ Â« text Â», chaÃ®ne de 1 Ã  2000 caractÃ¨res.
Ce fichier vÃ©rifie cette promesse Ã  ses frontiÃ¨res, puis au hasard (hypothesis).
"""
import json
from pathlib import Path

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

MODELE = Path(__file__).resolve().parents[1] / "models" / "sentiment.joblib"
pytestmark = pytest.mark.skipif(not MODELE.exists(), reason="modÃ¨le non produit : python src/train.py")

# Trois Ã©tiquettes possibles depuis le TP4 : abstention incluse.
ETIQUETTES = {"POSITIVE", "NEGATIVE", "INDETERMINE"}
BLANCS = " \t\n\r\x0b\x0c\x85\u00a0"


@pytest.fixture(scope="module")
def client():
    """PortÃ©e Â« module Â» : l'API dÃ©marre une fois pour tout le fichier (hypothesis l'exige)."""
    from fastapi.testclient import TestClient

    from api.main import app

    with TestClient(app) as c:  # le Â« with Â» exÃ©cute le lifespan : le modÃ¨le est chargÃ©
        yield c


def en_json(valeur: object) -> bytes:
    """Corps de requÃªte JSON, sous forme d'octets : permet aussi d'envoyer un corps invalide."""
    return json.dumps(valeur).encode("utf-8")


# Ã‰tape B.1 : huit cas au moins, chacun avec son code attendu.
CAS = [
    pytest.param(en_json({"text": ""}), 422, id="texte-vide"),
    pytest.param(en_json({"text": "   "}), 422, id="espaces"),
    pytest.param(en_json({"text": "a"}), 200, id="un-caractere"),
    pytest.param(en_json({"text": "a" * 2000}), 200, id="2000-caracteres"),
    pytest.param(en_json({"text": "a" * 2001}), 422, id="2001-caracteres"),
    pytest.param(en_json({}), 422, id="champ-absent"),
    pytest.param(en_json({"text": 42}), 422, id="mauvais-type"),
    pytest.param(b"pas du json", 422, id="corps-non-json"),
]


@pytest.mark.parametrize("corps, code_attendu", CAS)
def test_frontieres_du_contrat(client, corps, code_attendu):
    reponse = client.post("/predict", content=corps, headers={"Content-Type": "application/json"})
    assert reponse.status_code == code_attendu
    # Ã‰tape B.2 : pour chaque 422, la forme standard de FastAPI : liste d'objets {loc, msg, type}
    if code_attendu == 422:
        detail = reponse.json()["detail"]
        assert isinstance(detail, list), f"detail doit Ãªtre une liste, reÃ§u : {detail!r}"
        assert detail, "detail ne doit pas Ãªtre vide"
        for erreur in detail:
            assert "loc" in erreur and "msg" in erreur and "type" in erreur


# Ã‰tape B.5 : deux tests de propriÃ©tÃ© avec hypothesis.


@given(st.text(min_size=1, max_size=2000).filter(lambda s: s.strip()))
@settings(deadline=None, max_examples=30)
def test_texte_valide_recoit_200(client, texte):
    reponse = client.post("/predict", json={"text": texte})
    assert reponse.status_code == 200
    corps = reponse.json()
    assert corps["label"] in ETIQUETTES
    assert 0.0 <= corps["score"] <= 1.0


@given(st.text(alphabet=st.sampled_from(BLANCS), min_size=1, max_size=50))
@settings(deadline=None, max_examples=30)
def test_texte_de_blancs_recoit_422(client, texte):
    reponse = client.post("/predict", json={"text": texte})
    assert reponse.status_code == 422
    detail = reponse.json()["detail"]
    assert isinstance(detail, list)