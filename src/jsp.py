import MongoFunctions as mongo
import Neo4JFunctions as neo4j
from datetime import datetime

def init_db():
    # print(mongo.init_db())
    print(neo4j.import_persons_csv('./Data/tw_user.csv'))
    print(neo4j.import_tweets_csv('./Data/tweet.csv'))

neo4j.init_connection()
init_db()
neo4j.init_followers('./Data/tw_user_follow.csv')
mongo.add_user("040112","shrayzz","moi","guilty gear c'est très bien", "clermont", "fr")
print(mongo.get_user_by_id("040112"))
mongo.add_tweet("040112","040112","elphelt = queen", "mon pc", "fr")
print(mongo.get_tweet_by_id("040112"))
mongo.delete_user("040112")
print(mongo.get_user_by_id("040112"))
mongo.delete_tweet("040112")
print(mongo.get_tweet_by_id("040112"))