# 🚀 AI-Powered Face Detection & Tracking System

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)
![License](https://img.shields.io/badge/License-MIT-orange.svg)

A professional-grade real-time Face Detection and Tracking application built using OpenCV. The system detects human faces from a live webcam feed, tracks them in real-time using advanced tracking algorithms, provides performance analytics, event logging, screenshot capture, and an intuitive monitoring dashboard.

---

## 📌 Project Overview

This project demonstrates the fundamentals of Computer Vision and Real-Time Object Tracking.

The application:

- Detects faces from webcam streams.
- Tracks faces continuously in real-time.
- Displays live FPS statistics.
- Logs detection and tracking events.
- Captures screenshots on demand.
- Automatically re-detects faces if tracking is lost.
- Provides a professional monitoring interface.

This project is suitable for:

- Computer Vision Learning
- OpenCV Practice
- AI/ML Portfolio Projects
- Resume Building
- Final Year Mini Projects
- Interview Demonstrations

---

## 🎯 Features

### Face Detection

- Real-time face detection
- Haar Cascade based detection
- Bounding box visualization
- Multi-scale face detection

### Face Tracking

- CSRT Tracker Integration
- Auto face tracking
- Tracking status indicator
- Automatic re-detection

### Monitoring Dashboard

- Live FPS Counter
- Face Count Display
- Detection Statistics
- Session Uptime

### Screenshot System

- One-click screenshot capture
- Timestamp-based naming
- Automatic storage management

### Logging System

- Face detection events
- Tracking loss events
- Application lifecycle logs

### User Interface

- Professional overlay panel
- Real-time status updates
- Clean visual design

---

## 🛠 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Core Programming |
| OpenCV | Computer Vision |
| NumPy | Numerical Processing |
| CSRT Tracker | Object Tracking |
| Haar Cascade | Face Detection |

---

## 📂 Project Structure

```text
AI_Powered_Face_Detection & Tracking System
│
├── main.py
│
├── screenshots/
│   ├── 20260611_120501.jpg
│   ├── 20260611_120842.jpg
│
├── logs/
│   └── face_log.txt
│
├── assets/
│   └── demo.gif
│
├── requirements.txt
│
├── README.md
│
└── LICENSE
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/santhosh17905
```

```bash
cd AI-Face-Detection-Tracking
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

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

---

## 🎮 Controls

| Key | Function |
|------|----------|
| S | Save Screenshot |
| Q | Quit Application |

---

## 🧠 System Workflow

```text
Webcam Feed
      │
      ▼
Frame Acquisition
      │
      ▼
Grayscale Conversion
      │
      ▼
Face Detection
      │
      ▼
Face Tracking
      │
      ▼
Performance Analysis
      │
      ▼
UI Rendering
      │
      ▼
Display Output
```

---

## 📸 Screenshot Feature

Press:

```text
S
```

The application automatically saves screenshots inside:

```text
screenshots/
```

Example:

```text
screenshots/
├── 20260611_102301.jpg
├── 20260611_103120.jpg
```

---

## 📊 Logging

Application logs are stored in:

```text
logs/face_log.txt
```

Example:

```text
[2026-06-11 10:25:01] Face Detected
[2026-06-11 10:25:15] Tracking Started
[2026-06-11 10:26:10] Tracking Lost
[2026-06-11 10:27:20] Screenshot Saved
```

---

## 🚀 Future Enhancements

- Deep Learning Face Detection
- YOLO Face Detector
- Face Recognition
- Multi-Face Tracking
- Face Attendance System
- SQLite Database Integration
- Email Alerts
- Telegram Notifications
- Cloud Storage Support
- GPU Acceleration

---

## 💡 Real World Applications

### Security Surveillance

Monitor individuals in restricted areas.

### Smart Attendance

Automated employee/student attendance.

### Face Unlock Systems

Biometric authentication.

### Retail Analytics

Customer movement tracking.

### Smart Cameras

Auto-focus and person tracking.

### AI Monitoring Systems

Real-time visual analytics.

---

## 📈 Performance Metrics

| Metric | Value |
|----------|----------|
| Detection Speed | Real-Time |
| Tracking Accuracy | High |
| FPS | Hardware Dependent |
| Latency | Low |
| Resource Usage | Moderate |

---

## 🎓 Learning Outcomes

By completing this project, you will learn:

- Computer Vision Fundamentals
- Real-Time Video Processing
- Face Detection Techniques
- Object Tracking Algorithms
- OpenCV Development
- Performance Optimization
- OOP Design Patterns
- Event Logging Systems

---

## 🏆 Resume Description

Developed a professional real-time Face Detection and Tracking System using OpenCV and Python. Implemented face detection, object tracking, screenshot management, event logging, performance monitoring, and automated tracking recovery mechanisms. Designed a scalable architecture suitable for intelligent surveillance and monitoring applications.

---

## 👨‍💻 Author

Santhosh S

LinkedIn: https://www.linkedin.com/in/santhosh-s-8a21802a0

GitHub: https://github.com/santhosh17905

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

📢 Share with others

---

## 📜 License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project for educational and personal purposes.