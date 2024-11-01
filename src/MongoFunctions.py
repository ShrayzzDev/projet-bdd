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
def import_csv_file(database, coll_name, file_path):
    collection = database[coll_name]
    data = open(file_path, 'r', encoding='utf-8')

    reader = csv.DictReader(data, delimiter='\t')
    header = reader.fieldnames

    count = 0

    for each in reader:
        row = {}
        for field in header:
            row[field] = each[field]
        collection.insert_one(row)
        count += 1

    return count