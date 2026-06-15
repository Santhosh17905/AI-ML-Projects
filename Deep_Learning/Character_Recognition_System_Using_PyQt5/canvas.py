from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import (
    QPainter,
    QPen,
    QPixmap
)
from PyQt5.QtCore import Qt


class DrawingCanvas(QWidget):

    def __init__(self):

        super().__init__()

        self.setFixedSize(280, 280)

        self.canvas = QPixmap(
            self.width(),
            self.height()
        )

        self.canvas.fill(Qt.black)

        self.last_point = None

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.drawPixmap(
            self.rect(),
            self.canvas
        )

    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:

            self.last_point = event.pos()

    def mouseMoveEvent(self, event):

        if self.last_point is not None:

            painter = QPainter(self.canvas)

            pen = QPen(
                Qt.white,
                18,
                Qt.SolidLine,
                Qt.RoundCap,
                Qt.RoundJoin
            )

            painter.setPen(pen)

            painter.drawLine(
                self.last_point,
                event.pos()
            )

            self.last_point = event.pos()

            self.update()

    def mouseReleaseEvent(self, event):

        self.last_point = None

    def clear(self):

        self.canvas.fill(Qt.black)

        self.update()

    def save_canvas(self, path):

        self.canvas.save(path)