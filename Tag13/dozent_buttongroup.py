import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWidgets import QRadioButton, QButtonGroup, QLabel

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)
        self.setWindowTitle('Working ButtonGroup')

        self.label = QLabel('Default')

        self.rb1 = QRadioButton('Radio 1')
        self.rb2 = QRadioButton('Radio 2')
        self.rb3 = QRadioButton('Radio 3')

        self.group = QButtonGroup()
        self.group.addButton(self.rb1)
        self.group.addButton(self.rb2)
        self.group.addButton(self.rb3)

        self.group.buttonClicked.connect(self.change)


        # Layout

        vBox = QVBoxLayout()
        vBox.addWidget(self.rb1)
        vBox.addWidget(self.rb2)
        vBox.addWidget(self.rb3)
        vBox.addWidget(self.label)

        self.setLayout(vBox)
        self.show()

    def change(self):
        if self.rb1.isChecked():
            self.label.setText('erster')
        elif self.rb2.isChecked():
            self.label.setText('zweiter')
        elif self.rb3.isChecked():
            self.label.setText('dritter')

# Hauptprogramm
app = QApplication(sys.argv)
w = Window()
sys.exit(app.exec_())
