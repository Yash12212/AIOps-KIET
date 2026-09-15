#importing the required libraries
from datetime import datetime 
from airflow.providers.standard.operators.python import PythonOperator
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

#maiking the function for the start task
'''
1) Data collection
2) Data preprocessing
3)Anomaly Detection
4)Save the results
'''
def collect_data():
    print("Collecting the server data")
    print("CPU usage: 92")
    print("Memory usage: 78")
    print("Error logs: 12")

def process_data():
    print("Processing the server data")
    
def detect_anomalies():
    cpu=92
    if(cpu>80):
        print("ALERT: Anomaly detected in CPU usage")
    else:
        print("CPU usage is normal")

def save_results():
    print("Saving the results to the database......")

#making the DAG
with DAG(
    dag_id="aiops_pipeline",
    start_date=datetime(2026,9,9),
    schedule=None,
    catchup=False
) as dag:
    collect=PythonOperator(
        task_id="collect_data",
        python_callable=collect_data
    )
    process=PythonOperator(
        task_id="process_data",
        python_callable=process_data
    )
    detect=PythonOperator(
        task_id="detect_anomalies",
        python_callable=detect_anomalies
    )
    save=PythonOperator(
        task_id="save_results",
        python_callable=save_results
    )

    collect >> process >> detect >> save #making the dependency between the tasks
