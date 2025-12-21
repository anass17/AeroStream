Ce README est en français. Pour la version anglaise, voir [README_en.md](README_en.md).

# AeroStream – Système de classification automatique des avis clients

## Contexte du projet

AeroStream souhaite développer un système intelligent capable de classifier automatiquement les avis clients relatifs aux services des compagnies aériennes. L’objectif principal est d’analyser le niveau de satisfaction des clients à partir des données textuelles issues des avis utilisateurs.

Ce projet combine NLP, machine learning, bases vectorielles et visualisation interactive pour fournir des insights en temps réel sur la satisfaction des clients.

---

## Objectifs

Le système a pour but de :

- Collecter et prétraiter les avis clients.
- Analyser automatiquement le sentiment et la satisfaction.
- Générer des indicateurs de performance par compagnie aérienne.
- Visualiser les résultats via un tableau de bord interactif.

---

## Pipeline Batch

Le pipeline batch permet de préparer et traiter les données historiques et comprend les étapes suivantes :

- **Chargement des données** :Import des datasets d’avis clients depuis Hugging Face.
- **Analyse exploratoire des données (EDA)**: Étude des distributions, des classes et des statistiques principales.
- **Nettoyage des données**: Gestion des doublons, valeurs manquantes et nettoyage du texte.
- **Génération des embeddings**: Transformation des textes en vecteurs à l’aide de modèles NLP (Sentence Transformers).
- **Stockage des métadonnées et embeddings**: Sauvegarde des labels et vecteurs dans une base vectorielle ChromaDB, avec distinction des collections pour données d’entraînement et de test.
- **Entraînement et évaluation des modèles**: Construction des modèles de classification et sélection du meilleur modèle pour les prédictions futures.
- **Déploiement via API REST**: Le modèle entraîné est exposé pour des requêtes en production.

---

## Pipeline Streaming

Le pipeline streaming permet de traiter les avis clients en quasi-temps réel :

- **Récupération des données :** Collecte des avis clients via l’API en micro-batch.
- **Préparation des données :** Nettoyage et prétraitement des nouveaux avis pour prédiction.
- **Stockage des résultats :** Enregistrement des prédictions dans une base PostgreSQL.
- **Agrégation et KPI :**
    - Nombre de tweets par compagnie aérienne
    - Répartition des sentiments par compagnie
    - Taux de satisfaction par compagnie
    - Identification des principales causes de tweets négatifs
- **Visualisation :** Tableau de bord interactif Streamlit affichant les KPI principaux, mis à jour automatiquement à chaque récupération des données.
- **Automatisation :** Orchestration complète via Airflow, avec exécution programmée toutes les minutes.

---

## Technologies utilisées

- **Python** pour le traitement et le ML
- **Docker** pour la dockerisation de l'application
- **Sentence Transformers** pour le NLP
- **ChromaDB** pour la gestion des embeddings
- **PostgreSQL** pour le stockage des résultats
- **Streamlit** pour le dashboard interactif
- **Airflow** pour l’orchestration du pipeline

---

## Avantages du système

- Analyse en temps réel de la satisfaction client.
- Centralisation des données historiques et nouvelles dans un même système.
- Visualisation claire et interactive des KPI clés.
- Automatisation complète pour un suivi continu de la satisfaction des clients.

---

## Installation

### Prérequis

Assurez-vous d’avoir installé :

- Git
- Docker
- Docker Compose

### 1. Cloner le dépôt

```Bash
git clone https://github.com/anass17/AeroStream.git
cd AeroStream
```

### 2. Générer le fichier `.env`

- Créer le fichier `.env` à partir de l’exemple fourni :

```Bash
cp .env.example .env
```

Ensuite, ouvrez le fichier `.env` et adaptez les variables si nécessaire.

### 3. Construire et lancer les services Docker

- Construire les images Docker :

```Bash
docker-compose build
```

- Démarrer tous les services :

```Bash
docker-compose up -d
```

