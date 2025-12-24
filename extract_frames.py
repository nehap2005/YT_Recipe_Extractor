import cv2
import os

def extract_frames(video_path, out_dir="data/frames"):
    os.makedirs(out_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    idx = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_path = os.path.join(out_dir, f"{idx:04d}.jpg")
        if idx % 30 == 0:
             cv2.imwrite(frame_path, frame)
        idx += 1

    cap.release()
    return out_dir   
