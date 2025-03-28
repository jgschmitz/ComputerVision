# Pseudocode for GPT-4V with openai-python
from openai import OpenAI
client = OpenAI()

image_path = "id_card.jpg"
with open(image_path, "rb") as img:
    result = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {"role": "user", "content": [
                {"type": "text", "text": "Extract name, ID number, and expiration date."},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_encoded_image}"}}]}
        ]
    )
print(result.choices[0].message.content)
