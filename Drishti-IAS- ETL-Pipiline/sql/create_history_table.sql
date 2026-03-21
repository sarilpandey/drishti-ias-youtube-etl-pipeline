CREATE EXTERNAL TABLE video_history (
    video_id STRING,
    views INT,
    recorded_date STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 's3://your-bucket-name/youtube/history/';