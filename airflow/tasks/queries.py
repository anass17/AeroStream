from db.database import SessionLocal
from db.tables.prediction import Prediction
from sqlalchemy import select, func

##### Calculer le volume de tweets par compagnie

def tweets_count_per_airline():

    db = SessionLocal()

    stmt = (
        select(Prediction.airline, func.count(Prediction.airline))
        .group_by(Prediction.airline)
        .order_by(func.count(Prediction.airline).desc())
    )
    result = db.execute(stmt)

    data = result.all()

    return data
    


##### Calculer la répartition des sentiments

def sentiments_distribution():
    
    db = SessionLocal()

    stmt = (
        select(Prediction.label, func.count(Prediction.label))
        .group_by(Prediction.label)
        .order_by(func.count(Prediction.label).desc())
    )

    result = db.execute(stmt)

    data = result.all()

    return data



##### Calculer le taux de satisfaction

def satisfaction_rate():

    db = SessionLocal()

    stmt = select(func.count(Prediction.label))
    result = db.execute(stmt)
    total_tweets_count = (result.first())[0]

    stmt = select(func.count(Prediction.label)).where(Prediction.label == 'positive')
    result = db.execute(stmt)
    positive_tweets_count = (result.first())[0]

    return {"total": total_tweets_count, "positive": positive_tweets_count}