# Compléments après le TP6 : tests de /v1, analyse par lot, Docker

Ce document décrit quatre ajouts faits après le TP6, dans l'ordre des commits.

## 1. Tests des routes /v1 et de la clé d'API

**Le constat.** Le dernier commit du TP2 a ajouté `api/v1.py` et `api/securite.py` sans tests Python.
Mesure avant le changement : `pytest --cov=api` donnait **76 %** (securite.py à 43 %, v1.py à 55 %),
sous le seuil de 95 % que la CI exige (`--cov-fail-under=95`). L'étape « Tests et couverture » échouait donc.

**Ce qui a été ajouté.** `tests/test_v1_securite.py` (aucun test fourni n'a été modifié) :

| Ce qui est vérifié | Résultat attendu |
|---|---|
| `charger_cles()` lit `cle:role`, refuse un rôle inconnu et une clé de moins de 16 caractères | dictionnaire ou `ValueError` |
| `API_KEYS` vide : personne n'entre | `{}` (fermé par défaut) |
| `.env` lu sans écraser une variable déjà définie | l'environnement gagne |
| `/v1/predict` sans clé, ou avec une clé inconnue | 401 et en-tête `WWW-Authenticate: ApiKey` |
| `/v1/predict` avec une clé client ou admin | 200 |
| Un rôle non autorisé | 403 |
| Modèle non chargé, modèle en panne | 503, 500 sans message interne |

`.env.example` montre aussi le format attendu de `API_KEYS`.

## 2. POST /v1/predict/lot

Classe plusieurs avis en un seul appel (même clé d'API que `/v1/predict`).

```json
// Requête
{"avis": ["Très satisfait, livraison rapide", "Produit cassé, à fuir", "Bof"]}

// Réponse
{"resultats": [
   {"label": "POSITIVE",    "score": 0.77, "text": "Très satisfait, livraison rapide"},
   {"label": "NEGATIVE",    "score": 0.80, "text": "Produit cassé, à fuir"},
   {"label": "INDETERMINE", "score": 0.52, "text": "Bof"}],
 "resume": {"total": 3, "POSITIVE": 1, "NEGATIVE": 1, "INDETERMINE": 1}}
```

- **Contrat** (`LotRequest` dans `api/schemas.py`) : 1 à 100 avis ; chaque avis suit la règle de `PredictRequest`
  (1 à 2000 caractères, pas uniquement des blancs). Sinon 422.
- **Même verdict qu'un appel seul** : la route appelle le même `clf.predict()`, donc le seuil d'abstention s'applique.
- **Pourquoi une limite de 100** : un lot sans limite permettrait de bloquer le serveur avec un seul appel.

## 3. GET /v1/modele

Route publique qui dit quel modèle est servi : son nom, le seuil d'abstention (`SEUIL_ABSTENTION`, 0.60) et
le contenu de `models/metrics.json` (F1, exactitude, source des données), ou `null` si le fichier manque.
Utile pour vérifier, sans lire le code, que l'API sert bien le modèle mesuré.

Tests de 2 et 3 : `tests/test_v1_lot_modele.py` (ordre des verdicts, résumé, 401, cinq cas de 422, 500, metrics absent).

## 4. Docker

- `Dockerfile` : Python 3.11, uniquement les paquets de l'API et de l'entraînement. Le modèle n'est pas versionné
  (règle 2 du cours) : l'image exécute `make_demo.py` puis `train.py` pendant sa construction, comme la CI.
  L'API tourne avec un utilisateur non root ; un `HEALTHCHECK` interroge `/v1/health`.
- `.dockerignore` : ni `.venv`, ni `.env`, ni modèle local dans l'image.
- CI : un nouveau job `docker` construit l'image, lance le conteneur, attend `/v1/health`, puis essaie
  `/v1/modele`, un lot de deux avis, et vérifie qu'un lot sans clé reçoit 401.

```bash
docker build -t sentiment-api .
docker run --rm -p 8000:8000 -e API_KEYS="une-cle-de-16-caracteres:client" sentiment-api
# puis http://localhost:8000/docs
```

## Résultats mesurés

| | Avant | Après |
|---|---|---|
| `pytest -q` | 109 passed, 1 xfailed | 138 passed, 1 xfailed |
| Couverture de `api/` | 76 % (CI rouge) | 98 % |
| `ruff check .`, `mypy api` | muets | muets |
