# Semaine 5 : l'interface, notes du binôme

> Trois questions, quelques phrases chacune. Répondez avec ce que vous avez observé.

## 1. Pourquoi l'interface n'importe-t-elle jamais `predict()` ni le fichier `.joblib` ?

Parce que l'interface est un client de l'API, pas un classifieur. Elle ne connaît que `ui/client.py` et les codes HTTP (200, 422, 503). Si elle importait `predict()` ou `.joblib`, elle dupliquerait la logique de l'API, et un modèle réentraîné demanderait de modifier l'interface. C'est la troisième règle d'architecture du guide : « les clients passent par l'API, jamais par le fichier .joblib ».

## 2. Que montre l'interface quand le modèle hésite, et pourquoi est-ce mieux qu'un verdict forcé ?

Elle affiche « Je ne sais pas : à faire vérifier par un humain », avec le score (52 %), et un message d'information (« La confiance est sous le seuil d'abstention : un humain doit trancher »). C'est mieux qu'un verdict forcé parce qu'un avis mitigé ou ironique, classé à tort POSITIVE ou NEGATIVE, induirait le client en erreur. L'abstention renvoie l'avis à un humain, qui tranche avec le contexte.

## 3. Que voit l'utilisateur quand l'API tombe ? Et le fichier `data/avis_exemple.csv` : combien d'avis partent vers un humain ?

En haut de la page, une erreur rouge « API injoignable : lancez d'abord uvicorn api.main:app ». La page ne plante pas : elle reste affichée, avec ses onglets, mais signale que l'API est arrêtée. Si l'utilisateur clique sur « Analyser », il voit le même message dans la zone de résultat.

Pour `data/avis_exemple.csv`, le résumé affiché est `{'INDETERMINE': 1, 'NEGATIVE': 2, 'POSITIVE': 3}` : sur les 6 avis du fichier, **1 seul part vers un humain** (le verdict `INDETERMINE`), les 5 autres reçoivent un verdict automatique.