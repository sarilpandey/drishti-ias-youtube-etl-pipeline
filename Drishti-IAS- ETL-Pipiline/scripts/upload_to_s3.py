import boto3
import os
from dotenv import load_dotenv

Load environment variables
load_dotenv()

def upload():
    s3 = boto3.client('s3',,
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_DEFAULT_REGION")
        )

    s3.upload_file(
        '/opt/airflow/data/processed/videos.csv',
        'your-bucket-name',
        'youtube/videos.csv'
    )

    s3.upload_file(
        '/opt/airflow/data/processed/history.csv',
        'your-bucket-name',
        'youtube/history/history.csv'
    )