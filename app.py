import streamlit as st
import os
import json
import tempfile
from pathlib import Path

from yt_caption_downloader import download_video
from extract_frames import extract_frames
from caption_cleaner import clean_captions
from yolo_detector import run_yolo
from merge_context import merge_all
from recipe_generator import generate_recipe

st.set_page_config(page_title="Video-to-Recipe Generator", layout="wide")

st.title("🍳 Video-to-Recipe Generator")
st.caption("Enter a YouTube cooking video and get a structured recipe")

# Input
video_url = st.text_input("Enter YouTube Video URL")

if st.button("Generate Recipe") and video_url:
    with st.spinner("Processing video… this may take a few minutes ⏳"):

        # --- Temp workspace ---
        temp_dir = tempfile.mkdtemp()
        videos_dir = os.path.join(temp_dir, "videos")
        frames_dir = os.path.join(temp_dir, "frames")

        os.makedirs(videos_dir, exist_ok=True)
        os.makedirs(frames_dir, exist_ok=True)

        # --- Download video + captions ---
        st.info("📥 Downloading video and captions…")
        video_id = download_video(video_url, out_dir=videos_dir)
        video_path = os.path.join(videos_dir, f"{video_id}.mp4")

        # Move caption file where caption_cleaner expects it
        os.makedirs("data/videos", exist_ok=True)
        src_vtt = os.path.join(videos_dir, f"{video_id}.en.vtt")
        dst_vtt = os.path.join("data/videos", f"{video_id}.en.vtt")
        if os.path.exists(src_vtt):
            os.replace(src_vtt, dst_vtt)

        # --- Extract frames ---
        st.info("🖼️ Extracting frames…")
        frames_dir = extract_frames(video_path, out_dir=frames_dir)

        # --- Clean captions ---
        st.info("🧹 Cleaning captions…")
        captions = clean_captions(video_id)

        # --- YOLO detection ---
        st.info("🥕 Detecting ingredients…")
        detections = run_yolo(frames_dir)

        # --- Merge context ---
        context = merge_all(captions, detections)

        # --- Generate recipe ---
        st.info("🧠 Generating recipe…")
        recipe = generate_recipe(context)

        # --- Save output ---
        os.makedirs("data/output", exist_ok=True)
        output_path = f"data/output/{video_id}_recipe.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(recipe, f, indent=2)

    st.success("✅ Recipe generated successfully!")
    st.subheader("📄 Recipe Output")
    st.json(recipe)

    st.download_button(
        "⬇️ Download Recipe JSON",
        data=json.dumps(recipe, indent=2),
        file_name=f"{video_id}_recipe.json",
        mime="application/json"
    )
