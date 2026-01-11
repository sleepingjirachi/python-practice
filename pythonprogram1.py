import os
import certifi
from pymongo import MongoClient

# Get URI from environment variable
mongo_uri = os.environ.get("MONGO_URI")

if not mongo_uri:
    raise RuntimeError("MONGO_URI not set")

# Connect to MongoDB
client = MongoClient(
    mongo_uri,
    tlsCAFile=certifi.where()
)

# Choose database and collection
db = client.test_database
collection = db.pokemon

# Insert test data
data = {
    "name": "Jirachi",
    "type": "Steel",
    "level": 5
}

result = collection.insert_one(data)

print("Inserted document ID:", result.inserted_id)

# Verify insert
for doc in collection.find():
    print(doc)
