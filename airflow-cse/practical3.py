from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
import time

def check_server_status():
    print("Checking server status...")
    time.sleep(2)  # Simulating a delay for checking server status
    print("Server is up and running.")

def collect_server_metrics():
    print("Collecting server metrics...")
    time.sleep(2)  # Simulating a delay for collecting metrics
    print("CPU: 72")
    print("Memory: 65")
    print("Error Logs: 5")

def analyze_metrics():
    print("Analyzing server metrics...")
    time.sleep(2)  # Simulating a delay for analyzing metrics
    cpu_usage = 72
    if cpu_usage > 90:
        print("ALERT: High CPU usage detected!")
        raise Exception("High CPU usage")
    
    print("Server metrics are normal.")

def generate_report():
    print("Generating report...")
    time.sleep(2)  # Simulating a delay for generating report
    print("Report generated successfully.")

with DAG(
    dag_id="practical3",
    start_time=datetime(2026,9,15),
    schedule=None,
    catchup=False
) as dag:
    check=PythonOperator(
        task_id="check_server",
        python_callable=check_server_status
    )
    collect=PythonOperator(
        task_id="collect_metric",
        python_callable=collect_server_metrics
    )
    analyze=PythonOperator(
        task_id="analyze_metric",
        python_callable=analyze_metrics,
        retries= 2,             #retry and retry delay
        retry_delay= 10
    )
    report=PythonOperator(
        task_id="generate_report",
        python_callable=generate_report
    )

    check >> collect >> analyze >> report
