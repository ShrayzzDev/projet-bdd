import matplotlib.pyplot as plt
import MongoFunctions

# Affiche un graphe avec le rapport entre
# le nombre de tweets likés d'un utilisateurs
# et son nombre de followers
def show_nb_followers_by_likes():
    listFollowers = []
    listLikes = []
    print()
    for each in MongoFunctions.get_likes_and_follower():
        listFollowers.append(each['nbFollowers'])
        listLikes.append(each['nbFavorites'])
    
    plt.plot(listLikes,listFollowers)
    plt.title('nombre de likes par nombres de followers')

    plt.show()
