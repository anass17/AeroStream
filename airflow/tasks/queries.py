from db.database import SessionLocal
from db.tables.prediction import Prediction
from sqlalchemy import select, func

##### Calculer le volume de tweets par compagnie

def tweets_count():

    db = SessionLocal()

    stmt = (
        select(Prediction.airline, func.count(Prediction.airline))
        .group_by(Prediction.airline)
        .order_by(func.count(Prediction.airline).desc())
    )
    result = db.execute(stmt)

    data = result.all()

    return data
    