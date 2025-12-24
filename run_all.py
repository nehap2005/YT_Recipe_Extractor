from yt_caption_downloader import download_video
from pipeline import run_pipeline

import os

YOUTUBE_URL = input("Enter YouTube URL: ")

video_id = download_video(YOUTUBE_URL)

video_path = f"data/videos/{video_id}.mp4"

output = run_pipeline(video_path)

print("\n✅ DONE")
print("Recipe saved at:", output)
