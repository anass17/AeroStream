from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
import requests

def fetch_data():
    try:
        response = requests.get(url='http://localhost:8000/api/batch')
    except:
        print("Error !!! Could not fetch data")
        return
    
    if response.status_code != 200:
        print("Error !!! Response is not success")
        return

    data = response.json()

    print(data)

with DAG(
    dag_id="test",
    description="hh",
    schedule_interval="* * * * *",
    start_date=datetime(2025, 1, 1),
    catchup=False
):
    
    task_1 = PythonOperator(
        task_id = "first_task",
        python_callable=fetch_data
    )

    task_1