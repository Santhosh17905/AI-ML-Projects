
# 🎭 Image Classification using Convolutional Neural Networks (CNN)



## 📌 Project Overview

This project is a Deep Learning-based Image Classification System that distinguishes between two popular fictional characters:

* 🎭 Joker
* 🟣 Thanos

The model is built using Convolutional Neural Networks (CNNs) and trained on custom image datasets. The system automatically learns visual patterns from images and predicts whether a given image belongs to Joker or Thanos along with a confidence score.

The project demonstrates the complete Deep Learning workflow including:

* Data Preprocessing
* Data Augmentation
* CNN Model Development
* Model Training
* Model Evaluation
* Model Saving & Loading
* Image Prediction
* Confidence Score Generation

---

# 🚀 Features

### 🧠 Deep Learning Powered

* Convolutional Neural Network (CNN)
* Binary Image Classification

### 📊 Data Augmentation

* Rotation
* Zoom
* Horizontal Flip
* Width Shift
* Height Shift

### 🛡️ Overfitting Prevention

* Batch Normalization
* Dropout Layers
* Early Stopping

### ⚡ Training Optimization

* Adam Optimizer
* Reduce Learning Rate on Plateau
* Automatic Model Checkpoint Saving

### 📈 Visualization

* Accuracy Graph
* Loss Graph

### 🎯 Prediction Features

* Automatic Folder Testing
* Confidence Score
* Supports Multiple Image Formats

### 💾 Model Persistence

* Save Model Architecture
* Save Trained Weights
* Reload Trained Model

---

# 🏗️ Project Architecture

```text
Input Image
      │
      ▼
Image Preprocessing
      │
      ▼
Convolution Layer
      │
      ▼
Batch Normalization
      │
      ▼
Max Pooling
      │
      ▼
Convolution Layer
      │
      ▼
Batch Normalization
      │
      ▼
Max Pooling
      │
      ▼
Flatten
      │
      ▼
Dense Layer
      │
      ▼
Dropout
      │
      ▼
Output Layer
      │
      ▼
Prediction
```

---

# 📂 Project Structure

```text
Day_13_CNN_Joker_Thanos/
│
├── Dataset/
│   ├── train/
│   │   ├── Joker/
│   │   └── Thanos/
│   │
│   ├── val/
│   │   ├── Joker/
│   │   └── Thanos/
│   │
│   └── test/
│       ├── Joker/
│       └── Thanos/
│
├── models/
│   ├── best_model.keras
│   ├── model.json
│   └── model.weights.h5
│
├── plots/
│   ├── accuracy.png
│   └── loss.png
│
├── train.py
├── test.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🖼️ Dataset

The dataset contains images of:

### 🎭 Joker

Images collected from:

* Movie scenes
* Posters
* Wallpapers
* Fan art references

### 🟣 Thanos

Images collected from:

* Marvel movie scenes
* Posters
* Wallpapers
* Character renders

---

# ⚙️ Technologies Used

| Technology       | Purpose                 |
| ---------------- | ----------------------- |
| Python           | Programming Language    |
| TensorFlow/Keras | Deep Learning Framework |
| OpenCV           | Image Processing        |
| NumPy            | Numerical Computing     |
| Matplotlib       | Data Visualization      |
| Scikit-Learn     | Evaluation Utilities    |

---

# 🔧 Installation

## Clone Repository

```bash
git clone https://github.com/your-username/joker-vs-thanos-cnn.git
```

```bash
cd joker-vs-thanos-cnn
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

The model will:

* Load training images
* Apply data augmentation
* Train CNN
* Save best model
* Generate accuracy graph
* Generate loss graph

---

# 🔍 Testing the Model

Run:

```bash
python test.py
```

Example Output:

```text
--------------------------------------------------
Image      : joker1.jpg
Prediction : Joker
Confidence : 97.54%

--------------------------------------------------
Image      : thanos3.jpg
Prediction : Thanos
Confidence : 95.12%
```

---

# 📈 Training Features

### Early Stopping

Stops training automatically when validation performance stops improving.

### Model Checkpoint

Automatically saves the best performing model.

### Learning Rate Scheduler

Reduces learning rate when validation loss plateaus.

### Batch Normalization

Improves convergence speed and model stability.

### Dropout

Prevents overfitting by randomly disabling neurons during training.

---

# 📊 Model Performance

Metrics used:

* Accuracy
* Validation Accuracy
* Binary Cross Entropy Loss

Example Results:

| Metric              | Score             |
| ------------------- | ----------------- |
| Training Accuracy   | 85%+              |
| Validation Accuracy | 80%+              |
| Test Accuracy       | Dataset Dependent |

---

# 🎯 Real-World Applications

This project demonstrates concepts used in:

* Face Recognition Systems
* Character Recognition
* Object Classification
* Entertainment AI
* Computer Vision Applications
* Content Categorization Systems

---

# 📸 Sample Workflow

```text
Input Image
      │
      ▼
CNN Model
      │
      ▼
Feature Extraction
      │
      ▼
Classification
      │
      ▼
Joker / Thanos
      │
      ▼
Confidence Score
```

---

# 🧠 Deep Learning Concepts Covered

* Convolutional Neural Networks
* Feature Extraction
* Data Augmentation
* Binary Classification
* Batch Normalization
* Dropout Regularization
* Transfer Learning Concepts
* Model Evaluation
* Hyperparameter Tuning

---

# 🚀 Future Improvements

* Transfer Learning (MobileNetV2)
* EfficientNet Integration
* Real-Time Webcam Prediction
* Streamlit Web Application
* Flask API Deployment
* Multi-Class Character Classification
* GPU Acceleration
* Model Quantization

---

# 👨‍💻 Author

Santhosh S

Passionate about:

* Artificial Intelligence
* Machine Learning
* Deep Learning
* Computer Vision
* Full Stack Development

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

🛠️ Contribute improvements

📢 Share with others

---

# 📜 License

This project is developed for educational and learning purposes.

MIT License

Copyright (c) 2026 Santhosh S
