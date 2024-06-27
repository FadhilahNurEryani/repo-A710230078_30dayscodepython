import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class HelloWorld(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel("Hello, World!", self)
        label.move(50, 50)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Hello World")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = HelloWorld()
    sys.exit(app.exec_())