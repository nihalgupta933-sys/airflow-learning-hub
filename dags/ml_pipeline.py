from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

def preprocess_data():
    print("preprocessing data...")

def train_model():
    print("Training model...")

def evaluate_model1():
    print("Evaluate models")

with DAG(
    'ml_pipeline',
    start_date=datetime(2025, 4, 22), 
    schedule='@weekly'
) as dag:

    preprocess = PythonOperator(
        task_id="preprocess_task",
        python_callable=preprocess_data
    )
    
    train = PythonOperator(
        task_id="train_task",
        python_callable=train_model
    )
    
    evaluate = PythonOperator(
        task_id="evaluate_task",
        python_callable=evaluate_model1
    )
    
    preprocess >> train >> evaluate
