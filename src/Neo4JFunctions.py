import dotenv
import os
from neo4j import GraphDatabase

URI = ""
AUTH = ("","")

def init_connection():    
    load_status = dotenv.load_dotenv("./Data/neo4j_credentials.txt")
    if load_status is False:
        raise RuntimeError('Environment variables not loaded.')

    URI = os.getenv("NEO4J_URI")
    AUTH = (os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))

    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()
        print("Connection established.")