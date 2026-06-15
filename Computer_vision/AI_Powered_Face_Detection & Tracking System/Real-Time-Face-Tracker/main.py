import cv2
import time
import os
from datetime import datetime

class AdvancedFaceTracker:

    def __init__(self):

        self.face_detector = cv2.CascadeClassifier(
            cv2.data.haarcascades +
            "haarcascade_frontalface_default.xml"
        )

        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        self.tracker = None
        self.tracking = False

        self.face_count = 0
        self.total_detections = 0

        self.start_time = time.time()

        self.prev_time = 0
        self.fps = 0

        self.screenshot_folder = "screenshots"
        os.makedirs(self.screenshot_folder, exist_ok=True)

        self.log_file = "face_log.txt"

    def calculate_fps(self):

        current_time = time.time()

        fps = 1 / (current_time - self.prev_time)

        self.prev_time = current_time

        return int(fps)

    def log_event(self, message):

        with open(self.log_file, "a") as f:

            timestamp = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            f.write(f"[{timestamp}] {message}\n")

    def save_screenshot(self, frame):

        filename = datetime.now().strftime(
            "%Y%m%d_%H%M%S.jpg"
        )

        path = os.path.join(
            self.screenshot_folder,
            filename
        )

        cv2.imwrite(path, frame)

        print("Screenshot Saved:", path)

    def draw_ui(self, frame):

        cv2.rectangle(
            frame,
            (0, 0),
            (450, 140),
            (20, 20, 20),
            -1
        )

        cv2.putText(
            frame,
            f"FPS: {self.fps}",
            (15, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,0),
            2
        )

        cv2.putText(
            frame,
            f"Faces: {self.face_count}",
            (15, 60),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255,255,255),
            2
        )

        cv2.putText(
            frame,
            f"Detections: {self.total_detections}",
            (15, 90),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255,255,255),
            2
        )

        uptime = int(time.time() - self.start_time)

        cv2.putText(
            frame,
            f"Uptime: {uptime}s",
            (15,120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255,255,255),
            2
        )

    def run(self):

        print("=" * 50)
        print("ADVANCED FACE DETECTION & TRACKING")
        print("Press S = Screenshot")
        print("Press Q = Quit")
        print("=" * 50)

        while True:

            success, frame = self.cap.read()

            if not success:
                print("Camera Error")
                break

            frame = cv2.flip(frame, 1)

            gray = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2GRAY
            )

            self.fps = self.calculate_fps()

            # Face Detection
            if not self.tracking:

                faces = self.face_detector.detectMultiScale(
                    gray,
                    scaleFactor=1.2,
                    minNeighbors=5,
                    minSize=(80,80)
                )

                self.face_count = len(faces)

                if len(faces) > 0:

                    x,y,w,h = faces[0]

                    if hasattr(cv2, "TrackerCSRT_create"):
                        self.tracker = cv2.TrackerCSRT_create()
                    elif hasattr(cv2, "TrackerMIL_create"):
                        self.tracker = cv2.TrackerMIL_create()
                    elif hasattr(cv2, "legacy") and hasattr(cv2.legacy, "TrackerCSRT_create"):
                        self.tracker = cv2.legacy.TrackerCSRT_create()
                    else:
                        raise RuntimeError(
                            "OpenCV tracker API not available. "
                            "Install opencv-contrib-python or use a supported OpenCV build."
                        )

                    self.tracker.init(
                        frame,
                        (x,y,w,h)
                    )

                    self.tracking = True

                    self.total_detections += 1

                    self.log_event(
                        "Face Detected"
                    )

            # Tracking
            else:

                success, box = self.tracker.update(
                    frame
                )

                if success:

                    x,y,w,h = map(int, box)

                    cv2.rectangle(
                        frame,
                        (x,y),
                        (x+w,y+h),
                        (0,255,0),
                        3
                    )

                    cv2.putText(
                        frame,
                        "TRACKING",
                        (x,y-15),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0,255,0),
                        2
                    )

                    center_x = x + w // 2
                    center_y = y + h // 2

                    cv2.circle(
                        frame,
                        (center_x, center_y),
                        5,
                        (0,0,255),
                        -1
                    )

                else:

                    self.tracking = False

                    self.log_event(
                        "Tracking Lost"
                    )

            self.draw_ui(frame)

            cv2.imshow(
                "AI Face Detection & Tracking",
                frame
            )

            key = cv2.waitKey(1)

            if key == ord('s'):

                self.save_screenshot(frame)

            elif key == ord('q'):

                break

        self.cap.release()

        cv2.destroyAllWindows()

        self.log_event(
            "Application Closed"
        )

if __name__ == "__main__":

    app = AdvancedFaceTracker()

    app.run()