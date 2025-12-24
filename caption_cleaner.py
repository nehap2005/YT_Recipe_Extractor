import os
import webvtt

def clean_captions(video_id):
    vtt_file = f"data/videos/{video_id}.en.vtt"
    if not os.path.exists(vtt_file):
        return ""

    lines = []
    for cap in webvtt.read(vtt_file):
        text = cap.text.lower()
        for w in ["uh", "um", "okay", "you know"]:
            text = text.replace(w, "")
        if len(text.strip()) > 3:
            lines.append(text.strip())

    return " ".join(lines)
