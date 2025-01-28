from pymongo import MongoClient
from pprint import pprint

MONGO_URI = "mongodb://localhost:27017"
client = MongoClient(MONGO_URI)
db = client.admin
dbs_list = db.command("listDatabases")
pprint(dbs_list)
