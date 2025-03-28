# ComputerVision
let’s build out your workflow in a notebook-first setup using:  Voxel51 (FiftyOne) for visualizing and annotating ID card images  MongoDB Atlas to store the extracted fields as structured metadata  (Optional) OCR or Vision LLMs to extract the text fields from the image

### 🪪 ID Card Extraction, Visualization, and Atlas Sync Pipeline

#### 🔧 Setup & Imports
```python
import fiftyone as fo
import pytesseract
from pymongo import MongoClient
from PIL import Image
```

#### 🔧 Configuration
```python
IMAGE_PATH = "id_card.jpg"  # Replace with your actual image file path
MONGODB_URI = "mongodb+srv://<user>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority"
DB_NAME = "id_cards"
COLLECTION_NAME = "extracted_fields"
```

---

### 📸 Step 1: Load the Image and Run OCR
```python
img = Image.open(IMAGE_PATH)
text = pytesseract.image_to_string(img)
print(text)
```

---

### 📄 Step 2: Extract Basic Fields (Simulated for Now)
```python
extracted = {
    "name": "Jane Doe",
    "id_number": "12345678",
    "dob": "1990-01-01",
    "expiration": "2025-12-31",
    "image_path": IMAGE_PATH
}
```

---

### 🧪 Step 3: Visualize in FiftyOne
```python
dataset = fo.Dataset("id_cards_demo")
sample = fo.Sample(filepath=IMAGE_PATH)

# Add extracted fields to sample
for key, value in extracted.items():
    if key != "image_path":
        sample[key] = value

dataset.add_sample(sample)
session = fo.launch_app(dataset)
```

---

### ✍️ Step 4: Edit in FiftyOne UI
Make changes in the FiftyOne GUI.
Once done, return to this cell and run the next cell to sync.
```python
input("Edit the fields in the FiftyOne UI, then press ENTER to continue...")
```

---

### 🔁 Step 5: Sync Back to MongoDB Atlas
```python
client = MongoClient(MONGODB_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

updated_sample = dataset.first()

# Prepare document for MongoDB
doc = {
    "name": updated_sample.get("name"),
    "id_number": updated_sample.get("id_number"),
    "dob": updated_sample.get("dob"),
    "expiration": updated_sample.get("expiration"),
    "image_path": updated_sample.filepath
}

collection.update_one(
    {"id_number": doc["id_number"]},
    {"$set": doc},
    upsert=True
)
print("\n✅ Sync complete! Data pushed to MongoDB Atlas.")
```
