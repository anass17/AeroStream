from fastapi import FastAPI
from api.routers.batch import router as batch_router
from api.routers.predict import router as predict_router


app = FastAPI(
    title="AeroStream",
    version="1.0.0"
)

# Register routers
app.include_router(batch_router, prefix="/api", tags=["Batch"])
app.include_router(predict_router, prefix="/api", tags=["Predict"])


@app.get("/")
def root():
    return {
        "message": "API is running",
        "routes":
            {
                'Batch': '/api/batch',
                'Predict': '/api/predict',
            }
    }