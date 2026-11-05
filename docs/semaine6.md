# Semaine 6 : le paquet, notes du binôme

> Trois questions, quelques phrases chacune. Répondez avec ce que vous avez observé.

## 1. Pourquoi le modèle n'est-il pas dans la roue ? Comment le paquet le trouve-t-il ?

Le code et le modèle n'ont pas le même cycle de vie : on réentraîne le modèle (`python src/train.py`, ou `--allocine`) sans changer une ligne de code, et on corrige le code sans réentraîner. Mettre `sentiment.joblib` dans la roue obligerait à republier le paquet à chaque entraînement, et alourdirait la roue d'un fichier binaire. Nous l'avons vérifié : la roue construite ne contient que `api`, `sentiment_app`, `ui` et ses métadonnées, ni `models`, ni `data`, ni `tests`, ni `src`.

Le paquet trouve le modèle par la fonction `chemin_modele()` de `sentiment_app/predict.py` : il lit la variable d'environnement `SENTIMENT_MODELE` et, si elle n'est pas définie, prend `models/sentiment.joblib` à la racine du dépôt. Installée ailleurs, la roue cherche donc dans `site-packages/models/sentiment.joblib`, qui n'existe pas : la commande affiche « modèle introuvable », avec le chemin cherché, et sort avec le code 1.

## 2. Qu'est-ce qui a changé dans api/model.py quand predict() est entré dans le paquet, et pourquoi est-ce mieux ?

Avant, `api/model.py` calculait la racine du dépôt, ajoutait `src/` à `sys.path`, puis importait `from predict import ...` avec deux `# noqa: E402`. Maintenant, il écrit simplement `from sentiment_app.predict import charger_modele` et `from sentiment_app.predict import predict as _predict`, et les imports `sys` et `Path` ont disparu.

C'est mieux parce que l'import ne dépend plus de l'endroit d'où l'on lance Python : il marche aussi bien dans le dépôt qu'une fois la roue installée dans `site-packages`, où il n'y a pas de dossier `src/`. ruff n'a plus d'exception à tolérer, mypy n'a plus besoin de `mypy_path = "src"` pour suivre l'import, et le test `test_l_api_ne_bricole_plus_le_chemin_de_python` le vérifie à chaque push.

## 3. La roue installée hors du dépôt : qu'a-t-il fallu lui fournir, et pourquoi scikit-learn est-il épinglé dans pyproject.toml ?

Il a suffi de lui fournir le modèle, par `SENTIMENT_MODELE`. Les dépendances, `pip` les a installées tout seul à partir des métadonnées de la roue (FastAPI, uvicorn, Pydantic, scikit-learn, joblib). Sans la variable : « modèle introuvable » et code de sortie 1 ; avec : `{"label": "POSITIVE", "score": 0.777, ...}`, le même résultat que dans le dépôt.

scikit-learn est épinglé (`scikit-learn>=1.5,<1.6`) parce qu'un modèle sauvegardé avec joblib ne se relit qu'avec la version de scikit-learn qui l'a produit. Si la CI entraîne avec une version récente (1.9) et que la roue installe la 1.5, la relecture échoue avec `AttributeError: 'LogisticRegression' object has no attribute 'multi_class'`. C'est pourquoi le paquet et la CI épinglent tous deux la 1.5 : le code et l'artefact doivent être produits et relus avec la même version.
