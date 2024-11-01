import dotenv
import os
from neo4j import GraphDatabase
import csv

# Charge les identifiants et vérifie que la connexion est possible
def init_connection():    
    load_status = dotenv.load_dotenv("./Data/neo4j_credentials.txt")
    if load_status is False:
        raise RuntimeError('Environment variables not loaded.')

    URI = os.getenv("NEO4J_URI")
    AUTH = (os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))

    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()
        print("Connection established.")

# Importe un doucment csv dans la base Mongo
# et retourne le nombre d'élément dans 
def import_persons_csv(file_path, separator="\t"):
    URI = os.getenv("NEO4J_URI")
    AUTH = (os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))
    data = open(file_path, 'r', encoding='utf-8')

    reader = csv.DictReader(data, delimiter=separator)

    count = 0

    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        for each in reader:
            driver.execute_query(
                "CREATE (:Person {name: $name, id: $id})",
                name=each['screenName'],
                id=each['idUser']
            )

    return count