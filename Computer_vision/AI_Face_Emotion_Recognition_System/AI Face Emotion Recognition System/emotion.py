import cv2
import os
import time
import csv
from datetime import datetime
from collections import Counter, deque

from fer import FER

# ============================================================
# CONFIGURATION
# ============================================================

SAVE_CAPTURES = True
CAPTURE_CONFIDENCE = 0.90
LOG_FILE = "emotion_logs.csv"
CAPTURE_FOLDER = "captures"

os.makedirs(CAPTURE_FOLDER, exist_ok=True)

# ============================================================
# EMOTION RECOGNITION SYSTEM
# ============================================================

class EmotionRecognitionSystem:

    def __init__(self):

        self.detector = FER(mtcnn=False)

        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades +
            "haarcascade_frontalface_default.xml"
        )

        self.history = deque(maxlen=100)

        self.frame_count = 0
        self.start_time = time.time()

        self.last_capture_time = 0

        self.initialize_csv()

    # --------------------------------------------------------

    def initialize_csv(self):

        if not os.path.exists(LOG_FILE):

            with open(LOG_FILE, "w", newline="") as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Timestamp",
                    "Emotion",
                    "Confidence"
                ])

    # --------------------------------------------------------

    def log_emotion(self, emotion, confidence):

        with open(LOG_FILE, "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                emotion,
                round(confidence, 4)
            ])

    # --------------------------------------------------------

    def save_capture(self, frame, emotion):

        filename = os.path.join(
            CAPTURE_FOLDER,
            f"{emotion}_{int(time.time())}.jpg"
        )

        cv2.imwrite(filename, frame)

    # --------------------------------------------------------

    def get_fps(self):

        self.frame_count += 1

        elapsed = time.time() - self.start_time

        if elapsed == 0:
            return 0

        return self.frame_count / elapsed

    # --------------------------------------------------------

    def draw_dashboard(self, frame):

        h, w = frame.shape[:2]

        cv2.rectangle(
            frame,
            (0, 0),
            (350, 150),
            (30, 30, 30),
            -1
        )

        fps = self.get_fps()

        cv2.putText(
            frame,
            f"FPS: {fps:.2f}",
            (15, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 255),
            2
        )

        if len(self.history) > 0:

            stats = Counter(self.history)

            dominant = stats.most_common(1)[0][0]

            cv2.putText(
                frame,
                f"Dominant: {dominant}",
                (15, 65),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

            y = 100

            for emotion, count in stats.most_common(3):

                cv2.putText(
                    frame,
                    f"{emotion}: {count}",
                    (15, y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (255, 255, 255),
                    2
                )

                y += 25

    # --------------------------------------------------------

    def process_frame(self, frame):

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        faces = self.face_cascade.detectMultiScale(
            gray,
            1.3,
            5
        )

        face_count = 0

        for (x, y, w, h) in faces:

            face_count += 1

            face_roi = frame[
                y:y+h,
                x:x+w
            ]

            result = self.detector.top_emotion(
                face_roi
            )

            if result is None:
                continue

            emotion, confidence = result

            if emotion is None:
                continue

            self.history.append(emotion)

            self.log_emotion(
                emotion,
                confidence
            )

            color = (0, 255, 0)

            if emotion == "angry":
                color = (0, 0, 255)

            elif emotion == "happy":
                color = (0, 255, 0)

            elif emotion == "sad":
                color = (255, 0, 0)

            cv2.rectangle(
                frame,
                (x, y),
                (x+w, y+h),
                color,
                3
            )

            label = (
                f"{emotion.upper()} "
                f"{confidence*100:.1f}%"
            )

            cv2.putText(
                frame,
                label,
                (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                color,
                2
            )

            current_time = time.time()

            if (
                SAVE_CAPTURES
                and confidence > CAPTURE_CONFIDENCE
                and current_time - self.last_capture_time > 5
            ):

                self.save_capture(
                    frame,
                    emotion
                )

                self.last_capture_time = current_time

        cv2.putText(
            frame,
            f"Faces: {face_count}",
            (15, 180),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )

        self.draw_dashboard(frame)

        return frame

# ============================================================
# MAIN
# ============================================================

def main():

    print("=" * 60)
    print("AI FACE EMOTION RECOGNITION SYSTEM")
    print("=" * 60)

    system = EmotionRecognitionSystem()

    cap = cv2.VideoCapture(0)

    cap.set(
        cv2.CAP_PROP_FRAME_WIDTH,
        1280
    )

    cap.set(
        cv2.CAP_PROP_FRAME_HEIGHT,
        720
    )

    while True:

        success, frame = cap.read()

        if not success:
            break

        frame = cv2.flip(frame, 1)

        processed = system.process_frame(
            frame
        )

        cv2.imshow(
            "AI Emotion Recognition Dashboard",
            processed
        )

        key = cv2.waitKey(1)

        if key == ord("q"):
            break

    cap.release()

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()