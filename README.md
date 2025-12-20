Ce README est en français. Pour la version anglaise, voir [README_en.md](README_en.md).

# AeroStream
AeroStream est un système intelligent de classification des avis clients des compagnies aériennes en temps réel, basé sur le NLP et le machine learning. Il combine Batch et Streaming pour analyser le sentiment, générer des KPI et visualiser les résultats via Streamlit, avec orchestration assurée par Airflow.


## installation:

#### Créer une base de données

docker exec -it aerostream-postgres psql -U postgres 
CREATE DATABASE aerostream

#### Supprimer l'utilisateur `admin`
docker exec -it aerostream-airflow airflow users delete --username admin

#### Créer un nouveau utilisateur
docker exec -it aerostream-airflow airflow users create --username admin  --firstname Admin --lastname User --role Admin --email admin --password admin