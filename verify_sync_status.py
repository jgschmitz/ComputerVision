import fiftyone as fo
from pymongo import MongoClient

client = MongoClient("your_atlas_uri")
atlas_ids = {doc["id_number"] for doc in client["id_cards"]["extracted_fields"].find()}
dataset = fo.load_dataset("id_cards_demo")
local_ids = {sample["id_number"] for sample in dataset}

missing = local_ids - atlas_ids
print(f"Missing in MongoDB: {missing}")
