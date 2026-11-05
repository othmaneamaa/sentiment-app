# Semaine 4 : tests approfondis et qualité, notes du binôme

> Une à deux pages. Uniquement des chiffres issus de VOS exécutions.

## 1. Couverture

- Avant (étape A) : **91 %**, lignes jamais exécutées : **6** — `api/main.py` lignes 49, 77-79, 85-87.
- Pour chacune, le comportement qu'aucun test ne vérifiait :
  - ligne 49 : le 503 quand le modèle n'est pas chargé ;
  - lignes 77-79 : le 500 quand le modèle plante ;
  - lignes 85-87 : le lancement direct (`uvicorn.run`), jamais exécuté sous pytest.
- Après (étape D) : **97,47 %** (97 % arrondi) ; lignes exclues de la mesure : **83-85** (`if __name__ == "__main__"`), qui ne s'exécutent pas sous pytest. Avec cette exclusion, la couverture atteint **100 %**.

## 2. Défauts trouvés

| Symptôme | Test qui l'a révélé | Correction |
| --- | --- | --- |
| Texte fait d'espaces (`" "`, `"\x85"`) accepté par le schéma, puis refusé par `predict()` sous forme de **chaîne** au lieu de la liste Pydantic | `tests/test_limites.py::test_frontieres_du_contrat[espaces]` et `test_texte_de_blancs_recoit_422` (hypothesis) | `field_validator` dans `api/schemas.py` : refuse un texte vide une fois ses blancs retirés, avec la même règle que `predict()` |
| Toute `ValueError` du modèle convertie en **422 avec le message interne** (fuite d'information) | `tests/test_integration.py::test_modele_en_panne_renvoie_500_sans_message_interne[ValueError]` | Suppression de la conversion `ValueError → 422` dans `api/main.py` ; toute panne renvoie 500 sans message interne, avec `raise ... from None` |
| Label hors contrat (`PEUT_ETRE`) accepté par la réponse (200 au lieu de 500) | `tests/test_integration.py::test_etiquettes_inconnues_renvoient_500` | `Literal["POSITIVE", "NEGATIVE", "INDETERMINE"]` dans `PredictResponse` (`api/schemas.py`) |

## 3. Seuil d'abstention

- Trois points de la courbe (`python src/courbe_seuil.py`) :
  - 0,50 : 58 réponses (100 %), exactitude 0,879, 7 erreurs, 0 vers un humain ;
  - 0,60 : 42 réponses (72 %), exactitude 0,952, 2 erreurs, 16 vers un humain ;
  - 0,70 : 37 réponses (64 %), exactitude 1,000, 0 erreur, 21 vers un humain.
- Seuil retenu : **0,60** ; part des avis envoyés à un humain : **28 %** (16 sur 58) ; justification : on élimine 5 des 7 erreurs pour un peu plus d'un quart d'abstentions. À 0,70, on n'a plus aucune erreur, mais 36 % d'abstentions, ce qui coûte trop cher en couverture.

## 4. Jeu d'or

- Bilan (`python src/bilan_jeu_or.py`) : justes **9**, abstentions **10**, erreurs franches déclarées **1**.
- Ce que ces chiffres disent du modèle : il ne se trompe plus franchement que sur un avis, celui déclaré en `erreur_connue` (« Franchement déçu, je ne commanderai plus », négation `ne...plus`). Les 10 abstentions portent sur les avis mitigés, ironiques ou ambigus : c'est le comportement attendu, l'abstention élimine les erreurs franches au prix d'un passage à l'humain.

## 5. Outils statiques

- Remarques au départ : ruff **16**, mypy **0** (`Success: no issues found in 4 source files`).
- Parmi les défauts de la partie 2, combien ruff et mypy avaient-ils signalés ? **Aucun directement** : ruff signalait B904 (raise sans `from`) dans `api/main.py`, qui est la conséquence du défaut « ValueError → 422 avec message interne », mais pas le défaut lui-même. mypy ne signalait rien, parce que `predict()` renvoyait un `dict` (tout ce qui en sort est `Any`). Conclusion : les outils statiques attrapent la forme (imports, types, raises), pas la logique (fuite d'information, label hors contrat). Ce sont les tests d'intégration et de limites qui révèlent les défauts de comportement.

## 6. Biais : le modèle sert-il tous les avis de la même façon ? (étape F)

- `python src/biais.py`, au seuil 0.60 : les **17 avis avec retournement** n'ont que **0.588** d'exactitude (7 erreurs, 15 vers un humain, 2 erreurs restantes), contre **1.000** pour les **41 avis directs**.
- Les avis longs (27 avis, 0.741) semblent moins bien servis que les courts (31 avis, 1.000), mais la longueur n'est pas la cause : les **10 avis longs sans retournement** sont tous justes. C'est le retournement qui fait échouer le modèle, et la longueur n'est qu'un facteur confondant (un avis qui se retourne est forcément plus long).
- Question ouverte : l'abstention ne règle pas ce biais, elle le déplace. 15 des 17 avis avec retournement partent vers un humain : le client n'est plus mal classé, mais ce sont les agents qui absorbent le travail sur ce groupe. Avec des groupes de 17 et 41 avis, ces écarts restent à confirmer sur un jeu plus grand.
