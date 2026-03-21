CREATE EXTERNAL TABLE videos (
    video_id STRING,
    title STRING,
    views INT,
    likes INT,
    status STRING,
    date STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 's3://your-bucket-name/youtube/';