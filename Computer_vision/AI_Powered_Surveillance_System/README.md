# 🛡️ Intelligent Real-Time Surveillance System using YOLOv8 and OpenCV

An AI-powered real-time surveillance system that uses YOLOv8 and OpenCV to detect, monitor, and log objects from live camera feeds. The system can identify people and vehicles, trigger alarms, capture evidence screenshots, and maintain detection logs for security monitoring.

---

## 📌 Features

- Real-time object detection using YOLOv8
- Person detection
- Vehicle detection
- Bounding box visualization
- Confidence score display
- Automatic screenshot capture
- Alarm triggering on detection
- Event logging with timestamps
- FPS monitoring
- Object counting
- Live webcam support
- Evidence storage system
- Configurable detection classes

---

## 🚀 Technologies Used

- Python
- OpenCV
- YOLOv8
- Ultralytics
- NumPy
- Pygame

---

## 📂 Project Structure

```text
Intelligent-Real-Time-Surveillance-System/
│
├── main.py
├── requirements.txt
├── README.md
│
├── captures/
│   └── Detected screenshots
│
├── logs/
│   └── Detection logs
│
└── sounds/
    └── alarm.wav
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/santhosh17905

cd AI_Motion_Detector
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
python main.py
```

Press **ESC** key to exit.

---

## 🧠 How It Works

### Step 1

The webcam captures live video frames.

### Step 2

YOLOv8 processes each frame and detects objects.

### Step 3

Detected objects are filtered based on confidence threshold.

### Step 4

Bounding boxes and labels are drawn around detected objects.

### Step 5

An alarm is triggered whenever a target object is detected.

### Step 6

Detection events are logged into a log file.

### Step 7

Evidence screenshots are automatically saved.

---

## 🎯 Detectable Objects

Current configuration supports:

- Person
- Car
- Motorcycle
- Bus
- Truck

You can easily add more classes from the YOLO dataset.

---

## 📊 Output

The system displays:

- Object Labels
- Confidence Scores
- Object Count
- FPS Counter
- Current Timestamp
- Alert Status

---

## 📸 Screenshot Storage

Detected frames are automatically saved inside:

```text
captures/
```

Example:

```text
captures/
├── 20260611_180501.jpg
├── 20260611_180506.jpg
└── 20260611_180511.jpg
```

---

## 📝 Event Logs

Detection logs are stored inside:

```text
logs/events.log
```

Example:

```text
2026-06-11 18:05:01 | person | 0.92
2026-06-11 18:05:06 | car | 0.88
```

---

## 🔧 Configuration

Inside `main.py`

```python
CONFIDENCE_THRESHOLD = 0.55
SAVE_INTERVAL = 5

DETECTION_CLASSES = [
    "person",
    "car",
    "motorcycle",
    "bus",
    "truck"
]
```

---

## 💡 Future Improvements

- Face Recognition
- Intrusion Detection Zones
- Telegram Notifications
- Email Alerts
- WhatsApp Alerts
- Multi-Camera Support
- Cloud Storage Integration
- Web Dashboard
- License Plate Recognition
- Fire and Smoke Detection
- Person Tracking using DeepSORT

---

## 📈 Applications

- Smart Surveillance
- Home Security Systems
- Office Monitoring
- Traffic Monitoring
- Parking Management
- Industrial Safety Systems

---

## 👨‍💻 Author

Santhosh S

AI & Machine Learning Enthusiast

GitHub:
https://github.com/Santhosh17905

LinkedIn:
https://www.linkedin.com/in/santhosh-s-8a21802a0
---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.