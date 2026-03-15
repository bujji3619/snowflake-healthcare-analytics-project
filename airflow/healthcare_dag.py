from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    'healthcare_pipeline',
    start_date=datetime(2024,1,1),
    schedule_interval='@daily'
) as dag:

    upload_data = BashOperator(
        task_id='upload_data',
        bash_command='aws s3 cp datasets/healthcare_data.csv s3://healthcare-raw-data-bucket-demo/'
    )