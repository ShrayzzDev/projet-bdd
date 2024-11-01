import MongoFunctions as mongo
import Neo4JFunctions as neo4j

# mongo.init_db()
mongo.add_user("040112","shrayzz","moi","guilty gear c'est très bien", "clermont", "fr")
print(mongo.get_user_by_id("040112"))
mongo.add_tweet("040112","040112","elphelt = queen", "mon pc", "fr")
print(mongo.get_tweet_by_id("040112"))
mongo.delete_user("040112")
neo4j.init_connection()