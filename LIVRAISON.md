# Notice d'installation : sentiment-app 0.6.0

Bonjour, voici votre application d'analyse de sentiment des avis clients.

## 1. Installation

Ouvrez un terminal (Python 3.11 ou plus récent) et installez le paquet fourni :

```powershell
pip install sentiment_app-0.6.0-py3-none-any.whl
```

`pip` installe aussi les dépendances : FastAPI, uvicorn, Pydantic, scikit-learn 1.5 et joblib. Pour l'interface web, ajoutez ses dépendances :

```powershell
pip install "sentiment_app-0.6.0-py3-none-any.whl[ui]"
```

## 2. Configuration du modèle

Le paquet contient le code, mais pas le modèle d'IA, qui se met à jour sans republier le code. Indiquez le chemin du fichier `sentiment.joblib` fourni :

```powershell
$env:SENTIMENT_MODELE = "C:\chemin\vers\sentiment.joblib"
```

Sans cette variable, la commande affiche « modèle introuvable » et s'arrête.

## 3. Utilisation

- Vérifier la version : `sentiment --version`
- En ligne de commande : `sentiment predict "Votre avis ici"`
- Lancer l'API : `sentiment serve`, puis ouvrir `http://127.0.0.1:8000/health`
- Lancer l'interface web, l'API tournant dans un autre terminal : `sentiment ui`

## 4. Ce que répond l'application

`POSITIVE` ou `NEGATIVE`, avec une confiance entre 0 et 1. Sous 0.60, l'avis est marqué `INDETERMINE` : il doit être lu par une personne. Les conditions d'usage et les limites du modèle sont dans `docs/fiche-modele.md`.
