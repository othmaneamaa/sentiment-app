"""Contrats d'entrée et de sortie de l'API (Pydantic v2)."""
from typing import Literal

from pydantic import BaseModel, Field, field_validator


class PredictRequest(BaseModel):
    """Requête de prédiction."""
    text: str = Field(..., min_length=1, max_length=2000, description="Texte à classifier",
                      examples=["Livraison rapide, produit conforme, très satisfait"])

    @field_validator("text")
    @classmethod
    def texte_non_vide(cls, valeur: str) -> str:
        """Refuse un texte fait uniquement de blancs (même règle que predict() du TP2)."""
        if not valeur.strip():
            raise ValueError("texte vide")
        return valeur


class PredictResponse(BaseModel):
    """Réponse de prédiction."""
    label: Literal["POSITIVE", "NEGATIVE", "INDETERMINE"] = Field(
        ..., description="POSITIVE, NEGATIVE ou INDETERMINE"
    )
    score: float = Field(..., ge=0, le=1, description="Confiance de la classe prédite")
    text: str = Field(..., description="Aperçu du texte analysé (100 caractères)")


class HealthResponse(BaseModel):
    """Réponse de l'endpoint de santé."""
    status: str = Field(..., description="OK si le modèle est chargé")
    model: str = Field(..., description="Nom du modèle servi")


class ErrorResponse(BaseModel):
    """Format standard des erreurs FastAPI."""
    detail: str
# --- TP2 : format d'erreur unique pour /v1 ---
class ChampInvalide(BaseModel):
    champ: str = Field(..., description="Champ refusé, par exemple body.text")
    message: str = Field(..., description="Raison du refus")


class DetailError(BaseModel):
    code: str = Field(..., description="Code stable : ENTREE_INVALIDE, NON_AUTHENTIFIE...")
    message: str = Field(..., description="Message lisible, susceptible de changer")
    champs: list[ChampInvalide] = Field(default_factory=list)


class ErreurV1(BaseModel):
    """Format unique de toutes les erreurs de /v1."""
    erreur: DetailError
