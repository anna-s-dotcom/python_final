import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # QWidget.__init__(self)
        self.resize(640, 480)
        self.setWindowTitle('Hello World!')
        self.setWindowIcon(QIcon('welt.jpg'))
        self.show()

# Programmaufruf
app = QApplication(sys.argv)
w = Window()

sys.exit(app.exec_())
