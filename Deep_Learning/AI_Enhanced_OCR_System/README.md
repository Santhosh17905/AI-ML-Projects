# 🚀 AI Enhanced OCR System

An advanced Optical Character Recognition (OCR) application built using Deep Learning, OpenCV, and EasyOCR. This project accurately extracts text from images and live webcam feeds, providing real-time text recognition with bounding box visualization, confidence scoring, and structured output export.

---

## 📌 Overview

The AI Enhanced OCR System is designed to overcome the limitations of traditional OCR engines by leveraging deep learning-based text detection and recognition.

The system can:

- Detect text from images
- Perform real-time OCR using a webcam
- Recognize multiple font styles
- Handle noisy and low-quality images
- Display text bounding boxes
- Export OCR results to JSON
- Provide confidence scores for each detected text region

This project demonstrates the integration of Computer Vision and Artificial Intelligence for practical text extraction applications.

---

## 🎯 Features

### 🔥 AI-Based OCR
- Deep learning powered text recognition using EasyOCR
- Better accuracy than traditional OCR engines
- Robust font and text style detection

### 📷 Real-Time Webcam OCR
- Live text detection from webcam feed
- Continuous recognition pipeline
- Optimized frame processing

### 🖼 Image OCR
- Extract text from images
- Supports JPG, JPEG, PNG, BMP formats

### 📦 Structured Output
- Confidence score for each detection
- Bounding box coordinates
- JSON export support

### ⚡ Performance Optimization
- Frame skipping strategy
- Image preprocessing pipeline
- Improved OCR speed and stability

### 🎨 Visual Feedback
- Real-time bounding box visualization
- Text overlays on detected regions

---

# 🏗 System Architecture

```text
                Input Image / Webcam
                          │
                          ▼
                Image Preprocessing
                          │
                          ▼
                    EasyOCR Engine
                          │
                          ▼
                Text Detection & OCR
                          │
                          ▼
              Confidence Score Filter
                          │
                          ▼
             Bounding Box Visualization
                          │
                          ▼
          JSON Export + Screen Output
```

---

# 🧠 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Core Programming |
| OpenCV | Computer Vision |
| EasyOCR | AI OCR Engine |
| NumPy | Numerical Processing |
| Pillow | Image Processing |
| JSON | Result Export |

---

# 📂 Project Structure

```text
Day_17_AI_OCR/
│
├── ai_ocr.py
│
├── output/
│   ├── a.json
│   └── a.txt
│
├── Code
│   ├── opticalCharacterRecognition.py(additional)
│   ├── opticalCharacterRecognition2.py(additional)
│   └── TEST1.jpg
│   └── TEST2.jpg
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙ Installation

## Step 1: Clone Repository

```bash
git clone https://github.com/santhosh17905
cd AI-Enhanced-OCR
```

---

## Step 2: Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Usage

---

## Image OCR

```bash
python ai_ocr.py --image sample_images/test1.jpg
```

### Output

```text
Detected Text

AI Enhanced OCR (0.98)
Deep Learning OCR (0.96)
```

---

## Webcam OCR

```bash
python ai_ocr.py --webcam
```

### Controls

| Key | Action |
|------|---------|
| Q | Quit Application |

---

# 📊 Example JSON Output

```json
[
    {
        "text": "AI Enhanced OCR",
        "confidence": 0.98,
        "bbox": [
            [50,40],
            [300,40],
            [300,90],
            [50,90]
        ]
    }
]
```

---

# 🖼 OCR Pipeline

## 1. Image Acquisition

Input sources:
- Image files
- Live webcam feed

---

## 2. Image Preprocessing

Applied operations:

- Grayscale conversion
- Image upscaling
- Gaussian smoothing
- Noise reduction

---

## 3. AI Text Detection

EasyOCR Deep Learning Model:

- Text localization
- Character recognition
- Confidence estimation

---

## 4. Post Processing

- Confidence filtering
- Bounding box generation
- Result formatting

---

# 🚀 Applications

### 📄 Document Digitization

Convert physical documents into machine-readable text.

---

### 🏷 Product Label Reading

Extract:

- Product Name
- Price
- Expiry Date
- Manufacturing Details

---

### 💊 Medicine Recognition

Identify:

- Drug Name
- Batch Number
- Expiry Date

---

### 📚 Smart Study Assistant

Extract notes from:

- Books
- Handwritten notes
- Printed materials

---

### 🏢 Business Automation

OCR integration for:

- Invoices
- Receipts
- Forms
- Reports

---

# 📈 Future Enhancements

- Multi-language OCR
- PDF OCR Support
- Handwritten Text Recognition
- Text-to-Speech Conversion
- Flask Web Application
- Streamlit Dashboard
- Mobile App Integration
- Database Storage
- AI Spell Correction
- Document Scanner Mode

---

# 🔬 Performance

| Metric | Value |
|----------|--------|
| OCR Engine | EasyOCR |
| Language | English |
| Real-Time Support | Yes |
| Confidence Filtering | Yes |
| JSON Export | Yes |
| Webcam OCR | Yes |
| Bounding Boxes | Yes |

---

# 🛡 Error Handling

The system handles:

- Invalid image paths
- Webcam failures
- Empty detections
- Model initialization errors
- Export exceptions

---

# 📚 Learning Outcomes

Through this project, developers gain knowledge in:

- Computer Vision
- Deep Learning OCR
- OpenCV Processing
- AI-Based Text Recognition
- Real-Time Video Processing
- Python Application Development

---

# 🤝 Contributing

Contributions are welcome.

Steps:

1. Fork repository
2. Create feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added feature"
```

4. Push

```bash
git push origin feature-name
```

5. Open Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Santhosh S

AI • Machine Learning • Computer Vision • Deep Learning

---

## ⭐ If you found this project useful, consider giving it a Star on GitHub.