- Vérifier que les conteneurs sont bien lancés :

```Bash
docker-compose ps
```

### 4. Créer la base de données PostgreSQL

- Accéder au conteneur PostgreSQL :

```Bash
docker exec -it aerostream-postgres psql -U postgres 
```

- Créer la base de données :

```Bash
CREATE DATABASE aerostream;
```

- Vérifier la création :

```Bash
\l
```

- Quitter PostgreSQL :

```Bash
\q
```

### 5. Créer un utilisateur Airflow

- Supprimer l'utilisateur `admin`

```Bash
docker exec -it aerostream-airflow airflow users delete --username admin
```

- Créer un nouveau utilisateur

```Bash
docker exec -it aerostream-airflow airflow users create --username admin  --firstname Admin --lastname User --role Admin --email admin --password admin
```

Modifiez vos identifiants selon vos préférences.

### 6. Vérifier Airflow et les DAGs

- Accéder à l’interface Airflow :

```Bash
URL : http://localhost:8080
```

### 7. Vérifier l’API

- Tester que l’API est bien accessible :

```Bash
curl http://localhost:8000/
```

- Accéder à la documentation de l'API

```
http://localhost:8000/docs
```

### 8. Vérifier le dashboard Streamlit

- Accéder au dashboard :

```
http://localhost:8501
```

---

## Structure des fichiers

```
📁 AeroStream
│
├── 📁 notebooks
│   ├── 📄 01_loading.ipynb             # Charger les données brutes
│   ├── 📄 02_eda.ipynb                 # Analyse exploratoire des données (EDA)
│   ├── 📄 03_preprocessing.ipynb       # Nettoyage et prétraitement des données
│   ├── 📄 04_embeddings.ipynb          # Génération des vecteurs d'embeddings
│   ├── 📄 05_storage_chroma_db.ipynb   # Stockage des embeddings dans ChromaDB
│   └── 📄 06_model_training.ipynb      # Entraînement et Évaluation des modèles ML
│
├── 📁 data
│   ├── 📁 raw                          # Données brutes
│   ├── 📁 processed                    # Données nettoyées
│   ├── 📁 embeddings                   # Vecteurs d’embeddings
│   └── 📁 chromaDB                     # Collections stockées dans ChromaDB
│
├── 📁 api
│   └── 📁 routers                      # Définition des routes de l'API
│
├── 📁 dashboard
│   ├── 📁 components                   # Composants réutilisables pour l'interface
│   ├── 📁 extraction                   # Logique d'extraction des données
│   ├── 📁 pages                        # Pages du tableau de bord
│   └── 📄 app.py                       
│
├── 📁 airflow
│   └── 📁 dags
│       ├── 📁 tasks                            # Tâches individuelles des DAGs
│       └── 📄 aerostream_pipeline_dag.py       # DAG principal pour Airflow
│
├── 📁 models
│   ├── 📁 encoders                     # Modèles d'encodage
│   └── 📁 ml                           # Modèles de machine learning
│
├── 📁 docker                           # Dockerfiles
├── 📁 docs                              
├── 📁 pgdata                           # Fichiers de données PostgreSQL
├── 📁 requirements                     # Dépendances de chaque docker service
├── 📄 docker-compose.yml               
├── 📄 .env                             
├── 📄 README.md                        
├── 📄 README_en.md                     # La version anglaise de README
└── 📄 .gitignore                     
```

---

## Visualisations

### Interface Streamlit

![Streamlit UI](https://github.com/user-attachments/assets/883039ab-2919-4c9c-a29d-1508a40f5d3e)

### Interface Airflow

![Airflow UI](https://github.com/user-attachments/assets/1ffe1001-1031-426d-b6ac-cc71b4637287)

### API Endpoints

![API](https://github.com/user-attachments/assets/b81946b5-9c6d-42f7-8a25-7b418d566255)

### Architecture

![Architecture](https://github.com/user-attachments/assets/3841e38b-63cd-468e-870d-42222abf5419)