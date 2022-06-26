from  pymongo import MongoClient
import pymongo
url = "mongodb+srv://admin:admin@atlascluster.omkgj.mongodb.net/?retryWrites=true&w=majority"
from pymongo import mongo_client
client = MongoClient(url)
db = client.pytech
print(db.list_collection_names())