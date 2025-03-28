import streamlit as st
from pymongo import MongoClient
from PIL import Image

client = MongoClient("your_atlas_uri")
collection = client["id_cards"]["extracted_fields"]

query = st.text_input("Search name or ID")
if query:
    docs = collection.find({"$text": {"$search": query}})
    for doc in docs:
        st.image(doc["image_path"])
        st.json(doc)
