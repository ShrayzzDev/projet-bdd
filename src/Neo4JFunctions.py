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

# Importe rudimentaires des personnes dans la base neo4j*
# ces personnes servent simplement à pouvoir être identifiée dans des liens
# Pour plus de détails sur les personnes, veuillez requêter la base mongo
def import_persons_csv(file_path, separator="\t"):
    URI = os.getenv("NEO4J_URI")
    AUTH = (os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))
    data = open(file_path, 'r', encoding='utf-8')

    reader = csv.DictReader(data, delimiter=separator)

    count = 0

    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.execute_query("""
            MATCH (p:Person)
            DETACH DELETE p
            """
        )
        for each in reader:
            count += 1

    return count
# Importe rudimentaires des tweets dans la base neo4j*
# ces tweets servent simplement à pouvoir être identifiée dans des liens
# Pour plus de détails sur les tweets, veuillez requêter la base mongo
def import_tweets_csv(file_path, separator="<"):
    URI = os.getenv("NEO4J_URI")
    AUTH = (os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))
    data = open(file_path, 'r', encoding='utf-8')

    reader = csv.DictReader(data, delimiter=separator)

    count = 0


    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.execute_query("""
            MATCH (t:Tweet)
            DETACH DELETE t
            """
        )
        for each in reader:
            driver.execute_query(
                "CREATE (:Tweet {id: $id})",
                id=each['idTweet']
            )
            count += 1

    return count

def delete_user_by_id(user_id):
    URI = os.getenv("NEO4J_URI")
    AUTH = (os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))

    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.execute_query("""
            MATCH (p:Person {id: $id})
            DETACH DELETE p
            """,
            id = user_id
        )


def delete_tweet_by_id(user_id):
    URI = os.getenv("NEO4J_URI")
    AUTH = (os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))

    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.execute_query("""
            MATCH (t:Tweet {id: $id})
            DETACH DELETE t
            """,
            id = user_id
        )

def add_user(user_name,user_id):
    URI = os.getenv("NEO4J_URI")
    AUTH = (os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))

    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.execute_query(
            "CREATE (:Person {name: $name, id: $id})",
            name=user_name,
            id=user_id
        )

def add_tweet(tweet_id):
    URI = os.getenv("NEO4J_URI")
    AUTH = (os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))

    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.execute_query(
            "CREATE (t:Tweet {id: $id})",
            id = tweet_id
        )