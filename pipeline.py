import os
import json
from extract_frames import extract_frames
from caption_cleaner import clean_captions
from ocr_engine import run_ocr
from yolo_detector import run_yolo
from merge_context import merge_all
from recipe_generator import generate_recipe

def run_pipeline(video_path):
    video_id = os.path.splitext(os.path.basename(video_path))[0]

    frames = extract_frames(video_path)
    captions = clean_captions(video_id)
    #ocr_text = run_ocr(frames)
    detections = run_yolo(frames)

   #context = merge_all(captions, ocr_text, detections)
    context = merge_all(captions, detections)
    recipe = generate_recipe(context)

    os.makedirs("data/output", exist_ok=True)
    out_file = f"data/output/{video_id}_recipe.json"

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(recipe, f, indent=2)

    return out_file
