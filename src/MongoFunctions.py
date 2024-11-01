from pymongo import MongoClient
import pandas as pd
import csv

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