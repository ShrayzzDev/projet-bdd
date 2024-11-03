import MongoFunctions as mongo
import Neo4JFunctions as neo4j
import graphs as graph
from datetime import datetime

def init_db():
    print(mongo.init_db())
    print(neo4j.import_persons_csv('./Data/tw_user.csv'))
    print(neo4j.import_tweets_csv('./Data/tweet.csv'))

neo4j.init_connection()
# init_db()

graph.show_nb_followers_by_likes()