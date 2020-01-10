import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QTextEdit

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)
        self.setWindowTitle('Working Button')

        # self.line = QLineEdit()
        self.txt = QTextEdit()
        self.label = QLabel()
        self.senden = QPushButton('Senden')

        self.senden.clicked.connect(self.send)

        # Layout
        vBox = QVBoxLayout()
        # vBox.addWidget(self.line)
        vBox.addWidget(self.txt)
        vBox.addWidget(self.senden)
        vBox.addWidget(self.label)

        self.setLayout(vBox)
        self.show()

    def send(self):
        # txt = self.line.text()
        txt = self.txt.toPlainText()
        self.label.setText(txt)

# Hauptprogramm
app = QApplication(sys.argv)
w = Window()
sys.exit(app.exec_())
