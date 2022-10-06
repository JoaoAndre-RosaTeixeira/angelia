# angelia
le futur de la musique

Angelia est une intelligence artificielle qui prédit si un titre a une chance d'être dans le TOP 50 ou pas.

Pour utilisé cette IA il vous faudra les données d'une musique qui respecte certains parametres.

C'est parametre sont : Energy,duration,explicit,dancability,loudness, speechness,accoustisness,instrumentalness,liveness,valence,tempo.

Ces données devront êtres dans un Fichier csv.

En ayant completer les conditions l'IA vous predira si votre chansons a une chance d'être dans le TOP 50 ou pas.

IMPORTANT ! 
Cette IA n'a pas un taux de réussite a 100% ce qui signifie qu'il y a une marge d'erreur.

Pour crée cette IA nous avons :

Analyse des Données
Fait une Visualisation avec les parametres Popularity et Followers de l'artiste
Création de la heatmap grace a Seaborn

Nous avons testées 3 algorithmes pour l'IA.
2 Algorithmes de Regression et 
1 de classification

Arbre de Regression multiple
Regression lineaire multiples
Regression Logistique

Resultat obtenu : R squared: 0.21
accuracy 0.87

Pour utilisé cette IA il faut les parametres demander dans un fichier csv


la v1 pouvant etre ameliorer nous avons des pistes pour une v2 qui serait :
  - Amelirorer notre jeux de données en joignant des tables qui nous permettrait d'obtenir plus de data (années, popularité d'artiste et de genre) 
  - ameliorer le dashboard et l'interface graphique
  - ajouter l'ia a l'interface graphique (trouver la source de l'erreur)
