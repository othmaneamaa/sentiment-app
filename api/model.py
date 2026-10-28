"""Raccord entre l'API et le module entraine au TP2.

L'API n'entraine rien et ne connait pas scikit-learn : elle appelle la fonction
predict() de sentiment_app/predict.py, qui charge models/sentiment.joblib une seule fois.
"""
from typing import Literal, TypedDict

from sentiment_app.predict import charger_modele
from sentiment_app.predict import predict as _predict

# Seuil d'abstention : sous ce score, l'API renvoie INDETERMINE au lieu de forcer un verdict.
# Mesure avec src/courbe_seuil.py : a 0.60, 72 % de reponses, exactitude 0.952, 2 erreurs.
SEUIL_ABSTENTION = 0.60

Label = Literal["POSITIVE", "NEGATIVE", "INDETERMINE"]


class PredictionAPI(TypedDict):
    """Sortie typee de SentimentClassifier.predict()."""
    label: Label
    score: float
    text: str


class SentimentClassifier:
    """Enveloppe du module TP2 avec l'interface attendue par l'API."""

    model_name = "tfidf-logreg (TP2, models/sentiment.joblib)"

    def __init__(self) -> None:
        charger_modele()  # echoue immediatement si le joblib manque : on ne demarre pas sans module

    def predict(self, text: str) -> PredictionAPI:
        """Renvoie {'label': ..., 'score': ..., 'text': apercu}."""
        r = _predict(text)  # leve ValueError si le texte est vide
        # Correspondance explicite : mypy ne peut pas verifier .upper()
        if r["label"] == "positive":
            label: Label = "POSITIVE"
        elif r["label"] == "negative":
            label = "NEGATIVE"
        else:
            raise ValueError(f"etiquette inconnue : {r['label']!r}")
        score = float(r["score"])
        # Abstention : le module n'est pas assez sur de lui
        if score < SEUIL_ABSTENTION:
            label = "INDETERMINE"
        return {"label": label, "score": score, "text": text[:100]}


def load_model() -> SentimentClassifier:
    """Construit le classifier (le cache de chargement est dans sentiment_app/predict.py)."""
    return SentimentClassifier()