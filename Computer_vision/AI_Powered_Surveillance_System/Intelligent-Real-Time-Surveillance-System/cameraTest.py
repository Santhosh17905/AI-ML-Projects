import cv2
import os
import time
from datetime import datetime
from ultralytics import YOLO
from pygame import mixer

# ----------------------------
# Configuration
# ----------------------------

CONFIDENCE_THRESHOLD = 0.55

DETECTION_CLASSES = [
    "person",
    "car",
    "motorcycle",
    "bus",
    "truck","bike","motorbike","bicycle","traffic light","vehicle","license plate"
]

SAVE_INTERVAL = 5

# ----------------------------
# Folder Setup
# ----------------------------

os.makedirs("captures", exist_ok=True)
os.makedirs("logs", exist_ok=True)

# ----------------------------
# Alarm Setup
# ----------------------------

alarm_file = "sounds/alarm.wav"
alarm_loaded = False

try:
    mixer.init()
    mixer.music.load(alarm_file)
    alarm_loaded = True
except Exception as exc:
    print(
        f"Warning: could not load alarm sound '{alarm_file}': {exc}"
    )

# ----------------------------
# Load YOLO Model
# ----------------------------

model = YOLO("yolov8n.pt")

# ----------------------------
# Video Source
# ----------------------------

cap = cv2.VideoCapture(0)

last_capture_time = 0
previous_time = time.time()

# ----------------------------
# Logging Function
# ----------------------------

def log_event(label, confidence):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(
        "logs/events.log",
        "a"
    ) as file:

        file.write(
            f"{timestamp} | {label} | {confidence:.2f}\n"
        )

# ----------------------------
# Main Loop
# ----------------------------

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.resize(
        frame,
        (1280, 720)
    )

    results = model(
        frame,
        verbose=False
    )

    detection_count = 0

    for result in results:

        boxes = result.boxes

        for box in boxes:

            confidence = float(
                box.conf[0]
            )

            if confidence < CONFIDENCE_THRESHOLD:
                continue

            cls = int(
                box.cls[0]
            )

            label = model.names[cls]

            if label not in DETECTION_CLASSES:
                continue

            detection_count += 1

            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0]
            )

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                f"{label} {confidence:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

            log_event(
                label,
                confidence
            )

            current_time = time.time()

            if (
                current_time -
                last_capture_time
                > SAVE_INTERVAL
            ):

                filename = datetime.now().strftime(
                    "captures/%Y%m%d_%H%M%S.jpg"
                )

                cv2.imwrite(
                    filename,
                    frame
                )

                last_capture_time = current_time

    if detection_count > 0:

        if alarm_loaded and not mixer.music.get_busy():
            mixer.music.play()

        cv2.putText(
            frame,
            "ALERT DETECTED",
            (900, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            3
        )

    current_time = time.time()

    fps = 1 / (
        current_time -
        previous_time
    )

    previous_time = current_time

    cv2.putText(
        frame,
        f"FPS: {fps:.2f}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Objects: {detection_count}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 0),
        2
    )

    cv2.putText(
        frame,
        datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        ),
        (20, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 0),
        2
    )

    cv2.imshow(
        "AI Motion Detection System",
        frame
    )

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()