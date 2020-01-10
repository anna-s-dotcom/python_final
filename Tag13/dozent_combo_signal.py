import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QComboBox, QVBoxLayout)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)
        self.setWindowTitle('Working Combobox')

        # Widgets
        self.label = QLabel()

        self.combo = QComboBox()
        self.combo.addItem('Item 1')
        self.combo.addItem('Item 2')
        self.combo.addItem('Item 3')
        self.combo.addItem('Item 4')
        self.combo.addItem('Item 5')

        # Signal
        self.combo.activated[str].connect(self.change)

        # Layout
        vBox = QVBoxLayout()
        vBox.addWidget(self.combo)
        vBox.addWidget(self.label)

        self.setLayout(vBox)
        self.show()

    def change(self, x):
        self.label.setText(x)


# Hauptprogramm
app = QApplication(sys.argv)
w = Window()
sys.exit(app.exec_())
