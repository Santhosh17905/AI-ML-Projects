# 🌿 Plant Leaf Disease Detection using Deep Learning


## 📖 Overview

Plant diseases significantly impact agricultural productivity and food security worldwide. Early detection of plant diseases can help farmers take preventive actions and minimize crop losses.

This project uses **Deep Learning** and **Computer Vision** techniques to automatically detect plant leaf diseases from images. A pre-trained **MobileNetV2** model is used through Transfer Learning to classify leaf images into their respective disease categories with high accuracy.

The system is capable of:

- Detecting multiple plant diseases from leaf images
- Classifying healthy and infected leaves
- Providing prediction confidence scores
- Evaluating model performance using classification metrics
- Generating confusion matrices and training logs
- Saving the best performing model automatically

---

# 🚀 Features

### 🌱 Deep Learning Powered
- Transfer Learning using MobileNetV2
- Image Classification for Plant Disease Detection
- High Accuracy Predictions

### 📊 Model Evaluation
- Accuracy Score
- Validation Accuracy
- Classification Report
- Confusion Matrix
- Learning Curves

### ⚡ Training Optimizations
- Early Stopping
- Learning Rate Reduction
- Model Checkpointing
- Data Augmentation
- CSV Training Logs

### 💾 Production Ready
- Automatic Best Model Saving
- Organized Output Directory
- Standalone Prediction Script
- Easy Deployment Ready

---

# 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- OpenCV
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn

---

# 📂 Project Structure

```text
Plant_Leaf_Disease_Detection/
│
├── dataset/
│   ├── train/
│   │   ├── Disease_Class_1/
│   │   ├── Disease_Class_2/
│   │   └── ...
│   │
│   └── test/
│       ├── Disease_Class_1/
│       ├── Disease_Class_2/
│       └── ...
│
├── outputs/
│   ├── best_model.keras
│   ├── accuracy_loss.png
│   ├── confusion_matrix.png
│   └── training_log.csv
│
├── Cnn_train_fin.py(additonal)
├── predict_fin_GUI.py(additonal)
├── train.py
├── predict.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Dataset

This project expects the dataset to be organized in a folder-based structure.

Example:

```text
dataset/
│
├── train/
│   ├── Healthy/
│   ├── Early_Blight/
│   ├── Late_Blight/
│   └── ...
│
└── test/
    ├── Healthy/
    ├── Early_Blight/
    ├── Late_Blight/
    └── ...
```

Each folder name acts as a class label.

Popular Dataset:

PlantVillage Dataset

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/santhosh17905/Plant-Leaf-Disease-Detection.git

cd Plant-Leaf-Disease-Detection
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv myenv

myenv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv myenv

source myenv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🏋️ Training the Model

Run:

```bash
python train.py
```

Training process:

1. Load Dataset
2. Apply Data Augmentation
3. Build MobileNetV2 Model
4. Train Model
5. Evaluate Performance
6. Save Best Model
7. Generate Metrics and Graphs

---

# 🔍 Making Predictions

Place an image in the project folder and update:

```python
IMAGE_PATH = "sample_leaf.jpg"
```

Run:

```bash
python predict.py
```

Example Output:

```text
Prediction
---------------------------
Disease: Tomato_Early_Blight
Confidence: 98.75%
```

---

# 📈 Training Outputs

After training, the outputs folder contains:

### Best Model

```text
best_model.keras
```

### Accuracy Graph

```text
accuracy_loss.png
```

### Confusion Matrix

```text
confusion_matrix.png
```

### Training Log

```text
training_log.csv
```

---

# 🧠 Deep Learning Architecture

### Base Model

MobileNetV2

### Additional Layers

```text
Input Image
      ↓
MobileNetV2
      ↓
Global Average Pooling
      ↓
Dense Layer (512)
      ↓
Dropout Layer
      ↓
Softmax Output Layer
```

---

# 📊 Evaluation Metrics

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Validation Loss

---

# 🌾 Real-World Applications

### Smart Agriculture

Automatic disease monitoring in farms.

### Mobile Disease Detection Apps

Farmers can upload leaf images and get instant diagnosis.

### Crop Health Monitoring

Early disease detection reduces crop damage.

### Agricultural Research

Assist researchers in plant pathology studies.

---

# 🔮 Future Improvements

- Real-Time Webcam Detection
- Streamlit Web Application
- Flask API Deployment
- Mobile Application Integration
- Disease Treatment Recommendation System
- Multi-Crop Disease Detection
- Cloud Deployment

---

# 📸 Sample Workflow

```text
Leaf Image
     ↓
Image Preprocessing
     ↓
Deep Learning Model
     ↓
Disease Classification
     ↓
Prediction + Confidence Score
```

---

# 🎯 Learning Outcomes

Through this project, you will learn:

- Deep Learning Fundamentals
- Transfer Learning
- Image Classification
- Computer Vision
- Model Evaluation
- Production-Level ML Workflow
- TensorFlow and Keras

---

# 📚 Requirements

```text
tensorflow
numpy
opencv-python
matplotlib
seaborn
scikit-learn
pandas
```

Install manually:

```bash
pip install tensorflow numpy opencv-python matplotlib seaborn scikit-learn pandas
```

---

# 🏆 Project Highlights

✅ Transfer Learning

✅ MobileNetV2 Architecture

✅ Data Augmentation

✅ Early Stopping

✅ Learning Rate Scheduling

✅ Model Checkpointing

✅ Confusion Matrix

✅ Classification Report

✅ Prediction Confidence Scores

✅ Production-Ready Structure

---

# 👨‍💻 Author

Santhosh S

AI & Machine Learning Developer


---

# ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

🛠️ Contribute to improve the project

📢 Share with others

---

## License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project for educational and research purposes.