"""Routes de la version 1 de l'API (TP2)."""
import json
from collections import Counter
from pathlib import Path
from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException, Request

from api.model import SEUIL_ABSTENTION
from api.schemas import (
    ErreurV1,
    HealthResponse,
    LotRequest,
    LotResponse,
    ModeleResponse,
    PredictRequest,
    PredictResponse,
)
from api.securite import exiger

ERREURS: dict[int | str, dict[str, Any]] = {
    code: {"model": ErreurV1} for code in (401, 403, 422, 500, 503)
}
router = APIRouter(prefix="/v1", tags=["v1"], responses=ERREURS)


def classifier(request: Request):
    clf = getattr(request.app.state, "classifier", None)
    if clf is None:
        raise HTTPException(503, "Modele non charge")
    return clf


Classifier = Annotated[Any, Depends(classifier)]


@router.get("/health", response_model=HealthResponse, summary="Sante (public)")
def sante(clf: Classifier) -> dict[str, str]:
    return {"status": "OK", "model": clf.model_name}


@router.post(
    "/predict",
    response_model=PredictResponse,
    summary="Classer un avis (client, admin)",
    dependencies=[Depends(exiger("client", "admin"))],
)
def predire(corps: PredictRequest, clf: Classifier):
    try:
        resultat = clf.predict(corps.text)
    except Exception:
        raise HTTPException(500, "Erreur interne du serveur") from None
    return resultat


# --- Analyse par lot et informations sur le modèle ---
METRIQUES = Path(__file__).resolve().parents[1] / "models" / "metrics.json"


@router.post(
    "/predict/lot",
    response_model=LotResponse,
    summary="Classer plusieurs avis d'un coup (client, admin)",
    dependencies=[Depends(exiger("client", "admin"))],
)
def predire_lot(corps: LotRequest, clf: Classifier):
    try:
        resultats = [clf.predict(texte) for texte in corps.avis]
    except Exception:
        raise HTTPException(500, "Erreur interne du serveur") from None
    compte = Counter(r["label"] for r in resultats)
    resume = {
        "total": len(resultats),
        "POSITIVE": compte["POSITIVE"],
        "NEGATIVE": compte["NEGATIVE"],
        "INDETERMINE": compte["INDETERMINE"],
    }
    return {"resultats": resultats, "resume": resume}


@router.get("/modele", response_model=ModeleResponse, summary="Informations sur le modèle (public)")
def modele(clf: Classifier) -> dict[str, Any]:
    metriques = None
    if METRIQUES.exists():
        metriques = json.loads(METRIQUES.read_text(encoding="utf-8"))
    return {"model": clf.model_name, "seuil_abstention": SEUIL_ABSTENTION, "metriques": metriques}
