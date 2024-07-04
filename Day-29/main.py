import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        loadUi('calculator.ui', self)
        
        self.pushButton_0.clicked.connect(lambda: self.append_number('0'))
        self.pushButton_1.clicked.connect(lambda: self.append_number('1'))
        self.pushButton_2.clicked.connect(lambda: self.append_number('2'))
        self.pushButton_3.clicked.connect(lambda: self.append_number('3'))
        self.pushButton_4.clicked.connect(lambda: self.append_number('4'))
        self.pushButton_5.clicked.connect(lambda: self.append_number('5'))
        self.pushButton_6.clicked.connect(lambda: self.append_number('6'))
        self.pushButton_7.clicked.connect(lambda: self.append_number('7'))
        self.pushButton_8.clicked.connect(lambda: self.append_number('8'))
        self.pushButton_9.clicked.connect(lambda: self.append_number('9'))
        
        self.pushButton_plus.clicked.connect(lambda: self.append_operator('+'))
        self.pushButton_minus.clicked.connect(lambda: self.append_operator('-'))
        self.pushButton_kali.clicked.connect(lambda: self.append_operator('*'))
        self.pushButton_bagi.clicked.connect(lambda: self.append_operator('/'))
        
        self.pushButton_clear.clicked.connect(self.clear_display)
        self.pushButton_hasil.clicked.connect(self.calculate_result)
        
    def append_number(self, number):
        current_text = self.lineedit.text()
        new_text = current_text + number
        self.lineedit.setText(new_text)
        
    def append_operator(self, operator):
        current_text = self.lineedit.text()
        if current_text and current_text[-1] not in '+-*/':
            new_text = current_text + operator
            self.lineedit.setText(new_text)
            
    def clear_display(self):
        self.lineedit.clear()
        
    def calculate_result(self):
        try:
            result = eval(self.lineedit.text())
            self.lineedit.setText(str(result))
        except Exception as e:
            self.lineedit.setText('Error')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
