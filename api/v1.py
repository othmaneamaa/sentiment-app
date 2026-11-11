"""Routes de la version 1 de l'API (TP2)."""
from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException, Request

from api.schemas import ErreurV1, HealthResponse, PredictRequest, PredictResponse
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
