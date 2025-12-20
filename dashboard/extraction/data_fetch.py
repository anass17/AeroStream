
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from sqlalchemy import select, func, case
import os


def intiate_db():

    db_host = os.environ["POSTGRES_HOST"]
    db_pass = os.environ["POSTGRES_PASSWORD"]
    db_user = os.environ["POSTGRES_USER"]
    db_port = os.environ["POSTGRES_PORT"]
    db_name = os.environ["POSTGRES_DB"]

    ### Create prediction table if it does not exit

    DATABASE_URL = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(bind=engine)

    Base = declarative_base()

    class Prediction(Base):
        __tablename__ = "predictions"

        id = Column(Integer, primary_key=True)

        label = Column(String(10))
        text = Column(Text)
        airline = Column(String(50))
        airline_sentiment_confidence = Column(Float)
        negativereason = Column(String(50))
        tweet_created = Column(DateTime(timezone=True))
        
        predicted_at = Column(DateTime(timezone=True), server_default=func.now())

    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    return [db, Prediction]



##### Calculer le volume de tweets par compagnie

def tweets_count_per_airline(db, Prediction):

    stmt = (
        select(Prediction.airline, Prediction.label, func.count(Prediction.airline))
        .group_by(Prediction.airline, Prediction.label)
        .order_by(func.count(Prediction.airline).desc())
    )
    result = db.execute(stmt)

    data = result.all()

    return data
    


##### Calculer la répartition des sentiments

def sentiments_distribution(db, Prediction):

    stmt = (
        select(Prediction.label, func.count(Prediction.label))
        .group_by(Prediction.label)
        .order_by(func.count(Prediction.label).desc())
    )

    result = db.execute(stmt)

    data = result.all()

    return data


##### Calculer le nombre de tweet par date

def tweet_count_per_date(db, Prediction):
    stmt = (
        select(
            func.date(Prediction.tweet_created).label("date"),
            func.count().label("count")
        )
        .group_by(func.date(Prediction.tweet_created))
        .order_by(func.date(Prediction.tweet_created))
    )

    result = db.execute(stmt).all()

    return result



##### Calculer le taux de satisfaction par compagnie

def satisfaction_rate_per_airline(db, Prediction):

    stmt = select(Prediction.airline, func.count(Prediction.label)).group_by(Prediction.airline).order_by(Prediction.airline)
    result = db.execute(stmt)
    total_tweets_count = result.all()

    stmt = select(Prediction.airline, func.count(Prediction.label)).where(Prediction.label == 'positive').group_by(Prediction.airline).order_by(Prediction.airline)
    result = db.execute(stmt)
    positive_tweets_count = result.all()

    rates = []

    for i in range(len(total_tweets_count)):
        rate = round( ( positive_tweets_count[i][1] / total_tweets_count[i][1] ) * 100, 1)
        airline_rate = [ positive_tweets_count[i][0], rate]

        rates.append(airline_rate)

    return rates



##### Identifier les causes principales des avis négatifs

def identify_main_causes(db, Prediction):
    
    stmt = select(
        Prediction.negativereason, 
        func.count(Prediction.negativereason)
    ).where(
        Prediction.label == 'negative',
        Prediction.negativereason.is_not(None)
    ).group_by(
        Prediction.negativereason
    ).order_by(func.count(Prediction.negativereason).desc()).limit(7)

    result = db.execute(stmt)

    data = result.all()

    return data



##### Statistiques générales

def generale_statistics(db, Prediction):

    stmt = select(func.count(Prediction.label))
    result = db.execute(stmt)
    tweets = result.first()[0]

    stmt = select(func.count(func.distinct(Prediction.airline)))
    result = db.execute(stmt)
    airlines = result.first()[0]

    stmt = select(func.count(Prediction.label)).where(Prediction.label == "negative")
    result = db.execute(stmt)
    negatives = result.first()[0]

    negative_rate = round((negatives / tweets) * 100, 1)

    return [tweets, airlines, negative_rate]


##### 

def detailled_data(db, Prediction):
    stmt = (
        select(
            Prediction.airline.label("airline"),
            func.count().label("total_tweets"),
            func.sum(
                case((Prediction.label == "negative", 1), else_=0)
            ).label("negative_tweets"),
            func.sum(
                case((Prediction.label == "positive", 1), else_=0)
            ).label("positive_tweets"),
            func.sum(
                case((Prediction.label == "neutral", 1), else_=0)
            ).label("neutral_tweets"),
        )
        .group_by(Prediction.airline)
    )

    result = db.execute(stmt).all()

    return result