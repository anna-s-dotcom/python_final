# Erstelle eine GUI, welche eine Zahl über ein QLineEdit Feld einliest.
# Beim Drücken einer Schaltfläche soll die Zahl zu 10 addiert werden.
# Das ganze soll entweder als Label ausgegeben werden oder in einem anderen Textfeld.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QLineEdit


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)
        self.setWindowTitle('Plus from Line')


        self.line = QLineEdit()
        self.line.setPlaceholderText('Insert Number!')

        self.button = QPushButton('Add from Line')

        self.label = QLabel('10')

        self.value = 10

        self.button.clicked.connect(self.change)
        self.line.returnPressed.connect(self.change)

        # Layout
        vBox = QVBoxLayout()
        vBox.addWidget(self.line)
        vBox.addWidget(self.button)
        vBox.addWidget(self.label)

        self.setLayout(vBox)
        self.show()

    def change(self):
        try:
            val = float(self.line.text())
            self.value += val
            self.label.setText(str(self.value))
        except:
            pass
# Hauptprogramm
app = QApplication(sys.argv)
w = Window()
sys.exit(app.exec_())
