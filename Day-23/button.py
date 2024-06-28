import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class ButtonClick(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        button = QPushButton("Click me", self)
        button.move(50, 50)
        button.clicked.connect(self.onButtonClick)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Button Click")
        self.show()

    def onButtonClick(self):
        print("Button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ButtonClick()
    sys.exit(app.exec_())