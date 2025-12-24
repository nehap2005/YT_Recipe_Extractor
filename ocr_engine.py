import os
from paddleocr import PaddleOCR
from tqdm import tqdm

ocr = PaddleOCR(use_angle_cls=True, lang="en")

def run_ocr(frames_dir):
    texts = []
    valid_exts = (".jpg", ".jpeg", ".png", ".bmp", ".tiff")

    for img in tqdm(sorted(os.listdir(frames_dir)), desc="OCR"):
        if not img.lower().endswith(valid_exts):
            continue

        path = os.path.join(frames_dir, img)

        try:
            result = ocr.ocr(path)
        except Exception as e:
            print(f"Error reading {path}: {e}")
            continue

        if not result:
            continue

        for block in result:
            for line in block:
                if (
                    not isinstance(line, list)
                    or len(line) != 2
                    or not isinstance(line[1], (tuple, list))
                    or len(line[1]) != 2
                ):
                    continue  

                text, conf = line[1]
                if conf >= 0.6:
                    texts.append(text.lower())

    return list(set(texts))


if __name__ == "__main__":
    frames_dir = "data/frames"  
    detected_texts = run_ocr(frames_dir)
    print(f"\nDetected {len(detected_texts)} unique texts.")
    print("Sample texts:", detected_texts[:20]) 
