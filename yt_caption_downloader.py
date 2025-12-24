import yt_dlp
import os

def download_video(url, out_dir="data/videos"):
    os.makedirs(out_dir, exist_ok=True)

    ydl_opts = {
        "format": "bestvideo+bestaudio",
        "outtmpl": f"{out_dir}/%(id)s.%(ext)s",
        "writesubtitles": True,
        "writeautomaticsub": True,
        "subtitleslangs": ["en"],
        "subtitlesformat": "vtt",
        "merge_output_format": "mp4"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return info["id"]
