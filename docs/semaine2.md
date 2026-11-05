# Semaine 2 — Analyse des erreurs

Sur les 58 avis du jeu de test, le modèle se trompe 7 fois : 5 avis positifs classés négatifs et 2 avis négatifs classés positifs (ces 2 faux positifs sont les plus coûteux, car un client mécontent serait traité en retard).

Toutes ces erreurs portent sur des avis mitigés du type « bon puis mauvais » ou l'inverse, parce qu'un sac de mots ne tient pas compte de l'ordre : les deux formulations produisent le même vecteur, et le modèle suit la première moitié au lieu de la conclusion.

Pour corriger cela, il faudrait un modèle sensible à l'ordre des mots — par exemple des n-grammes (1-2 ou 1-3) ou un transformer (DistilBERT/CamemBERT), qui pèserait davantage la fin de l'avis, là où se trouve l'étiquette.

Ce que révèle l'explication SHAP (`python src/expliquer.py`) : parmi les termes les plus influents figurent des mots-outils, « je » (+0.771), « en » (+0.683) et « au » (-0.689), à côté de « cassé » (-0.923). Le modèle a donc appris les tournures du jeu de démonstration, pas seulement les mots porteurs de sentiment ; sur l'avis mitigé, 20 termes vers negative (-1.0061) l'emportent de peu sur 13 termes vers positive (+0.9177), d'où une confiance de 0.5335 seulement.
