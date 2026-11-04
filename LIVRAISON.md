\# Notice d'installation : sentiment-app 0.6.0



Bonjour, voici votre application d'analyse de sentiments.



\## 1. Installation

Ouvrez un terminal et installez le paquet fourni :

pip install sentiment\_app-0.6.0-py3-none-any.whl



\## 2. Configuration du modèle

Le paquet contient le code, mais pas le modèle d'IA (trop lourd). Indiquez le chemin du fichier sentiment.joblib fourni :

$env:SENTIMENT\_MODELE = "C:\\chemin\\vers\\sentiment.joblib"



\## 3. Utilisation

\- En ligne de commande : sentiment predict "Votre avis ici"

\- Lancer l'API : sentiment serve

\- Lancer l'interface web : sentiment ui

