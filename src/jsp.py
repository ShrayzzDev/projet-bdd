import MongoFunctions as mongo
import Neo4JFunctions as neo4j

# mongo.init_db()
print(mongo.get_user_by_id("262671176"))
mongo.add_user("040112","shrayzz","moi","guilty gear c'est très bien", "clermont", "fr")
print(mongo.get_user_by_id("040112"))
mongo.delete_user("040112")
neo4j.init_connection()