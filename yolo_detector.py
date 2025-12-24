from ultralytics import YOLO
import os
from collections import Counter

model = YOLO("best.pt")
def run_yolo(frames_dir):
    counts = Counter()

    for img in os.listdir(frames_dir):
        path = os.path.join(frames_dir, img)
        results = model(path, verbose=False)

        for r in results:
            for c in r.boxes.cls:
                label = r.names[int(c)]
                counts[label] += 1

    return dict(counts)
