from PySide6.QtWidgets import QLineEdit, QListWidget, QPushButton, QVBoxLayout, QWidget

from customer.phone import Phone


class StoreForm(QWidget):
    def __init__(self):
        super().__init__()

        self.phones = []

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Nome")
        layout.addWidget(self.name_edit)

        self.address_edit = QLineEdit()
        self.address_edit.setPlaceholderText("Endereço")
        layout.addWidget(self.address_edit)

        self.phone_edit = QLineEdit()
        self.phone_edit.setPlaceholderText("(DDD)XXXXXXXX")
        layout.addWidget(self.phone_edit)

        self.add_phone_button = QPushButton("Adicionar Telefone")
        self.add_phone_button.clicked.connect(self.add_phone)
        layout.addWidget(self.add_phone_button)

        self.remove_phone_button = QPushButton("Remover Telefone")
        self.remove_phone_button.clicked.connect(self.remove_phone)
        layout.addWidget(self.remove_phone_button)

        self.phone_list = QListWidget()
        layout.addWidget(self.phone_list)

    def add_phone(self):
        new_phone_number = self.phone_edit.text()
        new_phone = Phone(new_phone_number)
        if new_phone.is_valid():
            self.phones.append(new_phone)
            self.phone_list.addItem(new_phone.number)
            self.phone_edit.clear()

    def remove_phone(self):
        selected_item = self.phone_list.currentItem()
        if selected_item:
            selected_phone_number = selected_item.text()

            selected_phone = Phone(selected_phone_number)

            if selected_phone in self.phones:
                self.phones.remove(selected_phone)
                self.phone_list.takeItem(self.phone_list.row(selected_item))
