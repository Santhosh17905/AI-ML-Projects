# 👤 Face Recognition System using OpenCV

A real-time **Face Recognition System** built using **Python** and **OpenCV**. The application detects faces from a webcam feed and identifies known individuals using the **LBPH (Local Binary Pattern Histogram) Face Recognizer** algorithm.

This project demonstrates the fundamentals of **Computer Vision**, **Face Detection**, and **Face Recognition**, making it an excellent beginner-to-intermediate AI/ML project.

---

# 📌 Project Overview

Face Recognition is one of the most widely used applications of Computer Vision. It enables machines to identify and verify individuals from images or video streams.

In this project:

- Faces are collected and stored as training data.
- The LBPH algorithm is trained using multiple face images.
- The webcam captures real-time video.
- Detected faces are compared against trained data.
- Recognized users are displayed with their names.
- Unknown faces are marked as "Unknown".

For demonstration purposes, the dataset includes images of:

- Elon Musk
- Steve Jobs
- Dr. A.P.J. Abdul Kalam

---

# 🎯 Features

### Core Features

✅ Real-Time Face Detection

✅ Real-Time Face Recognition

✅ Multi-Person Recognition

✅ LBPH Face Recognizer

✅ Haar Cascade Face Detection

✅ Webcam Integration

✅ Unknown Face Detection

✅ Confidence Score Prediction

✅ OpenCV-Based Implementation

---

# 🧠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| OpenCV | Computer Vision Operations |
| NumPy | Numerical Computation |
| Haar Cascade | Face Detection |
| LBPH | Face Recognition |
| Webcam | Real-Time Video Input |

---

# 📂 Project Structure

```text
Face Recognition System using OpenCV/
│
├── datasets/
│   ├── Elon/
│   │   ├── 1.jpg
│   │   ├── 2.jpg
│   │   └── ...
│   │
│   ├── Steve/
│   │   ├── 1.jpg
│   │   ├── 2.jpg
│   │   └── ...
│   │
│   └── AbdulKalam/
│       ├── 1.jpg
│       ├── 2.jpg
│       └── ...
│
├── face_recognize.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

# ⚙️ How It Works

## Step 1: Dataset Collection

Images of known individuals are stored inside the `datasets` folder.

Example:

```text
datasets/
├── Elon/
├── Steve/
└── AbdulKalam/
```

Each folder represents a unique person.

---

## Step 2: Training Phase

The program:

1. Reads all images.
2. Converts them to grayscale.
3. Assigns labels.
4. Trains the LBPH recognizer.

```python
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(images, labels)
```

---

## Step 3: Face Detection

OpenCV Haar Cascade detects faces in the webcam stream.

```python
face_cascade.detectMultiScale()
```

---

## Step 4: Face Recognition

The detected face is compared with trained faces.

```python
prediction = model.predict(face_resize)
```

If confidence is high:

```text
Elon
Steve
AbdulKalam
```

Otherwise:

```text
Unknown
```

---

# 🔬 Algorithm Used

## LBPH (Local Binary Pattern Histogram)

LBPH is one of the most popular face recognition algorithms for small and medium datasets.

### Advantages

- Fast Training
- Real-Time Performance
- Works with Small Datasets
- Easy Implementation
- Suitable for Beginners

### Limitations

- Sensitive to Lighting Conditions
- Lower Accuracy than Deep Learning Models
- Requires Proper Face Alignment

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/santhosh17905
```

```bash
cd Face-Recognition-System
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

```bash
python face_recognize.py
```

Press:

```text
ESC
```

to exit the application.

---

# 📋 Requirements

Create a file named:

```text
requirements.txt
```

Add:

```text
opencv-contrib-python
numpy
```

Install:

```bash
pip install -r requirements.txt
```

---

# 📊 Sample Output

### Known Person

```text
Elon - 145
```

### Unknown Person

```text
Unknown
```

---

# 📸 Screenshots

## Face Detection

```text
[ Insert Screenshot Here ]
```

## Face Recognition

```text
[ Insert Screenshot Here ]
```

## Unknown Person Detection

```text
[ Insert Screenshot Here ]
```

---

# 💼 Real-World Applications

### Security Systems

- Office Access Control
- Building Entry Systems
- Visitor Verification

### Attendance Systems

- School Attendance
- College Attendance
- Employee Attendance

### Authentication

- Smartphone Unlock
- Banking Verification
- Identity Verification

### Surveillance

- Smart CCTV Systems
- Public Security Monitoring
- Criminal Identification

---

# 🏗 Future Improvements

- Face Recognition Attendance System
- Face Recognition with Database Integration
- Deep Learning Face Recognition
- FaceNet Integration
- Dlib Face Recognition
- Email Alerts
- Unknown Person Logging
- Cloud-Based Recognition
- Real-Time Dashboard

---

# 📈 Learning Outcomes

By completing this project, you will understand:

- Computer Vision Fundamentals
- Image Processing
- Face Detection Techniques
- Face Recognition Concepts
- OpenCV Library Usage
- Real-Time Video Processing
- Dataset Management
- Machine Learning Basics

---

# 🎓 AI/ML Concepts Covered

- Computer Vision
- Image Processing
- Feature Extraction
- Pattern Recognition
- Classification
- Real-Time Inference
- Human Face Analysis

---

# 🔐 Disclaimer

This project is developed for educational and learning purposes only.

The dataset used in this project contains publicly available images of:

- Elon Musk
- Steve Jobs
- Dr. A.P.J. Abdul Kalam

All rights belong to their respective owners.

---

# 👨‍💻 Author

**Santhosh S**

AI & Machine Learning Enthusiast



GitHub: https://github.com/Santhosh17905

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

📢 Share with others

---

