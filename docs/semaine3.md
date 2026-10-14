# Semaine 3 — Seuil d'incertitude

## Seuil retenu

Nous conservons le seuil par défaut `SEUIL_INCERTITUDE = 0.60` dans `ui/helpers.py` : en dessous de 60 % de confiance, l'interface n'affiche pas de verdict tranché mais « À vérifier par un agent » en orange.

## Combien d'avis cela envoie à un agent

Sur les 290 avis du jeu de démonstration, l'interface annonce **XX avis à vérifier** (soit environ **XX %**), à comparer aux 145 négatifs détectés. Ce sont principalement des avis mitigés, du type « bon puis mauvais » ou l'inverse, là où le sac de mots hésite parce que les deux moitiés se contredisent.

## Pourquoi ce compromis est juste

Avec un seuil plus bas (0,50), le modèle trancherait seul des cas qu'il ne maîtrise pas et laisserait passer des erreurs coûteuses — un client mécontent classé positif serait traité en retard. Avec un seuil plus haut (0,75), la file humaine se remplirait au point que l'automatisation perdrait tout intérêt. Le seuil de 0,60 nous paraît le bon équilibre : il n'envoie à un agent que les cas réellement douteux, et il rend visible l'hésitation du modèle au lieu de la cacher.

## Aperçu de l'application

### Onglet « Un avis » — cas incertain

![Cas mitigé classé « à vérifier »](captures/semaine3-un-avis.png)

### Onglet « Un fichier CSV » — traitement par lot

![Traitement par lot sur les 290 avis](captures/semaine3-csv.png)

