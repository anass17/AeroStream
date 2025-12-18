from fastapi import FastAPI
from pydantic import BaseModel
import joblib as jb
from sentence_transformers import SentenceTransformer

app = FastAPI()

log_reg = jb.load('./models/ml/logistic_regression_cv.pkl')
encoder = jb.load('./models/encoders/encoder_clean.pkl')
emb_model = SentenceTransformer('intfloat/e5-large-v2')

class Text(BaseModel):
    text: str

@app.post("/predict")
def predict(data: Text):

    embeddings = emb_model.encode([data.text], normalize_embeddings=True, convert_to_numpy=True)

    prediction = log_reg.predict(embeddings)

    class_name = encoder.inverse_transform(prediction)[0]

    return {
        "Label": str(class_name)
    }