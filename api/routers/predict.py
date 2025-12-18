from fastapi import APIRouter
from pydantic import BaseModel
import joblib as jb
from sentence_transformers import SentenceTransformer

router = APIRouter()

log_reg = jb.load('./models/ml/logistic_regression_cv.pkl')
encoder = jb.load('./models/encoders/encoder_clean.pkl')
emb_model = SentenceTransformer('intfloat/e5-large-v2')

class Texts(BaseModel):
    texts: list[str]

@router.post("/predict")
def predict(data: Texts):

    embeddings = emb_model.encode(data.texts, normalize_embeddings=True, convert_to_numpy=True)

    predictions = log_reg.predict(embeddings)

    class_names = encoder.inverse_transform(predictions).tolist()

    return {
        "predictions": class_names
    }