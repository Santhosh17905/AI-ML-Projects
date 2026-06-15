import argparse
import json
import os
import queue
import threading
import time
import warnings

warnings.filterwarnings("ignore", message=r".*pin_memory.*", category=UserWarning)

import cv2
import easyocr
import numpy as np
from datetime import datetime


class AIOCR:

    def __init__(self):
        print("Loading AI OCR model...")
        self.reader = easyocr.Reader(
            ['en'],
            gpu=False,
            verbose=False
        )

        self._detect_queue = queue.Queue(maxsize=1)
        self._detections = []
        self._lock = threading.Lock()
        self._stop_event = threading.Event()
        self._ocr_thread = threading.Thread(target=self._ocr_worker, daemon=True)
        self._ocr_thread.start()

        print("Model ready!")

    def preprocess(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, None, fx=1.8, fy=1.8, interpolation=cv2.INTER_CUBIC)

        # Illumination normalization for bright screens / glare
        blur = cv2.medianBlur(gray, 3)
        normalized = cv2.divide(gray, blur, scale=255)

        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
        enhanced = clahe.apply(normalized)

        gamma = 1.4
        inv_gamma = 1.0 / gamma
        table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(256)]).astype('uint8')
        corrected = cv2.LUT(enhanced, table)

        thresh = cv2.adaptiveThreshold(
            corrected,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            15,
            3
        )

        combined = cv2.addWeighted(corrected, 0.6, thresh, 0.4, 0)
        return combined

    def detect(self, img):
        results = self.reader.readtext(
            img,
            detail=1,
            paragraph=False,
            min_size=6,
            contrast_ths=0.05,
            adjust_contrast=1.7,
            filter_ths=0.0001,
            text_threshold=0.18,
            low_text=0.16,
            link_threshold=0.15,
            mag_ratio=2.0,
            rotation_info=[-15, -5, 0, 5, 15],
            slope_ths=0.1,
            ycenter_ths=0.5,
            width_ths=0.5,
            height_ths=0.5,
            bbox_min_score=0.18,
            bbox_min_size=3,
            allowlist='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        )

        detections = []
        for bbox, text, confidence in results:
            if confidence >= 0.18 and text.strip():
                bbox_list = [[int(point[0]), int(point[1])] for point in bbox]
                detections.append({
                    "text": text.strip(),
                    "confidence": round(confidence, 2),
                    "bbox": bbox_list
                })
        return detections

    def _ocr_worker(self):
        while not self._stop_event.is_set():
            try:
                frame = self._detect_queue.get(timeout=0.1)
            except queue.Empty:
                continue

            detections = self.detect(frame)
            with self._lock:
                self._detections = detections
            self._detect_queue.task_done()

    def request_detection(self, frame):
        if self._stop_event.is_set():
            return False
        if self._detect_queue.full():
            return False
        try:
            self._detect_queue.put_nowait(frame)
            return True
        except queue.Full:
            return False

    def get_detections(self):
        with self._lock:
            return list(self._detections)

    def stop(self):
        self._stop_event.set()
        try:
            self._detect_queue.put_nowait(np.zeros((8, 8, 3), dtype=np.uint8))
        except queue.Full:
            pass
        self._ocr_thread.join(timeout=1)

    def draw(self, frame, detections):
        for det in detections:
            pts = np.array(det["bbox"], np.int32).reshape((-1, 2))
            cv2.polylines(frame, [pts], True, (0, 255, 0), 2)

            x, y = pts[0]
            label = f'{det["text"]} ({det["confidence"]})'
            (tw, th), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
            cv2.rectangle(frame, (x, y - th - baseline - 8), (x + tw + 4, y - 4), (0, 255, 0), -1)
            cv2.putText(frame, label, (x + 2, y - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

        return frame


ocr = AIOCR()


def save_results(detections):
    os.makedirs("output", exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"output/ocr_{ts}.json", "w", encoding="utf-8") as f:
        json.dump(detections, f, indent=4, ensure_ascii=False)


def image_mode(path):
    img = cv2.imread(path)
    if img is None:
        print("Image not found")
        return

    processed = ocr.preprocess(img)
    detections = ocr.detect(processed)

    print("\nDetected Text\n")
    for d in detections:
        print(f'{d["text"]}  ({d["confidence"]})')

    save_results(detections)
    output = ocr.draw(img.copy(), detections)
    cv2.imshow("AI OCR", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def webcam_mode():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        print("Unable to open webcam")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)

    frame_count = 0
    last_request_time = 0
    detection_interval = 0.25

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            if frame.shape[1] > 960 or frame.shape[0] > 540:
                frame = cv2.resize(frame, (960, 540), interpolation=cv2.INTER_AREA)

            now = time.time()
            if now - last_request_time >= detection_interval:
                if ocr.request_detection(frame.copy()):
                    last_request_time = now

            detections = ocr.get_detections()
            display = frame.copy()
            if detections:
                display = ocr.draw(display, detections)

            cv2.putText(
                display,
                "Press q to quit | Live OCR",
                (12, 28),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2,
                cv2.LINE_AA
            )

            cv2.imshow("AI OCR Webcam", display)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
    finally:
        ocr.stop()
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", type=str)
    parser.add_argument("--webcam", action="store_true")
    args = parser.parse_args()

    if args.webcam:
        webcam_mode()
    elif args.image:
        image_mode(args.image)
    else:
        print("Usage:")
        print("python ai_ocr.py --webcam")
        print("python ai_ocr.py --image test.jpg")