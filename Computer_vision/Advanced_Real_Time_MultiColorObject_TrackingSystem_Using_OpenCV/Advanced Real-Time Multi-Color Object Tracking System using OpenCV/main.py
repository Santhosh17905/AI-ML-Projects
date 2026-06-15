import cv2
import numpy as np
import imutils
import time
import math
from collections import deque
from datetime import datetime

# ====================================
# CONFIGURATION
# ====================================

FRAME_WIDTH = 1280
MAX_TRAIL = 64
MIN_RADIUS = 10

# ====================================
# COLOR RANGES (HSV)
# ====================================

COLOR_RANGES = {
    "RED": [
        ((0, 120, 70), (10, 255, 255)),
        ((170, 120, 70), (180, 255, 255))
    ],

    "GREEN": [
        ((35, 50, 50), (85, 255, 255))
    ],

    "BLUE": [
        ((100, 150, 50), (140, 255, 255))
    ]
}

# ====================================
# INITIALIZATION
# ====================================

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Cannot open camera")
    exit()

trail = deque(maxlen=MAX_TRAIL)

recording = False
writer = None

frame_count = 0
start_time = time.time()

last_center = None

# ====================================
# FUNCTIONS
# ====================================

def calculate_direction(prev, current):

    if prev is None:
        return "Still"

    dx = current[0] - prev[0]
    dy = current[1] - prev[1]

    if abs(dx) > abs(dy):

        if dx > 20:
            return "Right"

        elif dx < -20:
            return "Left"

    else:

        if dy > 20:
            return "Down"

        elif dy < -20:
            return "Up"

    return "Still"


def estimate_distance(radius):

    if radius == 0:
        return 0

    return round(5000 / radius, 2)


def draw_dashboard(frame,
                   fps,
                   color_name,
                   center,
                   radius,
                   direction):

    cv2.rectangle(frame, (0, 0), (420, 220), (30, 30, 30), -1)

    cv2.putText(frame,
                f"FPS: {fps:.2f}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0,255,0),
                2)

    cv2.putText(frame,
                f"Color: {color_name}",
                (20, 75),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255,255,255),
                2)

    if center:

        cv2.putText(frame,
                    f"Center X: {center[0]}",
                    (20,110),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255,255,255),
                    2)

        cv2.putText(frame,
                    f"Center Y: {center[1]}",
                    (20,145),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255,255,255),
                    2)

        cv2.putText(frame,
                    f"Direction: {direction}",
                    (20,180),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0,255,255),
                    2)

        cv2.putText(frame,
                    f"Distance: {estimate_distance(radius)} cm",
                    (20,215),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0,255,255),
                    2)

# ====================================
# MAIN LOOP
# ====================================

while True:

    grabbed, frame = camera.read()

    if not grabbed:
        break

    frame = imutils.resize(frame, width=FRAME_WIDTH)

    blurred = cv2.GaussianBlur(frame, (11,11), 0)

    hsv = cv2.cvtColor(
        blurred,
        cv2.COLOR_BGR2HSV
    )

    detected_color = "None"

    largest_contour = None
    largest_radius = 0
    center = None

    mask_display = None

    # ====================================
    # SEARCH ALL COLORS
    # ====================================

    for color_name, ranges in COLOR_RANGES.items():

        mask = np.zeros(
            hsv.shape[:2],
            dtype=np.uint8
        )

        for lower, upper in ranges:

            lower = np.array(lower)
            upper = np.array(upper)

            mask += cv2.inRange(
                hsv,
                lower,
                upper
            )

        mask = cv2.erode(
            mask,
            None,
            iterations=2
        )

        mask = cv2.dilate(
            mask,
            None,
            iterations=2
        )

        contours = cv2.findContours(
            mask.copy(),
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )[-2]

        if len(contours) > 0:

            c = max(
                contours,
                key=cv2.contourArea
            )

            ((x,y), radius) = cv2.minEnclosingCircle(c)

            if radius > largest_radius:

                largest_radius = radius
                largest_contour = c
                detected_color = color_name
                mask_display = mask

    # ====================================
    # OBJECT FOUND
    # ====================================

    if largest_contour is not None:

        M = cv2.moments(
            largest_contour
        )

        if M["m00"] > 0:

            center = (
                int(M["m10"]/M["m00"]),
                int(M["m01"]/M["m00"])
            )

            trail.appendleft(center)

            direction = calculate_direction(
                last_center,
                center
            )

            last_center = center

            ((x,y), radius) = cv2.minEnclosingCircle(
                largest_contour
            )

            if radius > MIN_RADIUS:

                cv2.circle(
                    frame,
                    (int(x), int(y)),
                    int(radius),
                    (0,255,255),
                    3
                )

                cv2.circle(
                    frame,
                    center,
                    6,
                    (0,0,255),
                    -1
                )

                area = cv2.contourArea(
                    largest_contour
                )

                cv2.putText(
                    frame,
                    f"Area: {int(area)}",
                    (center[0]+20,
                     center[1]),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (255,255,255),
                    2
                )

    else:
        direction = "No Object"

    # ====================================
    # DRAW TRAIL
    # ====================================

    for i in range(
        1,
        len(trail)
    ):

        if trail[i-1] is None \
           or trail[i] is None:
            continue

        thickness = int(
            np.sqrt(
                MAX_TRAIL/(i+1)
            ) * 2
        )

        cv2.line(
            frame,
            trail[i-1],
            trail[i],
            (0,255,0),
            thickness
        )

    # ====================================
    # FPS
    # ====================================

    frame_count += 1

    fps = frame_count / (
        time.time() - start_time
    )

    draw_dashboard(
        frame,
        fps,
        detected_color,
        center,
        largest_radius,
        direction
    )

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    cv2.putText(
        frame,
        timestamp,
        (900,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255,255,255),
        2
    )

    # ====================================
    # RECORD VIDEO
    # ====================================

    if recording:

        if writer is None:

            fourcc = cv2.VideoWriter_fourcc(
                *'XVID'
            )

            writer = cv2.VideoWriter(
                f"recording_{int(time.time())}.avi",
                fourcc,
                20,
                (frame.shape[1],
                 frame.shape[0])
            )

        writer.write(frame)

        cv2.putText(
            frame,
            "REC",
            (1150,80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,0,255),
            3
        )

    cv2.imshow(
        "Professional Color Tracker",
        frame
    )

    if mask_display is not None:
        cv2.imshow(
            "Mask",
            mask_display
        )

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

    elif key == ord("s"):

        filename = f"screenshot_{int(time.time())}.png"

        cv2.imwrite(
            filename,
            frame
        )

        print(
            f"Saved: {filename}"
        )

    elif key == ord("r"):

        recording = not recording

        if not recording and writer:

            writer.release()
            writer = None

camera.release()

if writer:
    writer.release()

cv2.destroyAllWindows()