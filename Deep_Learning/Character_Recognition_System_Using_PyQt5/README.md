# ✍️ AI Character Recognition System (EMNIST + CNN + PyQt5)

A **deep learning-based character recognition desktop application** that recognizes handwritten **A–Z and 0–9 characters (47 classes)** using a Convolutional Neural Network (CNN) trained on the EMNIST Balanced dataset.

The project features a **modern PyQt5 GUI**, real-time drawing canvas, prediction history, confidence scoring, and database logging — making it a complete **end-to-end AI desktop application**.

---

# 🚀 Project Overview

This system allows users to:

- Draw characters on a canvas 🖊️
- Upload handwritten images 📂
- Predict characters using CNN 🤖
- View confidence scores 📊
- Store prediction history 🗃️
- Get voice feedback 🔊

It is built using **Deep Learning + Computer Vision + Desktop GUI Development**.

---

# 🧠 Tech Stack

| Component | Technology |
|----------|------------|
| Deep Learning | TensorFlow / Keras |
| Dataset | EMNIST Balanced |
| GUI | PyQt5 |
| Image Processing | OpenCV |
| Data Handling | NumPy / Pandas |
| Database | SQLite |
| Voice Output | pyttsx3 |

---

# 📂 Dataset Used

We use the **EMNIST Balanced dataset**:

- 47 Classes (A–Z, 0–9, special characters)
- 112,800 training images
- 18,800 test images

Dataset source:
https://www.nist.gov/itl/products-and-services/emnist-dataset

---

# 🧠 Model Architecture

The CNN model includes:

- Convolutional Layers (Conv2D)
- Batch Normalization
- MaxPooling Layers
- Dropout Regularization
- Fully Connected Dense Layers

### Final Accuracy:
~89% on EMNIST Balanced


---

# 🖥️ Features

## 🎨 Drawing Canvas
- Draw characters using mouse
- Real-time stroke rendering
- Clear canvas option

## 🤖 AI Prediction
- CNN-based classification
- Predicts A–Z / 0–9
- Top-3 probability output
- Confidence percentage

## 📊 Analytics
- Prediction history
- Timestamp logging
- CSV export support

## 🗃️ Database
- SQLite integration
- Stores predictions permanently

## 🔊 Voice Output
- Speaks predicted character

---

# 📁 Project Structure
Character_Recognition_Pro/

│
├── dataset/
│ ├── emnist-balanced-train-images-idx3-ubyte
│ ├── emnist-balanced-train-labels-idx1-ubyte
│ ├── emnist-balanced-test-images-idx3-ubyte
│ └── emnist-balanced-test-labels-idx1-ubyte
│
├── model/
│ └── emnist_cnn_model.h5
│
├── database/
│ └── predictions.db
│
├── logs/
│ └── prediction_log.csv
│
├── canvas.py
├── utils.py
├── class_mapping.py
├── database.py
├── train_model.py
├── gui.py
├── requirements.txt
└── README.md


🧠 How It Works

User draws character
        ↓
Canvas converts to image
        ↓
Preprocessing (OpenCV)
        ↓
EMNIST normalization
        ↓
CNN Model prediction
        ↓
Top-3 results + confidence
        ↓
GUI displays output + logs result


---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository
```bash
git clone https://github.com/santhosh17905
cd character-recognition-ai

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Training (Optional if model exists)
python train_model.py
5️⃣ Run Application
python gui.py


📊 Model Performance

| Metric     | Value           |
| ---------- | --------------- |
| Accuracy   | ~89%            |
| Classes    | 47              |
| Input Size | 28×28           |
| Dataset    | EMNIST Balanced |


🔥 Future Improvements


🌐 Web deployment using Flask/FastAPI
📱 Mobile app version
🧠 Transformer-based OCR upgrade
🎯 Real-time webcam character recognition
☁️ Cloud model deployment

👨‍💻 Author

Santhosh S
AI/ML Developer

⭐ If you like this project

Give a ⭐ on GitHub and share it with others!

📌 License

This project is for educational purposes.