import MongoFunctions as mongo

aura = "VmaizN0uVsUGTIbu6-0H_aYXsexRwxrwpD_siLuRCOs"

db = mongo.get_database()
print(mongo.import_csv_file(db, 'users', './Data/tw_user.csv'))