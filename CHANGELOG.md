# Journal des versions

Le numéro de version suit les TP : 0.N.0 à la fin du TP N. Chaque version publiée porte une étiquette Git `v0.N.0`.

## Non publié

- Fiche modèle `docs/fiche-modele.md` (TP6, étape G) : usage, données, performances, limites, biais, conditions d'usage ; testée par `tests/test_fiche_modele.py`, qui vérifie que les chiffres cités sont ceux de `models/metrics.json`.
- Explicabilité avec SHAP, `src/expliquer.py` (TP2, étape F) ; mesure des biais par groupe d'avis, `src/biais.py` (TP4, étape F) ; deux graphiques dans l'onglet fichier de la page, `ui/graphiques.py` (TP5, étape G).
- CI : pytest épinglé en 8.3 et SHAP installé ; noms des étapes et commentaires remis en UTF-8.
- Message « modèle introuvable » réécrit : il donne le chemin cherché et les deux remèdes.

## 0.6.4

- Test : `test_lot_et_resume` recharge le classifieur avant ses prédictions, pour ne plus dépendre de l'ordre des tests.

## 0.6.2 et 0.6.3

- CI : runner épinglé sur `ubuntu-24.04`, au lieu de `ubuntu-latest` qui passe à 26.04.

## 0.6.1

- Test : `app.state.classifier` est restauré après `test_modele_non_charge`, qui laissait l'API sans modèle pour les tests suivants.

## 0.6.0 (TP6) : le paquet

- **Pour celui qui installe** : l'application est une roue, `sentiment_app-0.6.0-py3-none-any.whl`. `pip install` installe aussi ses dépendances (FastAPI, uvicorn, Pydantic, scikit-learn 1.5, joblib) et fournit la commande `sentiment` : `--version`, `predict`, `serve`, `ui`. Le modèle n'est pas dans la roue : on indique son chemin dans la variable `SENTIMENT_MODELE`.
- **Pour celui qui développe** : `predict.py` est passé de `src/` au paquet `sentiment_app` par `git mv`, son historique est conservé. `api/model.py` importe `from sentiment_app.predict import ...` et ne modifie plus `sys.path`. `src/predict.py` reste comme fichier de compatibilité, pour les tests et `python src/predict.py`. La version est écrite à un seul endroit, `sentiment_app/__init__.py`. Installation en mode développement : `pip install -e .`.
- **Pour la CI** : scikit-learn est épinglé en 1.5, et une nouvelle étape construit la roue, l'installe dans un environnement neuf hors du dépôt et lance une prédiction. Six tests de packaging s'ajoutent (`tests/test_packaging.py`).

## 0.5.0 (TP5) : l'interface

- Page Streamlit : un avis, ou un fichier d'avis ; le client HTTP traduit chaque réponse de l'API.

## 0.4.0 (TP4) : tests et qualité

- Contrat d'entrée testé, abstention `INDETERMINE`, jeu d'or, tests d'intégration, contrat typé, ruff, mypy, pre-commit.

## 0.3.0 (TP3) : l'API

- FastAPI : `/health`, `/predict`, contrat Pydantic ; la CI entraîne le modèle avant les tests.

## 0.2.0 (TP2) : le modèle

- TF-IDF et régression logistique ; les métriques sont versionnées, le modèle ne l'est pas.

## 0.1.0 (TP1) : le cadrage

- Environnement Python 3.11, structure du dépôt, trois fiches de cadrage, dépôt GitHub à deux auteurs.
