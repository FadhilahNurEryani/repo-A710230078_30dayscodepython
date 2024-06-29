import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel

class TextInput(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel("Enter your name:", self)
        label.move(50, 50)
        self.textbox = QLineEdit(self)
        self.textbox.move(50, 80)
        self.textbox.returnPressed.connect(self.onEnterPressed)
        self.output_label = QLabel(self)
        self.output_label.move(50, 110)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Text Input")
        self.show()

    def onEnterPressed(self):
        text = self.textbox.text()
        self.output_label.setText("Hello, " + text + "!")
        self.output_label.adjustSize()  # Add this line to update the label size

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = TextInput()
    sys.exit(app.exec_())