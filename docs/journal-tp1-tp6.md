# Journal de bord du binÃƒÆ’Ã‚Â´me : TP1 ÃƒÆ’Ã‚Â  TP6

**Module** : DÃƒÆ’Ã‚Â©veloppement et dÃƒÆ’Ã‚Â©ploiement d'applications intelligentes Ãƒâ€šÃ‚Â· **Enseignant** : A. Larhlimi

|  | Membre A | Membre B |
| :---- | :---- | :---- |
| Nom | Othmane Amaadour | Mohcine Errachid |
| Compte GitHub | @othmaneamaa | @mohcine00errachind |

**Dépôt** : https://github.com/othmaneamaa/sentiment-app

## Comment remplir ce journal

Ce fichier se place dans votre dÃƒÆ’Ã‚Â©pÃƒÆ’Ã‚Â´t, sous `docs/journal-tp1-tp6.md`, et vos captures d'ÃƒÆ’Ã‚Â©cran dans `docs/captures/`. CrÃƒÆ’Ã‚Â©ez ce dossier une fois :

```powershell
New-Item -ItemType Directory -Force docs\captures
```

&nbsp;

AprÃƒÆ’Ã‚Â¨s chaque contrÃƒÆ’Ã‚Â´le, remplissez les quatre rubriques de son bloc :

1. **Obtenu** : collez les lignes utiles de la sortie (la derniÃƒÆ’Ã‚Â¨re ligne de pytest, le message affichÃƒÆ’Ã‚Â©), pas tout le terminal.  
2. **Conforme** : cochez la case en remplaÃƒÆ’Ã‚Â§ant `[ ]` par `[x]` si le rÃƒÆ’Ã‚Â©sultat est celui attendu.  
3. **Commentaire** : deux ou trois phrases. Ce que le rÃƒÆ’Ã‚Â©sultat montre, et, s'il diffÃƒÆ’Ã‚Â¨re de l'attendu, la cause trouvÃƒÆ’Ã‚Â©e et la correction faite.  
4. **Capture** : enregistrez l'image sous le nom exact indiquÃƒÆ’Ã‚Â© dans le bloc. Une image manquante s'affiche comme un lien cassÃƒÆ’Ã‚Â© : c'est ce qui reste ÃƒÆ’Ã‚Â  faire.

**Faire une capture sous Windows** : `Windows + Maj + S`, sÃƒÆ’Ã‚Â©lectionnez la zone (la commande et son rÃƒÆ’Ã‚Â©sultat, pas tout l'ÃƒÆ’Ã‚Â©cran), puis collez dans Paint (`Ctrl + V`) et enregistrez au format PNG dans `docs/captures/`, sous le nom demandÃƒÆ’Ã‚Â©. Dans VS Code, coller l'image directement dans ce fichier fonctionne aussi : dÃƒÆ’Ã‚Â©placez ensuite l'image crÃƒÆ’Ã‚Â©ÃƒÆ’Ã‚Â©e dans `docs/captures/` et renommez-la.

**Ne capturez jamais** un jeton d'accÃƒÆ’Ã‚Â¨s, un mot de passe ou le contenu d'un fichier `.env`.

ÃƒÆ’Ã¢â€šÂ¬ la fin de chaque TP, commitez le journal et les captures :

```powershell
git add docs/journal-tp1-tp6.md docs/captures
git commit -m "Journal : TPn complÃƒÆ’Ã‚Â©tÃƒÆ’Ã‚Â©"
git push
```

&nbsp;

---

## 0\. La prÃƒÆ’Ã‚Â©paration des postes

### Poste du membre A

```powershell
py -0
py -3.11 --version
git --version
git config --global user.name
```

&nbsp;

**Attendu** : une version 3.11 dans la liste, `Python 3.11.x`, une version de Git, le nom du membre A.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![Poste du membre A](captures/tp0-poste-membre-a.png)

### Poste du membre B

```powershell
py -0
py -3.11 --version
git --version
git config --global user.name
```

&nbsp;

**Attendu** : une version 3.11, `Python 3.11.x`, une version de Git, le nom du membre B, diffÃƒÆ’Ã‚Â©rent de celui du membre A.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![Poste du membre B](captures/tp0-poste-membre-b.png)

---

## TP1 : cadrer l'application et prÃƒÆ’Ã‚Â©parer l'environnement

### T0 Ãƒâ€šÃ‚Â· La structure du kit (membre A)

```powershell
Get-ChildItem -Force
```

&nbsp;

**Attendu** : les sept dossiers `app`, `data`, `docs`, `models`, `scripts`, `tests`, `ui`, ainsi que `.github` et `.gitignore`.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T0 : structure du kit](captures/tp1-t0-structure.png)

### T1 Ãƒâ€šÃ‚Â· L'environnement et le point de dÃƒÆ’Ã‚Â©part (membre A)

```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
python --version
pip install -r requirements.txt
python -m pip freeze | Out-File -Encoding utf8 requirements.lock
python scripts/check_setup.py
python -m pytest -q
```

&nbsp;

**Attendu** : `Python 3.11.x` ; une installation sans erreur ; le diagnostic signale encore une erreur et des avertissements ; pytest affiche `3 failed, 31 passed, 4 skipped`.

**Obtenu** (version de Python, rÃƒÆ’Ã‚Â©sumÃƒÆ’Ã‚Â© du diagnostic, derniÃƒÆ’Ã‚Â¨re ligne de pytest) :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** (que rÃƒÆ’Ã‚Â©clament les trois ÃƒÆ’Ã‚Â©checs, et pourquoi quatre tests sont ignorÃƒÆ’Ã‚Â©s ?) :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T1 : pytest au dÃƒÆ’Ã‚Â©part](captures/tp1-t1-pytest.png)

### T2 Ãƒâ€šÃ‚Â· Les fiches de cadrage (ÃƒÆ’Ã‚Â  deux)

```powershell
python -m pytest tests/test_cadrage.py -q
python -m pytest -q
```

&nbsp;

**Attendu** : `12 passed`, puis `34 passed, 4 skipped`.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** (l'approche retenue pour chacun des trois cas, et les deux critÃƒÆ’Ã‚Â¨res qui la justifient) :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T2 : fiches complÃƒÆ’Ã‚Â¨tes](captures/tp1-t2-cadrage.png)

### T3 Ãƒâ€šÃ‚Â· Le dÃƒÆ’Ã‚Â©pÃƒÆ’Ã‚Â´t GitHub et le premier push (membre A)

```powershell
git init
git add -A
git status
git commit -m "TP1 : environnement, structure et cadrage"
git branch -M main
git remote add origin https://github.com/<compte-A>/sentiment-app.git
git push -u origin main
python -m pytest -q
```

&nbsp;

**Attendu** : `git status` ne liste ni `.venv/`, ni `.env`, ni fichier `.joblib` ; aprÃƒÆ’Ã‚Â¨s le push, les fichiers apparaissent sur GitHub ; pytest affiche `37 passed, 1 failed`.

**Obtenu** (extrait de `git status`, derniÃƒÆ’Ã‚Â¨re ligne de pytest) :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** (quel test ÃƒÆ’Ã‚Â©choue encore, et pourquoi ?) :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T3 : le dÃƒÆ’Ã‚Â©pÃƒÆ’Ã‚Â´t sur GitHub](captures/tp1-t3-depot-github.png)

### T4 Ãƒâ€šÃ‚Â· L'environnement du membre B (membre B)

```powershell
git clone https://github.com/<compte-A>/sentiment-app.git sentiment-app
cd sentiment-app
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python scripts/check_setup.py
```

&nbsp;

**Attendu** : `0 erreur(s)` au diagnostic.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T4 : diagnostic du membre B](captures/tp1-t4-check-setup-b.png)

### T5 Ãƒâ€šÃ‚Â· Un commit par membre (membres B puis A)

```powershell
git pull
git add README.md
git commit -m "README : ajout de <nom> au tableau du binome"
git push
git shortlog -sn --all
python -m pytest tests/test_git_history.py -q
```

&nbsp;

**Attendu** : deux noms distincts dans `git shortlog`, puis `3 passed`.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T5 : deux auteurs](captures/tp1-t5-shortlog.png)

### T6 Ãƒâ€šÃ‚Â· La vÃƒÆ’Ã‚Â©rification finale (ÃƒÆ’Ã‚Â  deux)

```powershell
git pull
python scripts/check_setup.py
python -m pytest -q
```

&nbsp;

**Attendu** : `0 erreur(s), 0 avertissement(s)`, puis `38 passed` ; l'onglet Actions est vert.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T6 : pytest final](captures/tp1-t6-pytest.png)

![T6 : la CI verte](captures/tp1-t6-actions.png)

### T7 Ãƒâ€šÃ‚Â· Le clone frais

```powershell
cd $env:TEMP
git clone https://github.com/<compte-A>/sentiment-app.git verif
cd verif
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python scripts/check_setup.py
python -m pytest -q
```

&nbsp;

**Attendu** : `0 erreur(s)` et `38 passed`, sans aucune intervention.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** (qu'est-ce que ce contrÃƒÆ’Ã‚Â´le prouve que T6 ne prouvait pas ?) :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T7 : clone frais](captures/tp1-t7-clone-frais.png)

---

## TP2 : entraÃƒÆ’Ã‚Â®ner, ÃƒÆ’Ã‚Â©valuer et sauvegarder le modÃƒÆ’Ã‚Â¨le

### C1 Ãƒâ€šÃ‚Â· Le kit installÃƒÆ’Ã‚Â© (membre A)

```powershell
python C:\IA-DEV\tp2-semaine2\appliquer_tp2.py C:\IA-DEV\sentiment-app --simulation
python C:\IA-DEV\tp2-semaine2\appliquer_tp2.py C:\IA-DEV\sentiment-app
python -m pytest -q
```

&nbsp;

**Attendu** : la simulation liste les fichiers du kit et l'ajout de `!models/metrics.json` au `.gitignore` ; pytest affiche `2 failed, 38 passed, 2 skipped`.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** (que rÃƒÆ’Ã‚Â©clament les deux ÃƒÆ’Ã‚Â©checs ?) :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![C1 : point de dÃƒÆ’Ã‚Â©part du TP2](captures/tp2-c1-pytest.png)

### C2 Ãƒâ€šÃ‚Â· Le jeu de dÃƒÆ’Ã‚Â©monstration

```powershell
python src/make_demo.py
```

&nbsp;

**Attendu** : `290 avis ÃƒÆ’Ã‚Â©crits`, 145 positifs et 145 nÃƒÆ’Ã‚Â©gatifs.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** (recopiez un avis mitigÃƒÆ’Ã‚Â© et expliquez sa structure) :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![C2 : jeu de dÃƒÆ’Ã‚Â©monstration](captures/tp2-c2-make-demo.png)

### C3 Ãƒâ€šÃ‚Â· L'entraÃƒÆ’Ã‚Â®nement

```powershell
python src/train.py
git status --short
```

&nbsp;

**Attendu** : `Vocabulaire : 316 termes`, `F1 macro sur le jeu de test : 0.879 (seuil 0.85)` ; dans `git status`, `models/metrics.json` apparaÃƒÆ’Ã‚Â®t, ni `models/sentiment.joblib` ni `data/demo_reviews.csv`.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** (pourquoi la mesure est-elle versionnÃƒÆ’Ã‚Â©e, et pas le modÃƒÆ’Ã‚Â¨le ?) :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![C3 : entraÃƒÆ’Ã‚Â®nement](captures/tp2-c3-train.png)

### C4 Ãƒâ€šÃ‚Â· L'ÃƒÆ’Ã‚Â©valuation

```powershell
python src/evaluate.py
```

&nbsp;

**Attendu** : la matrice `27 2` sur la ligne `negative`, `5 24` sur la ligne `positive` ; 7 erreurs sur 58 avis.

**Obtenu** (la matrice et les trois erreurs affichÃƒÆ’Ã‚Â©es) :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** (pourquoi le modÃƒÆ’Ã‚Â¨le se trompe-t-il sur ces avis ?) :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![C4 : matrice de confusion](captures/tp2-c4-evaluate.png)

### C5 Ãƒâ€šÃ‚Â· Le vrai jeu de donnÃƒÆ’Ã‚Â©es, les tests, le push

```powershell
python src/train.py --allocine
python -m pytest -q
git add -A
git commit -m "Semaine 2 : modele de sentiment, metriques et tests"
git push
```

&nbsp;

**Attendu** : `Source : allocine, 20000 avis`, `F1 macro sur le jeu de test : 0.920`, puis `42 passed` ; l'onglet Actions est vert.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** (pourquoi le F1 est-il meilleur sur AllocinÃƒÆ’Ã‚Â© ?) :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![C5 : AllocinÃƒÆ’Ã‚Â© et tests](captures/tp2-c5-allocine.png)

### Membre B, aprÃƒÆ’Ã‚Â¨s le TP2

```powershell
git pull
python src/make_demo.py
python src/train.py
python -m pytest -q
```

&nbsp;

**Attendu** : `42 passed`.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

![TP2 : poste du membre B](captures/tp2-membre-b.png)

> Les rÃƒÆ’Ã‚Â©sultats attendus de chaque contrÃƒÆ’Ã‚Â´le, les sept erreurs du jeu de dÃƒÆ’Ã‚Â©monstration, un exemple de `docs/semaine2.md` et la fin du TP2 (push, CI, part du membre B) sont dÃƒÆ’Ã‚Â©taillÃƒÆ’Ã‚Â©s dans l'**annexe B**, ÃƒÆ’Ã‚Â  la fin de ce journal. Le script d'entraÃƒÆ’Ã‚Â®nement, `src/train.py`, est expliquÃƒÆ’Ã‚Â© pas ÃƒÆ’Ã‚Â  pas dans l'**annexe C**.

---

## TP3 : exposer le modÃƒÆ’Ã‚Â¨le par une API

### T14 Ãƒâ€šÃ‚Â· Le kit installÃƒÆ’Ã‚Â© (membre A)

```powershell
python C:\IA-DEV\kit-tp3\appliquer_tp3.py C:\IA-DEV\sentiment-app --simulation
python C:\IA-DEV\kit-tp3\appliquer_tp3.py C:\IA-DEV\sentiment-app
pip install -r requirements.txt
python src/train.py
python -m pytest -q
```

&nbsp;

**Attendu** : la simulation liste les fichiers copiÃƒÆ’Ã‚Â©s et les complÃƒÆ’Ã‚Â©ments de `pytest.ini` et de `ci.yml` ; pytest affiche `48 passed`.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** (pourquoi rÃƒÆ’Ã‚Â©entraÃƒÆ’Ã‚Â®ner sur le jeu de dÃƒÆ’Ã‚Â©monstration avant les tests ?) :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T14 : 48 tests verts](captures/tp3-t14-pytest.png)

### T15 Ãƒâ€šÃ‚Â· `/health`

```powershell
uvicorn api.main:app --reload
```

&nbsp;

Puis, dans `http://localhost:8000/docs` : `GET /health`, Ãƒâ€šÃ‚Â« Try it out Ãƒâ€šÃ‚Â», Ãƒâ€šÃ‚Â« Execute Ãƒâ€šÃ‚Â».

**Attendu** : `200`, `"status": "OK"`, `"model": "tfidf-logreg (TP2, models/sentiment.joblib)"`.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T15 : health dans /docs](captures/tp3-t15-health.png)

### T16 Ãƒâ€šÃ‚Â· Un avis positif

`POST /predict` avec `{"text": "Livraison rapide, produit conforme, trÃƒÆ’Ã‚Â¨s satisfait"}`.

**Attendu** : `200`, `"label": "POSITIVE"`, `"score": 0.777`.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T16 : avis positif](captures/tp3-t16-positif.png)

Facultatif, la mÃƒÆ’Ã‚Âªme requÃƒÆ’Ã‚Âªte en ligne de commande (API lancÃƒÆ’Ã‚Â©e dans un autre terminal) :

```powershell
python -c "import httpx; r = httpx.post('http://127.0.0.1:8000/predict', json={'text': 'Livraison rapide, produit conforme, trÃƒÆ’Ã‚Â¨s satisfait'}); print(r.status_code, r.json())"
```

&nbsp;

### T17 Ãƒâ€šÃ‚Â· Un avis nÃƒÆ’Ã‚Â©gatif

`POST /predict` avec `{"text": "Produit cassÃƒÆ’Ã‚Â© et service injoignable, ÃƒÆ’Ã‚Â  fuir"}`.

**Attendu** : `200`, `"label": "NEGATIVE"`, `"score": 0.7465`.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T17 : avis nÃƒÆ’Ã‚Â©gatif](captures/tp3-t17-negatif.png)

### T18 Ãƒâ€šÃ‚Â· Les refus

`POST /predict` avec `{"text": ""}`, puis `{}`, puis `{"text": 42}`.

**Attendu** : `422` dans les trois cas.

**Obtenu** (le code et le `detail` de chaque rÃƒÆ’Ã‚Â©ponse) :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** (que dit `detail`, et pourquoi 422 plutÃƒÆ’Ã‚Â´t que 500 ?) :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T18 : un refus 422](captures/tp3-t18-refus.png)

### T19 Ãƒâ€šÃ‚Â· La CI

```powershell
git add -A
git commit -m "Semaine 3 : API FastAPI"
git push
```

&nbsp;

**Attendu** : dans l'onglet Actions, l'ÃƒÆ’Ã‚Â©tape Ãƒâ€šÃ‚Â« ModÃƒÆ’Ã‚Â¨le de dÃƒÆ’Ã‚Â©monstration, pour les tests de l'API (TP3) Ãƒâ€šÃ‚Â» passe, puis l'ÃƒÆ’Ã‚Â©tape Ãƒâ€šÃ‚Â« Tests Ãƒâ€šÃ‚Â» affiche `48 passed`.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** (pourquoi la CI doit-elle entraÃƒÆ’Ã‚Â®ner le modÃƒÆ’Ã‚Â¨le ?) :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T19 : la CI du TP3](captures/tp3-t19-actions.png)

### T20 Ãƒâ€šÃ‚Â· L'API sans modÃƒÆ’Ã‚Â¨le

```powershell
Rename-Item models/sentiment.joblib sentiment.bak
uvicorn api.main:app
Rename-Item models/sentiment.bak sentiment.joblib
```

&nbsp;

**Attendu** : `FileNotFoundError: models/sentiment.joblib absent : lancez python src/train.py`, puis `Application startup failed`.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T20 : refus de dÃƒÆ’Ã‚Â©marrer](captures/tp3-t20-sans-modele.png)

### Membre B, aprÃƒÆ’Ã‚Â¨s le TP3

```powershell
git pull
python src/make_demo.py
python src/train.py
python -m pytest -q
```

&nbsp;

**Attendu** : `48 passed`.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

![TP3 : poste du membre B](captures/tp3-membre-b.png)

> Les contrÃƒÆ’Ã‚Â´les T15 ÃƒÆ’Ã‚Â  T20 sont expliquÃƒÆ’Ã‚Â©s en dÃƒÆ’Ã‚Â©tail dans l'**annexe D**, ÃƒÆ’Ã‚Â  la fin de ce journal : ce qui se passe dans l'API ÃƒÆ’Ã‚Â  chaque essai, les rÃƒÆ’Ã‚Â©ponses exactes attendues, et pourquoi. La structure de la page `/docs` et une liste de vingt essais ÃƒÆ’Ã‚Â  y faire sont dans l'**annexe E**.

---

## TP4 : tests approfondis et qualitÃƒÆ’Ã‚Â©

### T21 Ãƒâ€šÃ‚Â· Le kit installÃƒÆ’Ã‚Â© et le point de dÃƒÆ’Ã‚Â©part (membre A)

