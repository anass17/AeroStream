from fastapi import APIRouter
from pydantic import BaseModel
import joblib as jb
from sentence_transformers import SentenceTransformer

router = APIRouter()

log_reg = jb.load('./models/ml/logistic_regression_cv.pkl')
encoder = jb.load('./models/encoders/encoder_clean.pkl')
emb_model = SentenceTransformer('intfloat/e5-large-v2')

class Text(BaseModel):
    text: str

@router.post("/predict")
def predict(data: Text):

    embeddings = emb_model.encode([data.text], normalize_embeddings=True, convert_to_numpy=True)

    prediction = log_reg.predict(embeddings)

    class_name = encoder.inverse_transform(prediction)[0]

    return {
        "label": str(class_name)
    }