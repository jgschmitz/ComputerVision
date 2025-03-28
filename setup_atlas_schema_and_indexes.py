from pymongo import MongoClient, ASCENDING

client = MongoClient("your_atlas_uri")
collection = client["id_cards"]["extracted_fields"]

collection.create_index([("id_number", ASCENDING)], unique=True)
collection.create_index("expiration")

# Optional: Add validation
client["id_cards"].command({
    "collMod": "extracted_fields",
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["id_number", "name", "expiration"],
            "properties": {
                "id_number": {"bsonType": "string"},
                "expiration": {"bsonType": "string"},
            }
        }
    }
})
