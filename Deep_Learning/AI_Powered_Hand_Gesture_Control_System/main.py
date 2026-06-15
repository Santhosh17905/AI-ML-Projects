import cv2
import mediapipe as mp
import numpy as np
import pandas as pd
import time
import os
from collections import Counter, deque
from datetime import datetime

try:
    import pyttsx3
    TTS = True
except:
    TTS = False

SAVE_DIR = "captures"
LOG_FILE = "gesture_log.csv"

os.makedirs(SAVE_DIR, exist_ok=True)

if TTS:
    engine = pyttsx3.init()

    def speak(text):
        try:
            engine.say(text)
            engine.runAndWait()
        except:
            pass
else:
    def speak(text):
        pass

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

gesture_history = deque(maxlen=10)
gesture_counter = Counter()
last_spoken = ""

def log_gesture(gesture):
    row = pd.DataFrame([{
        "timestamp": datetime.now(),
        "gesture": gesture
    }])

    if os.path.exists(LOG_FILE):
        row.to_csv(LOG_FILE, mode="a", header=False, index=False)
    else:
        row.to_csv(LOG_FILE, index=False)

def fingers_up(hand):
    tips = [4, 8, 12, 16, 20]
    fingers = []

    fingers.append(
        1 if hand.landmark[tips[0]].x < hand.landmark[tips[0]-1].x else 0
    )

    for tip in tips[1:]:
        fingers.append(
            1 if hand.landmark[tip].y < hand.landmark[tip-2].y else 0
        )

    return fingers

def classify(fingers):

    total = sum(fingers)

    if total == 0:
        return "FIST"

    if total == 5:
        return "OPEN PALM"

    if total == 1:
        if fingers[0]:
            return "THUMBS UP"
        return "ONE"

    if total == 2:
        return "TWO"

    if total == 3:
        return "THREE"

    if total == 4:
        return "FOUR"

    return "UNKNOWN"

cap = cv2.VideoCapture(0)

prev = time.time()

while True:

    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    gesture = "NO HAND"

    if result.multi_hand_landmarks:

        for hand in result.multi_hand_landmarks:

            mp_draw.draw_landmarks(
                frame,
                hand,
                mp_hands.HAND_CONNECTIONS
            )

            gesture = classify(fingers_up(hand))

    gesture_history.append(gesture)

    stable_gesture = max(
        set(gesture_history),
        key=gesture_history.count
    )

    gesture_counter[stable_gesture] += 1

    if stable_gesture != last_spoken and stable_gesture != "NO HAND":
        last_spoken = stable_gesture

    now = time.time()
    fps = int(1 / max(now - prev, 0.0001))
    prev = now

    cv2.rectangle(frame, (0, 0), (470, 180), (40, 40, 40), -1)

    cv2.putText(frame, f"Gesture: {stable_gesture}",
                (15, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

    cv2.putText(frame, f"FPS: {fps}",
                (15, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255), 2)

    if gesture_counter:
        common = gesture_counter.most_common(1)[0][0]

        cv2.putText(frame, f"Most Seen: {common}",
                    (15, 120), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (255,255,255), 2)

    cv2.putText(frame,
                "S=Screenshot  L=Log  ESC=Exit",
                (15, 160),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255,255,255),
                2)

    cv2.imshow("AI Hand Gesture Control System", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("s"):
        name = os.path.join(
            SAVE_DIR,
            f"capture_{int(time.time())}.jpg"
        )
        cv2.imwrite(name, frame)
        print("Saved:", name)

    elif key == ord("l"):
        log_gesture(stable_gesture)
        print("Logged:", stable_gesture)

    elif key == 27:
        break

cap.release()
cv2.destroyAllWindows()
