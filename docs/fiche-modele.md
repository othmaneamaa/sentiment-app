# Fiche modèle : sentiment-app

> Une fiche modèle dit, en une page, ce que fait le modèle, sur quelles données il a appris, ce qu'il
> vaut, où il se trompe et dans quelles conditions on peut s'en servir. Remplacez chaque consigne par
> votre texte ; les lignes qui commencent par « > » ne comptent pas. Les tests vérifient que chaque
> rubrique est remplie et que les chiffres cités sont ceux du dépôt.

## Identité du modèle

> Nom, version du paquet (celle de sentiment_app.__version__), date d'entraînement, type de modèle.

Classifieur de sentiment `sentiment-app`, livré avec le paquet `sentiment_app` en version 0.6.0. C'est un
pipeline scikit-learn 1.5 : vectorisation TF-IDF (mots et paires de mots), puis régression logistique à deux
classes, `positive` et `negative`. Le modèle mesuré ici a été entraîné le 2026-10-21 sur le jeu de
démonstration (`python src/train.py`, sans option) ; le fichier `models/sentiment.joblib` n'est ni dans Git
ni dans la roue.

## Usage prévu

> Pour qui, pour quelle décision, dans quel flux de travail (relation client, avis en français).

Trier des avis clients en français, courts et écrits sur un site de vente (livraison, produit, service
client), pour que l'équipe de relation client traite d'abord les avis négatifs. Le modèle passe par l'API
(`/predict`), qui ajoute un seuil d'abstention : sous 0.60 de confiance, l'avis est marqué `INDETERMINE` et
part vers une personne. La page Streamlit et la commande `sentiment predict` passent par la même API.

## Usages exclus

> Ce pour quoi le modèle ne doit pas servir : au moins deux cas.

- Décider seul d'une sanction, d'un remboursement ou d'un refus pour un client : le modèle trie, il ne juge pas.
- Évaluer un employé, un livreur ou un vendeur à partir des avis qui le citent.
- Analyser des textes d'un autre domaine (santé, politique, réseaux sociaux) ou d'une autre langue que le
  français : il n'a rien appris de tels textes.
- Détecter l'ironie, la menace ou une urgence : il n'a que deux classes, et aucune ne couvre ces cas.

## Données d'entraînement

> Source, taille, répartition des classes, langue, domaine ; ce que ces données ne couvrent pas.

Jeu de démonstration généré par `src/make_demo.py` : 290 avis en français sur le commerce en ligne, 145
positifs et 145 négatifs, dont 100 avis mitigés et 30 neutres, volontairement difficiles. Découpage : 232
avis d'entraînement, 58 de test. Ces avis sont synthétiques, construits à partir de tournures répétées : ils
ne couvrent ni les fautes de frappe, ni l'argot, ni les avis très longs, ni les autres domaines. Le dépôt
peut aussi entraîner sur le jeu public Allociné (`--allocine`, 20 000 critiques de films, F1 macro 0,920),
mais ce n'est pas le modèle décrit dans cette fiche.

## Performances mesurées

> Le F1 macro et le rappel des négatifs, tels que dans models/metrics.json ; le seuil d'abstention de
> l'API et ce qu'il change (part des avis traités, erreurs restantes, avis envoyés à un humain).

Sur les 58 avis de test (`models/metrics.json`) : F1 macro 0.879, exactitude 0.879, rappel des négatifs
0.931, soit 7 erreurs. Le seuil d'acceptation fixé au TP2 est 0.85 : il est atteint. Avec le seuil
d'abstention de l'API à 0.60 (`python src/courbe_seuil.py`), le modèle répond à 42 avis sur 58 (72 %),
avec une exactitude de 0.952 et 2 erreurs restantes ; les 16 autres avis partent vers un humain. À 0.70,
il ne fait plus d'erreur, mais n'en traite plus que 64 %.

## Limites connues

> Les cas où le modèle se trompe, avec un exemple : ce que montrent l'étape F du TP2 et le jeu d'or.

Le modèle se trompe surtout sur les avis qui se retournent (« mais », « sauf que », « ensuite ») : les 7
erreurs du test sont toutes de ce type. Exemple : « Taille trop petite et retour payant au déballage, sauf
que ensuite produit conforme à la description, très satisfait » est classé `negative` à 0.5335. Sur le jeu
d'or du binôme (20 avis), 9 sont justes, 10 partent en abstention et 1 est une erreur franche : « Franchement
déçu, je ne commanderai plus » est donné `POSITIVE` à 0.67. La négation (« pas mauvais, mais pas bon non
plus ») reste mal comprise : un test du jeu d'or est marqué xfail pour cette raison.

## Biais mesurés

> Les groupes d'avis moins bien servis, chiffres de python src/biais.py à l'appui.

`python src/biais.py`, sur les 58 avis de test, au seuil 0.60 : les 17 avis avec retournement n'ont que
0.588 d'exactitude (7 erreurs, 15 vers un humain, 2 erreurs restantes), contre 1.000 pour les 41 avis
directs. Les avis longs (27 avis, 0.741) semblent moins bien servis que les courts (31 avis, 1.000), mais la
longueur n'est pas la cause : les 10 avis longs sans retournement sont tous justes. Les effectifs sont
petits, ces écarts sont donc des signaux à confirmer sur de vraies données. L'abstention protège le client,
mais elle reporte ces avis difficiles sur les agents.

## Explicabilité

> Ce que montre python src/expliquer.py : les termes qui pèsent le plus, et ce que cela révèle.

Avec SHAP (`python src/expliquer.py`), les termes qui poussent le plus vers `positive` sont « je » (+0.771),
« que je » (+0.764) et « en » (+0.683) ; vers `negative`, « cassé » et « arrivée » (-0.923), puis « au »
(-0.689). Des mots-outils pèsent donc autant que des mots de sentiment : le modèle a appris les tournures du
jeu de démonstration, pas seulement le sens. Sur l'avis mitigé, 20 termes vers `negative` (-1.0061) battent
de peu 13 termes vers `positive` (+0.9177), ce qui explique sa confiance de 0.5335.

## Conditions d'usage

> Ce qu'un humain doit vérifier, quand, et ce qu'on ne doit jamais décider sur la seule foi du modèle.

Un humain relit tous les avis `INDETERMINE` (confiance sous 0.60) et un échantillon des avis `NEGATIVE`
avant toute action envers le client. Il relit aussi les avis qui contiennent un retournement, même tranchés,
puisque c'est le groupe le moins bien servi. Aucune décision qui touche un client (remboursement, refus,
blocage de compte) ne se prend sur la seule foi du modèle. Le score affiché est une confiance du modèle, pas
une probabilité d'avoir raison.

## Maintenance

> Quand réentraîner, avec quelle version de scikit-learn, comment indiquer le modèle au paquet.

Réentraîner avec `python src/train.py` quand les données changent, puis mettre à jour cette fiche :
`tests/test_fiche_modele.py` échoue si le F1 cité n'est plus celui de `models/metrics.json`. Entraîner et
relire avec scikit-learn 1.5, la version épinglée par le paquet et la CI : un modèle produit par une autre
version provoque `AttributeError: 'LogisticRegression' object has no attribute 'multi_class'`. Le paquet
trouve le modèle par la variable `SENTIMENT_MODELE` ; sans elle, il cherche `models/sentiment.joblib` à la
racine du dépôt.
