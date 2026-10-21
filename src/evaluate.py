#!/usr/bin/env python
"""Ã‰value le modÃ¨le sauvegardÃ© et affiche la matrice de confusion.

Usage :
  python src/evaluate.py             # sur le jeu de dÃ©monstration
  python src/evaluate.py --allocine  # sur le jeu AllocinÃ©
"""
import argparse
import sys
from pathlib import Path

import joblib
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

sys.path.insert(0, str(Path(__file__).resolve().parent))   # pour lancer depuis la racine
from train import GRAINE, MODELE, charger  # mÃªmes constantes que l'entraÃ®nement

RACINE = Path(__file__).resolve().parents[1]
ETIQUETTES = ["negative", "positive"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--allocine", action="store_true")
    args = parser.parse_args()

    if not MODELE.exists():
        raise SystemExit("ModÃ¨le absent : lancez d'abord python src/train.py")
    pipeline = joblib.load(MODELE)

    df, source = charger(args.allocine)
    # MÃªme dÃ©coupage que l'entraÃ®nement : mÃªme graine, mÃªmes proportions
    _, X_test, _, y_test = train_test_split(
        df["review"], df["label"], test_size=0.2, random_state=GRAINE, stratify=df["label"]
    )
    y_pred = pipeline.predict(X_test)

    print(f"Ã‰valuation sur {len(X_test)} avis ({source})\n")
    print(classification_report(y_test, y_pred, digits=3, zero_division=0))
    mc = confusion_matrix(y_test, y_pred, labels=ETIQUETTES)
    print("Matrice de confusion (lignes = vÃ©ritÃ©, colonnes = prÃ©diction)")
    print(f"{'':>10}{ETIQUETTES[0]:>10}{ETIQUETTES[1]:>10}")
    for nom, ligne in zip(ETIQUETTES, mc, strict=False):
        print(f"{nom:>10}{ligne[0]:>10}{ligne[1]:>10}")

    faux_negatifs = mc[1][0]
    faux_positifs = mc[0][1]
    print(f"\n{faux_positifs} nÃ©gatifs classÃ©s positifs, {faux_negatifs} positifs classÃ©s nÃ©gatifs")

    # Trois erreurs Ã  lire, pour comprendre ce que le sac de mots ne voit pas
    erreurs = [(t, v, p) for t, v, p in zip(X_test, y_test, y_pred, strict=False) if v != p]
    print(f"\n{len(erreurs)} erreurs au total. Trois exemples :")
    for texte, vrai, predit in erreurs[:3]:
        print(f"  vÃ©ritÃ©={vrai:9s} prÃ©dit={predit:9s} | {texte[:90]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
