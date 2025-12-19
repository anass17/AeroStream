
from db.database import Base, engine, SessionLocal
from db.tables.prediction import Prediction

def insert_predictions(data, predictions):

    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        for i in range(len(predictions)):
            prediction = Prediction(
                text=data[i]['text'],
                label=predictions[i],
                airline = data[i]['airline'],
                airline_sentiment_confidence = data[i]['airline_sentiment_confidence'],
                negativereason = data[i]['negativereason'],
                tweet_created = data[i]['tweet_created']
            )
            db.add(prediction)
            
        db.commit()

        print("Les données ont été stockées avec succès !")
    except:
        print("Échec du stockage des données.")
    finally:
        db.close()