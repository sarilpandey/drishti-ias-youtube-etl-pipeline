import pandas as pd
from datetime import datetime

def transform():
    df = pd.read_csv('/opt/airflow/data/raw/videos.csv')

    today = datetime.today().strftime('%Y-%m-%d')

    try:
        old_df = pd.read_csv('/opt/airflow/data/processed/videos.csv')
        old_ids = set(old_df['video_id'])
    except:
        old_ids = set()

    df['status'] = df['video_id'].apply(
        lambda x: 'new' if x not in old_ids else 'old'
    )

    df['date'] = today

    df.to_csv('/opt/airflow/data/processed/videos.csv', index=False)

    history = df[['video_id', 'views']].copy()
    history['recorded_date'] = today

    try:
        old_history = pd.read_csv('/opt/airflow/data/processed/history.csv')
        history = pd.concat([old_history, history])
    except:
        pass

    history.to_csv('/opt/airflow/data/processed/history.csv', index=False)