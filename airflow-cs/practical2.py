from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def collect_data():
    print("Collecting data from the server....")
    print("CPU usage: 70")
    print("Memory usage: 80")
    print("Error rate: 15")

def process_data():
    print("Processing the collected data....")

def detect_anomalies():
    CPU =70
    if CPU > 80:
        print("ALERT: Anomaly detected in CPU usage")
    else:
        print("NORMAL: No anomalies detected in CPU usage")

def saving_results():
    print("Saving the results to the database....")

with DAG(
    dag_id="practical2_aiops_dag",
    start_date=datetime(2026, 9, 14),
    schedule=None,
    catchup=False
) as dag:
    collect = PythonOperator(
        task_id="collect_data",
        python_callable=collect_data,
    )

    process = PythonOperator(
        task_id="process_data",
        python_callable=process_data,
    )

    detect = PythonOperator(
        task_id="detect_anomalies",
        python_callable=detect_anomalies,
    )

    saving = PythonOperator(
        task_id="saving_results",
        python_callable=saving_results,
    )

    collect >> process >> detect >> saving
    