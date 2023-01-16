import sys
from main import RunPingFinder
import random
from PySide6 import QtCore, QtWidgets, QtGui
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.button = QtWidgets.QPushButton("Start Test")
        self.entry = QtWidgets.QLineEdit("")
        self.entry.setPlaceholderText("Enter Time in Seconds")
        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.entry)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.run)
        

    @QtCore.Slot()
    def run(self):
        RunPingFinder(int(self.entry.text()))

app = QtWidgets.QApplication([])

widget = MyWidget()
widget.resize(700, 200)
widget.show()

sys.exit(app.exec())