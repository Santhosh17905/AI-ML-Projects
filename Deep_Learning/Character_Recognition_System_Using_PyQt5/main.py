from gui import App
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
window = App()
window.show()
sys.exit(app.exec_())