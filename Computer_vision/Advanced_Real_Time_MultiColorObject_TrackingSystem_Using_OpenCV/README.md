# 🎯 Advanced Real-Time Multi-Color Object Tracking System using OpenCV


## 📌 Project Overview

The **Advanced Real-Time Multi-Color Object Tracking System** is a Computer Vision application developed using **Python** and **OpenCV** that can detect, track, and analyze colored objects in real time through a webcam feed.

Unlike traditional beginner-level color tracking projects, this system provides advanced functionalities such as:

- Real-time object tracking
- Multi-color detection
- Motion trail visualization
- Object direction prediction
- FPS monitoring
- Screenshot capture
- Video recording
- Distance estimation
- Live dashboard analytics
- Noise reduction using morphological operations

This project demonstrates fundamental and intermediate Computer Vision concepts used in robotics, surveillance systems, industrial automation, autonomous navigation, and AI-powered tracking applications.

---

# 🚀 Features

### 🎨 Multi-Color Detection

Detect and track:

- 🔴 Red Objects
- 🟢 Green Objects
- 🔵 Blue Objects

---

### 🎯 Real-Time Object Tracking

Tracks the largest detected colored object and continuously updates:

- Object Position
- Center Coordinates
- Radius
- Area

---

### 📍 Center Point Detection

Calculates the object's centroid using image moments.

Displays:

```text
X Coordinate
Y Coordinate
```

---

### 📈 FPS Monitoring

Calculates real-time processing performance.

Example:

```text
FPS: 32.8
```

---

### 🛣️ Motion Trail Visualization

Displays the path traveled by the tracked object.

Useful for:

- Robot Navigation
- Motion Analysis
- Gesture Tracking

---

### 🧭 Direction Detection

Detects movement direction:

- Left
- Right
- Up
- Down
- Still

---

### 📏 Distance Estimation

Provides approximate distance estimation based on object radius.

```text
Distance ≈ Object Size Relationship
```

---

### 📸 Screenshot Capture

Press:

```text
S
```

to save the current frame.

Example:

```text
screenshot_17253021.png
```

---

### 🎥 Video Recording

Press:

```text
R
```

to start/stop recording.

Example:

```text
recording_17253021.avi
```

---

### 🕒 Timestamp Overlay

Displays current date and time on every frame.

---

### 🧹 Noise Removal

Uses:

- Erosion
- Dilation
- Gaussian Blur

to improve tracking accuracy.

---

## 🏗️ System Architecture

```text
Webcam Input
      │
      ▼
Frame Capture
      │
      ▼
Image Preprocessing
(Gaussian Blur)
      │
      ▼
HSV Conversion
      │
      ▼
Color Masking
      │
      ▼
Morphological Operations
      │
      ▼
Contour Detection
      │
      ▼
Object Localization
      │
      ▼
Tracking & Analytics
      │
      ▼
Display Output
```

---

# 🧠 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| OpenCV | Computer Vision |
| NumPy | Numerical Operations |
| Imutils | Image Processing Utilities |
| Collections | Motion Trail Storage |
| Datetime | Timestamp Generation |

---

# 📂 Project Structure

```text
Advanced_Real_Time_MultiColorObject_TrackingSystem_Using_OpenCV
│
├── main.py
├── requirements.txt
├── README.md
│
├── screenshots/
│   ├── tracking_demo.png
│   ├── dashboard.png
│
├── recordings/
│   ├── sample_recording.avi
│
└── assets/
    └── poster.png
```

---

# ⚙️ Installation

## Step 1: Clone Repository

```bash
git clone https://github.com/santhosh17905
```

---

## Step 2: Navigate to Project

```bash
cd Advanced-Color-Object-Tracking
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Project

```bash
python main.py
```

---

# 🎮 Controls

| Key | Action |
|------|---------|
| Q | Quit Application |
| S | Capture Screenshot |
| R | Start/Stop Video Recording |

---

# 📊 Output Information

The dashboard displays:

```text
FPS
Detected Color
Center Coordinates
Object Direction
Distance Estimate
Timestamp
```

---

# 🖼️ Sample Workflow

### Step 1

Launch application.

```bash
python main.py
```

---

### Step 2

Show a colored object in front of the webcam.

Examples:

- Red Ball
- Blue Bottle
- Green Marker

---

### Step 3

System detects the object.

---

### Step 4

Tracking information appears:

```text
Color: RED
Direction: LEFT
Distance: 42 cm
FPS: 31
```

---

### Step 5

Motion trail is generated automatically.

---

# 💡 Real-World Applications

## 🤖 Robotics

Object following robots.

---

## 🏭 Industrial Automation

Product sorting based on color.

---

## 🚗 Autonomous Vehicles

Lane and marker detection.

---

## 🎮 Gaming

Gesture-controlled systems.

---

## 🎥 Surveillance

Suspicious object monitoring.

---

## 🏥 Healthcare

Motion tracking systems.

---

# 🔬 Computer Vision Concepts Covered

### Image Processing

- Gaussian Blur
- Morphological Operations

### Color Spaces

- BGR
- HSV

### Object Detection

- Contours
- Centroids
- Bounding Circles

### Object Tracking

- Motion Path
- Direction Analysis

### Performance Metrics

- FPS Monitoring

---

# 📈 Future Enhancements

- Deep Learning Based Tracking
- YOLO Object Detection Integration
- Face Tracking
- Hand Gesture Recognition
- Object Counting
- MQTT IoT Integration
- Arduino Robot Control
- Distance Measurement using Depth Cameras
- Multi-Object Tracking
- Kalman Filter Tracking
- Object Speed Estimation

---

# 🛠️ Requirements

```txt
opencv-python
numpy
imutils
```

---

# 🎯 Learning Outcomes

After completing this project, you will understand:

✅ Real-Time Video Processing

✅ HSV Color Space

✅ Color Segmentation

✅ Contour Detection

✅ Object Localization

✅ Motion Tracking

✅ OpenCV Practical Implementation

✅ Computer Vision Project Development

---

# 📚 Project Level

```text
Difficulty: Intermediate to Advanced
Category: Computer Vision
Domain: Artificial Intelligence
Project Type: Real-Time Tracking System
```

---

# 👨‍💻 Author

**Santhosh S**

Artificial Intelligence & Machine Learning Enthusiast


---

# ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

📢 Share with others

---

## 🎉  Completed Successfully

Advanced Real-Time Multi-Color Object Tracking System using OpenCV 🚀