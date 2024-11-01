from pymongo import MongoClient
import pandas as pd
import csv
from datetime import datetime

# Se connecte à la base en cloud et nous la retourne
def get_database():
    connection_string = "mongodb+srv://renaud:7PfyHUZrRy4HW2SF@cluster0.rhmbu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(connection_string)
    return client['twitter']

# Importe un doucment csv dans la base Mongo
# et retourne le nombre d'élément dans 
def import_csv_file(database, coll_name, file_path, separator="\t"):
    collection = database[coll_name]
    collection.delete_many({})
    data = open(file_path, 'r', encoding='utf-8')

    reader = csv.DictReader(data, delimiter=separator)
    header = reader.fieldnames

    count = 0

    for each in reader:
        row = {}
        for field in header:
            row[field] = each[field]
        collection.insert_one(row)
        count += 1

    return count

# Rentre les données dans la bd depuis les fichiers csv.
# Retourne un dictionnaire avec le nombre d'insertions pour chaque
# collection
def init_db():
    results = {}
    db = get_database()
    results['users'] = import_csv_file(db, 'users', './Data/tw_user.csv')
    results['tweets'] = import_csv_file(db, 'tweets', './Data/tweet.csv','<')

def add_user(id_user, screen_name, name, description, location, lang):
    user = {
        'idUser' : id_user,
        'screenName' : screen_name,
        'name' : name,
        'description' : description,
        'location' : location,
        'lang' : lang,
        'url' : 'https://twitter.com/' + screen_name,
        'createdAt' : datetime.today().strftime("DD/MM/YY"),
        'nbStatuses' : 0,
        'nbFavorites' : 0,
        'nbFollowers' : 0,
        'nbFollowing' : 0
    }
    db = get_database()
    collection = db['users']
    collection.insert_one(user)

def delete_user(id_user):
    db = get_database()
    collection = db['users']
    collection.delete_one({ "idUser" : id_user })

def get_user_by_id(user_id):
    db = get_database()
    collection = db['users']
    return collection.find_one({ "idUser" : user_id })

def add_tweet(id_tweet, id_user, text, source, lang, reply_id_tweet = "", reply_id_user = "", quoted_id_tweet = "", quoted_id_user = ""):
    user = get_user_by_id(id_user)
    tweet = {
        'idTweet' : id_tweet,
        'idUser' : id_user,
        'replyIdTweet' : reply_id_tweet,
        'replyIdUser' : reply_id_user,
        'quotedIdTweet' : quoted_id_tweet,
        'quotedIdUser' : quoted_id_user,
        'text' : text,
        'createdAt' : datetime.today().strftime("DD/MM/YY"),
        'url' : 'https://twitter.com/' + user['screenName'] + '/status/' + id_tweet,
        'source' : source,
        'lang' : lang,
        'nbRetweet' : 0,
        'nbFavorites' : 0
    }
    db = get_database()
    collection = db['tweets']
    collection.insert_one(tweet)

def delete_tweet(id_tweet):
    db = get_database()
    collection = db['tweets']
    collection.delete_one({ "idTweet" : id_tweet })

def get_tweet_by_id(tweet_id):
    db = get_database()
    collection = db['tweets']
    return collection.find_one({ "idTweet" : tweet_id })