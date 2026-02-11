from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

sys.path.append('/opt/airflow/dags/api-request')

def safe_main_callable():
    from insert_records import main
    main()

default_args = {
    'description': 'A DAG to orchestrate the weather API data fetching and insertion into the database',
    'start_date': datetime(2025, 2, 10),
    'catchup': False,
}

dag = DAG(
    dag_id="weather-api-orchestrator",
    default_args=default_args,
    schedule=timedelta(minutes=1)
)

with dag:
    task1 = PythonOperator(
        task_id='example_task',
        python_callable=safe_main_callable
    )
    #task2