```powershell
python C:\IA-DEV\tp4-tests-qualite\appliquer_tp4.py C:\IA-DEV\sentiment-app
pip install -r requirements-dev.txt
python src/train.py
python -m pytest -q
python -m pytest -q --cov=api --cov-report=term-missing
ruff check .
mypy api
```

&nbsp;

**Attendu** : `1 failed, 51 passed, 1 skipped` ; couverture de `api/` ÃƒÆ’Ã‚Â  91 % ; quelques remarques de ruff ; mypy `Success: no issues found in 4 source files`.

**Obtenu** (derniÃƒÆ’Ã‚Â¨re ligne de pytest, ligne `TOTAL`, nombre de remarques de ruff, sortie de mypy) :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** (ÃƒÆ’Ã‚Â  quels comportements de l'API correspondent les lignes non couvertes ?) :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T21 : couverture de dÃƒÆ’Ã‚Â©part](captures/tp4-t21-couverture.png)

### T22 Ãƒâ€šÃ‚Â· Le contrat d'entrÃƒÆ’Ã‚Â©e corrigÃƒÆ’Ã‚Â©

Avant la correction du schÃƒÆ’Ã‚Â©ma :

```powershell
python -m pytest -q tests/test_limites.py
```

&nbsp;

**Attendu avant correction** : `2 failed, 8 passed`, et un contre-exemple d'hypothesis sous Ãƒâ€šÃ‚Â« Falsifying example Ãƒâ€šÃ‚Â».

**Obtenu avant correction** (derniÃƒÆ’Ã‚Â¨re ligne et contre-exemple) :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

AprÃƒÆ’Ã‚Â¨s la correction, dans `/docs` : `POST /predict` avec `{"text": "   "}`.

**Attendu aprÃƒÆ’Ã‚Â¨s correction** : `422`, avec un `detail` en liste, comme pour `{"text": ""}`.

**Obtenu aprÃƒÆ’Ã‚Â¨s correction** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** (pourquoi deux formes de 422 posaient problÃƒÆ’Ã‚Â¨me, et quel caractÃƒÆ’Ã‚Â¨re hypothesis a trouvÃƒÆ’Ã‚Â©) :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T22 : refus des espaces](captures/tp4-t22-espaces.png)

### T23 Ãƒâ€šÃ‚Â· Les propriÃƒÆ’Ã‚Â©tÃƒÆ’Ã‚Â©s

```powershell
python -m pytest -q tests/test_limites.py
python -m pytest -q tests/test_limites.py
python -m pytest -q tests/test_limites.py
```

&nbsp;

**Attendu** : `10 passed`, trois fois de suite.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T23 : propriÃƒÆ’Ã‚Â©tÃƒÆ’Ã‚Â©s vertes](captures/tp4-t23-proprietes.png)

### T24 Ãƒâ€šÃ‚Â· L'abstention

```powershell
python src/courbe_seuil.py
```

&nbsp;

**Attendu** : la premiÃƒÆ’Ã‚Â¨re ligne `0.50  58  100%  0.879  7  0`. Dans `/docs`, un texte fait de mots inventÃƒÆ’Ã‚Â©s reÃƒÆ’Ã‚Â§oit ensuite `INDETERMINE`.

**Obtenu** (deux ou trois lignes de la courbe, puis la rÃƒÆ’Ã‚Â©ponse au texte inventÃƒÆ’Ã‚Â©) :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** (le seuil retenu, combien d'avis partent vers un humain, combien d'erreurs sont ÃƒÆ’Ã‚Â©vitÃƒÆ’Ã‚Â©es) :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T24 : courbe du seuil](captures/tp4-t24-courbe.png)

![T24 : verdict INDETERMINE](captures/tp4-t24-indetermine.png)

### T25 Ãƒâ€šÃ‚Â· Le jeu d'or

```powershell
python src/bilan_jeu_or.py
python -m pytest -q tests/test_jeu_or.py
```

&nbsp;

**Attendu** : le bilan des 20 avis ; aucun `failed`, les erreurs dÃƒÆ’Ã‚Â©clarÃƒÆ’Ã‚Â©es en `xfailed`.

**Obtenu** (la ligne de bilan, puis la derniÃƒÆ’Ã‚Â¨re ligne de pytest) :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** (ce que les abstentions et les erreurs dÃƒÆ’Ã‚Â©clarÃƒÆ’Ã‚Â©es disent du modÃƒÆ’Ã‚Â¨le) :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T25 : bilan du jeu d'or](captures/tp4-t25-jeu-or.png)

### T26 Ãƒâ€šÃ‚Â· L'intÃƒÆ’Ã‚Â©gration et la couverture

```powershell
python -m pytest -q tests/test_integration.py
python -m pytest -q --cov=api --cov-report=term-missing --cov-fail-under=95
```

&nbsp;

**Attendu** : avant la correction de `main.py`, la panne `ValueError` reÃƒÆ’Ã‚Â§oit 422 ; aprÃƒÆ’Ã‚Â¨s, toute panne rÃƒÆ’Ã‚Â©pond 500 et la sortie se termine par `Required test coverage of 95% reached`.

**Obtenu** (le test qui ÃƒÆ’Ã‚Â©chouait avant la correction, puis la couverture finale) :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** (pourquoi une panne du modÃƒÆ’Ã‚Â¨le doit-elle rÃƒÆ’Ã‚Â©pondre 500, et pas 422 ?) :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T26 : couverture finale](captures/tp4-t26-couverture.png)

### T27 Ãƒâ€šÃ‚Â· QualitÃƒÆ’Ã‚Â© statique, crochet et CI

```powershell
mypy api
ruff check .
python -m pytest -q
pre-commit install
```

&nbsp;

**Attendu** : mypy signale `.upper()` une fois les types prÃƒÆ’Ã‚Â©cisÃƒÆ’Ã‚Â©s, puis `Success: no issues found in 4 source files` aprÃƒÆ’Ã‚Â¨s la correspondance explicite ; `All checks passed!` ; aucun `failed` ; un commit fautif refusÃƒÆ’Ã‚Â© par le crochet ; l'onglet Actions vert avec les ÃƒÆ’Ã‚Â©tapes ruff, mypy et Ãƒâ€šÃ‚Â« Tests et couverture Ãƒâ€šÃ‚Â».

**Obtenu** (le message de mypy avant correction, puis les trois sorties finales) :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** (parmi les dÃƒÆ’Ã‚Â©fauts trouvÃƒÆ’Ã‚Â©s au TP4, combien ruff et mypy avaient-ils signalÃƒÆ’Ã‚Â©s au dÃƒÆ’Ã‚Â©part ?) :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T27 : commit refusÃƒÆ’Ã‚Â© par pre-commit](captures/tp4-t27-pre-commit.png)

![T27 : la CI du TP4](captures/tp4-t27-actions.png)

### Membre B, aprÃƒÆ’Ã‚Â¨s le TP4

```powershell
git pull
pip install -r requirements-dev.txt
python src/train.py
pre-commit install
python -m pytest -q
```

&nbsp;

**Attendu** : aucun `failed`.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

![TP4 : poste du membre B](captures/tp4-membre-b.png)

> Ce que sont `ruff` et `mypy`, ce que chacun vÃƒÆ’Ã‚Â©rifie et pourquoi ils figurent dans la CI sont expliquÃƒÆ’Ã‚Â©s dans l'**annexe F**, ÃƒÆ’Ã‚Â  la fin de ce journal.

---

## TP5 : l'interface Streamlit

### T28 Ãƒâ€šÃ‚Â· Le kit installÃƒÆ’Ã‚Â© (membre A)

```powershell
python C:\IA-DEV\tp5-interface\appliquer_tp5.py C:\IA-DEV\sentiment-app --simulation
python C:\IA-DEV\tp5-interface\appliquer_tp5.py C:\IA-DEV\sentiment-app
python src/train.py
python -m pytest -q
```

&nbsp;

**Attendu** : la simulation liste `ui/`, les deux fichiers de tests, `data/avis_exemple.csv` et `docs/semaine5.md`, puis les complÃƒÆ’Ã‚Â©ments du `.gitignore` et de la CI ; pytest n'affiche aucun `failed`, avec douze tests de plus qu'ÃƒÆ’Ã‚Â  la fin du TP4.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** (que vÃƒÆ’Ã‚Â©rifient les tests du client, et ceux de la page ?) :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T28 : tests du TP5](captures/tp5-t28-pytest.png)

### T29 Ãƒâ€šÃ‚Â· La page ouverte, l'API prÃƒÆ’Ã‚Âªte

Deux terminaux, dans le dÃƒÆ’Ã‚Â©pÃƒÆ’Ã‚Â´t :

```powershell
uvicorn api.main:app --reload
```

&nbsp;

```powershell
streamlit run ui/app.py
```

&nbsp;

**Attendu** : la page s'ouvre sur `http://localhost:8501` et affiche `API prÃƒÆ’Ã‚Âªte : tfidf-logreg (TP2, models/sentiment.joblib)`.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T29 : la page ouverte](captures/tp5-t29-page.png)

### T30 Ãƒâ€šÃ‚Â· Les verdicts

Analysez Ãƒâ€šÃ‚Â« Livraison rapide, produit conforme, trÃƒÆ’Ã‚Â¨s satisfait Ãƒâ€šÃ‚Â», puis Ãƒâ€šÃ‚Â« Produit cassÃƒÆ’Ã‚Â© et service injoignable, ÃƒÆ’Ã‚Â  fuir Ãƒâ€šÃ‚Â».

**Attendu** : Avis positif, 78 % ; puis Avis nÃƒÆ’Ã‚Â©gatif, 75 %.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** (d'oÃƒÆ’Ã‚Â¹ viennent ces pourcentages ?) :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T30 : avis positif](captures/tp5-t30-positif.png)

![T30 : avis nÃƒÆ’Ã‚Â©gatif](captures/tp5-t30-negatif.png)

### T31 Ãƒâ€šÃ‚Â· L'abstention

Analysez Ãƒâ€šÃ‚Â« xqzvb wlkptr grombu Ãƒâ€šÃ‚Â».

**Attendu** : Ãƒâ€šÃ‚Â« Je ne sais pas : ÃƒÆ’Ã‚Â  faire vÃƒÆ’Ã‚Â©rifier par un humain Ãƒâ€šÃ‚Â», 52 %, et le message sur le seuil d'abstention.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** (pourquoi cet affichage vaut-il mieux qu'un verdict forcÃƒÆ’Ã‚Â© ?) :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T31 : je ne sais pas](captures/tp5-t31-abstention.png)

### T32 Ãƒâ€šÃ‚Â· Les erreurs

Analysez trois espaces. ArrÃƒÆ’Ã‚Âªtez ensuite l'API (`Ctrl+C` dans son terminal), rechargez la page, puis relancez l'API.

