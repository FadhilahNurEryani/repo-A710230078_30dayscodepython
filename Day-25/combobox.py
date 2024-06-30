import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel

class ComboBox(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel("Select an option:", self)
        label.move(50, 50)
        self.combobox = QComboBox(self)
        self.combobox.addItem("Option 1")
        self.combobox.addItem("Option 2")
        self.combobox.addItem("Option 3")
        self.combobox.move(50, 80)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Combo Box")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ComboBox()
    sys.exit(app.exec_())