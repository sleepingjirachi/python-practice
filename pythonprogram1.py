from dotenv import load_dotenv
import os
import certifi
from pymongo import MongoClient

load_dotenv()

uri = os.getenv("MONGO_URI")
if not uri:
    raise RuntimeError("MONGO_URI not found")

client = MongoClient(
    uri,
    tls=True,
    tlsCAFile=certifi.where()
)

db = client["test_db"]
collection = db["pokemon"]

collection.insert_one({
    "name": "Jirachi",
    "type": "Steel"
})

print("Data inserted!")