**Attendu** : l'avertissement Ãƒâ€šÃ‚Â« Texte refusÃƒÆ’Ã‚Â© Ãƒâ€šÃ‚Â» ; puis, l'API arrÃƒÆ’Ã‚ÂªtÃƒÆ’Ã‚Â©e, Ãƒâ€šÃ‚Â« API injoignable : lancez d'abord uvicorn api.main:app Ãƒâ€šÃ‚Â».

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** (quelle rÃƒÆ’Ã‚Â©ponse de l'API se cache derriÃƒÆ’Ã‚Â¨re chaque message ?) :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T32 : texte refusÃƒÆ’Ã‚Â©](captures/tp5-t32-refus.png)

![T32 : API injoignable](captures/tp5-t32-injoignable.png)

### T33 Ãƒâ€šÃ‚Â· Un fichier d'avis

Onglet Ãƒâ€šÃ‚Â« Un fichier d'avis Ãƒâ€šÃ‚Â», fichier `data/avis_exemple.csv`, puis Ãƒâ€šÃ‚Â« TÃƒÆ’Ã‚Â©lÃƒÆ’Ã‚Â©charger les rÃƒÆ’Ã‚Â©sultats Ãƒâ€šÃ‚Â».

**Attendu** : un tableau de six avis ; le rÃƒÆ’Ã‚Â©sumÃƒÆ’Ã‚Â© `{'INDETERMINE': 1, 'NEGATIVE': 2, 'POSITIVE': 3}` ; un fichier `resultats.csv` tÃƒÆ’Ã‚Â©lÃƒÆ’Ã‚Â©chargÃƒÆ’Ã‚Â©.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** (combien d'avis partent vers un humain, et lesquels ?) :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T33 : le lot d'avis](captures/tp5-t33-lot.png)

### T34 Ãƒâ€šÃ‚Â· Compte rendu, push, CI

```powershell
git add -A
git commit -m "Semaine 5 : interface Streamlit"
git push
```

&nbsp;

**Attendu** : `docs/semaine5.md` complÃƒÆ’Ã‚Â©tÃƒÆ’Ã‚Â© ; l'onglet Actions vert, Streamlit installÃƒÆ’Ã‚Â© par la CI et les douze tests du TP5 rejouÃƒÆ’Ã‚Â©s.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

**Commentaire** :

> ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter.

![T34 : la CI du TP5](captures/tp5-t34-actions.png)

### Membre B, aprÃƒÆ’Ã‚Â¨s le TP5

```powershell
git pull
python src/train.py
python -m pytest -q
streamlit run ui/app.py
```

&nbsp;

**Attendu** : aucun `failed`, puis la page Ãƒâ€šÃ‚Â« API prÃƒÆ’Ã‚Âªte Ãƒâ€šÃ‚Â» une fois l'API lancÃƒÆ’Ã‚Â©e.

**Obtenu** :

```
ÃƒÆ’Ã¢â€šÂ¬ complÃƒÆ’Ã‚Â©ter
```

- [ ] Conforme

![TP5 : poste du membre B](captures/tp5-membre-b.png)

---

## TP6 : packager l'application

### T35 · Le kit installé (membre A)

```powershell
python -m pytest -q
```

**Attendu** : 2 failed, voulus : `test_le_modele_se_place_ou_l_on_veut` et `test_l_api_ne_bricole_plus_le_chemin_de_python`

**Obtenu** :

```
2 failed, 100 passed, 1 xfailed
FAILED tests/test_packaging.py::test_l_api_ne_bricole_plus_le_chemin_de_python
FAILED tests/test_packaging.py::test_le_modele_se_place_ou_l_on_veut
```

- [x] Conforme

**Commentaire** :

> Les deux échecs sont attendus. Le premier réclame que le modèle ait un emplacement configurable (`SENTIMENT_MODELE`) ; le second que l'API n'utilise plus `sys.path` pour trouver le paquet.

![T35](captures/tp6-t35-pytest.png)

### T36 · predict.py dans le paquet

```powershell
git mv src/predict.py sentiment_app/predict.py
python -m pytest -q
python src/predict.py "Livraison rapide, produit conforme, très satisfait"
```

**Attendu** : 1 failed ; `positive (confiance 78%)`

**Obtenu** :

```
1 failed, 101 passed, 1 xfailed
positive (confiance 78%)
```

- [x] Conforme

**Commentaire** :

> `git mv` a déplacé `src/predict.py` dans `sentiment_app/predict.py`. Le fichier de compatibilité `src/predict.py` redirige les anciens imports (`import predict`) vers le paquet, pour que les tests du TP2 et du TP4 continuent de fonctionner. La commande `python src/predict.py "..."` affiche toujours `positive (confiance 78%)`.

![T36](captures/tp6-t36-deplacement.png)

### T37 · L'API branchée sur le paquet

```powershell
python -m pytest -q
Select-String -Path api\*.py -Pattern "sys.path"
ruff check .
mypy api
```

**Attendu** : aucun failed ; `Select-String` ne trouve rien ; ruff et mypy muets

**Obtenu** :

```
102 passed, 1 xfailed
ruff check . : All checks passed!
mypy api : Success: no issues found in 4 source files
```

- [x] Conforme

**Commentaire** :

> `api/model.py` importe désormais `from sentiment_app.predict import charger_modele, predict as _predict`, sans plus modifier `sys.path`. Le test `test_l_api_ne_bricole_plus_le_chemin_de_python` passe, et `Select-String` ne trouve plus `sys.path` dans `api/`.

![T37](captures/tp6-t37-api.png)

### T38 · La commande sentiment

```powershell
pip install -e .
sentiment --version
sentiment predict "Livraison rapide, produit conforme, très satisfait"
sentiment predict "xqzvb wlKptr grombub"
```

**Attendu** : `sentiment-app 0.6.0` ; `POSITIVE` 0.777 ; `INDETERMINE` 0.5162

**Obtenu** :

```
sentiment-app 0.6.0
{"label": "POSITIVE", "score": 0.777, "text": "Livraison rapide, produit conforme, très satisfait"}
{"label": "INDETERMINE", "score": 0.5162, "text": "xqzvb wlKptr grombub"}
```

- [x] Conforme

**Commentaire** :

> `pip install -e .` installe le paquet en mode éditable et crée la commande `sentiment`. `sentiment predict` passe par `api/model.py`, donc le seuil d'abstention s'applique : `xqzvb wlKptr grombub` reçoit `INDETERMINE`. `sentiment serve` lance l'API et `/health` répond `OK`.

![T38](captures/tp6-t38-commande.png)

### T39 · La roue

```powershell
Remove-Item -Recurse -Force dist -ErrorAction SilentlyContinue
python -m build --wheel
```

**Attendu** : `sentiment_app-0.6.0-py3-none-any.whl`, avec `api`, `sentiment_app`, `ui` seulement

**Obtenu** :

```
Successfully built sentiment_app-0.6.0-py3-none-any.whl
```

La roue contient `api/`, `sentiment_app/`, `ui/` et `sentiment_app-0.6.0.dist-info/`, mais ni `tests/`, ni `data/`, ni `models/`, ni `src/`.

- [x] Conforme

**Commentaire** :

> La roue ne contient que le code et les métadonnées. Ni les tests, ni les données, ni le modèle n'y sont : les tests ne servent pas en production, les données sont fournies par l'utilisateur, et le modèle est trop lourd pour un paquet.

![T39](captures/tp6-t39-roue.png)

### T40 · La roue hors du dépôt

```powershell
cd $env:TEMP
$env:SENTIMENT_MODELE = "C:\Users\Lenovo\Desktop\IA-DEV-2\Tp1\Tp1\sentiment-app\sentiment-app\models\sentiment.joblib"
```

**Attendu** : sans la variable : « modèle introuvable », code 1 ; avec : `POSITIVE` 0.777

**Obtenu** :

```
C:\Users\Lenovo\AppData\Local\Temp\roue\Lib\site-packages\models\sentiment.joblib absent : lancez python src/train.py, ou definissez SENTIMENT_MODELE
{"label": "POSITIVE", "score": 0.777, "text": "Livraison rapide, produit conforme, très satisfait"}
{"label": "INDETERMINE", "score": 0.5162, "text": "xqzvb wlKptr grombub"}
```

- [x] Conforme

**Commentaire** :

> Sans `SENTIMENT_MODELE`, la roue ne trouve pas le modèle : elle échoue avec un code 1. Avec la variable, elle fonctionne et renvoie `POSITIVE 0.777`. La roue a installé seule les dépendances (`fastapi`, `uvicorn`, `pydantic`, `scikit-learn`), mais le modèle doit être fourni.

![T40](captures/tp6-t40-ailleurs.png)

### T41 · Version, étiquette, push

```powershell
git add docs/journal-tp1-tp6.md docs/captures
git commit -m "TP6 : paquet sentiment_app 0.6.0, commande sentiment, roue testee hors depot"
git push origin main
git tag -a v0.6.0 -m "TP6 : paquet installable"
git push origin v0.6.0
```

**Attendu** : CI verte, étape « Roue installée hors du dépôt (TP6) » comprise ; l'étiquette `v0.6.0` visible sur GitHub

**Obtenu** :

```
[main a19d2d7] TP6 : paquet sentiment_app 0.6.0, commande sentiment, roue testee hors depot
To ssh://ssh.github.com:443/othmaneamaa/sentiment-app.git
11de69c..a19d2d7 main -> main

[new tag] v0.6.0 -> v0.6.0
```

CI verte (run #35) : `succeeded in 1m 11s`, toutes les étapes passent, y compris « Roue installée hors du dépôt (TP6) » qui affiche `{"label": "POSITIVE", "score": 0.7087, ...}`.

- [x] Conforme

**Commentaire** :

> La CI est verte sur le dernier run. L'étiquette `v0.6.0` est poussée et visible sur GitHub. Le score 0.7087 (au lieu de 0.777) vient de l'absence d'accents dans le texte envoyé par la CI (`tres satisfait`), ce n'est pas bloquant.

![T41](captures/tp6-t41-actions.png)

### Membre B, après le TP6

```powershell
git pull
pip install -e .
python -m pytest -q
sentiment --version
```

**Attendu** : aucun `failed`, puis `sentiment-app 0.6.0`.

**Obtenu** :

```
103 passed, 1 xfailed
sentiment-app 0.6.0
```

- [x] Conforme

**Commentaire** :

> Le membre B récupère les changements, installe le paquet en mode éditable, puis vérifie que les tests passent et que la commande répond `sentiment-app 0.6.0`. Le dépôt fonctionne pour les deux membres.

![TP6 : poste du membre B](captures/tp6-membre-b.png)

> Les commandes de ce TP, leurs notions prÃƒÆ’Ã‚Â©alables et les points d'attention (ordre de T36, paquet `build`) sont expliquÃƒÆ’Ã‚Â©s dans l'**annexe H**, ÃƒÆ’Ã‚Â  la fin de ce journal.

---

## Les difficultés rencontrées

Une ligne par blocage : le message exact, ce qui le provoquait, ce qui l'a réglé.

| TP | Commande | Message | Cause | Solution |
| :---- | :---- | :---- | :---- | :---- |
| TP6 | `git push` | `Could not resolve host: github.com` | DNS bloqué par le réseau | Passage en SSH sur le port 443 (`ssh://git@ssh.github.com:443/...`) |
| TP6 | `python -m pytest -q` | `ModuleNotFoundError: No module named 'build'` | `build` installé hors du `.venv` | `pip install build` dans le `.venv` |
| TP6 | `test_lot_et_resume` | `{'REFUS OU ERREUR': 3}` | Test partagé avec un autre test qui met `classifier = None` | `test_lot_et_resume` recharge `load_model()` |
| TP6 | CI | `Process completed with exit code 1` | `ubuntu-latest` migré vers Ubuntu 26.04 | Épingler `runs-on: ubuntu-24.04` |

## La répartition du travail

| TP | Ce qu'a fait le membre A | Ce qu'a fait le membre B |
| :---- | :---- | :---- |
| TP1 | Environnement, fiches, dépôt GitHub, premier push | Clone, environnement, commit README |
| TP2 | Kit, make_demo, train, evaluate | git pull, réentraînement, analyse des erreurs |
| TP3 | Kit, API, tests | git pull, réentraînement, essais API |
| TP4 | Contrat, abstention, intégration, ruff/mypy | Étapes D et E, jeu d'or |
| TP5 | Kit, page, essais T29 à T31 | Essais T32, T33, analyse du fichier |
| TP6 | Kit, predict.py, API, commande, roue | git pull, pip install -e ., sentiment --version |

## Le bilan

**TP1** : cadrage de l'application et mise en place de l'environnement (Python 3.11, venv, diagnostic initial avec 3 failed / 31 passed / 4 skipped).

**TP2** : kit de démarrage, génération du jeu de démo, entraînement du modèle TF-IDF + régression logistique, évaluation.

**TP3** : restructuration en paquet, API FastAPI, premiers tests d'endpoints.

**TP4** : contrat d'entrée/sortie, seuil d'abstention, intégration continue, ruff et mypy propres, jeu d'or de référence.

**TP5** : page d'interface, essais T29 à T33, analyse du fichier de données.

**TP6** : le dépôt devient un paquet installable `sentiment_app 0.6.0` avec la commande `sentiment` (`--version`, `predict`, `serve`) et une roue `.whl` testée hors du dépôt. Le modèle n'est pas dans la roue : il est trouvé via `SENTIMENT_MODELE`. La CI vérifie tout, y compris la roue, et l'étiquette `v0.6.0` fige la version remise.

---

## Annexe A : comprendre tests/test\_cadrage.py

Ce fichier contient les douze tests qui vÃƒÆ’Ã‚Â©rifient les trois fiches de cadrage du TP1 (contrÃƒÆ’Ã‚Â´le T2). Pour l'afficher : `Get-Content tests\test_cadrage.py`. Il comprend deux constantes, deux fonctions outils, utilisÃƒÆ’Ã‚Â©es par les tests, et cinq tests, que pytest reconnaÃƒÆ’Ã‚Â®t parce que leur nom commence par `test_`.

### Les constantes

```py
REQUIRED_SECTIONS = [
    "Besoin en une phrase",
    "Utilisateur final",
    "Approche retenue",
    "Justification",
    "DonnÃƒÆ’Ã‚Â©es nÃƒÆ’Ã‚Â©cessaires",
    "MÃƒÆ’Ã‚Â©trique de succÃƒÆ’Ã‚Â¨s",
    "ConsÃƒÆ’Ã‚Â©quence d'une erreur",
    "Risques ÃƒÆ’Ã‚Â©thiques",
]
CRITERIA = ["(a)", "(b)", "(c)", "(d)"]
```

Les huit titres de rubrique attendus, et les quatre critÃƒÆ’Ã‚Â¨res acceptÃƒÆ’Ã‚Â©s dans la justification : (a) donnÃƒÆ’Ã‚Â©es ÃƒÆ’Ã‚Â©tiquetÃƒÆ’Ã‚Â©es, (b) vÃƒÆ’Ã‚Â©rifiabilitÃƒÆ’Ã‚Â©, (c) coÃƒÆ’Ã‚Â»t par requÃƒÆ’Ã‚Âªte, (d) consÃƒÆ’Ã‚Â©quence d'une erreur. Elles sont en haut du fichier pour ÃƒÆ’Ã‚Âªtre lues sans chercher. Ne les modifiez pas pour faire passer un test : c'est prÃƒÆ’Ã‚Â©cisÃƒÆ’Ã‚Â©ment ce que la notation vÃƒÆ’Ã‚Â©rifie.

### Les deux fonctions outils

#### `fiches(cadrage_dir)`

```py
def fiches(cadrage_dir: Path):
    return sorted(cadrage_dir.glob("cas*.md"))
```

**RÃƒÆ’Ã‚Â´le :** donner la liste des fiches ÃƒÆ’Ã‚Â  contrÃƒÆ’Ã‚Â´ler.

- `cadrage_dir.glob("cas*.md")` cherche dans `docs/cadrage/` les fichiers dont le nom commence par `cas` et finit par `.md`.  
- `sorted(...)` les range par ordre alphabÃƒÆ’Ã‚Â©tique : `cas1-pharmacie.md`, `cas2-reglement.md`, `cas3-avis-negatifs.md`.

**ConsÃƒÆ’Ã‚Â©quences :**

- `TEMPLATE.md`, `EXEMPLE-corrige.md` et `BANQUE-DE-CAS.md` ne commencent pas par `cas` : ils ne sont jamais contrÃƒÆ’Ã‚Â´lÃƒÆ’Ã‚Â©s.  
- Le tri explique pourquoi les erreurs apparaissent toujours d'abord sur `cas1`.

#### `section_body(text, title)`

```py
def section_body(text: str, title: str) -> str:
    pattern = re.compile(rf"^## {re.escape(title)}.*?$\n(.*?)(?=^## |\Z)", re.M | re.S)
    m = pattern.search(text)
    return m.group(1).strip() if m else ""
```

**RÃƒÆ’Ã‚Â´le :** extraire le texte d'une rubrique, c'est-ÃƒÆ’Ã‚Â -dire tout ce qui se trouve entre son titre et le titre suivant.

L'expression rÃƒÆ’Ã‚Â©guliÃƒÆ’Ã‚Â¨re, morceau par morceau :

| Morceau | Ce qu'il reconnaÃƒÆ’Ã‚Â®t |
| :---- | :---- |
| `^##&nbsp;` | Une ligne qui commence par `##`  (un titre de niveau 2\) |
| `{re.escape(title)}` | Le titre exact. `re.escape` neutralise les caractÃƒÆ’Ã‚Â¨res spÃƒÆ’Ã‚Â©ciaux, comme l'apostrophe de Ãƒâ€šÃ‚Â« ConsÃƒÆ’Ã‚Â©quence d'une erreur Ãƒâ€šÃ‚Â» |
| `.*?$` | La fin de la ligne de titre, quelle qu'elle soit : `## Justification (deux critÃƒÆ’Ã‚Â¨res)` convient aussi |
| `\n` | Le saut de ligne qui termine le titre |
| `(.*?)` | **Ce qu'on capture** : le corps de la rubrique, le plus court possible |
| `(?=^## |\Z)` | La limite : on s'arrÃƒÆ’Ã‚Âªte juste avant le prochain `##`  en dÃƒÆ’Ã‚Â©but de ligne, ou ÃƒÆ’Ã‚Â  la fin du fichier (`\Z`), sans les inclure |

Les deux options :

- `re.M` fait agir `^` et `$` au dÃƒÆ’Ã‚Â©but et ÃƒÆ’Ã‚Â  la fin de **chaque ligne**, et non du texte entier ;  
- `re.S` permet au point de traverser les sauts de ligne, pour que le corps puisse tenir sur plusieurs lignes.

Ensuite, `m.group(1).strip()` renvoie le corps sans les espaces de dÃƒÆ’Ã‚Â©but et de fin. Si le titre est absent, la fonction renvoie une chaÃƒÆ’Ã‚Â®ne vide.

**Un exemple.** Pour cette fiche :

```markdown
## Justification
> Citez au moins deux critÃƒÆ’Ã‚Â¨res.
(a) Aucune donnÃƒÆ’Ã‚Â©e ÃƒÆ’Ã‚Â©tiquetÃƒÆ’Ã‚Â©e n'existe. (d) Une erreur peut ÃƒÆ’Ã‚Âªtre grave.

## DonnÃƒÆ’Ã‚Â©es nÃƒÆ’Ã‚Â©cessaires
```

&nbsp;

`section_body(texte, "Justification")` renvoie les deux lignes situÃƒÆ’Ã‚Â©es entre les deux titres : la consigne et la phrase rÃƒÆ’Ã‚Â©digÃƒÆ’Ã‚Â©e.

### Les cinq tests

#### `test_three_fiches_exist`

```py
def test_three_fiches_exist(cadrage_dir: Path):
    assert len(fiches(cadrage_dir)) >= 3, "trois fiches cas*.md attendues dans docs/cadrage/"
```

**VÃƒÆ’Ã‚Â©rifie** qu'il y a au moins trois fiches. Le paramÃƒÆ’Ã‚Â¨tre `cadrage_dir` est une **fixture** : pytest le fournit automatiquement ÃƒÆ’Ã‚Â  partir de `tests/conftest.py`, qui le fait pointer vers `docs/cadrage/`. Le texte aprÃƒÆ’Ã‚Â¨s la virgule de l'`assert` est le message affichÃƒÆ’Ã‚Â© en cas d'ÃƒÆ’Ã‚Â©chec.

**ÃƒÆ’Ã¢â‚¬Â°choue si** une fiche a ÃƒÆ’Ã‚Â©tÃƒÆ’Ã‚Â© supprimÃƒÆ’Ã‚Â©e ou renommÃƒÆ’Ã‚Â©e, par exemple `Cas1.md` avec une majuscule.

#### `test_sections_present_in_every_fiche` (8 tests)

```py
@pytest.mark.parametrize("title", REQUIRED_SECTIONS)
def test_sections_present_in_every_fiche(cadrage_dir: Path, title):
    for fiche in fiches(cadrage_dir):
        assert f"## {title}" in fiche.read_text(encoding="utf-8"), f"{fiche.name} : rubrique '{title}' absente"
```

**VÃƒÆ’Ã‚Â©rifie** que chaque titre de rubrique figure dans chaque fiche.

- Le dÃƒÆ’Ã‚Â©corateur `@pytest.mark.parametrize` exÃƒÆ’Ã‚Â©cute la fonction **une fois par rubrique**, avec `title` qui prend tour ÃƒÆ’Ã‚Â  tour les huit valeurs de `REQUIRED_SECTIONS`. Une seule fonction donne donc huit tests, affichÃƒÆ’Ã‚Â©s par exemple `test_sections_present_in_every_fiche[Justification]`.  
- Pour chaque rubrique, la boucle parcourt les trois fiches et cherche le texte exact `## <titre>`.

**ÃƒÆ’Ã¢â‚¬Â°choue si** un titre a ÃƒÆ’Ã‚Â©tÃƒÆ’Ã‚Â© modifiÃƒÆ’Ã‚Â© ou supprimÃƒÆ’Ã‚Â© : `## justification` sans majuscule, ou `### Justification` avec trois diÃƒÆ’Ã‚Â¨ses au lieu de deux, ne correspondent pas. Ces huit tests passent dÃƒÆ’Ã‚Â¨s le dÃƒÆ’Ã‚Â©part, puisque les fiches du kit contiennent dÃƒÆ’Ã‚Â©jÃƒÆ’Ã‚Â  les titres. Ils protÃƒÆ’Ã‚Â¨gent la structure.

#### `test_sections_are_filled`

```py
def test_sections_are_filled(cadrage_dir: Path):
    empty = []
    for fiche in fiches(cadrage_dir):
        text = fiche.read_text(encoding="utf-8")
        for title in REQUIRED_SECTIONS:
            if title == "Approche retenue":
                continue
            body = section_body(text, title)
            body = "\n".join(
                l for l in body.splitlines() if l.strip() and not l.startswith(">") and not l.startswith("- [")
            )
            if len(body) < 20:
                empty.append(f"{fiche.name} / {title}")
    assert not empty, "rubriques vides ou trop courtes : " + ", ".join(empty)
```

**VÃƒÆ’Ã‚Â©rifie** que chaque rubrique contient au moins 20 caractÃƒÆ’Ã‚Â¨res **rÃƒÆ’Ã‚Â©digÃƒÆ’Ã‚Â©s par le binÃƒÆ’Ã‚Â´me**.

1. Pour chaque fiche et chaque rubrique, sauf Ãƒâ€šÃ‚Â« Approche retenue Ãƒâ€šÃ‚Â» qui ne contient que des cases ÃƒÆ’Ã‚Â  cocher, la fonction extrait le corps avec `section_body`.  
2. Elle retire trois sortes de lignes :  
   - les lignes vides (`l.strip()` est faux) ;  
   - les consignes du modÃƒÆ’Ã‚Â¨le, qui commencent par `>` ;  
   - les cases ÃƒÆ’Ã‚Â  cocher, qui commencent par `- [`.  
3. Elle mesure ce qui reste. Sous 20 caractÃƒÆ’Ã‚Â¨res, la rubrique est notÃƒÆ’Ã‚Â©e dans la liste `empty`.  
4. L'`assert` final ÃƒÆ’Ã‚Â©choue si la liste n'est pas vide.

Contrairement aux autres tests, celui-ci **rassemble toutes les rubriques trop courtes** avant d'ÃƒÆ’Ã‚Â©chouer : son message les liste toutes, sous la forme `cas1-pharmacie.md / Besoin en une phrase, cas1-pharmacie.md / Justification, ...`.

**Une subtilitÃƒÆ’Ã‚Â© :** `startswith(">")` teste le dÃƒÆ’Ã‚Â©but exact de la ligne. Une consigne prÃƒÆ’Ã‚Â©cÃƒÆ’Ã‚Â©dÃƒÆ’Ã‚Â©e d'espaces, comme   `> texte`, n'est donc pas retirÃƒÆ’Ã‚Â©e.

#### `test_exactly_one_approach_checked`

```py
def test_exactly_one_approach_checked(cadrage_dir: Path):
    for fiche in fiches(cadrage_dir):
        text = fiche.read_text(encoding="utf-8")
        assert text.count("- [x]") == 1, f"{fiche.name} : cocher exactement une approche"
```

**VÃƒÆ’Ã‚Â©rifie** qu'une seule approche est cochÃƒÆ’Ã‚Â©e par fiche. `text.count("- [x]")` compte les occurrences exactes de `- [x]` **dans tout le fichier**, et le test exige exactement 1\.

**ÃƒÆ’Ã¢â‚¬Â°choue si :**

- aucune case n'est cochÃƒÆ’Ã‚Â©e, comme dans les fiches du kit : le compte vaut 0 ;  
- deux cases sont cochÃƒÆ’Ã‚Â©es : le compte vaut 2 ;  
- la case est ÃƒÆ’Ã‚Â©crite autrement : `- [X]` avec un X majuscule, `-[x]` sans espace, ou `[x]` sans tiret ne comptent pas.

La boucle s'arrÃƒÆ’Ã‚Âªte ÃƒÆ’Ã‚Â  la **premiÃƒÆ’Ã‚Â¨re fiche fautive**, dÃƒÆ’Ã‚Â¨s qu'un `assert` ÃƒÆ’Ã‚Â©choue.

#### `test_justification_cites_two_criteria`

```py
def test_justification_cites_two_criteria(cadrage_dir: Path):
    for fiche in fiches(cadrage_dir):
        body = section_body(fiche.read_text(encoding="utf-8"), "Justification")
        cited = [c for c in CRITERIA if c in body]
        assert len(cited) >= 2, f"{fiche.name} : la justification doit citer au moins deux critÃƒÆ’Ã‚Â¨res (a), (b), (c), (d)"
```

**VÃƒÆ’Ã‚Â©rifie** que la justification s'appuie sur au moins deux critÃƒÆ’Ã‚Â¨res.

1. La fonction extrait le corps de la rubrique Ãƒâ€šÃ‚Â« Justification Ãƒâ€šÃ‚Â».  
2. La liste `cited` garde, parmi `(a)`, `(b)`, `(c)` et `(d)`, ceux qui apparaissent dans ce corps.  
3. Il en faut au moins deux.

**ÃƒÆ’Ã¢â‚¬Â°choue si :**

- les critÃƒÆ’Ã‚Â¨res sont citÃƒÆ’Ã‚Â©s ailleurs que sous Ãƒâ€šÃ‚Â« Justification Ãƒâ€šÃ‚Â» ;  
- ils sont ÃƒÆ’Ã‚Â©crits autrement : `a)` sans parenthÃƒÆ’Ã‚Â¨se ouvrante, ou `(A)` en majuscule, ne comptent pas.

Ici, les consignes ne sont **pas retirÃƒÆ’Ã‚Â©es** du corps : une consigne qui contiendrait Ãƒâ€šÃ‚Â« (a) Ãƒâ€šÃ‚Â» compterait. C'est aussi un test qui s'arrÃƒÆ’Ã‚Âªte ÃƒÆ’Ã‚Â  la premiÃƒÆ’Ã‚Â¨re fiche fautive.

Le test ne vÃƒÆ’Ã‚Â©rifie que la **prÃƒÆ’Ã‚Â©sence** des lettres. Que les critÃƒÆ’Ã‚Â¨res citÃƒÆ’Ã‚Â©s s'appliquent vraiment au cas, c'est l'enseignant qui le juge ÃƒÆ’Ã‚Â  la lecture : la grille du TP1 y consacre 4 points sur 10\.

### Lancer ces tests seuls

```powershell
python -m pytest tests/test_cadrage.py -q
python -m pytest tests/test_cadrage.py -v
```

&nbsp;

La premiÃƒÆ’Ã‚Â¨re commande affiche un caractÃƒÆ’Ã‚Â¨re par test (`.` rÃƒÆ’Ã‚Â©ussi, `F` ÃƒÆ’Ã‚Â©chouÃƒÆ’Ã‚Â©, `s` ignorÃƒÆ’Ã‚Â©), puis une ligne de bilan : `12 passed` quand les trois fiches sont complÃƒÆ’Ã‚Â¨tes. La seconde affiche le nom de chaque test et son rÃƒÆ’Ã‚Â©sultat.

---

## Annexe B : le TP2 en dÃƒÆ’Ã‚Â©tail

Les valeurs ci-dessous ont ÃƒÆ’Ã‚Â©tÃƒÆ’Ã‚Â© mesurÃƒÆ’Ã‚Â©es sur le jeu de dÃƒÆ’Ã‚Â©monstration, avec la graine fixÃƒÆ’Ã‚Â©e du kit : vous devez obtenir exactement les mÃƒÆ’Ã‚Âªmes.

### Les rÃƒÆ’Ã‚Â©sultats attendus, contrÃƒÆ’Ã‚Â´le par contrÃƒÆ’Ã‚Â´le

| ContrÃƒÆ’Ã‚Â´le | Commande | RÃƒÆ’Ã‚Â©sultat attendu |
| :---- | :---- | :---- |
| C1 | `python -m pytest -q`, juste aprÃƒÆ’Ã‚Â¨s `appliquer_tp2.py` | 2 failed, 38 passed, 2 skipped : les deux ÃƒÆ’Ã‚Â©checs rÃƒÆ’Ã‚Â©clament `models/metrics.json`, les deux tests ignorÃƒÆ’Ã‚Â©s attendent le modÃƒÆ’Ã‚Â¨le |
| C2 | `python src/make_demo.py` | `290 avis ÃƒÆ’Ã‚Â©crits`, 145 positifs et 145 nÃƒÆ’Ã‚Â©gatifs, dont 100 mitigÃƒÆ’Ã‚Â©s et 30 neutres |
| C3 | `python src/train.py`, puis `git status --short` | `Vocabulaire : 316 termes`, `F1 macro sur le jeu de test : 0.879 (seuil 0.85)` ; `models/metrics.json` apparaÃƒÆ’Ã‚Â®t, ni `models/sentiment.joblib` ni `data/demo_reviews.csv` |
| C4 | `python src/evaluate.py` | La matrice `27 2` sur la ligne `negative`, `5 24` sur la ligne `positive` : 7 erreurs sur 58 |
| C5 | `python src/train.py --allocine`, puis `python -m pytest -q` | `Source : allocine, 20000 avis`, F1 macro 0,920 sur 4 000 avis de test, puis 42 passed |

### Les sept erreurs du jeu de dÃƒÆ’Ã‚Â©monstration

`python src/evaluate.py` n'en affiche que trois. Voici les sept :

| VÃƒÆ’Ã‚Â©ritÃƒÆ’Ã‚Â© | PrÃƒÆ’Ã‚Â©dit | Avis | Retournement |
| :---- | :---- | :---- | :---- |
| positive | negative | Taille trop petite et retour payant au dÃƒÆ’Ã‚Â©ballage, sauf que ensuite produit conforme ÃƒÆ’Ã‚Â  la description, trÃƒÆ’Ã‚Â¨s satisfait. | sauf que ensuite |
| positive | negative | Commande jamais reÃƒÆ’Ã‚Â§ue et remboursement en attente au dÃƒÆ’Ã‚Â©but, sauf que ensuite je recommande sans hÃƒÆ’Ã‚Â©siter. | sauf que ensuite |
| negative | positive | Service impeccable et livraison en avance sur le papier, sauf que ensuite produit cassÃƒÆ’Ã‚Â© ÃƒÆ’Ã‚Â  l'arrivÃƒÆ’Ã‚Â©e. | sauf que ensuite |
| positive | negative | Facture erronÃƒÆ’Ã‚Â©e, aucun geste commercial sur le papier, puis rapidement service impeccable et livraison en avance. | puis rapidement |
| positive | negative | Commande jamais reÃƒÆ’Ã‚Â§ue et remboursement en attente au dÃƒÆ’Ã‚Â©but, avant que emballage soignÃƒÆ’Ã‚Â© et finitions propres. | avant que |
| negative | positive | Service impeccable et livraison en avance les premiers jours, avant que notice incomprÃƒÆ’Ã‚Â©hensible et piÃƒÆ’Ã‚Â¨ces manquantes. | avant que |
| positive | negative | Se casse au bout de deux utilisations ÃƒÆ’Ã‚Â  la livraison, mais finalement excellent rapport qualitÃƒÆ’Ã‚Â© prix. | mais finalement |

Ce sont tous des avis mitigÃƒÆ’Ã‚Â©s : ils commencent dans un sens, puis se retournent. Dans les sept cas, la prÃƒÆ’Ã‚Â©diction suit la premiÃƒÆ’Ã‚Â¨re partie de l'avis, alors que le verdict est donnÃƒÆ’Ã‚Â© par la fin.

### Un exemple de docs/semaine2.md

L'ÃƒÆ’Ã‚Â©noncÃƒÆ’Ã‚Â© demande trois phrases : quelles erreurs, pourquoi, et ce qu'il faudrait pour les corriger. C'est la partie Ãƒâ€šÃ‚Â« Analyse des erreurs Ãƒâ€šÃ‚Â» ci-dessous ; la partie Ãƒâ€šÃ‚Â« Mesures Ãƒâ€šÃ‚Â» donne le contexte. **C'est un exemple : ÃƒÆ’Ã‚Â©crivez votre compte rendu avec vos propres mots.** Des comptes rendus identiques d'un binÃƒÆ’Ã‚Â´me ÃƒÆ’Ã‚Â  l'autre font partie des signaux d'alerte de la grille.

```markdown
# Semaine 2 : le modÃƒÆ’Ã‚Â¨le de sentiment

## Mesures

| Jeu de donnÃƒÆ’Ã‚Â©es | Avis de test | F1 macro |
| --- | --- | --- |
| DÃƒÆ’Ã‚Â©monstration (290 avis) | 58 | 0,879 |
| AllocinÃƒÆ’Ã‚Â© (20 000 avis) | 4 000 | 0,920 |

Sur le jeu de dÃƒÆ’Ã‚Â©monstration, la matrice de confusion compte 27 nÃƒÆ’Ã‚Â©gatifs et 24 positifs bien classÃƒÆ’Ã‚Â©s,
2 nÃƒÆ’Ã‚Â©gatifs classÃƒÆ’Ã‚Â©s positifs et 5 positifs classÃƒÆ’Ã‚Â©s nÃƒÆ’Ã‚Â©gatifs : 7 erreurs sur 58.

## Analyse des erreurs

Les 7 erreurs portent toutes sur des avis mitigÃƒÆ’Ã‚Â©s, qui commencent dans un sens et se retournent
ensuite (Ãƒâ€šÃ‚Â« sauf que ensuite Ãƒâ€šÃ‚Â», Ãƒâ€šÃ‚Â« mais finalement Ãƒâ€šÃ‚Â», Ãƒâ€šÃ‚Â« avant que Ãƒâ€šÃ‚Â», Ãƒâ€šÃ‚Â« puis rapidement Ãƒâ€šÃ‚Â») : par
exemple, Ãƒâ€šÃ‚Â« Taille trop petite et retour payant au dÃƒÆ’Ã‚Â©ballage, sauf que ensuite produit conforme ÃƒÆ’Ã‚Â  la
description, trÃƒÆ’Ã‚Â¨s satisfait Ãƒâ€šÃ‚Â» est classÃƒÆ’Ã‚Â© nÃƒÆ’Ã‚Â©gatif alors qu'il est positif. Dans chacune de ces 7
erreurs, la prÃƒÆ’Ã‚Â©diction suit la premiÃƒÆ’Ã‚Â¨re partie de l'avis, alors que le verdict est donnÃƒÆ’Ã‚Â© par la fin :
le modÃƒÆ’Ã‚Â¨le additionne les poids des mots sans tenir compte de leur ordre, et un sac de mots ne voit
pas qu'un connecteur comme Ãƒâ€šÃ‚Â« sauf que Ãƒâ€šÃ‚Â» renverse le sens de ce qui prÃƒÆ’Ã‚Â©cÃƒÆ’Ã‚Â¨de. Pour corriger ces
erreurs, il faudrait une reprÃƒÆ’Ã‚Â©sentation qui tient compte de l'ordre et du contexte des mots, comme
les embeddings de phrase vus en semaine 9.
```

&nbsp;

Trois remarques :

- **VÃƒÆ’Ã‚Â©rifiez vos chiffres.** Si `python src/evaluate.py` ne donne pas la matrice `27 2` / `5 24`, le modÃƒÆ’Ã‚Â¨le n'est pas celui du jeu de dÃƒÆ’Ã‚Â©monstration : relancez `python src/train.py`, sans `--allocine`.  
- **N'ÃƒÆ’Ã‚Â©voquez pas les bigrammes comme remÃƒÆ’Ã‚Â¨de.** Le vectoriseur en utilise dÃƒÆ’Ã‚Â©jÃƒÆ’Ã‚Â  : son vocabulaire contient par exemple Ãƒâ€šÃ‚Â« service client Ãƒâ€šÃ‚Â». Ils ne suffisent pas, car le retournement porte sur toute la phrase.  
- **Si le tÃƒÆ’Ã‚Â©lÃƒÆ’Ã‚Â©chargement d'AllocinÃƒÆ’Ã‚Â© a ÃƒÆ’Ã‚Â©chouÃƒÆ’Ã‚Â©**, remplacez la deuxiÃƒÆ’Ã‚Â¨me ligne du tableau par une phrase qui le signale.

Ce critÃƒÆ’Ã‚Â¨re vaut 2 points sur 10 au TP2 : la lecture vÃƒÆ’Ã‚Â©rifie surtout que les avis mitigÃƒÆ’Ã‚Â©s sont identifiÃƒÆ’Ã‚Â©s et que la limite du sac de mots est expliquÃƒÆ’Ã‚Â©e.

### Finir le TP2

**1\. VÃƒÆ’Ã‚Â©rifier ce qui part dans Git, puis pousser.**

```powershell
git status --short
git add -A
git commit -m "Semaine 2 : modele de sentiment, metriques et tests"
git push
```

&nbsp;

`git status` doit montrer `src/`, `tests/test_model.py`, `notebooks/`, `docs/semaine2.md`, `models/metrics.json` et les deux documents du TP ; jamais `models/sentiment.joblib` ni `data/demo_reviews.csv`, qui sont ignorÃƒÆ’Ã‚Â©s.

**2\. La CI.** Dans l'onglet Actions, la nouvelle exÃƒÆ’Ã‚Â©cution doit ÃƒÆ’Ã‚Âªtre verte, avec 42 passed dans l'ÃƒÆ’Ã‚Â©tape des tests. Sur GitHub, la CI n'a pas le modÃƒÆ’Ã‚Â¨le : les deux tests de prÃƒÆ’Ã‚Â©diction y sont ignorÃƒÆ’Ã‚Â©s, et les deux tests de mÃƒÆ’Ã‚Â©triques lisent `metrics.json`.

**3\. La part du membre B.** Chaque membre doit commiter dans chaque TP. Sur son poste, le membre B fait `git pull`, `python src/make_demo.py`, `python src/train.py`, puis `python -m pytest -q` (42 passed), et rÃƒÆ’Ã‚Â©dige une partie de `docs/semaine2.md`. Si une seule personne joue les deux rÃƒÆ’Ã‚Â´les, elle commite cette partie sous l'identitÃƒÆ’Ã‚Â© du membre B, la mÃƒÆ’Ã‚Âªme qu'au TP1 :

```powershell
git add docs/semaine2.md
git -c user.name="Nom du membre B" -c user.email="adresse-du-membre-B" commit -m "Semaine 2 : analyse des erreurs"
git push
```

&nbsp;

**4\. Avant le TP3.** Le TP2 se termine sur le modÃƒÆ’Ã‚Â¨le AllocinÃƒÆ’Ã‚Â©, alors que les tests de l'API attendent le modÃƒÆ’Ã‚Â¨le de dÃƒÆ’Ã‚Â©monstration, celui que la CI entraÃƒÆ’Ã‚Â®ne. AprÃƒÆ’Ã‚Â¨s avoir installÃƒÆ’Ã‚Â© le kit du TP3, lancez donc `python src/train.py`, sans `--allocine`, avant `python -m pytest -q` (contrÃƒÆ’Ã‚Â´le T14 : 48 passed). Si votre chemin de travail contient des espaces, mettez les chemins des commandes entre guillemets.

---

## Annexe C : comprendre src/train.py

`src/train.py` entraÃƒÆ’Ã‚Â®ne le modÃƒÆ’Ã‚Â¨le de sentiment et le sauvegarde. Il produit deux fichiers : `models/sentiment.joblib`, le modÃƒÆ’Ã‚Â¨le, qui reste hors de Git ; et `models/metrics.json`, sa mesure, qui est versionnÃƒÆ’Ã‚Â©e. Il s'utilise de deux faÃƒÆ’Ã‚Â§ons :

```powershell
python src/train.py              # jeu de dÃƒÆ’Ã‚Â©monstration (data/demo_reviews.csv)
python src/train.py --allocine   # vrai jeu public : 20 000 avis AllocinÃƒÆ’Ã‚Â©
```

&nbsp;

### Les constantes, en tÃƒÆ’Ã‚Âªte du fichier

```py
RACINE = Path(__file__).resolve().parents[1]
DEMO = RACINE / "data" / "demo_reviews.csv"
URL_ALLOCINE = "https://huggingface.co/datasets/tblard/allocine/resolve/main/allocine/validation-00000-of-00001.parquet"
MODELE = RACINE / "models" / "sentiment.joblib"
METRIQUES = RACINE / "models" / "metrics.json"
SEUIL_F1 = 0.85
GRAINE = 42
```

&nbsp;

| Constante | RÃƒÆ’Ã‚Â´le |
| :---- | :---- |
| `RACINE` | La racine du dÃƒÆ’Ã‚Â©pÃƒÆ’Ã‚Â´t, calculÃƒÆ’Ã‚Â©e ÃƒÆ’Ã‚Â  partir de l'emplacement du script : celui-ci fonctionne quel que soit le dossier courant |
| `DEMO` | Le jeu de dÃƒÆ’Ã‚Â©monstration, ÃƒÆ’Ã‚Â©crit par `make_demo.py` |
| `URL_ALLOCINE` | Le jeu public AllocinÃƒÆ’Ã‚Â©, hÃƒÆ’Ã‚Â©bergÃƒÆ’Ã‚Â© sur Hugging Face au format Parquet : 20 000 critiques de films |
| `MODELE`, `METRIQUES` | Les deux fichiers produits |
| `SEUIL_F1` | Le F1 minimal attendu, 0,85. Le script se contente de l'afficher : c'est `test_model.py` qui le fait respecter |
| `GRAINE` | La graine du hasard, 42 : deux exÃƒÆ’Ã‚Â©cutions donnent exactement le mÃƒÆ’Ã‚Âªme dÃƒÆ’Ã‚Â©coupage et le mÃƒÆ’Ã‚Âªme modÃƒÆ’Ã‚Â¨le |

`evaluate.py` et `courbe_seuil.py` importent `GRAINE`, `MODELE` et `charger` depuis ce fichier. Ils retrouvent ainsi exactement le mÃƒÆ’Ã‚Âªme jeu de test.

### `charger(allocine)` : lire les donnÃƒÆ’Ã‚Â©es

```py
def charger(allocine: bool) -> tuple[pd.DataFrame, str]:
    if allocine:
        df = pd.read_parquet(URL_ALLOCINE)
        df["label"] = df["label"].map({0: "negative", 1: "positive"})
        return df[["review", "label"]].dropna(), "allocine"
    if not DEMO.exists():
        raise SystemExit("data/demo_reviews.csv absent : lancez d'abord python src/make_demo.py")
    return pd.read_csv(DEMO), "demo"
```

La fonction renvoie un tableau ÃƒÆ’Ã‚Â  deux colonnes, `review` (le texte) et `label` (`positive` ou `negative`), ainsi que le nom de la source.

- **AllocinÃƒÆ’Ã‚Â©** : elle tÃƒÆ’Ã‚Â©lÃƒÆ’Ã‚Â©charge le fichier, ce qui demande une connexion et pyarrow. Les ÃƒÆ’Ã‚Â©tiquettes 0 et 1 deviennent `negative` et `positive`, comme dans le jeu de dÃƒÆ’Ã‚Â©monstration, et les lignes incomplÃƒÆ’Ã‚Â¨tes sont retirÃƒÆ’Ã‚Â©es.  
- **DÃƒÆ’Ã‚Â©monstration** : elle lit le CSV. S'il manque, elle s'arrÃƒÆ’Ã‚Âªte avec un message qui dit quoi faire.

### `construire_pipeline()` : le modÃƒÆ’Ã‚Â¨le

```py
return Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=2, sublinear_tf=True)),
    ("clf", LogisticRegression(max_iter=1000, class_weight="balanced", random_state=GRAINE)),
])
```

Le modÃƒÆ’Ã‚Â¨le a **deux ÃƒÆ’Ã‚Â©tages**. Le vectoriseur TF-IDF transforme chaque texte en vecteur de nombres, puis la rÃƒÆ’Ã‚Â©gression logistique classe ce vecteur.

| RÃƒÆ’Ã‚Â©glage | Effet |
| :---- | :---- |
| `ngram_range=(1, 2)` | Le vocabulaire contient les mots seuls et les **paires de mots consÃƒÆ’Ã‚Â©cutifs** (bigrammes), comme Ãƒâ€šÃ‚Â« service client Ãƒâ€šÃ‚Â» |
| `min_df=2` | Un terme prÃƒÆ’Ã‚Â©sent dans moins de deux avis d'entraÃƒÆ’Ã‚Â®nement est ignorÃƒÆ’Ã‚Â© : moins de bruit. Le jeu de dÃƒÆ’Ã‚Â©monstration donne 316 termes |
| `sublinear_tf=True` | Un mot rÃƒÆ’Ã‚Â©pÃƒÆ’Ã‚Â©tÃƒÆ’Ã‚Â© compte de moins en moins : son poids croÃƒÆ’Ã‚Â®t comme 1 \+ log(frÃƒÆ’Ã‚Â©quence), et non proportionnellement |
| `max_iter=1000` | Laisse ÃƒÆ’Ã‚Â  l'optimisation le temps de converger |
| `class_weight="balanced"` | Compense un ÃƒÆ’Ã‚Â©ventuel dÃƒÆ’Ã‚Â©sÃƒÆ’Ã‚Â©quilibre entre avis positifs et nÃƒÆ’Ã‚Â©gatifs |
| `random_state=GRAINE` | RÃƒÆ’Ã‚Â©sultat reproductible |

**Pourquoi un `Pipeline` ?** Le vectoriseur et le classifieur forment un seul objet, sauvegardÃƒÆ’Ã‚Â© d'un bloc. En production, `predict()` applique donc forcÃƒÆ’Ã‚Â©ment la mÃƒÆ’Ã‚Âªme transformation qu'ÃƒÆ’Ã‚Â  l'entraÃƒÆ’Ã‚Â®nement. Sauvegarder le classifieur seul est un piÃƒÆ’Ã‚Â¨ge classique : sans son vocabulaire, il est inutilisable.

### `main()` : les ÃƒÆ’Ã‚Â©tapes, dans l'ordre

**a. Lire les options et les donnÃƒÆ’Ã‚Â©es**, puis afficher la source : `Source : demo, 290 avis (145 nÃƒÆ’Ã‚Â©gatifs)`.

**b. DÃƒÆ’Ã‚Â©couper avant toute transformation.**

```py
X_train, X_test, y_train, y_test = train_test_split(
    df["review"], df["label"], test_size=0.2, random_state=GRAINE, stratify=df["label"]
)
```

- 20 % des avis sont mis de cÃƒÆ’Ã‚Â´tÃƒÆ’Ã‚Â© pour le test : 232 pour l'entraÃƒÆ’Ã‚Â®nement et 58 pour le test sur le jeu de dÃƒÆ’Ã‚Â©monstration, 16 000 et 4 000 sur AllocinÃƒÆ’Ã‚Â©.  
- `stratify` garde la mÃƒÆ’Ã‚Âªme proportion de positifs et de nÃƒÆ’Ã‚Â©gatifs dans les deux parties.  
- **Le dÃƒÆ’Ã‚Â©coupage prÃƒÆ’Ã‚Â©cÃƒÆ’Ã‚Â¨de la vectorisation**, et c'est le point essentiel du script. Si le vectoriseur apprenait son vocabulaire sur toutes les donnÃƒÆ’Ã‚Â©es, le jeu de test Ãƒâ€šÃ‚Â« fuirait Ãƒâ€šÃ‚Â» dans l'entraÃƒÆ’Ã‚Â®nement, et le score serait artificiellement bon.

**c. EntraÃƒÆ’Ã‚Â®ner.** `pipeline.fit(X_train, y_train)` apprend le vocabulaire et les poids **uniquement sur les avis d'entraÃƒÆ’Ã‚Â®nement**. Le script affiche ensuite `Vocabulaire : 316 termes`.

**d. Mesurer sur le jeu de test.** `classification_report` compare les prÃƒÆ’Ã‚Â©dictions aux vraies ÃƒÆ’Ã‚Â©tiquettes des 58 avis jamais vus. Le script en retient le **F1 macro**, la moyenne des F1 des deux classes, chacune comptant autant, et l'affiche : `F1 macro sur le jeu de test : 0.879 (seuil 0.85)`.

**e. Sauvegarder.**

- `joblib.dump(pipeline, MODELE)` ÃƒÆ’Ã‚Â©crit le modÃƒÆ’Ã‚Â¨le, un fichier binaire, ignorÃƒÆ’Ã‚Â© par Git.  
- `metrics.json` reÃƒÆ’Ã‚Â§oit la source, la date, les tailles d'entraÃƒÆ’Ã‚Â®nement et de test, le F1 macro, l'exactitude, le rappel de la classe nÃƒÆ’Ã‚Â©gative et le seuil. Ce petit fichier texte est versionnÃƒÆ’Ã‚Â© : il garde la trace de chaque mesure, et la CI le lit sans avoir le modÃƒÆ’Ã‚Â¨le.

Sur le jeu de dÃƒÆ’Ã‚Â©monstration, la sortie complÃƒÆ’Ã‚Â¨te est :

```
Source : demo, 290 avis (145 nÃƒÆ’Ã‚Â©gatifs)
232 avis d'entraÃƒÆ’Ã‚Â®nement, 58 de test
Vocabulaire : 316 termes
F1 macro sur le jeu de test : 0.879 (seuil 0.85)
ModÃƒÆ’Ã‚Â¨le : models/sentiment.joblib
MÃƒÆ’Ã‚Â©triques : models/metrics.json (versionnÃƒÆ’Ã‚Â© dans Git, contrairement au modÃƒÆ’Ã‚Â¨le)
```

### Ce qu'il faut savoir en pratique

- **`--allocine` ÃƒÆ’Ã‚Â©crase le modÃƒÆ’Ã‚Â¨le de dÃƒÆ’Ã‚Â©monstration.** Les tests de l'API (TP3 et suivants) attendent le modÃƒÆ’Ã‚Â¨le de dÃƒÆ’Ã‚Â©monstration, celui que la CI entraÃƒÆ’Ã‚Â®ne : relancez `python src/train.py`, sans option, avant `pytest`.  
- **`metrics.json` change ÃƒÆ’Ã‚Â  chaque entraÃƒÆ’Ã‚Â®nement**, mÃƒÆ’Ã‚Âªme si le F1 est identique, parce qu'il contient la date du jour. C'est pourquoi `git status` le montre modifiÃƒÆ’Ã‚Â©.  
- **Le modÃƒÆ’Ã‚Â¨le dÃƒÆ’Ã‚Â©pend de la version de scikit-learn** qui l'a produit. Un modÃƒÆ’Ã‚Â¨le entraÃƒÆ’Ã‚Â®nÃƒÆ’Ã‚Â© avec une version et relu par une autre peut ÃƒÆ’Ã‚Â©chouer ; c'est l'objet du TP6.  
- **Un avertissement `OptimizeWarning: Unknown solver options: iprint`** peut apparaÃƒÆ’Ã‚Â®tre avec une version rÃƒÆ’Ã‚Â©cente de SciPy : il est sans consÃƒÆ’Ã‚Â©quence.

---

## Annexe D : les contrÃƒÆ’Ã‚Â´les T15 ÃƒÆ’Ã‚Â  T20 expliquÃƒÆ’Ã‚Â©s

Les rÃƒÆ’Ã‚Â©ponses citÃƒÆ’Ã‚Â©es ont ÃƒÆ’Ã‚Â©tÃƒÆ’Ã‚Â© mesurÃƒÆ’Ã‚Â©es sur l'API du TP3, avec le modÃƒÆ’Ã‚Â¨le de dÃƒÆ’Ã‚Â©monstration : vous devez obtenir exactement les mÃƒÆ’Ã‚Âªmes.

### Ce qui se passe au lancement de l'API

```powershell
uvicorn api.main:app --reload
```

&nbsp;

`uvicorn` est le serveur web : il lance l'application `app` du fichier `api/main.py`, sur le port 8000\. `--reload` la relance ÃƒÆ’Ã‚Â  chaque modification du code. Au dÃƒÆ’Ã‚Â©marrage, la fonction `lifespan` de `main.py` charge le modÃƒÆ’Ã‚Â¨le **une seule fois**, avant la premiÃƒÆ’Ã‚Â¨re requÃƒÆ’Ã‚Âªte, et le range dans `app.state.classifier`. Le terminal l'annonce :

```
INFO     DÃƒÆ’Ã‚Â©marrage de l'API...
INFO     ModÃƒÆ’Ã‚Â¨le chargÃƒÆ’Ã‚Â© avec succÃƒÆ’Ã‚Â¨s : tfidf-logreg (TP2, models/sentiment.joblib)
INFO:    Application startup complete.
```

Ensuite, chaque requÃƒÆ’Ã‚Âªte suit le mÃƒÆ’Ã‚Âªme chemin :

1. FastAPI choisit la fonction de la route : `health_check` pour `GET /health`, `predict` pour `POST /predict`.  
2. Pour `/predict`, **Pydantic vÃƒÆ’Ã‚Â©rifie le corps de la requÃƒÆ’Ã‚Âªte** avec le contrat `PredictRequest` de `api/schemas.py` : un champ `text`, une chaÃƒÆ’Ã‚Â®ne de 1 ÃƒÆ’Ã‚Â  2000 caractÃƒÆ’Ã‚Â¨res. Si le corps ne respecte pas ce contrat, FastAPI rÃƒÆ’Ã‚Â©pond 422 **sans mÃƒÆ’Ã‚Âªme exÃƒÆ’Ã‚Â©cuter la fonction**.  
3. `_classifier()` rÃƒÆ’Ã‚Â©cupÃƒÆ’Ã‚Â¨re le modÃƒÆ’Ã‚Â¨le chargÃƒÆ’Ã‚Â© au dÃƒÆ’Ã‚Â©marrage, ou rÃƒÆ’Ã‚Â©pond 503 s'il manque.  
4. `api/model.py` appelle `predict()` du TP2, puis met l'ÃƒÆ’Ã‚Â©tiquette en majuscules.  
5. La rÃƒÆ’Ã‚Â©ponse est vÃƒÆ’Ã‚Â©rifiÃƒÆ’Ã‚Â©e par le contrat `PredictResponse`, puis renvoyÃƒÆ’Ã‚Â©e en JSON.

**La page `/docs`.** FastAPI gÃƒÆ’Ã‚Â©nÃƒÆ’Ã‚Â¨re ÃƒÆ’Ã‚Â  partir du code une page de test, `http://localhost:8000/docs`. Pour chaque route : la dÃƒÆ’Ã‚Â©plier, cliquer sur Ãƒâ€šÃ‚Â« Try it out Ãƒâ€šÃ‚Â», saisir le corps de la requÃƒÆ’Ã‚Âªte, puis Ãƒâ€šÃ‚Â« Execute Ãƒâ€šÃ‚Â». La rÃƒÆ’Ã‚Â©ponse s'affiche sous Ãƒâ€šÃ‚Â« Code Ãƒâ€šÃ‚Â» (le code HTTP) et Ãƒâ€šÃ‚Â« Response body Ãƒâ€šÃ‚Â» (le JSON), et une ligne s'ajoute dans le terminal de l'API.

### T15 : GET /health, l'API est-elle prÃƒÆ’Ã‚Âªte ?

**Ce qu'on fait :** `GET /health`, sans corps.

**Ce qui se passe :** `health_check` appelle `_classifier()`. Si le modÃƒÆ’Ã‚Â¨le est chargÃƒÆ’Ã‚Â©, elle renvoie son nom ; sinon, `_classifier()` lÃƒÆ’Ã‚Â¨ve une erreur 503, Ãƒâ€šÃ‚Â« ModÃƒÆ’Ã‚Â¨le non chargÃƒÆ’Ã‚Â© Ãƒâ€šÃ‚Â».

**Attendu :** `200`, et

```json
{"status": "OK", "model": "tfidf-logreg (TP2, models/sentiment.joblib)"}
```

**Pourquoi c'est utile :** les outils de dÃƒÆ’Ã‚Â©ploiement et de surveillance interrogent `/health` en boucle pour savoir si le service est prÃƒÆ’Ã‚Âªt ÃƒÆ’Ã‚Â  recevoir des requÃƒÆ’Ã‚Âªtes. La page Streamlit du TP5 s'en sert aussi, pour afficher Ãƒâ€šÃ‚Â« API prÃƒÆ’Ã‚Âªte Ãƒâ€šÃ‚Â».

### T16 et T17 : POST /predict, deux avis ÃƒÆ’Ã‚Â©vidents

**Ce qu'on fait :** `POST /predict` avec `{"text": "Livraison rapide, produit conforme, trÃƒÆ’Ã‚Â¨s satisfait"}`, puis avec `{"text": "Produit cassÃƒÆ’Ã‚Â© et service injoignable, ÃƒÆ’Ã‚Â  fuir"}`.

**Attendu :**

```json
{"label": "POSITIVE", "score": 0.777, "text": "Livraison rapide, produit conforme, trÃƒÆ’Ã‚Â¨s satisfait"}
{"label": "NEGATIVE", "score": 0.7465, "text": "Produit cassÃƒÆ’Ã‚Â© et service injoignable, ÃƒÆ’Ã‚Â  fuir"}
```

&nbsp;

| Champ | Ce qu'il contient |
| :---- | :---- |
| `label` | L'ÃƒÆ’Ã‚Â©tiquette du modÃƒÆ’Ã‚Â¨le (`positive` ou `negative`), mise en majuscules par `api/model.py` |
| `score` | La confiance du modÃƒÆ’Ã‚Â¨le dans la classe prÃƒÆ’Ã‚Â©dite : la plus grande des deux probabilitÃƒÆ’Ã‚Â©s, entre 0,5 et 1 |
| `text` | Les 100 premiers caractÃƒÆ’Ã‚Â¨res de l'avis, pour vÃƒÆ’Ã‚Â©rifier ce qui a ÃƒÆ’Ã‚Â©tÃƒÆ’Ã‚Â© analysÃƒÆ’Ã‚Â© |

Le terminal de l'API ajoute une ligne par requÃƒÆ’Ã‚Âªte, par exemple `predict: 'Livraison rapide, produit conforme, trÃƒÆ’Ã‚Â¨s sati' -> POSITIVE (0.78)`. Les scores sont exactement 0,777 et 0,7465 parce que le modÃƒÆ’Ã‚Â¨le de dÃƒÆ’Ã‚Â©monstration est entraÃƒÆ’Ã‚Â®nÃƒÆ’Ã‚Â© avec une graine fixÃƒÆ’Ã‚Â©e. Si vous obtenez d'autres valeurs, le modÃƒÆ’Ã‚Â¨le chargÃƒÆ’Ã‚Â© est celui d'AllocinÃƒÆ’Ã‚Â© : `python src/train.py`, sans option, puis relancez l'API.

### T18 : trois requÃƒÆ’Ã‚Âªtes invalides, trois refus 422

**Ce qu'on fait :** `POST /predict` avec `{"text": ""}`, puis `{}`, puis `{"text": 42}`.

**Ce qui se passe :** Pydantic refuse les trois corps avant que la fonction `predict` ne s'exÃƒÆ’Ã‚Â©cute. FastAPI rÃƒÆ’Ã‚Â©pond 422 (Ãƒâ€šÃ‚Â« Unprocessable Entity Ãƒâ€šÃ‚Â», requÃƒÆ’Ã‚Âªte mal formÃƒÆ’Ã‚Â©e) avec un `detail` qui est une **liste** d'erreurs. Dans chacune, `loc` dÃƒÆ’Ã‚Â©signe le champ fautif, `msg` explique le refus et `type` le classe :

| Corps envoyÃƒÆ’Ã‚Â© | `type` | `loc` | `msg` |
| :---- | :---- | :---- | :---- |
| `{"text": ""}` | `string_too_short` | `["body", "text"]` | String should have at least 1 character |
| `{}` | `missing` | `["body", "text"]` | Field required |
| `{"text": 42}` | `string_type` | `["body", "text"]` | Input should be a valid string |

**Pourquoi 422 et pas 500 :** l'erreur vient du client, qui a envoyÃƒÆ’Ã‚Â© une requÃƒÆ’Ã‚Âªte invalide ; le serveur, lui, fonctionne. Un 500 signalerait une panne du serveur.

**ÃƒÆ’Ã¢â€šÂ¬ observer, sans le corriger :** envoyez aussi `{"text": "   "}`, trois espaces. La requÃƒÆ’Ã‚Âªte passe le contrat (elle a bien un caractÃƒÆ’Ã‚Â¨re au moins), puis `predict()` du TP2 la refuse. `main.py` transforme ce refus en 422, mais avec un `detail` qui est une simple chaÃƒÆ’Ã‚Â®ne : `{"detail": "texte vide"}`. Deux formes pour le mÃƒÆ’Ã‚Âªme refus : c'est le premier dÃƒÆ’Ã‚Â©faut que le TP4 fera trouver et corriger.

### T19 : la CI entraÃƒÆ’Ã‚Â®ne le modÃƒÆ’Ã‚Â¨le, puis teste l'API

**Ce qu'on fait :** `git add -A`, `git commit`, `git push`, puis l'onglet Actions sur GitHub.

**Ce qui se passe :** le kit du TP3 a modifiÃƒÆ’Ã‚Â© la CI. Elle installe dÃƒÆ’Ã‚Â©sormais FastAPI, httpx et uvicorn, et une nouvelle ÃƒÆ’Ã‚Â©tape, Ãƒâ€šÃ‚Â« ModÃƒÆ’Ã‚Â¨le de dÃƒÆ’Ã‚Â©monstration, pour les tests de l'API (TP3) Ãƒâ€šÃ‚Â», lance `make_demo.py` puis `train.py` **avant** les tests. Le modÃƒÆ’Ã‚Â¨le n'est jamais dans Git : sans cette ÃƒÆ’Ã‚Â©tape, les six tests de l'API seraient ignorÃƒÆ’Ã‚Â©s sur GitHub, faute de modÃƒÆ’Ã‚Â¨le ÃƒÆ’Ã‚Â  charger. Le kit a aussi ajoutÃƒÆ’Ã‚Â© `pythonpath = .` ÃƒÆ’Ã‚Â  `pytest.ini`, pour que les tests trouvent le paquet `api`.

**Attendu :** les ÃƒÆ’Ã‚Â©tapes sont toutes vertes, et l'ÃƒÆ’Ã‚Â©tape Ãƒâ€šÃ‚Â« Tests Ãƒâ€šÃ‚Â» affiche `48 passed`.

### T20 : sans modÃƒÆ’Ã‚Â¨le, l'API refuse de dÃƒÆ’Ã‚Â©marrer

**Ce qu'on fait :**

```powershell
Rename-Item models/sentiment.joblib sentiment.bak
uvicorn api.main:app
Rename-Item models/sentiment.bak sentiment.joblib
```

&nbsp;

**Ce qui se passe :** au dÃƒÆ’Ã‚Â©marrage, `lifespan` appelle `load_model()`, qui appelle `charger_modele()` du TP2. Le fichier manque : `charger_modele()` lÃƒÆ’Ã‚Â¨ve une `FileNotFoundError`, le dÃƒÆ’Ã‚Â©marrage ÃƒÆ’Ã‚Â©choue, et uvicorn s'arrÃƒÆ’Ã‚Âªte.

**Attendu :**

```
INFO     DÃƒÆ’Ã‚Â©marrage de l'API...
ERROR:    Traceback (most recent call last):
FileNotFoundError: models/sentiment.joblib absent : lancez python src/train.py
ERROR:    Application startup failed. Exiting.
```

Lancez la troisiÃƒÆ’Ã‚Â¨me commande seulement aprÃƒÆ’Ã‚Â¨s cet ÃƒÆ’Ã‚Â©chec : elle remet le modÃƒÆ’Ã‚Â¨le en place.

**Pourquoi refuser de dÃƒÆ’Ã‚Â©marrer plutÃƒÆ’Ã‚Â´t que rÃƒÆ’Ã‚Â©pondre 503 :** une API sans modÃƒÆ’Ã‚Â¨le ne pourra jamais rÃƒÆ’Ã‚Â©pondre correctement. En refusant de dÃƒÆ’Ã‚Â©marrer, elle rend la panne visible tout de suite, au moment du dÃƒÆ’Ã‚Â©ploiement, au lieu de paraÃƒÆ’Ã‚Â®tre en marche et de rÃƒÆ’Ã‚Â©pondre 503 ÃƒÆ’Ã‚Â  chaque client. Le code 503 sert aux indisponibilitÃƒÆ’Ã‚Â©s passagÃƒÆ’Ã‚Â¨res, quand le modÃƒÆ’Ã‚Â¨le a ÃƒÆ’Ã‚Â©tÃƒÆ’Ã‚Â© retirÃƒÆ’Ã‚Â© en cours de route.

### Les mÃƒÆ’Ã‚Âªmes essais en ligne de commande

L'API lancÃƒÆ’Ã‚Â©e dans un autre terminal, `httpx`, installÃƒÆ’Ã‚Â© avec `requirements.txt`, permet les mÃƒÆ’Ã‚Âªmes essais :

```powershell
python -c "import httpx; print(httpx.get('http://127.0.0.1:8000/health').json())"
python -c "import httpx; r = httpx.post('http://127.0.0.1:8000/predict', json={'text': 'Livraison rapide, produit conforme, trÃƒÆ’Ã‚Â¨s satisfait'}); print(r.status_code, r.json())"
python -c "import httpx; print([httpx.post('http://127.0.0.1:8000/predict', json=c).status_code for c in ({'text': ''}, {}, {'text': 42})])"
```

&nbsp;

Attendu : le JSON de T15, puis `200` et le JSON de T16, puis `[422, 422, 422]`.

### Le lien avec docs/semaine3.md

Les deux questions du compte rendu s'appuient sur ces contrÃƒÆ’Ã‚Â´les :

- **Pourquoi l'API refuse-t-elle de dÃƒÆ’Ã‚Â©marrer sans modÃƒÆ’Ã‚Â¨le, plutÃƒÆ’Ã‚Â´t que de rÃƒÆ’Ã‚Â©pondre 503 ?** Ce que vous avez vu en T20.  
- **Un texte vide est refusÃƒÆ’Ã‚Â© deux fois, par Pydantic puis par `predict()` : est-ce redondant ?** Ce que vous avez vu en T18, avec `""` puis avec `"   "`.

---

## Annexe E : l'interface de l'API, la page /docs

FastAPI gÃƒÆ’Ã‚Â©nÃƒÆ’Ã‚Â¨re automatiquement une interface web pour essayer l'API : `http://localhost:8000/docs`, qui s'ouvre une fois l'API lancÃƒÆ’Ã‚Â©e par `uvicorn api.main:app --reload`. Rien n'y est ÃƒÆ’Ã‚Â©crit ÃƒÆ’Ã‚Â  la main : la page est construite ÃƒÆ’Ã‚Â  partir du code, c'est-ÃƒÆ’Ã‚Â -dire des dÃƒÆ’Ã‚Â©corateurs de routes de `api/main.py`, de leurs `summary` et docstrings, et des contrats Pydantic de `api/schemas.py`. Modifier le code modifie la page.

### La structure de la page, de haut en bas

**1\. L'en-tÃƒÆ’Ã‚Âªte.**

- Le titre, Ãƒâ€šÃ‚Â« Sentiment Analysis API Ãƒâ€šÃ‚Â», et la description, Ãƒâ€šÃ‚Â« Classifie le sentiment d'un avis en franÃƒÆ’Ã‚Â§ais (modÃƒÆ’Ã‚Â¨le du TP2) Ãƒâ€šÃ‚Â» : ce sont les paramÃƒÆ’Ã‚Â¨tres `title` et `description` de `FastAPI(...)` dans `main.py`.  
- Deux ÃƒÆ’Ã‚Â©tiquettes : `1.0.0`, la version de l'API (paramÃƒÆ’Ã‚Â¨tre `version`), et `OAS 3.1`, la norme OpenAPI 3.1 dans laquelle la description de l'API est ÃƒÆ’Ã‚Â©crite.  
- Un lien, `/openapi.json` : la mÃƒÆ’Ã‚Âªme description, en JSON, lisible par des programmes.

**2\. Les routes**, regroupÃƒÆ’Ã‚Â©es sous Ãƒâ€šÃ‚Â« default Ãƒâ€šÃ‚Â». Chacune est une barre de couleur, avec sa mÃƒÆ’Ã‚Â©thode, son chemin et son rÃƒÆ’Ã‚Â©sumÃƒÆ’Ã‚Â© :

| Barre | Route | RÃƒÆ’Ã‚Â©sumÃƒÆ’Ã‚Â© | Fonction dans `main.py` |
| :---- | :---- | :---- | :---- |
| GET, en bleu | `/` | Accueil | `root` |
| GET, en bleu | `/health` | SantÃƒÆ’Ã‚Â© de l'API | `health_check` |
| POST, en vert | `/predict` | Classifier un texte | `predict` |

**3\. Une route, une fois dÃƒÆ’Ã‚Â©pliÃƒÆ’Ã‚Â©e.** Pour `POST /predict` :

- **La description** : la docstring de la fonction, qui annonce les codes 422, 503 et 500\.  
- **Parameters** : aucun, car tout passe par le corps de la requÃƒÆ’Ã‚Âªte.  
- **Request body**, obligatoire, au format `application/json`. L'onglet Ãƒâ€šÃ‚Â« Example Value Ãƒâ€šÃ‚Â» montre `{"text": "Livraison rapide, produit conforme, trÃƒÆ’Ã‚Â¨s satisfait"}`, l'exemple dÃƒÆ’Ã‚Â©clarÃƒÆ’Ã‚Â© dans `schemas.py`. L'onglet Ãƒâ€šÃ‚Â« Schema Ãƒâ€šÃ‚Â» montre le contrat : un champ `text`, une chaÃƒÆ’Ã‚Â®ne de 1 ÃƒÆ’Ã‚Â  2000 caractÃƒÆ’Ã‚Â¨res.  
- **Responses** : les codes documentÃƒÆ’Ã‚Â©s, `200` (Ãƒâ€šÃ‚Â« Successful Response Ãƒâ€šÃ‚Â», avec un exemple de `PredictResponse`) et `422` (Ãƒâ€šÃ‚Â« Validation Error Ãƒâ€šÃ‚Â»). Les codes 503 et 500 existent dans le code, mais ne sont pas dÃƒÆ’Ã‚Â©clarÃƒÆ’Ã‚Â©s : la page ne les montre pas. C'est une limite de la documentation automatique.  
- **Deux boutons.** Ãƒâ€šÃ‚Â« Try it out Ãƒâ€šÃ‚Â» rend le corps modifiable ; Ãƒâ€šÃ‚Â« Execute Ãƒâ€šÃ‚Â» envoie la requÃƒÆ’Ã‚Âªte. Apparaissent alors :  
  - **Curl** : la commande ÃƒÆ’Ã‚Â©quivalente en ligne de commande ;  
  - **Request URL** : l'adresse appelÃƒÆ’Ã‚Â©e ;  
  - **Server response** : le code (`Code`), le JSON reÃƒÆ’Ã‚Â§u (`Response body`) et les en-tÃƒÆ’Ã‚Âªtes.

**4\. En bas, Ãƒâ€šÃ‚Â« Schemas Ãƒâ€šÃ‚Â».** Les contrats de donnÃƒÆ’Ã‚Â©es :

- `PredictRequest`, `PredictResponse` et `HealthResponse`, dÃƒÆ’Ã‚Â©finis dans `schemas.py` ;  
- `HTTPValidationError` et `ValidationError`, ajoutÃƒÆ’Ã‚Â©s par FastAPI pour dÃƒÆ’Ã‚Â©crire les refus 422\.

`ErrorResponse` est dÃƒÆ’Ã‚Â©fini dans `schemas.py`, mais aucune route ne l'utilise : il n'apparaÃƒÆ’Ã‚Â®t pas.

**5\. Les pages voisines.**

- `http://localhost:8000/redoc` : la mÃƒÆ’Ã‚Âªme documentation, prÃƒÆ’Ã‚Â©sentÃƒÆ’Ã‚Â©e autrement, en lecture seule ;  
- `http://localhost:8000/openapi.json` : la description en JSON ;  
- `http://localhost:8000/` : l'accueil de l'API, en JSON.

### Vingt essais ÃƒÆ’Ã‚Â  faire

Les rÃƒÆ’Ã‚Â©ponses ont ÃƒÆ’Ã‚Â©tÃƒÆ’Ã‚Â© mesurÃƒÆ’Ã‚Â©es sur l'API du TP3, avec le modÃƒÆ’Ã‚Â¨le de dÃƒÆ’Ã‚Â©monstration. Sauf mention contraire, chaque essai se fait dans la page : dÃƒÆ’Ã‚Â©pliez la route, Ãƒâ€šÃ‚Â« Try it out Ãƒâ€šÃ‚Â», saisissez le corps, puis Ãƒâ€šÃ‚Â« Execute Ãƒâ€šÃ‚Â».

| NÃƒâ€šÃ‚Â° | Essai | Attendu | Ce que cela montre |
| :---- | :---- | :---- | :---- |
| 1 | `GET /` | 200, `{"message": "Sentiment Analysis API", "docs": "/docs", "health": "/health"}` | L'accueil indique oÃƒÆ’Ã‚Â¹ trouver la documentation |
| 2 | `GET /health` | 200, `{"status": "OK", "model": "tfidf-logreg (TP2, models/sentiment.joblib)"}` | L'API est prÃƒÆ’Ã‚Âªte (T15) |
| 3 | `{"text": "Livraison rapide, produit conforme, trÃƒÆ’Ã‚Â¨s satisfait"}` | 200, `POSITIVE`, 0,777 | Un avis ÃƒÆ’Ã‚Â©vident (T16) |
| 4 | `{"text": "Produit cassÃƒÆ’Ã‚Â© et service injoignable, ÃƒÆ’Ã‚Â  fuir"}` | 200, `NEGATIVE`, 0,7465 | L'autre classe (T17) |
| 5 | `{"text": ""}` | 422, `string_too_short` | Le contrat refuse le texte vide (T18) |
| 6 | `{}` | 422, `missing` | Le champ est obligatoire (T18) |
| 7 | `{"text": 42}` | 422, `string_type` | Le champ doit ÃƒÆ’Ã‚Âªtre une chaÃƒÆ’Ã‚Â®ne (T18) |
| 8 | `{"text": null}` | 422, `string_type` | `null` n'est pas une chaÃƒÆ’Ã‚Â®ne |
| 9 | `{"text": "a"}` | 200, `NEGATIVE`, 0,5162 | Un caractÃƒÆ’Ã‚Â¨re suffit au contrat |
| 10 | 2000 caractÃƒÆ’Ã‚Â¨res (voir ci-dessous) | 200, `NEGATIVE`, 0,5162 | La limite haute est acceptÃƒÆ’Ã‚Â©e |
| 11 | 2001 caractÃƒÆ’Ã‚Â¨res | 422, `string_too_long` | Au-delÃƒÆ’Ã‚Â , le contrat refuse |
| 12 | `{"text": "   "}`, trois espaces | 422, mais `{"detail": "texte vide"}` : une chaÃƒÆ’Ã‚Â®ne, pas une liste | Le contrat laisse passer, `predict()` refuse : deux formes de refus, le dÃƒÆ’Ã‚Â©faut que le TP4 corrigera |
| 13 | `{"text": "xqzvb wlkptr grombu"}` | 200, `NEGATIVE`, 0,5162 | Aucun mot connu : le modÃƒÆ’Ã‚Â¨le devine ; le TP4 ajoutera l'abstention |
| 14 | `{"text": "Taille trop petite et retour payant au dÃƒÆ’Ã‚Â©ballage, sauf que ensuite produit conforme ÃƒÆ’Ã‚Â  la description, trÃƒÆ’Ã‚Â¨s satisfait."}` | 200, `NEGATIVE`, 0,5335, alors que l'avis est positif | La limite du sac de mots, vue au TP2 |
| 15 | `{"text": "TrÃƒÆ’Ã‚Â¨s satisfait", "langue": "fr"}` | 200, `POSITIVE`, 0,7461 | Un champ en trop est ignorÃƒÆ’Ã‚Â© |
| 16 | Un corps qui n'est pas du JSON (en ligne de commande, voir ci-dessous) | 422, `json_invalid` | Le corps doit ÃƒÆ’Ã‚Âªtre du JSON |
| 17 | Dans le navigateur, `http://localhost:8000/predict` | 405, `{"detail": "Method Not Allowed"}` | Le navigateur fait un GET ; `/predict` n'accepte que POST |
| 18 | Dans le navigateur, `http://localhost:8000/inconnue` | 404, `{"detail": "Not Found"}` | Route inexistante |
| 19 | Dans le navigateur, `http://localhost:8000/redoc` | La documentation, autre prÃƒÆ’Ã‚Â©sentation | La mÃƒÆ’Ã‚Âªme description OpenAPI |
| 20 | L'API lancÃƒÆ’Ã‚Â©e sans modÃƒÆ’Ã‚Â¨le (contrÃƒÆ’Ã‚Â´le T20) | Pas de page : l'API ne dÃƒÆ’Ã‚Â©marre pas | Refus de dÃƒÆ’Ã‚Â©marrer, `FileNotFoundError` |

Trois remarques sur ces essais :

- **0,5162 revient trois fois** (essais 9, 10 et 13). Quand aucun mot du texte n'est dans le vocabulaire du modÃƒÆ’Ã‚Â¨le, la reprÃƒÆ’Ã‚Â©sentation TF-IDF est nulle : il ne reste que l'ordonnÃƒÆ’Ã‚Â©e ÃƒÆ’Ã‚Â  l'origine de la rÃƒÆ’Ã‚Â©gression logistique, toujours la mÃƒÆ’Ã‚Âªme.

- **Pour les essais 10 et 11**, prÃƒÆ’Ã‚Â©parez le texte dans le presse-papiers, puis collez-le entre les guillemets de `{"text": ""}` :

  ```powershell

  python -c "print('a' * 2000, end='')" | Set-Clipboard

  ```

  Pour l'essai 11, remplacez `2000` par `2001`.

- **Pour l'essai 16**, la page ne permet pas facilement d'envoyer autre chose que du JSON. En ligne de commande, l'API lancÃƒÆ’Ã‚Â©e dans un autre terminal :

  ```powershell

  python -c "import httpx; r = httpx.post('http://127.0.0.1:8000/predict', content=b'pas du json', headers={'Content-Type': 'application/json'}); print(r.status_code, r.json()['detail'][0]['type'])"

  ```

  Attendu : `422 json_invalid`.

La commande Ãƒâ€šÃ‚Â« Curl Ãƒâ€šÃ‚Â» affichÃƒÆ’Ã‚Â©e par la page est ÃƒÆ’Ã‚Â©crite pour Linux et macOS. Sous Windows, PowerShell interprÃƒÆ’Ã‚Â¨te mal ses guillemets : pour rejouer un essai en ligne de commande, prÃƒÆ’Ã‚Â©fÃƒÆ’Ã‚Â©rez les commandes `httpx` de l'annexe D.

---

## Annexe F : ruff et mypy, deux outils d'analyse statique

`ruff` et `mypy` lisent le code sans l'exÃƒÆ’Ã‚Â©cuter pour y repÃƒÆ’Ã‚Â©rer des problÃƒÆ’Ã‚Â¨mes avant mÃƒÆ’Ã‚Âªme de lancer les tests. Ils sont installÃƒÆ’Ã‚Â©s dans le `.venv` par `requirements-dev.txt` au contrÃƒÆ’Ã‚Â´le T21. S'ils manquent (Ãƒâ€šÃ‚Â« Le terme ruff n'est pas reconnu Ãƒâ€šÃ‚Â») :

```powershell
pip install pytest-cov ruff mypy
```

&nbsp;

### ruff : le linter et le formateur

`ruff` vÃƒÆ’Ã‚Â©rifie le style et les erreurs courantes : imports inutilisÃƒÆ’Ã‚Â©s, variables jamais lues, lignes trop longues, nommage non conforme ÃƒÆ’Ã‚Â  PEP 8, comparaisons douteuses (`== None`), f-strings sans variable. Il remplace ÃƒÆ’Ã‚Â  lui seul plusieurs outils plus anciens (flake8, isort, pyflakes, une partie de black) et il est trÃƒÆ’Ã‚Â¨s rapide car ÃƒÆ’Ã‚Â©crit en Rust.

```powershell
ruff check .          # signale les problÃƒÆ’Ã‚Â¨mes
ruff check . --fix    # corrige ceux qui peuvent l'ÃƒÆ’Ã‚Âªtre automatiquement
ruff format .         # reformate le code
```

&nbsp;

Quand tout est en ordre, il affiche `All checks passed!`.

### mypy : le vÃƒÆ’Ã‚Â©rificateur de types

`mypy` s'appuie sur les annotations de type (`def predict(text: str) -> dict:`) pour dÃƒÆ’Ã‚Â©tecter les incohÃƒÆ’Ã‚Â©rences : passer un `int` lÃƒÆ’Ã‚Â  oÃƒÆ’Ã‚Â¹ une `str` est attendue, oublier un `return`, appeler une mÃƒÆ’Ã‚Â©thode qui n'existe pas sur le type dÃƒÆ’Ã‚Â©clarÃƒÆ’Ã‚Â©, retourner `None` sans l'avoir annoncÃƒÆ’Ã‚Â©. Ces erreurs ne seraient visibles qu'ÃƒÆ’Ã‚Â  l'exÃƒÆ’Ã‚Â©cution, parfois seulement sur un cas rare ; `mypy` les trouve ÃƒÆ’Ã‚Â  la lecture. C'est lui qui signale le `.upper()` au contrÃƒÆ’Ã‚Â´le T26, une fois les types prÃƒÆ’Ã‚Â©cisÃƒÆ’Ã‚Â©s.

```powershell
mypy api              # analyse tout le dossier api
```

&nbsp;

Quand tout est en ordre, il affiche `Success: no issues found in 4 source files`. S'il signale des bibliothÃƒÆ’Ã‚Â¨ques sans annotations (joblib, scikit-learn), on ajoute dans `pyproject.toml` ou `mypy.ini` :

```ini
[mypy]
ignore_missing_imports = True
```

&nbsp;

### En rÃƒÆ’Ã‚Â©sumÃƒÆ’Ã‚Â©

|  | ruff | mypy |
| :---- | :---- | :---- |
| Ce qu'il vÃƒÆ’Ã‚Â©rifie | Style, erreurs de logique simples, imports | CohÃƒÆ’Ã‚Â©rence des types |
| S'appuie sur | RÃƒÆ’Ã‚Â¨gles de style (PEP 8 et autres) | Annotations de type |
| Peut corriger seul | Oui (`--fix`, `format`) | Non, il signale seulement |

Dans un projet dÃƒÆ’Ã‚Â©ployÃƒÆ’Ã‚Â©, on les place avec `pytest` dans le pipeline d'intÃƒÆ’Ã‚Â©gration continue (`ci.yml`) et dans le crochet `pre-commit` : si `ruff` ou `mypy` ÃƒÆ’Ã‚Â©choue, le commit est refusÃƒÆ’Ã‚Â© et le dÃƒÆ’Ã‚Â©ploiement est bloquÃƒÆ’Ã‚Â©, ce qui ÃƒÆ’Ã‚Â©vite de mettre en production un code fragile. C'est pour cela que le TP4 enchaÃƒÆ’Ã‚Â®ne les trois commandes.

---

## Annexe G : rÃƒÆ’Ã‚Â´le des packages Python

### MÃƒÆ’Ã‚Â©thode et lÃƒÆ’Ã‚Â©gende

Chaque package reÃƒÆ’Ã‚Â§oit un rÃƒÆ’Ã‚Â´le et un type : DÃƒÆ’Ã‚Â©veloppement (ÃƒÆ’Ã‚Â©crire, explorer, entraÃƒÆ’Ã‚Â®ner et tester le code), DÃƒÆ’Ã‚Â©ploiement (faire fonctionner l'application en production : serveur, API, tÃƒÆ’Ã‚Â¢ches de fond, infrastructure) ou Les deux. Les dÃƒÆ’Ã‚Â©pendances transitives suivent l'usage de leur package parent. Les frontiÃƒÆ’Ã‚Â¨res sont floues : une mÃƒÆ’Ã‚Âªme bibliothÃƒÆ’Ã‚Â¨que peut servir aux deux, et le classement exact de ton projet dÃƒÆ’Ã‚Â©pend de tes imports rÃƒÆ’Ã‚Â©els.

### Calcul scientifique et donnÃƒÆ’Ã‚Â©es

| Package | RÃƒÆ’Ã‚Â´le | Type |
| :---- | :---- | :---- |
| numpy | Calcul numÃƒÆ’Ã‚Â©rique sur tableaux multidimensionnels | Les deux |
| pandas | Manipulation de donnÃƒÆ’Ã‚Â©es tabulaires (DataFrames) | Les deux |
| pyarrow | Format colonnaire Arrow, lecture et ÃƒÆ’Ã‚Â©criture Parquet | Les deux |
| scipy | Algorithmes scientifiques (statistiques, optimisation, algÃƒÆ’Ã‚Â¨bre linÃƒÆ’Ã‚Â©aire) | DÃƒÆ’Ã‚Â©veloppement |
| sympy | Calcul symbolique | DÃƒÆ’Ã‚Â©veloppement |
| mpmath | ArithmÃƒÆ’Ã‚Â©tique en prÃƒÆ’Ã‚Â©cision arbitraire (dÃƒÆ’Ã‚Â©pendance de sympy) | DÃƒÆ’Ã‚Â©veloppement |
| networkx | Graphes et rÃƒÆ’Ã‚Â©seaux | DÃƒÆ’Ã‚Â©veloppement |
| numba | Compilation JIT pour accÃƒÆ’Ã‚Â©lÃƒÆ’Ã‚Â©rer le code Python | DÃƒÆ’Ã‚Â©veloppement |
| llvmlite | Backend LLVM utilisÃƒÆ’Ã‚Â© par numba | DÃƒÆ’Ã‚Â©veloppement |
| narwhals | API DataFrame commune ÃƒÆ’Ã‚Â  plusieurs bibliothÃƒÆ’Ã‚Â¨ques | DÃƒÆ’Ã‚Â©veloppement |
| tabulate | Affichage de tableaux en texte formatÃƒÆ’Ã‚Â© | DÃƒÆ’Ã‚Â©veloppement |
| regex | Expressions rÃƒÆ’Ã‚Â©guliÃƒÆ’Ã‚Â¨res avancÃƒÆ’Ã‚Â©es (extension de re) | DÃƒÆ’Ã‚Â©veloppement |
| pyparsing | Construction de parseurs | DÃƒÆ’Ã‚Â©veloppement |

### Machine learning et IA

| Package | RÃƒÆ’Ã‚Â´le | Type |
| :---- | :---- | :---- |
| scikit-learn | Apprentissage automatique classique | DÃƒÆ’Ã‚Â©veloppement |
| joblib | ParallÃƒÆ’Ã‚Â©lisme et sÃƒÆ’Ã‚Â©rialisation (utilisÃƒÆ’Ã‚Â© par scikit-learn) | Les deux |
| threadpoolctl | ContrÃƒÆ’Ã‚Â´le du nombre de threads BLAS et OpenMP | DÃƒÆ’Ã‚Â©veloppement |
| torch | Deep learning (PyTorch) | DÃƒÆ’Ã‚Â©veloppement |
| transformers | ModÃƒÆ’Ã‚Â¨les de langage prÃƒÆ’Ã‚Â©-entraÃƒÆ’Ã‚Â®nÃƒÆ’Ã‚Â©s (Hugging Face) | DÃƒÆ’Ã‚Â©veloppement |
| tokenizers | Tokenisation rapide pour les modÃƒÆ’Ã‚Â¨les de langage | DÃƒÆ’Ã‚Â©veloppement |
| sentence-transformers | Embeddings de phrases et de textes | DÃƒÆ’Ã‚Â©veloppement |
| huggingface-hub | TÃƒÆ’Ã‚Â©lÃƒÆ’Ã‚Â©chargement et partage de modÃƒÆ’Ã‚Â¨les et de jeux de donnÃƒÆ’Ã‚Â©es | DÃƒÆ’Ã‚Â©veloppement |
| safetensors | Format sÃƒÆ’Ã‚Â©curisÃƒÆ’Ã‚Â© pour sauvegarder les poids de modÃƒÆ’Ã‚Â¨les | Les deux |
| shap | ExplicabilitÃƒÆ’Ã‚Â© des modÃƒÆ’Ã‚Â¨les (valeurs de Shapley) | DÃƒÆ’Ã‚Â©veloppement |
| slicer | Slicing de tableaux (dÃƒÆ’Ã‚Â©pendance de shap) | DÃƒÆ’Ã‚Â©veloppement |
| mlflow | Suivi d'expÃƒÆ’Ã‚Â©riences et gestion de modÃƒÆ’Ã‚Â¨les | DÃƒÆ’Ã‚Â©veloppement |
| mlflow-skinny | Version allÃƒÆ’Ã‚Â©gÃƒÆ’Ã‚Â©e de MLflow | Les deux |
| cloudpickle | SÃƒÆ’Ã‚Â©rialisation d'objets Python (fonctions, lambdas) | Les deux |

### Visualisation

| Package | RÃƒÆ’Ã‚Â´le | Type |
| :---- | :---- | :---- |
| matplotlib | Graphiques | DÃƒÆ’Ã‚Â©veloppement |
| altair | Visualisation dÃƒÆ’Ã‚Â©clarative | DÃƒÆ’Ã‚Â©veloppement |
| pydeck | Cartes et visualisations gÃƒÆ’Ã‚Â©ospatiales | DÃƒÆ’Ã‚Â©veloppement |
| pillow | Traitement d'images | Les deux |
| contourpy | Calcul de contours (dÃƒÆ’Ã‚Â©pendance de matplotlib) | DÃƒÆ’Ã‚Â©veloppement |
| cycler | Cycles de styles, couleurs et traits (dÃƒÆ’Ã‚Â©pendance de matplotlib) | DÃƒÆ’Ã‚Â©veloppement |
| kiwisolver | RÃƒÆ’Ã‚Â©solution de contraintes de mise en page (dÃƒÆ’Ã‚Â©pendance de matplotlib) | DÃƒÆ’Ã‚Â©veloppement |
| fonttools | Manipulation des polices (dÃƒÆ’Ã‚Â©pendance de matplotlib) | DÃƒÆ’Ã‚Â©veloppement |
| pydot | GÃƒÆ’Ã‚Â©nÃƒÆ’Ã‚Â©ration de graphes au format DOT | DÃƒÆ’Ã‚Â©veloppement |
| grandalf | Mise en page automatique de graphes | DÃƒÆ’Ã‚Â©veloppement |

### Applications web et API

| Package | RÃƒÆ’Ã‚Â´le | Type |
| :---- | :---- | :---- |
| Flask | Micro-framework web | DÃƒÆ’Ã‚Â©ploiement |
| werkzeug | Utilitaires WSGI (base de Flask) | DÃƒÆ’Ã‚Â©ploiement |
| itsdangerous | Signature de donnÃƒÆ’Ã‚Â©es (sessions Flask) | DÃƒÆ’Ã‚Â©ploiement |
| blinker | Signaux (dÃƒÆ’Ã‚Â©pendance de Flask) | DÃƒÆ’Ã‚Â©ploiement |
| fastapi | API web asynchrone | DÃƒÆ’Ã‚Â©ploiement |
| starlette | Toolkit ASGI sur lequel repose FastAPI | DÃƒÆ’Ã‚Â©ploiement |
| uvicorn | Serveur ASGI | DÃƒÆ’Ã‚Â©ploiement |
| httptools | Parseur HTTP rapide (utilisÃƒÆ’Ã‚Â© par uvicorn) | DÃƒÆ’Ã‚Â©ploiement |
| waitress | Serveur WSGI pour la production | DÃƒÆ’Ã‚Â©ploiement |
| tornado | Framework web asynchrone | DÃƒÆ’Ã‚Â©ploiement |
| websockets | Communication WebSocket | DÃƒÆ’Ã‚Â©ploiement |
| graphene | Construction d'API GraphQL en Python | DÃƒÆ’Ã‚Â©ploiement |
| graphql-core | ImplÃƒÆ’Ã‚Â©mentation de GraphQL | DÃƒÆ’Ã‚Â©ploiement |
| graphql-relay | Extensions Relay pour GraphQL | DÃƒÆ’Ã‚Â©ploiement |
| streamlit | Applications web de data science | Les deux |
| Jinja2 | Moteur de templates | Les deux |
| markupsafe | ÃƒÆ’Ã¢â‚¬Â°chappement HTML (utilisÃƒÆ’Ã‚Â© par Jinja2) | Les deux |
| Mako | Moteur de templates | DÃƒÆ’Ã‚Â©veloppement |

### RequÃƒÆ’Ã‚Âªtes HTTP et rÃƒÆ’Ã‚Â©seau

| Package | RÃƒÆ’Ã‚Â´le | Type |
| :---- | :---- | :---- |
| requests | Client HTTP synchrone | Les deux |
| urllib3 | Client HTTP bas niveau (base de requests) | DÃƒÆ’Ã‚Â©ploiement |
| httpx | Client HTTP synchrone et asynchrone | DÃƒÆ’Ã‚Â©ploiement |
| httpcore | Couche bas niveau de httpx | DÃƒÆ’Ã‚Â©ploiement |
| h11 | ImplÃƒÆ’Ã‚Â©mentation du protocole HTTP/1.1 | DÃƒÆ’Ã‚Â©ploiement |
| anyio | Abstraction pour la programmation asynchrone | DÃƒÆ’Ã‚Â©ploiement |
| sniffio | DÃƒÆ’Ã‚Â©tection de la bibliothÃƒÆ’Ã‚Â¨que asynchrone utilisÃƒÆ’Ã‚Â©e | DÃƒÆ’Ã‚Â©ploiement |
| aiohttp | Client et serveur HTTP asynchrones | DÃƒÆ’Ã‚Â©ploiement |
| aiohttp-retry | Nouvelles tentatives pour aiohttp | DÃƒÆ’Ã‚Â©ploiement |
| aiosignal, frozenlist, multidict, yarl, propcache, aiohappyeyeballs | DÃƒÆ’Ã‚Â©pendances internes d'aiohttp | DÃƒÆ’Ã‚Â©ploiement |
| idna | Prise en charge des noms de domaine internationalisÃƒÆ’Ã‚Â©s | DÃƒÆ’Ã‚Â©ploiement |
| certifi | Bundle de certificats SSL racine | DÃƒÆ’Ã‚Â©ploiement |
| charset\_normalizer | DÃƒÆ’Ã‚Â©tection de l'encodage des textes | DÃƒÆ’Ã‚Â©ploiement |
| asyncssh | Client et serveur SSH asynchrones | DÃƒÆ’Ã‚Â©ploiement |
| docker | Client de l'API Docker | DÃƒÆ’Ã‚Â©ploiement |

### TÃƒÆ’Ã‚Â¢ches asynchrones, bases de donnÃƒÆ’Ã‚Â©es et messagerie

| Package | RÃƒÆ’Ã‚Â´le | Type |
| :---- | :---- | :---- |
| celery | ExÃƒÆ’Ã‚Â©cution de tÃƒÆ’Ã‚Â¢ches asynchrones distribuÃƒÆ’Ã‚Â©es | DÃƒÆ’Ã‚Â©ploiement |
| kombu | Abstraction de messagerie (backend de Celery) | DÃƒÆ’Ã‚Â©ploiement |
| amqp | Client du protocole AMQP (RabbitMQ) | DÃƒÆ’Ã‚Â©ploiement |
| vine | Promesses et chaÃƒÆ’Ã‚Â®nage asynchrone (Celery et kombu) | DÃƒÆ’Ã‚Â©ploiement |
| billiard | Fork de multiprocessing (Celery) | DÃƒÆ’Ã‚Â©ploiement |
| tenacity | Nouvelles tentatives avec attente exponentielle | DÃƒÆ’Ã‚Â©ploiement |
| databricks-sdk | SDK pour Databricks | DÃƒÆ’Ã‚Â©ploiement |
| sqlalchemy | ORM et toolkit SQL | Les deux |
| alembic | Migrations de schÃƒÆ’Ã‚Â©ma pour SQLAlchemy | Les deux |
| sqlparse | Analyse et formatage de SQL | DÃƒÆ’Ã‚Â©veloppement |

### Validation, configuration et sÃƒÆ’Ã‚Â©rialisation

| Package | RÃƒÆ’Ã‚Â´le | Type |
| :---- | :---- | :---- |
| pydantic | Validation de donnÃƒÆ’Ã‚Â©es par typage | Les deux |
| pydantic-core | CÃƒâ€¦Ã¢â‚¬Å“ur en Rust de pydantic | Les deux |
| annotated-types | Types d'annotations pour pydantic | Les deux |
| typing-inspection | Introspection des annotations de type | Les deux |
| typing-extensions | Backports d'annotations de type rÃƒÆ’Ã‚Â©centes | Les deux |
| jsonschema | Validation JSON Schema | Les deux |
| pyyaml | Lecture et ÃƒÆ’Ã‚Â©criture de YAML | Les deux |
| protobuf | SÃƒÆ’Ã‚Â©rialisation de donnÃƒÆ’Ã‚Â©es structurÃƒÆ’Ã‚Â©es (Google) | Les deux |
| six | CompatibilitÃƒÆ’Ã‚Â© Python 2 et 3 (code historique) | Les deux |
| orjson | SÃƒÆ’Ã‚Â©rialisation JSON trÃƒÆ’Ã‚Â¨s rapide | Les deux |
| pydantic-settings | Gestion des configurations via pydantic | DÃƒÆ’Ã‚Â©ploiement |
| python-dotenv | Chargement des variables du fichier .env | DÃƒÆ’Ã‚Â©ploiement |
| voluptuous | Validation de schÃƒÆ’Ã‚Â©mas de donnÃƒÆ’Ã‚Â©es | DÃƒÆ’Ã‚Â©veloppement |
| jsonschema-specifications | SchÃƒÆ’Ã‚Â©mas officiels pour jsonschema | DÃƒÆ’Ã‚Â©veloppement |
| referencing | RÃƒÆ’Ã‚Â©solution des rÃƒÆ’Ã‚Â©fÃƒÆ’Ã‚Â©rences JSON Schema | DÃƒÆ’Ã‚Â©veloppement |
| rpds-py | Structures de donnÃƒÆ’Ã‚Â©es immuables (dÃƒÆ’Ã‚Â©pendance de jsonschema) | DÃƒÆ’Ã‚Â©veloppement |
| attrs | Classes Python avec moins de code rÃƒÆ’Ã‚Â©pÃƒÆ’Ã‚Â©titif | DÃƒÆ’Ã‚Â©veloppement |
| omegaconf | Configuration hiÃƒÆ’Ã‚Â©rarchique | DÃƒÆ’Ã‚Â©veloppement |
| hydra-core | Gestion de configurations et d'expÃƒÆ’Ã‚Â©riences | DÃƒÆ’Ã‚Â©veloppement |
| antlr4-python3-runtime | Runtime ANTLR pour le parsing (dÃƒÆ’Ã‚Â©pendance d'omegaconf) | DÃƒÆ’Ã‚Â©veloppement |
| ruamel.yaml | YAML avec prÃƒÆ’Ã‚Â©servation des commentaires | DÃƒÆ’Ã‚Â©veloppement |
| tomlkit | Lecture et ÃƒÆ’Ã‚Â©criture de TOML en conservant le formatage | DÃƒÆ’Ã‚Â©veloppement |
| toml | Lecture de fichiers TOML | DÃƒÆ’Ã‚Â©veloppement |
| configobj | Fichiers de configuration au format INI | DÃƒÆ’Ã‚Â©veloppement |
| dictdiffer | Comparaison de dictionnaires | DÃƒÆ’Ã‚Â©veloppement |
| flatten-dict | Aplatissement de dictionnaires imbriquÃƒÆ’Ã‚Â©s | DÃƒÆ’Ã‚Â©veloppement |
| dpath | AccÃƒÆ’Ã‚Â¨s aux dictionnaires par chemins | DÃƒÆ’Ã‚Â©veloppement |
| sqltrie | Structure de type trie | DÃƒÆ’Ã‚Â©veloppement |
| pygtrie | Arbres de prÃƒÆ’Ã‚Â©fixes | DÃƒÆ’Ã‚Â©veloppement |
| funcy | Utilitaires fonctionnels | DÃƒÆ’Ã‚Â©veloppement |

### Interface en ligne de commande, terminal et texte

| Package | RÃƒÆ’Ã‚Â´le | Type |
| :---- | :---- | :---- |
| click | CrÃƒÆ’Ã‚Â©ation d'outils en ligne de commande | Les deux |
| tqdm | Barres de progression | Les deux |
| click-plugins | Extensions de click | DÃƒÆ’Ã‚Â©veloppement |
| click-didyoumean | Suggestions de commandes pour click | DÃƒÆ’Ã‚Â©veloppement |
| click-repl | Shell interactif basÃƒÆ’Ã‚Â© sur click | DÃƒÆ’Ã‚Â©veloppement |
| shtab | ComplÃƒÆ’Ã‚Â©tion automatique pour le shell | DÃƒÆ’Ã‚Â©veloppement |
| rich | Affichage riche dans le terminal | DÃƒÆ’Ã‚Â©veloppement |
| prompt\_toolkit | Interfaces interactives dans le terminal | DÃƒÆ’Ã‚Â©veloppement |
| wcwidth | Largeur d'affichage des caractÃƒÆ’Ã‚Â¨res (dÃƒÆ’Ã‚Â©pendance de prompt\_toolkit) | DÃƒÆ’Ã‚Â©veloppement |
| colorama | Couleurs dans le terminal, notamment sous Windows | DÃƒÆ’Ã‚Â©veloppement |
| pygments | Coloration syntaxique | DÃƒÆ’Ã‚Â©veloppement |
| markdown | Conversion Markdown vers HTML | DÃƒÆ’Ã‚Â©veloppement |
| markdown-it-py | Parseur Markdown compatible CommonMark | DÃƒÆ’Ã‚Â©veloppement |
| mdurl | Gestion des URL dans markdown-it | DÃƒÆ’Ã‚Â©veloppement |
| pathspec | Motifs de fichiers de type .gitignore | DÃƒÆ’Ã‚Â©veloppement |

### Dates, fuseaux horaires et systÃƒÆ’Ã‚Â¨me

| Package | RÃƒÆ’Ã‚Â´le | Type |
| :---- | :---- | :---- |
| python-dateutil | Analyse et calcul de dates | Les deux |
| tzlocal | Fuseau horaire local | Les deux |
| psutil | Informations sur le CPU, la mÃƒÆ’Ã‚Â©moire et les processus | Les deux |
| pywin32 | AccÃƒÆ’Ã‚Â¨s aux API Windows (Windows uniquement) | Les deux |
| filelock | Verrouillage de fichiers | Les deux |
| fsspec | SystÃƒÆ’Ã‚Â¨me de fichiers abstrait (local, S3, etc.) | Les deux |
| diskcache | Cache sur disque | Les deux |
| cachetools | Caches en mÃƒÆ’Ã‚Â©moire | Les deux |
| pytz | Fuseaux horaires (mÃƒÆ’Ã‚Â©thode historique) | DÃƒÆ’Ã‚Â©veloppement |
| tzdata | Base de donnÃƒÆ’Ã‚Â©es des fuseaux horaires | DÃƒÆ’Ã‚Â©veloppement |
| appdirs | RÃƒÆ’Ã‚Â©pertoires standards par OS (ancienne version de platformdirs) | DÃƒÆ’Ã‚Â©veloppement |
| distro | Informations sur la distribution Linux | DÃƒÆ’Ã‚Â©veloppement |
| flufl.lock | Verrouillage de fichiers (dÃƒÆ’Ã‚Â©pendance de DVC) | DÃƒÆ’Ã‚Â©veloppement |
| zc.lockfile | Verrouillage de fichiers | DÃƒÆ’Ã‚Â©veloppement |
| entrypoints | DÃƒÆ’Ã‚Â©couverte des points d'entrÃƒÆ’Ã‚Â©e des packages (ancienne mÃƒÆ’Ã‚Â©thode) | DÃƒÆ’Ã‚Â©veloppement |
| watchdog | Surveillance des modifications de fichiers | DÃƒÆ’Ã‚Â©veloppement |
| watchfiles | Surveillance des modifications de fichiers | DÃƒÆ’Ã‚Â©veloppement |
| semver | Gestion des versions sÃƒÆ’Ã‚Â©mantiques | DÃƒÆ’Ã‚Â©veloppement |
| packaging | Manipulation des versions et spÃƒÆ’Ã‚Â©cifications de packages | DÃƒÆ’Ã‚Â©veloppement |
| setuptools | Construction et installation de packages | DÃƒÆ’Ã‚Â©veloppement |
| platformdirs | RÃƒÆ’Ã‚Â©pertoires standards par OS (configuration, cache, donnÃƒÆ’Ã‚Â©es) | DÃƒÆ’Ã‚Â©ploiement |
| shortuuid | UUID courts | DÃƒÆ’Ã‚Â©ploiement |

### Tests, sÃƒÆ’Ã‚Â©curitÃƒÆ’Ã‚Â© et outils de dÃƒÆ’Ã‚Â©veloppement

| Package | RÃƒÆ’Ã‚Â´le | Type |
| :---- | :---- | :---- |
| pytest | Framework de tests unitaires | DÃƒÆ’Ã‚Â©veloppement |
| pluggy | SystÃƒÆ’Ã‚Â¨me de plugins (utilisÃƒÆ’Ã‚Â© par pytest) | DÃƒÆ’Ã‚Â©veloppement |
| iniconfig | Lecture de fichiers ini (utilisÃƒÆ’Ã‚Â© par pytest) | DÃƒÆ’Ã‚Â©veloppement |
| atpublic | Export des symboles d'un module | DÃƒÆ’Ã‚Â©veloppement |
| importlib-metadata | AccÃƒÆ’Ã‚Â¨s aux mÃƒÆ’Ã‚Â©tadonnÃƒÆ’Ã‚Â©es des packages | DÃƒÆ’Ã‚Â©veloppement |
| zipp | AccÃƒÆ’Ã‚Â¨s aux archives zip (dÃƒÆ’Ã‚Â©pendance d'importlib-metadata) | DÃƒÆ’Ã‚Â©veloppement |
| cryptography | Primitives cryptographiques | DÃƒÆ’Ã‚Â©ploiement |
| cffi | Interface entre Python et du code C | DÃƒÆ’Ã‚Â©ploiement |
| pycparser | Analyse de code C (dÃƒÆ’Ã‚Â©pendance de cffi) | DÃƒÆ’Ã‚Â©ploiement |
| pyasn1 | Encodage ASN.1 (certificats, authentification) | DÃƒÆ’Ã‚Â©ploiement |
| pyasn1-modules | Modules ASN.1 pour certificats | DÃƒÆ’Ã‚Â©ploiement |
| google-auth | Authentification auprÃƒÆ’Ã‚Â¨s des services Google | DÃƒÆ’Ã‚Â©ploiement |

### Gestion de versions, de donnÃƒÆ’Ã‚Â©es et observabilitÃƒÆ’Ã‚Â©

| Package | RÃƒÆ’Ã‚Â´le | Type |
| :---- | :---- | :---- |
| dvc | Versionnage des donnÃƒÆ’Ã‚Â©es et des pipelines de ML | DÃƒÆ’Ã‚Â©veloppement |
| dvc-render | Rendu des mÃƒÆ’Ã‚Â©triques et graphiques de DVC | DÃƒÆ’Ã‚Â©veloppement |
| dvc-objects | Abstraction du stockage d'objets pour DVC | DÃƒÆ’Ã‚Â©veloppement |
| dvc-data | Gestion des jeux de donnÃƒÆ’Ã‚Â©es dans DVC | DÃƒÆ’Ã‚Â©veloppement |
| dvc-http | AccÃƒÆ’Ã‚Â¨s HTTP aux donnÃƒÆ’Ã‚Â©es pour DVC | DÃƒÆ’Ã‚Â©veloppement |
| dvc-task | ExÃƒÆ’Ã‚Â©cution de tÃƒÆ’Ã‚Â¢ches pour DVC | DÃƒÆ’Ã‚Â©veloppement |
| dvc-studio-client | Connexion ÃƒÆ’Ã‚Â  DVC Studio | DÃƒÆ’Ã‚Â©veloppement |
| iterative-telemetry | TÃƒÆ’Ã‚Â©lÃƒÆ’Ã‚Â©mÃƒÆ’Ã‚Â©trie anonyme des outils Iterative | DÃƒÆ’Ã‚Â©veloppement |
| gto | Gestion des versions de modÃƒÆ’Ã‚Â¨les via des tags Git | DÃƒÆ’Ã‚Â©veloppement |
| scmrepo | Interface unifiÃƒÆ’Ã‚Â©e pour les dÃƒÆ’Ã‚Â©pÃƒÆ’Ã‚Â´ts Git utilisÃƒÆ’Ã‚Â©e par DVC | DÃƒÆ’Ã‚Â©veloppement |
| gitpython | Manipulation de dÃƒÆ’Ã‚Â©pÃƒÆ’Ã‚Â´ts Git en Python | DÃƒÆ’Ã‚Â©veloppement |
| gitdb, smmap | DÃƒÆ’Ã‚Â©pendances de gitpython | DÃƒÆ’Ã‚Â©veloppement |
| dulwich | ImplÃƒÆ’Ã‚Â©mentation de Git en Python pur | DÃƒÆ’Ã‚Â©veloppement |
| pygit2 | Liaisons Python vers libgit2 | DÃƒÆ’Ã‚Â©veloppement |
| opentelemetry-api | Interface de traÃƒÆ’Ã‚Â§age et d'observabilitÃƒÆ’Ã‚Â© | DÃƒÆ’Ã‚Â©ploiement |
| opentelemetry-sdk | ImplÃƒÆ’Ã‚Â©mentation du traÃƒÆ’Ã‚Â§age et des mÃƒÆ’Ã‚Â©triques | DÃƒÆ’Ã‚Â©ploiement |
| opentelemetry-semantic-conventions | Conventions de nommage pour l'observabilitÃƒÆ’Ã‚Â© | DÃƒÆ’Ã‚Â©ploiement |

### Remarques sur les frontiÃƒÆ’Ã‚Â¨res

La sÃƒÆ’Ã‚Â©paration entre dÃƒÆ’Ã‚Â©veloppement et dÃƒÆ’Ã‚Â©ploiement est indicative. Les packages d'entraÃƒÆ’Ã‚Â®nement comme torch ou transformers servent aussi ÃƒÆ’Ã‚Â  l'infÃƒÆ’Ã‚Â©rence en production. Pour un classement exact de ton projet, le plus fiable reste de comparer cette liste avec tes imports rÃƒÆ’Ã‚Â©els ou avec ton requirements.txt, car beaucoup de packages listÃƒÆ’Ã‚Â©s ici sont seulement des dÃƒÆ’Ã‚Â©pendances transitives que tu n'importes jamais directement.

---

## Annexe H : le TP6 en dÃƒÆ’Ã‚Â©tail

Cette annexe explique les commandes du TP6 et les notions qu'elles supposent. Elle ne remplace pas les champs Ãƒâ€šÃ‚Â« Obtenu Ãƒâ€šÃ‚Â», Ãƒâ€šÃ‚Â« Conforme Ãƒâ€šÃ‚Â» et Ãƒâ€šÃ‚Â« Commentaire Ãƒâ€šÃ‚Â» du TP6, qui doivent reflÃƒÆ’Ã‚Â©ter ce que vous observez sur votre machine.

### Notions prÃƒÆ’Ã‚Â©alables

**Environnement virtuel (`.venv`)** : un dossier qui contient sa propre copie de Python et ses propres bibliothÃƒÆ’Ã‚Â¨ques. `py -3.11 -m venv .venv` le crÃƒÆ’Ã‚Â©e, et `.venv\Scripts\Activate.ps1` l'active : `python` et `pip` dÃƒÆ’Ã‚Â©signent alors ceux du venv.

**`python -m module`** : lance un module installÃƒÆ’Ã‚Â© comme programme. `python -m pytest` utilise le Python actif, ce qui ÃƒÆ’Ã‚Â©vite de lancer une autre installation de pytest.

**Installation ÃƒÆ’Ã‚Â©ditable (`pip install -e .`)** : installe le paquet par un lien vers le dossier du projet, au lieu de copier les fichiers. Une modification du code prend effet sans rÃƒÆ’Ã‚Â©installation.

**Roue (`.whl`)** : le format d'archive standard d'un paquet Python. Dans `sentiment_app-0.6.0-py3-none-any.whl`, les parties indiquent le nom, la version, la version de Python (`py3`), la compatibilitÃƒÆ’Ã‚Â© (`none`) et la plateforme (`any`). Une roue Ãƒâ€šÃ‚Â« pure Python Ãƒâ€šÃ‚Â» s'installe donc sur tous les systÃƒÆ’Ã‚Â¨mes.

**Variable d'environnement** : une valeur dÃƒÆ’Ã‚Â©finie dans le shell et lue par le programme. `$env:SENTIMENT_MODELE = "..."` la dÃƒÆ’Ã‚Â©finit pour la session PowerShell en cours.

**Code de sortie** : nombre renvoyÃƒÆ’Ã‚Â© par un programme, 0 pour un succÃƒÆ’Ã‚Â¨s, une autre valeur pour une erreur. `$LASTEXITCODE` affiche le code de la derniÃƒÆ’Ã‚Â¨re commande.

### T35 : le kit installÃƒÆ’Ã‚Â©

```powershell
python C:\IA-DEV\tp6-packaging\appliquer_tp6.py C:\IA-DEV\sentiment-app
pip install -r requirements-dev.txt
python -m pytest -q
```

&nbsp;

Le premier script copie les fichiers du TP6 dans le dÃƒÆ’Ã‚Â©pÃƒÆ’Ã‚Â´t. Le deuxiÃƒÆ’Ã‚Â¨me installe les outils de dÃƒÆ’Ã‚Â©veloppement (pytest, ruff, mypy). Le troisiÃƒÆ’Ã‚Â¨me lance les tests.

Les deux ÃƒÆ’Ã‚Â©checs sont voulus. Ils constatent que le code n'est pas encore rÃƒÆ’Ã‚Â©organisÃƒÆ’Ã‚Â© : le modÃƒÆ’Ã‚Â¨le n'a pas d'emplacement configurable, et l'API modifie `sys.path` pour trouver le paquet. Le TP consiste ÃƒÆ’Ã‚Â  corriger ces deux points.

### T36 : predict.py dans le paquet

```powershell
git mv src/predict.py sentiment_app/predict.py
Copy-Item C:\IA-DEV\tp6-packaging\extraits\predict_compatibilite.py src\predict.py
python -m pytest -q
python src/predict.py "Livraison rapide, produit conforme, trÃƒÆ’Ã‚Â¨s satisfait"
```

&nbsp;

`git mv` dÃƒÆ’Ã‚Â©place le fichier et enregistre le dÃƒÆ’Ã‚Â©placement dans Git : l'historique du fichier est conservÃƒÆ’Ã‚Â©, contrairement ÃƒÆ’Ã‚Â  un dÃƒÆ’Ã‚Â©placement suivi d'un simple commit.

`Copy-Item` recrÃƒÆ’Ã‚Â©e `src/predict.py` comme fichier de compatibilitÃƒÆ’Ã‚Â©. Les anciennes habitudes, comme `python src/predict.py "..."`, continuent de fonctionner. Ce fichier ne contient aucune logique mÃƒÆ’Ã‚Â©tier : il appelle le paquet.

L'attendu est `positive (confiance 78%)`, le score 0,777 arrondi en pourcentage.

**Ordre des commandes.** Le fichier de compatibilitÃƒÆ’Ã‚Â© importe `sentiment_app`. LancÃƒÆ’Ã‚Â© comme script depuis `src/`, Python ne trouve ce paquet que s'il est installÃƒÆ’Ã‚Â©. Si la commande ÃƒÆ’Ã‚Â©choue avec `ModuleNotFoundError: No module named 'sentiment_app'`, lancez d'abord `pip install -e .` (T38), puis reprenez T36.

### T37 : l'API branchÃƒÆ’Ã‚Â©e sur le paquet

```powershell
python -m pytest -q
Select-String -Path api\*.py -Pattern "sys.path"
ruff check .
mypy api
```

&nbsp;

`Select-String` est l'ÃƒÆ’Ã‚Â©quivalent PowerShell de `grep` : il cherche le texte `sys.path` dans les fichiers de l'API. Il ne doit rien trouver, car l'API n'a plus ÃƒÆ’Ã‚Â  modifier le chemin d'import. C'est ce que vÃƒÆ’Ã‚Â©rifie le test `test_l_api_ne_bricole_plus_le_chemin_de_python`.

`ruff check .` contrÃƒÆ’Ã‚Â´le le style et les erreurs courantes, `mypy api` les types. Ni l'un ni l'autre ne doit signaler de problÃƒÆ’Ã‚Â¨me.

### T38 : la commande `sentiment`

```powershell
pip install -e .
sentiment --version
sentiment predict "Livraison rapide, produit conforme, trÃƒÆ’Ã‚Â¨s satisfait"
sentiment predict "xqzvb wlkptr grombu"
sentiment serve
```

&nbsp;

`pip install -e .` lit `pyproject.toml`, installe les dÃƒÆ’Ã‚Â©pendances et crÃƒÆ’Ã‚Â©e la commande `sentiment`. La section `[project.scripts]` indique que `sentiment` appelle la fonction `main` du module `sentiment_app.cli`.

- `sentiment --version` affiche `sentiment-app 0.6.0`, la version dÃƒÆ’Ã‚Â©clarÃƒÆ’Ã‚Â©e dans `pyproject.toml`.  
- `sentiment predict` charge le modÃƒÆ’Ã‚Â¨le puis affiche l'ÃƒÆ’Ã‚Â©tiquette et le score. Pour l'avis positif : `POSITIVE 0.777`. Pour un texte sans mots connus, le score reste sous le seuil d'abstention et la rÃƒÆ’Ã‚Â©ponse est `INDETERMINE 0.5162`.  
- `sentiment serve` lance l'API avec uvicorn sur `http://127.0.0.1:8000`. Ouvrez `/health` pour vÃƒÆ’Ã‚Â©rifier qu'elle rÃƒÆ’Ã‚Â©pond `OK`, puis arrÃƒÆ’Ã‚Âªtez-la avec `Ctrl+C`.

### T39 : construire la roue

```powershell
Remove-Item -Recurse -Force dist -ErrorAction SilentlyContinue
python -m build --wheel
```

&nbsp;

`Remove-Item` supprime les anciennes constructions, pour que `dist/` ne contienne que la version courante. `-ErrorAction SilentlyContinue` ÃƒÆ’Ã‚Â©vite une erreur si le dossier n'existe pas.

`python -m build --wheel` construit la roue dans `dist/`. Le paquet `build` doit ÃƒÆ’Ã‚Âªtre installÃƒÆ’Ã‚Â© (`pip install build`), il ne figure pas forcÃƒÆ’Ã‚Â©ment dans `requirements-dev.txt` : ajoutez-le si la commande ÃƒÆ’Ã‚Â©choue. Ouvrez la roue avec un explorateur d'archives : elle contient `api`, `sentiment_app` et `ui`, mais ni tests, ni donnÃƒÆ’Ã‚Â©es, ni modÃƒÆ’Ã‚Â¨le. Ce tri est dÃƒÆ’Ã‚Â©fini par `[tool.setuptools.packages.find]`.

### T40 : la roue hors du dÃƒÆ’Ã‚Â©pÃƒÆ’Ã‚Â´t

```powershell
cd $env:TEMP
py -3.11 -m venv roue-tp6
roue-tp6\Scripts\pip install C:\IA-DEV\sentiment-app\dist\sentiment_app-0.6.0-py3-none-any.whl
roue-tp6\Scripts\sentiment predict "Livraison rapide, produit conforme, trÃƒÆ’Ã‚Â¨s satisfait"
echo $LASTEXITCODE
$env:SENTIMENT_MODELE = "C:\IA-DEV\sentiment-app\models\sentiment.joblib"
roue-tp6\Scripts\sentiment predict "Livraison rapide, produit conforme, trÃƒÆ’Ã‚Â¨s satisfait"
```

&nbsp;

Cette sÃƒÆ’Ã‚Â©rie simule un utilisateur qui installe le paquet ailleurs. Le venv neuf ne voit ni le dÃƒÆ’Ã‚Â©pÃƒÆ’Ã‚Â´t ni son `.venv`. L'installation tÃƒÆ’Ã‚Â©lÃƒÆ’Ã‚Â©charge les dÃƒÆ’Ã‚Â©pendances depuis PyPI, ce qui peut prendre plusieurs minutes.

La premiÃƒÆ’Ã‚Â¨re prÃƒÆ’Ã‚Â©diction doit ÃƒÆ’Ã‚Â©chouer : le paquet installÃƒÆ’Ã‚Â© ne sait pas oÃƒÆ’Ã‚Â¹ se trouve le modÃƒÆ’Ã‚Â¨le. `$LASTEXITCODE` vaut alors 1 et le message Ãƒâ€šÃ‚Â« modÃƒÆ’Ã‚Â¨le introuvable Ãƒâ€šÃ‚Â» s'affiche. Le modÃƒÆ’Ã‚Â¨le n'est pas dans la roue : il est lourd et n'est pas versionnÃƒÆ’Ã‚Â© dans Git.

On indique ensuite son emplacement avec `SENTIMENT_MODELE`, puis on relance la prÃƒÆ’Ã‚Â©diction, qui affiche `POSITIVE 0.777`. Ce contrÃƒÆ’Ã‚Â´le montre que la roue fonctionne seule, avec pour seule dÃƒÆ’Ã‚Â©pendance externe le modÃƒÆ’Ã‚Â¨le.

### T41 : version, ÃƒÆ’Ã‚Â©tiquette et publication

```powershell
git add -A
git commit -m "Semaine 6 : paquet installable, version 0.6.0"
git tag -a v0.6.0 -m "TP6 : paquet installable"
git push
git push origin v0.6.0
```

&nbsp;

Une ÃƒÆ’Ã‚Â©tiquette (*tag*) fixe un point prÃƒÆ’Ã‚Â©cis de l'historique sous un nom stable. `-a` crÃƒÆ’Ã‚Â©e une ÃƒÆ’Ã‚Â©tiquette annotÃƒÆ’Ã‚Â©e, qui porte un message et un auteur.

`git push` n'envoie pas les ÃƒÆ’Ã‚Â©tiquettes : la derniÃƒÆ’Ã‚Â¨re commande les transmet explicitement ÃƒÆ’Ã‚Â  GitHub. VÃƒÆ’Ã‚Â©rifiez ensuite l'onglet Actions : l'ÃƒÆ’Ã‚Â©tape Ãƒâ€šÃ‚Â« Roue installÃƒÆ’Ã‚Â©e hors du dÃƒÆ’Ã‚Â©pÃƒÆ’Ã‚Â´t (TP6) Ãƒâ€šÃ‚Â» doit passer.

### Membre B, aprÃƒÆ’Ã‚Â¨s le TP6

```powershell
git pull
pip install -e .
python -m pytest -q
sentiment --version
```

&nbsp;

Le membre B rÃƒÆ’Ã‚Â©cupÃƒÆ’Ã‚Â¨re les changements, installe le paquet en mode ÃƒÆ’Ã‚Â©ditable dans son propre venv, puis vÃƒÆ’Ã‚Â©rifie que les tests passent et que la commande rÃƒÆ’Ã‚Â©pond `sentiment-app 0.6.0`. Ces commandes prouvent que le dÃƒÆ’Ã‚Â©pÃƒÆ’Ã‚Â´t fonctionne pour les deux membres, et pas seulement sur le poste qui a ÃƒÆ’Ã‚Â©crit le code.