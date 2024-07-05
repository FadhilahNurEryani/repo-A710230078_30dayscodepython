import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox

class ContactManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contact Manager")
        self.setGeometry(100, 100, 400, 300)
        
        self.contacts = []

        self.initUI()

    def initUI(self):
        widget = QWidget()
        self.setCentralWidget(widget)

        layout = QVBoxLayout()
        widget.setLayout(layout)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Nama")
        layout.addWidget(self.name_input)

        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Nomor Telepon")
        layout.addWidget(self.phone_input)

        self.add_button = QPushButton("Tambah Kontak")
        self.add_button.clicked.connect(self.add_contact)
        layout.addWidget(self.add_button)

        self.contact_list = QListWidget()
        layout.addWidget(self.contact_list)

        self.delete_button = QPushButton("Hapus Kontak")
        self.delete_button.clicked.connect(self.delete_contact)
        layout.addWidget(self.delete_button)

    def add_contact(self):
        name = self.name_input.text()
        phone = self.phone_input.text()

        if name and phone:
            self.contacts.append((name, phone))
            self.contact_list.addItem(f"{name} - {phone}")
            self.name_input.clear()
            self.phone_input.clear()
        else:
            QMessageBox.warning(self, "Peringatan", "Nama dan nomor telepon harus diisi!")

    def delete_contact(self):
        selected_items = self.contact_list.selectedItems()
        if not selected_items:
            return

        for item in selected_items:
            self.contact_list.takeItem(self.contact_list.row(item))
            contact = item.text().split(" - ")
            self.contacts.remove((contact[0], contact[1]))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ContactManager()
    window.show()
    sys.exit(app.exec_())
