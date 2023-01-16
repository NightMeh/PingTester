import sys
from main import RunPingFinder
import random
from PySide6 import QtCore, QtWidgets, QtGui
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.button = QtWidgets.QPushButton("Start Testing")
        self.text = QtWidgets.QLabel("Hello World")
        self.entry = QtWidgets.QLineEdit("Testing Time")
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.entry)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.run)

    @QtCore.Slot()
    def run(self):
        RunPingFinder()

app = QtWidgets.QApplication([])

widget = MyWidget()
widget.resize(100, 200)
widget.show()

sys.exit(app.exec())