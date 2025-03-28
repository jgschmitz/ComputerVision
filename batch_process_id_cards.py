import os, pytesseract
from PIL import Image
from pymongo import MongoClient

client = MongoClient("your_atlas_uri")
collection = client["id_cards"]["extracted_fields"]

folder = "./id_images"

for filename in os.listdir(folder):
    if filename.endswith((".jpg", ".png")):
        path = os.path.join(folder, filename)
        img = Image.open(path)
        text = pytesseract.image_to_string(img)

        doc = {
            "file": filename,
            "text": text,
        }

        collection.insert_one(doc)
