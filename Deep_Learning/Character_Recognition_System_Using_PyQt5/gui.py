import sys
import numpy as np
import cv2
import datetime
import pyttsx3

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from tensorflow.keras.models import load_model

from canvas import DrawingCanvas
from utils import preprocess_character
from database import init_db, log_prediction

# =========================
# LOAD MODEL
# =========================

model = load_model("model/emnist_cnn_model.h5")

# =========================
# VOICE ENGINE
# =========================

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# =========================
# MAIN APP
# =========================

class App(QMainWindow):

    def __init__(self):

        super().__init__()
        init_db()

        self.setWindowTitle("AI Character Recognition Pro")
        self.setGeometry(100, 100, 1000, 600)

        self.init_ui()

    def init_ui(self):

        central = QWidget()
        self.setCentralWidget(central)

        layout = QHBoxLayout()

        # ================= LEFT PANEL =================
        left = QVBoxLayout()

        self.canvas = DrawingCanvas()

        self.result = QLabel("Prediction: -")
        self.result.setAlignment(Qt.AlignCenter)

        self.conf = QLabel("Confidence: -")
        self.conf.setAlignment(Qt.AlignCenter)

        btn_predict = QPushButton("Predict")
        btn_clear = QPushButton("Clear")
        btn_save = QPushButton("Save")

        btn_predict.clicked.connect(self.predict)
        btn_clear.clicked.connect(self.canvas.clear)
        btn_save.clicked.connect(self.save_canvas)

        left.addWidget(self.canvas)
        left.addWidget(btn_predict)
        left.addWidget(btn_clear)
        left.addWidget(btn_save)
        left.addWidget(self.result)
        left.addWidget(self.conf)

        # ================= RIGHT PANEL =================
        right = QVBoxLayout()

        self.history = QListWidget()
        right.addWidget(QLabel("Prediction History"))
        right.addWidget(self.history)

        # ================= FINAL LAYOUT =================
        layout.addLayout(left, 2)
        layout.addLayout(right, 1)

        central.setLayout(layout)

        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                color: white;
                font-size: 14px;
            }
            QPushButton {
                background-color: #333;
                padding: 8px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #555;
            }
        """)

    # ================= PREDICTION =================

    def predict(self):

        # save canvas temporarily
        path = "temp.png"
        self.canvas.save_canvas(path)

        img = preprocess_character(path)

        prediction = model.predict(img)[0]

        class_id = np.argmax(prediction)
        confidence = np.max(prediction) * 100

        # EMNIST ASCII FIX (IMPORTANT)
        char = self.decode_emnist(class_id)

        self.result.setText(f"Prediction: {char}")
        self.conf.setText(f"Confidence: {confidence:.2f}%")

        speak(f"Predicted character {char}")

        # database log
        log_prediction(char, confidence)

        # history
        time = str(datetime.datetime.now())

        self.history.addItem(
            f"{time} | {char} | {confidence:.2f}%"
        )

    # ================= SAVE =================

    def save_canvas(self):

        path = f"saved_{datetime.datetime.now().timestamp()}.png"
        self.canvas.save_canvas(path)

        QMessageBox.information(
            self,
            "Saved",
            "Image Saved Successfully"
        )

    # ================= EMNIST DECODER =================

    def decode_emnist(self, idx):

        # EMNIST Balanced mapping fix
        if idx < 10:
            return str(idx)

        elif 10 <= idx < 36:
            return chr(idx + 55)   # A-Z

        else:
            return chr(idx + 61)   # a-z (fallback)

# ================= RUN APP =================

app = QApplication(sys.argv)
window = App()
window.show()
sys.exit(app.exec_())