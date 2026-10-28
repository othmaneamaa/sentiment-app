#!/usr/bin/env python
"""Prediction unitaire : la fonction que l'API de la semaine 3 appellera.

Usage :
  python src/predict.py "Livraison rapide, tres satisfait"
  >>> from predict import predict ; predict("texte")

Le modele est cherchable par la variable d'environnement SENTIMENT_MODELE ;
sinon, on utilise models/sentiment.joblib a la racine du depot.
"""
import os
import sys
from functools import lru_cache
from pathlib import Path
from typing import Literal, TypedDict

import joblib

RACINE = Path(__file__).resolve().parents[1]


def chemin_modele() -> Path:
    """SENTIMENT_MODELE si elle est definie, sinon le modele entraine dans le depot."""
    return Path(os.environ.get("SENTIMENT_MODELE") or RACINE / "models" / "sentiment.joblib")


MODELE = chemin_modele()


class Prediction(TypedDict):
    """Sortie typee de predict() : etiquette et confiance."""
    label: Literal["positive", "negative"]
    score: float


@lru_cache(maxsize=1)
def charger_modele():
    """Charge une seule fois par processus, pas a chaque appel."""
    if not MODELE.exists():
        raise FileNotFoundError(
            f"{MODELE} absent : lancez python src/train.py, "
            "ou definissez SENTIMENT_MODELE"
        )
    return joblib.load(MODELE)


def predict(texte: str) -> Prediction:
    """Renvoie {'label': 'positive'|'negative', 'score': float}."""
    if not isinstance(texte, str) or not texte.strip():
        raise ValueError("texte vide")
    pipeline = charger_modele()
    etiquette = pipeline.predict([texte])[0]
    score = float(pipeline.predict_proba([texte]).max())
    return {"label": etiquette, "score": round(score, 4)}


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    resultat = predict(" ".join(sys.argv[1:]))
    print(f"{resultat['label']} (confiance {resultat['score']:.0%})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())