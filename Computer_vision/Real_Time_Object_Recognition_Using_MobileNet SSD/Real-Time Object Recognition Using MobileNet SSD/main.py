import cv2
import numpy as np
import time
import os
from datetime import datetime

# ==================================================
# CONFIGURATION
# ==================================================

PROTOTXT = r"MobileNetSSD_deploy.prototxt"
MODEL = r"MobileNetSSD_deploy.caffemodel"

CONFIDENCE_THRESHOLD = 0.20
CAMERA_INDEX = 0
FRAME_WIDTH = 1280

SAVE_DIR = "detections"
os.makedirs(SAVE_DIR, exist_ok=True)

# ==================================================
# CLASSES
# ==================================================

CLASSES = [
    "background", "aeroplane", "bicycle", "bird", "boat",
    "bottle", "bus", "car", "cat", "chair", "cow",
    "diningtable", "dog", "horse", "motorbike", "person",
    "pottedplant", "sheep", "sofa", "train", "tvmonitor"
]

COLORS = np.random.randint(
    0, 255,
    size=(len(CLASSES), 3),
    dtype="uint8"
)

# ==================================================
# LOAD MODEL
# ==================================================

print("[INFO] Loading Model...")
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PROTOTXT = os.path.join(
    BASE_DIR,
    "MobileNetSSD_deploy.prototxt"
)

MODEL = os.path.join(
    BASE_DIR,
    "MobileNetSSD_deploy.caffemodel"
)
print(PROTOTXT)
print(MODEL)
print("[INFO] Loading Model...")

net = cv2.dnn.readNetFromCaffe(
    PROTOTXT,
    MODEL
)

print("[INFO] Model Loaded Successfully")

# ==================================================
# CAMERA
# ==================================================

cap = cv2.VideoCapture(CAMERA_INDEX)

if not cap.isOpened():
    raise Exception("Unable to access camera")

# ==================================================
# VARIABLES
# ==================================================

fps = 0
frame_count = 0
start_time = time.time()

total_detections = 0
total_detections = 0

# Auto screenshot timer
last_save_time = 0
AUTO_SAVE_INTERVAL = 10  # seconds


# ==================================================
# MAIN LOOP
# ==================================================

while True:

    ret, frame = cap.read()

    if not ret:
        print("[WARNING] Camera frame not received")
        break

    # ------------------------------------------
    # Resize
    # ------------------------------------------

    h, w = frame.shape[:2]

    scale = FRAME_WIDTH / w

    frame = cv2.resize(
        frame,
        (FRAME_WIDTH, int(h * scale))
    )

    h, w = frame.shape[:2]

    # ------------------------------------------
    # Create Blob
    # ------------------------------------------

    blob = cv2.dnn.blobFromImage(
        cv2.resize(frame, (300, 300)),
        0.007843,
        (300, 300),
        127.5
    )

    net.setInput(blob)

    detections = net.forward()

    object_counter = {}

    # ------------------------------------------
    # Detection Loop
    # ------------------------------------------

    for i in range(detections.shape[2]):

        confidence = detections[0, 0, i, 2]

        if confidence < CONFIDENCE_THRESHOLD:
            continue

        idx = int(detections[0, 0, i, 1])

        if idx >= len(CLASSES):
            continue

        label = CLASSES[idx]

        object_counter[label] = (
            object_counter.get(label, 0) + 1
        )

        total_detections += 1

        box = detections[0, 0, i, 3:7] * \
              np.array([w, h, w, h])

        startX, startY, endX, endY = box.astype("int")

        color = [int(c) for c in COLORS[idx]]
        print(label, confidence)

        # Bounding Box
        cv2.rectangle(
            frame,
            (startX, startY),
            (endX, endY),
            color,
            2
        )

        text = f"{label}: {confidence*100:.1f}%"

        y = startY - 10 if startY > 20 else startY + 20

        cv2.putText(
            frame,
            text,
            (startX, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            color,
            2
        )

    # ==================================================
    # FPS CALCULATION
    # ==================================================

    frame_count += 1

    elapsed = time.time() - start_time

    if elapsed > 0:
        fps = frame_count / elapsed

    # ==================================================
    # DASHBOARD PANEL
    # ==================================================

    overlay = frame.copy()

    cv2.rectangle(
        overlay,
        (10, 10),
        (350, 230),
        (0, 0, 0),
        -1
    )

    frame = cv2.addWeighted(
        overlay,
        0.4,
        frame,
        0.6,
        0
    )

    cv2.putText(
        frame,
        "AI OBJECT RECOGNITION",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"FPS: {fps:.2f}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Objects: {sum(object_counter.values())}",
        (20, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Total Detections: {total_detections}",
        (20, 160),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    # ==================================================
    # OBJECT LIST
    # ==================================================

    y_pos = 200

    for obj, count in object_counter.items():

        cv2.putText(
            frame,
            f"{obj}: {count}",
            (20, y_pos),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 255),
            2
        )

        y_pos += 25

    # ==================================================
    # AUTO SCREENSHOT
    # ==================================================

    current_time = time.time()

    if len(object_counter) > 0 and \
       current_time - last_save_time >= AUTO_SAVE_INTERVAL:

        filename = datetime.now().strftime(
            "%Y%m%d_%H%M%S.jpg"
        )

        filepath = os.path.join(
            SAVE_DIR,
            filename
        )

        cv2.imwrite(filepath, frame)

        print(f"[INFO] Auto Screenshot Saved: {filepath}")

        last_save_time = current_time

    # ==================================================
    # DISPLAY
    # ==================================================

    cv2.imshow(
        "Day 12 - Premium Object Recognition System",
        frame
    )

    key = cv2.waitKey(1) & 0xFF

    # ==================================================
    # SHORTCUTS
    # ==================================================

    # ESC
    if key == 27:
        break

    # S = Screenshot
    elif key == ord("s"):

        filename = datetime.now().strftime(
            "%Y%m%d_%H%M%S.jpg"
        )

        filepath = os.path.join(
            SAVE_DIR,
            filename
        )

        cv2.imwrite(
            filepath,
            frame
        )

        print(
            f"[INFO] Screenshot Saved: {filepath}"
        )

# ==================================================
# CLEANUP
# ==================================================

cap.release()
cv2.destroyAllWindows()

print("\n========== SESSION SUMMARY ==========")
print("Total Detections :", total_detections)
print("Average FPS      :", round(fps, 2))
print("=====================================")