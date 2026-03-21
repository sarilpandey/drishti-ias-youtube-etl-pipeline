from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from scripts.extract_youtube_data import fetch_data
from scripts.transform_data import transform
from scripts.upload_to_s3 import upload

with DAG(
    'youtube_etl_pipeline',
    start_date=datetime(2024,1,1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id='extract',
        python_callable=fetch_data
    )

    t2 = PythonOperator(
        task_id='transform',
        python_callable=transform
    )

    t3 = PythonOperator(
        task_id='load_s3',
        python_callable=upload
    )

    t1 >> t2 >> t3