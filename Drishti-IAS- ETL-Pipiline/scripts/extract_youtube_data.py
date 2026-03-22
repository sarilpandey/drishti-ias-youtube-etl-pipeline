from googleapiclient.discovery import build
import pandas as pd
import os
from dotenv import load_dotenv

#Load environment variables
load_dotenv()

API_KEY = os.getenv("AIzaSyC-KkJoAW1PhEiRz26HC9qMU2YsYm9k0uE")
CHANNEL_ID = "YOUTUBE_API_KE"

youtube = build('youtube', 'v3', developerKey=API_KEY)

def fetch_data():
    request = youtube.search().list(
        part="snippet",
        channelId=CHANNEL_ID,
        maxResults=5,
        order="date"
    )
    response = request.execute()

    video_ids = []
    videos = []

    for item in response['items']:
        if item['id']['kind'] == 'youtube#video':
            video_ids.append(item['id']['videoId'])
            videos.append({
                "video_id": item['id']['videoId'],
                "title": item['snippet']['title']
            })

    stats_request = youtube.videos().list(
        part="statistics",
        id=",".join(video_ids)
    )
    stats_response = stats_request.execute()

    stats_map = {}
    for item in stats_response['items']:
        stats_map[item['id']] = item['statistics']

    for v in videos:
        stats = stats_map.get(v['video_id'], {})
        v['views'] = int(stats.get('viewCount', 0))
        v['likes'] = int(stats.get('likeCount', 0))

    df = pd.DataFrame(videos)
    df.to_csv('/opt/airflow/data/raw/videos.csv', index=False)
