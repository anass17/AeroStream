
from db.database import Base, engine, SessionLocal
from db.tables.prediction import Prediction

def insert_predictions(data, predictions):

    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        for i in range(len(predictions)):
            prediction = Prediction(
                text=data[i]['text'],
                label=predictions[i]
            )
            db.add(prediction)
            
        db.commit()

        print("Les données ont été stockées avec succès !")
    except:
        print("Échec du stockage des données.")
    finally:
        db.close()