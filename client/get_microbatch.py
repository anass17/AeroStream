import requests
import re

url = "http://127.0.0.1:8000/api/batch"

response = requests.get(url)

if response.status_code != 200:
    print("Error! Could not load data from the API")
    exit()

data = response.json()

### Nettoyer et prétraiter les nouveaux avis

for item in data:
    item['text'] = re.sub(r'@[^\s]+', '', item['text'])
    item['text'] = re.sub(r'\s+', ' ', item['text'])
    item['text'] = item['text'].strip()

print(data)