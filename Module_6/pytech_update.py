from unittest import removeResult
from  pymongo import MongoClient
import pymongo
url = "mongodb+srv://admin:admin@atlascluster.omkgj.mongodb.net/?retryWrites=true&w=majority"
from pymongo import mongo_client
client = MongoClient(url)
db = client.pytech
result = db.students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Bilbo"}})
print(db.students.find_one({"student_id":"1007"}))