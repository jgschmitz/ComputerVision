from pymongo import MongoClient
import pandas as pd

client = MongoClient("your_atlas_uri")
collection = client["id_cards"]["extracted_fields"]

docs = list(collection.find({"expiration": {"$lt": "2025-01-01"}}))
df = pd.DataFrame(docs)
df.to_csv("expired_ids.csv")

# Optional: delete them
collection.delete_many({"expiration": {"$lt": "2025-01-01"}})
