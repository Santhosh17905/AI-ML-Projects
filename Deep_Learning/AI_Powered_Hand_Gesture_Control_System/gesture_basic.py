import cv2
import mediapipe as mp
import numpy as np
import time
import os
from collections import Counter

# ==================================================
# CONFIGURATION
# ==================================================

SAVE_FOLDER = "captures"

if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

# ==================================================
# MEDIAPIPE SETUP
# ==================================================

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# ==================================================
# CAMERA
# ==================================================

cap = cv2.VideoCapture(0)

gesture_counter = Counter()

prev_time = time.time()

# ==================================================
# HELPER FUNCTIONS
# ==================================================

def fingers_up(hand_landmarks):

    tips = [4, 8, 12, 16, 20]

    fingers = []

    # Thumb
    if hand_landmarks.landmark[tips[0]].x < hand_landmarks.landmark[tips[0]-1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers
    for tip in tips[1:]:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip-2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers


def recognize_gesture(fingers):

    total = sum(fingers)

    if total == 0:
        return "FIST"

    elif total == 5:
        return "OPEN PALM"

    elif total == 1:

        if fingers[1] == 1:
            return "ONE"

        elif fingers[0] == 1:
            return "THUMBS UP"

    elif total == 2:
        return "TWO"

    elif total == 3:
        return "THREE"

    elif total == 4:
        return "FOUR"

    return "UNKNOWN"

# ==================================================
# MAIN LOOP
# ==================================================

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    gesture = "NO HAND"
    confidence = 0

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            fingers = fingers_up(hand_landmarks)

            gesture = recognize_gesture(fingers)

            confidence = round((sum(fingers)/5)*100, 1)

            gesture_counter[gesture] += 1

    # =====================================
    # FPS
    # =====================================

    current_time = time.time()
    fps = int(1 / (current_time - prev_time))
    prev_time = current_time

    # =====================================
    # UI PANEL
    # =====================================

    cv2.rectangle(frame, (0, 0), (420, 170), (40, 40, 40), -1)

    cv2.putText(
        frame,
        f"Gesture : {gesture}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,0),
        2
    )

    cv2.putText(
        frame,
        f"Confidence : {confidence}%",
        (20, 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255,255,0),
        2
    )

    cv2.putText(
        frame,
        f"FPS : {fps}",
        (20,110),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,255),
        2
    )

    if len(gesture_counter) > 0:

        most_common = gesture_counter.most_common(1)[0]

        cv2.putText(
            frame,
            f"Most Seen : {most_common[0]}",
            (20,145),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255,255,255),
            2
        )

    # =====================================
    # INSTRUCTIONS
    # =====================================

    cv2.putText(
        frame,
        "S = Screenshot | R = Reset Stats | ESC = Exit",
        (10, frame.shape[0]-15),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255,255,255),
        2
    )

    cv2.imshow("AI Hand Gesture Recognition", frame)

    key = cv2.waitKey(1) & 0xFF

    # Screenshot
    if key == ord("s"):

        filename = os.path.join(
            SAVE_FOLDER,
            f"gesture_{int(time.time())}.jpg"
        )

        cv2.imwrite(filename, frame)

        print("Saved:", filename)

    # Reset stats
    elif key == ord("r"):

        gesture_counter.clear()

    # Exit
    elif key == 27:

        break

# ==================================================
# CLEANUP
# ==================================================

cap.release()
cv2.destroyAllWindows()