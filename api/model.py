"""Raccord entre l'API et le modÃ¨le entraÃ®nÃ© au TP2.

L'API n'entraÃ®ne rien et ne connaÃ®t pas scikit-learn : elle appelle la fonction
predict() de src/predict.py, qui charge models/sentiment.joblib une seule fois.
"""
import sys
from pathlib import Path
from typing import Literal, TypedDict

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "src"))
from predict import charger_modele  # noqa: E402  (fonctions du TP2)
from predict import predict as _predict  # noqa: E402  (fonctions du TP2)

# Seuil d'abstention : sous ce score, l'API renvoie INDETERMINE au lieu de forcer un verdict.
# MesurÃ© avec src/courbe_seuil.py : Ã  0.60, 72 % de rÃ©ponses, exactitude 0.952, 2 erreurs.
SEUIL_ABSTENTION = 0.60

Label = Literal["POSITIVE", "NEGATIVE", "INDETERMINE"]


class PredictionAPI(TypedDict):
    """Sortie typÃ©e de SentimentClassifier.predict()."""
    label: Label
    score: float
    text: str


class SentimentClassifier:
    """Enveloppe du modÃ¨le TP2 avec l'interface attendue par l'API."""

    model_name = "tfidf-logreg (TP2, models/sentiment.joblib)"

    def __init__(self) -> None:
        charger_modele()  # Ã©choue immÃ©diatement si le joblib manque : on ne dÃ©marre pas sans modÃ¨le

    def predict(self, text: str) -> PredictionAPI:
        """Renvoie {'label': ..., 'score': ..., 'text': aperÃ§u}."""
        r = _predict(text)  # lÃ¨ve ValueError si le texte est vide
        # Correspondance explicite : mypy ne peut pas vÃ©rifier .upper()
        if r["label"] == "positive":
            label: Label = "POSITIVE"
        elif r["label"] == "negative":
            label = "NEGATIVE"
        else:
            raise ValueError(f"Ã©tiquette inconnue : {r['label']!r}")
        score = float(r["score"])
        # Abstention : le modÃ¨le n'est pas assez sÃ»r de lui
        if score < SEUIL_ABSTENTION:
            label = "INDETERMINE"
        return {"label": label, "score": score, "text": text[:100]}


def load_model() -> SentimentClassifier:
    """Construit le classifier (le cache de chargement est dans src/predict.py)."""
    return SentimentClassifier()