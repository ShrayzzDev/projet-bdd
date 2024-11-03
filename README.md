# projet-bdd

L'ajout de donnée étant écrit sans trop réfléchir à sa vitesse, il est très lent surtout quand on parle à un base dans le cloud, mais ça fonctionne bien.

## Dépendances

Ce projet nécessite les packets pythons suivants:

- python-dotenv
- pandas
- pymango
- neo4j
- matplotlib
  
## Comment utiliser ?

Il est possible qu'il puisse fonctionner étant donné que je fourni mes indentifiants a mes instances.  
Cependant, il est possible qu'elle soit down si elle ne sont pas utilisés.  
Pour pouvoir utiliser d'autres instances, il faut changer :  

- Pour MongoDB : La connection string ligne 16 dans le fichier MongoFunctions.py. MongoDB Cloud fourni la connection string quand l'instance est créée.
- Pour Neo4j : Dans le même esprit, Neo4j aura fourni un fichier qui contient tout ce dont il a besoin. Renommez ce fichier en "neo4j_credentials.txt" et remplacez celui qu'il y a dans ./Data

## Ce qui fonctionne

Le programme peut importer les fichiers csv dans la base. Utilisé uniquement pour les fichiers utilisateurs et tweets du jeu de données fourni, mais la fonction est générique et devrait donc fonctionner pour tout. On peut aussi récupérer individuellement un utilisateur ou un tweet via son id. On peut aussi en insérer ou supprimer. On peut incrémenter des valeur aussi (utile pour l'ajout du compteur de follower.)  
  
Pour Neo4j, il y a des méthodes qui permettent d'importer des utilisateurs simples (nom + id) et des tweets simples (id seulement) pour pouvoir créer des relations. Possibilité de supprimer, ajouter, etc . . . comme pour la base MongoDB. La relation follow fonctionne, mais la relation de retweets n'a pas été implémentée.  
  
Il y a un graphe, sous forme de nuage de points, qui est généré qui fait un lien entre le nombre de follower d'un utilisateur.
