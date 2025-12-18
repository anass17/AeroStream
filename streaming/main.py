import requests
import re

batch_url = "http://127.0.0.1:8000/api/batch"
predict_url = "http://127.0.0.1:8000/api/predict"

response = requests.get(batch_url)

if response.status_code != 200:
    print("Error! Could not load data from the API")
    exit()

data = response.json()

### Nettoyer et prétraiter les nouveaux avis

for item in data:
    item['text'] = re.sub(r'@[^\s]+', '', item['text'])
    item['text'] = re.sub(r'\s+', ' ', item['text'])
    item['text'] = item['text'].strip()

### Générer les prédictions de sentiment

payload = {
    "texts": [item['text'] for item in data]
}

predict_response = requests.post(predict_url, json=payload)

print(predict_response.json())
