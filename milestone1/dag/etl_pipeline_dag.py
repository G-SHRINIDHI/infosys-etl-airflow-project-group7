from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Default arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1),
    'retries': 1
}

# Define DAG
with DAG(
    dag_id='milestone1_etl_pipeline',
    default_args=default_args,
    schedule=None,   # Manual trigger only
    catchup=False
) as dag:

    # Task 1: Create Tables
    create_tables = BashOperator(
        task_id='create_tables',
        bash_command='python3 ~/airflow/scripts/create_tables.py'
    )

    # Task 2: Load Data
    load_data = BashOperator(
        task_id='load_data',
        bash_command='python3 ~/airflow/scripts/load_data.py'
    )

    # Task 3: Check Data
    check_data = BashOperator(
        task_id='check_data',
        bash_command='python3 ~/airflow/scripts/check_data.py'
    )

    # Task Flow
    create_tables >> load_data >> check_data
