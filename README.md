# sentiment-app : dépôt du binôme

Application fil rouge du cours **Développement et déploiement d'applications intelligentes**.

Ce dépôt grandit chaque semaine ; la semaine 1 met en place le cadrage et l'environnement. Rien n'est jeté.

## Démarrage rapide

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
# Linux / macOS / Git Bash
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Puis vérifiez :

```bash
python scripts/check_setup.py
pytest -q
```

- `scripts/check_setup.py` : diagnostic lisible des versions, dossiers, de Git et des fiches.
- `pytest -q` : exécute les vérifications sous forme de tests.

**Au premier lancement, `pytest` affiche `3 failed, 31 passed, 4 skipped` : c'est normal.** Les trois échecs correspondent aux fiches de cadrage encore vides, et les quatre tests ignorés attendent que le dépôt Git existe. En fin de TP, la même commande affiche `38 passed`.

Les scripts `scripts/setup.sh` (Linux, macOS, Git Bash) et `scripts/setup.ps1` (Windows) automatisent l'installation et le diagnostic.

## Par où commencer

| Fichier | Quand le lire |
|---|---|
| `MARCHE-A-SUIVRE.md` | Pendant la séance : huit étapes, huit contrôles et les résultats attendus |
| `TP1-ENONCE.md` | L'énoncé du TP : objectifs, livrables et grille de notation |
| `TESTS.md` | La démarche de test en détail et les trois états de référence |
| `AIDE-GIT.md` | Les commandes Git du TP et la résolution d'un conflit |
| `DEPANNAGE.md` | Quand quelque chose échoue |
| `docs/cadrage/GRILLE-DE-DECISION.md` | Pendant la partie A, pour remplir les fiches |
| `exemples/README.md` | Après le TP, pour découvrir ce que contiendront les semaines 2 et 5 |

## Raccourcis

Sous Linux, macOS et Git Bash, le `Makefile` permet d'exécuter rapidement les commandes suivantes :

```bash
make setup          # Environnement virtuel, dépendances et diagnostic
make check          # Diagnostic seul
make test           # Exécuter les tests
make test-cadrage   # Exécuter les 12 tests des fiches
make verif URL=https://github.com/<organisation>/sentiment-app.git
make exemple-ml     # Entraîner le modèle d'exemple (facultatif)
make help           # Afficher la liste complète
```

*Remarque : les commandes `make` nécessitent un environnement compatible avec Make.*

## Structure du projet

```text
sentiment-app/
├── README.md
├── MARCHE-A-SUIVRE.md
├── TP1-ENONCE.md
├── TESTS.md
├── AIDE-GIT.md
├── DEPANNAGE.md
├── Makefile              # Raccourcis (optionnel)
├── requirements.txt      # Dépendances du semestre, versions figées
├── .gitignore
├── .env.example
├── .editorconfig
├── pytest.ini
├── .vscode/              # Interpréteur et tests préconfigurés
├── images/               # Photos des membres du binôme
├── data/                 # Jeux de données (DVC à partir de la semaine 7)
├── models/               # Modèles entraînés (jamais dans Git)
├── app/                  # API FastAPI (semaine 3)
├── ui/                   # Interface Streamlit (semaine 5)
├── tests/                # Tests pytest
├── scripts/              # Installation, diagnostic et scripts utilitaires
├── notebooks/            # Variante Colab du TP1
└── docs/
    └── cadrage/          # Fiches, exemple corrigé, grille et banque de cas
```

## Membres du binôme

| Rôle | Nom | Identifiant GitHub | Travail de la semaine 1 |
|---|---|---|---|
| Membre A | Othmane Amaadour | [@othmaneamaa](https://github.com/othmaneamaa) | Cadrage des trois cas et préparation de l'environnement |
| Membre B | Mohcine Errachid | [@mohcine00errachind](https://github.com/mohcine00errachind) | Cadrage et vérification de l'environnement |

## Photos du binôme

<p align="center">
  <img src="images/othmane.jpg" alt="Photo d'Othmane Amaadour" width="250" />
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="images/mohcine.jpg" alt="Photo de Mohcine Errachid" width="250" />
</p>

<p align="center">
  <strong><a href="https://github.com/othmaneamaa">Othmane Amaadour</a></strong>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <strong><a href="https://github.com/mohcine00errachind">Mohcine Errachid</a></strong>
</p>

---

*Projet réalisé dans le cadre du cours Développement et déploiement d'applications intelligentes.*
