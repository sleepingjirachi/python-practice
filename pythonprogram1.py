import certifi
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://py:sleepingjirachi@cluster0.vlvh7vg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
    tlsCAFile=certifi.where()
)
db = client.my_database
collection = db.my_collection

# Insert multiple sample documents
sample_data = [
    {"name": "Jirachi", "type": "Steel", "level": 5},
    {"name": "Pikachu", "type": "Electric", "level": 10},
    {"name": "Bulbasaur", "type": "Grass", "level": 7},
    {"name": "Charmander", "type": "Fire", "level": 8}
]

# Use insert_many to add all documents at once
collection.insert_many(sample_data)

# Query and print all documents to verify
for doc in collection.find():
    print(doc)