from  pymongo import MongoClient
import pymongo
url = "mongodb+srv://admin:admin@atlascluster.omkgj.mongodb.net/?retryWrites=true&w=majority"
from pymongo import mongo_client
client = MongoClient(url)
db = client.pytech

students = db.students

Baggins={
    "student_id": "1007",
    "first_name":"Bilbo",
    "last_name":"Baggins"
}
Baggins_student_id = students.insert_one(Baggins).inserted_id

Oakenshield = {
    "student_id": "1008",
    "first_name":"Thorin",
    "last_name":"Oakenshield"
}
Oakenshield_student_id = students.insert_one(Oakenshield).inserted_id

McCracken={
    "student_id": "1009",
    "first_name":"Chris",
    "last_name":"McCracken"
}
McCracken_student_id = students.insert_one(McCracken).inserted_id
print(f"\nInserted student record", Oakenshield, Oakenshield_student_id)
print(f"\nInserted student record", Baggins, Baggins_student_id)
print(f"\nInserted student record", McCracken, Oakenshield_student_id)

for doc in docs:
    print(doc)

doc = db.students.find_one({'student_id"':"1007"})
print(f"\n")
print("Display student document from find one:")
print(f"\n")
print(doc)