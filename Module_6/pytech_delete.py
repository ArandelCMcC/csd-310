from  pymongo import MongoClient
import pymongo
url = "mongodb+srv://admin:admin@atlascluster.omkgj.mongodb.net/?retryWrites=true&w=majority"
from pymongo import mongo_client
client = MongoClient(url)
db = client.pytech
students = db.students


docs = db.students.find({})
print("\n displaying find() query")
for doc in docs:
    print("Student ID: " + doc["student_id"] + "\nFirst Name: " + doc["first_name"] + "\nLast Name: " + doc["last_name"] + "\n")


# insert()
Chris = {
    "student_id": "1010",
    "first_name": "Chris",
    "last_name": "McCracken"
    }

Chris_student_id = students.insert_one(Chris).inserted_id

print("\n")
print("document inserted" + str(Chris))

# find_one()
Chris = students.find_one({"student_id": "1010"})
print("Student ID: " + Chris["student_id"] + "\nFirst Name: " + Chris["first_name"] + "\nLast Name: " + Chris["last_name"] + "\n")

# student_id
print("\n -student list-")
for doc in docs:
    print("Student ID: " + doc["student_id"] + "\nFirst Name: " + doc["first_name"] + "\nLast Name: " + doc["last_name"] + "\n")

# Call delete_one() method to remove student_id 1010
students.delete_one({"student_id": "1010"})

# output ids
print("\n deleted")
for doc in docs:
    print("Student ID: " + doc["student_id"] + "\nFirst Name: " + doc["first_name"] + "\nLast Name: " + doc["last_name"] + "\n")
