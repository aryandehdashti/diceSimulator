import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QTextEdit
import random as ran

class DiceSimulator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._diceSize = 0
        self.setWindowTitle('Dice Simulator')
        self.resize( 500, 300)

        layout = QHBoxLayout()

        self.textEdit = QTextEdit()
        layout.addWidget(self.textEdit)

        self.btn4 = QPushButton('4')
        layout.addWidget(self.btn4)

        self.btn6 = QPushButton('6')
        layout.addWidget(self.btn6)

        self.btn8 = QPushButton('8')
        layout.addWidget(self.btn8)

        self.btn10 = QPushButton('10')
        layout.addWidget(self.btn10)

        self.btn12 = QPushButton('12')
        layout.addWidget(self.btn12)

        self.btn20 = QPushButton('20')
        layout.addWidget(self.btn20)

        self.btn100 = QPushButton('100')
        layout.addWidget(self.btn100)

        self.setLayout(layout)

        self.btn4.clicked.connect(self.btn4Clicked)
        self.btn6.clicked.connect(self.btn6Clicked)
        self.btn8.clicked.connect(self.btn8Clicked)
        self.btn10.clicked.connect(self.btn10Clicked)
        self.btn12.clicked.connect(self.btn12Clicked)
        self.btn20.clicked.connect(self.btn20Clicked)
        self.btn100.clicked.connect(self.btn100Clicked)

    def btn4Clicked(self):
        self.textEdit.setPlainText(str(ran.randrange(4) + 1))
        
    def btn6Clicked(self):
        self.textEdit.setPlainText(str(ran.randrange(6) + 1))
        
    def btn8Clicked(self):
        self.textEdit.setPlainText(str(ran.randrange(8) + 1))

    def btn10Clicked(self):
        self.textEdit.setPlainText(str(ran.randrange(10) + 1))

    def btn12Clicked(self):
        self.textEdit.setPlainText(str(ran.randrange(12) + 1))

    def btn20Clicked(self):
        self.textEdit.setPlainText(str(ran.randrange(20) + 1))

    def btn100Clicked(self):
        self.textEdit.setPlainText(str(ran.randrange(100) + 1))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = DiceSimulator()
    w.show()
    sys.exit(app.exec_())