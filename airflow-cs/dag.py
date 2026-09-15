from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

def start_task():
        print("Aiops pipeline started")

def process_task():
        print("Processing the server data")

def finish_task():
      print("Aiops pipeline completed")
    
with DAG(
dag_id="my_first_aiops_dag",
start_date=datetime(2026,9,8),
schedule=None,
catchup=False
) as dag:
        start=PythonOperator(
            task_id="start_task",
            python_callable=start_task,
        )
        process=PythonOperator(
            task_id="process_task",
            python_callable=process_task,
        )
        end=PythonOperator(
            task_id="finish_task",
            python_callable=finish_task,
        )

        start >> process >> end