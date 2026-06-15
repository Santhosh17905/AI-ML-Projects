# 🩺 Covid-19 Detection using Deep Learning (CNN + ResNet50)

An advanced AI-powered web application that detects **Covid-19 from Chest X-ray images** using **Deep Learning (ResNet50)** and provides **visual explanations (Grad-CAM)**.

---

## 🚀 Features

* 🤖 Deep Learning Model (ResNet50 - Transfer Learning)
* 🧠 Binary Classification (Covid vs Normal)
* 🔥 Grad-CAM Visualization (Explainable AI)
* 📊 Confidence Score Display
* 🖥️ Modern Glass UI (Streamlit)
* 📂 Image Upload & Instant Prediction
* 💾 Model Saving & Loading

---

## 🧠 Tech Stack

* Python
* TensorFlow / Keras
* OpenCV
* NumPy
* Streamlit
* Matplotlib
* Pillow

---

## 📁 Project Structure

Covid19_Detection_Using_CNN/
│
├── app.py                # Streamlit Web App
├── train.py              # Model Training Script
├── gradcam.py            # Grad-CAM Visualization
├── requirements.txt
├── README.md
│
├── model/
│   └── covid_resnet50.h5
│
├── TestingDataset/
│   ├── train/
│   │   ├── Covid/
│   │   └── Normal/
│   │
│── TrainingDataset/
│       ├── Covid/
│       └── Normal/

---

## ▶️ How to Run

### 1️⃣ Clone Repository

git clone https://github.com/Santhosh17905/covid-ai-app.git
cd Covid19_Detection_Using_CNN

---

### 2️⃣ Install Dependencies

pip install -r requirements.txt

---

### 3️⃣ Train Model

python train.py

👉 This will:

* Train ResNet50 model
* Save model in `model/` folder

---

### 4️⃣ Run Web App

streamlit run app.py

---

## 🎮 Usage

1. Upload a chest X-ray image
2. Model predicts:

   * ✅ Normal
   * ⚠️ Covid Positive
3. View:

   * Confidence score
   * AI focus area (Grad-CAM)

---

## 📊 Model Details

* Architecture: ResNet50 (Transfer Learning)
* Input Size: 224 × 224
* Output: Binary Classification
* Activation: Sigmoid

---

## 🧠 How It Works

### 🔹 Step 1: Image Preprocessing

* Resize to 224x224
* Normalize pixel values

### 🔹 Step 2: Prediction

* Model outputs probability

### 🔹 Step 3: Grad-CAM

* Highlights important lung regions
* Shows where AI is focusing

---

## 🔥 Output Example

* Prediction: Covid Positive
* Confidence: 92.45%
* Heatmap: Shows infected lung region

---

## 🧪 Future Improvements

* 🏥 Multi-class classification (Pneumonia, TB)
* 📊 Patient history tracking
* ☁️ Cloud deployment (Streamlit Cloud)
* 📱 Mobile-friendly UI
* 📄 PDF report generation

---

## 💼 Resume Description

Built an AI-powered medical image classification system using ResNet50 and Grad-CAM to detect Covid-19 from chest X-rays with explainable predictions and a modern web interface.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---

## 📬 Contact

Santhosh
GitHub: https://github.com/Santhosh17905

---
