import sys
from airflow.models import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator
from datetime import datetime


with DAG('dag', schedule_interval='@daily', 
         start_date=datetime(2020, 1, 1), catchup=False) as dag:

    @task.docker(
        image="quay.io/bitnami/python:3.9",
        network_mode="bridge",
        api_version="auto",
    )
    def containerized():
        import random
        print("executing containerized task change")
        print(f"{sys.platform}")
        return [random.random() for _ in range(100)]

    start_task = BashOperator(
        task_id='start',
        bash_command='echo "{{ task_instance_key_str }}" && sleep 1'
    )

    numbers = containerized()

    end_task = BashOperator(
        task_id='end',
        bash_command='echo "run_id={{ run_id }} | dag_run={{ dag_run }}"'
    )

    start_task >> numbers >> end_task