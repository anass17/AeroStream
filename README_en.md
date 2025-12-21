This README is written in English. For the French version, see [README.md](README.md).

# AeroStream – Automated Customer Review Classification System

## Project Context

AeroStream aims to develop an intelligent system capable of automatically classifying customer reviews related to airline services. The main objective is to analyze customer satisfaction levels based on textual data extracted from user reviews.

This project combines NLP, machine learning, vector databases, and interactive visualization to provide real-time insights into customer satisfaction.

---

## Objectives

The system aims to:

- Collect and preprocess customer reviews
- Automatically analyze sentiment and satisfaction
- Generate performance indicators per airline
- Visualize results through an interactive dashboard

---

## Batch Pipeline

The batch pipeline is designed to prepare and process historical data and includes the following steps:

- **Data loading:** Import customer review datasets from Hugging Face
- **Exploratory Data Analysis (EDA):** Study class distributions, data distributions, and key statistics
- **Data cleaning:** Handle duplicates, missing values, and clean text data
- **Embedding generation:** Transform text into vector representations using NLP models (Sentence Transformers)
- **Metadata and embedding storage:** Store labels and vectors in a ChromaDB vector database, with separate collections for training and testing data
- **Model training and evaluation:** Train classification models and select the best-performing model for future predictions
- **Deployment via REST API:** Expose the trained model for production inference

---

## Streaming Pipeline

The streaming pipeline processes customer reviews in near real time:

- **Data ingestion:** Collect customer reviews via the API in micro-batches
- **Data preparation:** Clean and preprocess incoming reviews for sentiment prediction
- **Result storage:** Store predicted reviews in a PostgreSQL database
- **Aggregation and KPIs:**
    - Number of tweets per airline
    - Sentiment distribution per airline
    - Customer satisfaction rate per airline
    - Identification of the main causes of negative tweets
- **Visualization:** Interactive Streamlit dashboard displaying key KPIs, automatically updated with each data ingestion cycle
- **Automation:** Full pipeline orchestration using Airflow, scheduled to run every minute

---

## Technologies Used

- **Python** for data processing and machine learning
- **Docker** for application containerization
- **Sentence Transformers** for NLP
- **ChromaDB** for embedding management
- **PostgreSQL** for result storage
- **Streamlit** for the interactive dashboard
- **Airflow** for pipeline orchestration

---

## System Benefits

- Real-time customer satisfaction analysis
- Centralized management of historical and streaming data
- Clear and interactive visualization of key KPIs
- Fully automated pipeline for continuous customer feedback monitoring

---

## Installation

### Prerequisites

Make sure you have the following installed:

- Git
- Docker
- Docker Compose

### 1. Clone the repository

```Bash
git clone https://github.com/anass17/AeroStream.git
cd AeroStream
```

### 2. Generate the `.env` file

Create the `.env` file from the provided example:

```Bash
cp .env.example .env
```

Then open the `.env` file and adjust the variables if necessary.

### 3. Build and start Docker services

- Build Docker images:

```Bash
docker-compose build
```

- Start all services:

```Bash
docker-compose up -d
```

- Verify that containers are running correctly:

```Bash
docker-compose ps
```

### 4. Create the PostgreSQL database

- Access the PostgreSQL container:

```Bash
docker exec -it aerostream-postgres psql -U postgres
```

- Create the database:

```Bash
CREATE DATABASE aerostream;
```

- Verify database creation:

```Bash
\l
```

- Exit PostgreSQL:

```Bash
\q
```

### 5. Create an Airflow user

- Delete the default admin user:

```Bash
docker exec -it aerostream-airflow airflow users delete --username admin
```

- Create a new Airflow admin user:

```Bash
docker exec -it aerostream-airflow airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin --password admin
```

You may change the credentials according to your preferences.

### 6. Verify Airflow and DAGs

- Access the Airflow web interface:

```
http://localhost:8080
```

### 7. Verify the API

- Test that the API is accessible:

```Bash
curl http://localhost:8000/
```

- Access the API documentation:

```
http://localhost:8000/docs
```

### 8. Verify the Streamlit dashboard

- Access the dashboard:

```
http://localhost:8501
```

---

### Structure

```
📁 AeroStream
│
├── 📁 notebooks
│   ├── 📄 01_loading.ipynb             # Load raw data
│   ├── 📄 02_eda.ipynb                 # Exploratory Data Analysis (EDA)
│   ├── 📄 03_preprocessing.ipynb       # Data cleaning and preprocessing
│   ├── 📄 04_embeddings.ipynb          # Embedding vector generation
│   ├── 📄 05_storage_chroma_db.ipynb   # Store embeddings in ChromaDB
│   └── 📄 06_model_training.ipynb      # ML model training and evaluation
│
├── 📁 data
│   ├── 📁 raw                          # Raw data
│   ├── 📁 processed                    # Cleaned and processed data
│   ├── 📁 embeddings                   # Embedding vectors
│   └── 📁 chromaDB                     # Collections stored in ChromaDB
│
├── 📁 api
│   └── 📁 routers                      # API route definitions
│
├── 📁 dashboard
│   ├── 📁 components                   # Reusable UI components
│   ├── 📁 extraction                   # Data extraction logic
│   ├── 📁 pages                        # Dashboard pages
│   └── 📄 app.py                       # Streamlit application entry point
│
├── 📁 airflow
│   └── 📁 dags
│       ├── 📁 tasks                    # Individual DAG tasks
│       └── 📄 aerostream_pipeline_dag.py # Main Airflow DAG
│
├── 📁 models
│   ├── 📁 encoders                     # Encoder models
│   └── 📁 ml                           # Machine learning models
│
├── 📁 docker                           # Dockerfiles
├── 📁 docs                             # Project documentation
├── 📁 pgdata                           # PostgreSQL data files
├── 📁 requirements                    # Dependencies for each Docker service
├── 📄 docker-compose.yml               # Docker Compose configuration
├── 📄 .env                             # Environment variables
├── 📄 README.md                        # Project documentation (French)
├── 📄 README_en.md                     # Project documentation (English)
└── 📄 .gitignore                       # Git ignore rules
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