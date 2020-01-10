import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtWidgets import QVBoxLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)
        self.setWindowTitle('PlusMinus')

        self.x = 0
        self.label = QLabel(f'{self.x}')
        self.plus = QPushButton('Plus 5')
        self.minus = QPushButton('Minus 5')

        self.plus.clicked.connect(lambda: self.calc(5))
        self.minus.clicked.connect(lambda: self.calc(-5))

        # Layout
        vBox = QVBoxLayout()
        vBox.addWidget(self.plus)
        vBox.addWidget(self.minus)
        vBox.addWidget(self.label)

        self.setLayout(vBox)
        self.show()


    def calc(self, value):
        self.x += value
        self.label.setText(f'{self.x}')


# Hauptprogramm
app = QApplication(sys.argv)
w = Window()
sys.exit(app.exec_())
