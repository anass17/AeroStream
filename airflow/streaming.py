import requests
import re
from tasks.fetch import fetch_data
from tasks.clean import clean_data
from tasks.predict import generate_predictions
from tasks.stock import insert_predictions

API_BATCH_URL = "http://127.0.0.1:8000/api/batch"
API_PREDICT_URL = "http://127.0.0.1:8000/api/predict"

### Récupérer les données

data = fetch_data(API_BATCH_URL)

if (not data):
    print("Error! Could not fetch data")
    exit()

### Nettoyer et prétraiter les nouveaux avis

data = clean_data(data)

### Générer les prédictions de sentiment

predictions = generate_predictions(API_PREDICT_URL, data)

if (not predictions):
    print("Error! Could not generate predictions for the provided data")
    exit()

### Stockage dans la base de données

insert_predictions(data, predictions)