from PySide6.QtWidgets import (
    QComboBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from customer.customer import Customer

from customer.phone import Phone


class CustomerRegistrationForm(QWidget):
    def __init__(self):
        super().__init__()

        self.phones = []

        # only until db impl
        self.store_names = ["Store 1", "Store 2", "Store 3"]

        self.selected_store = None

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.sotore_label = QLabel("Loja:")
        layout.addWidget(self.sotore_label)

        self.store_combo = QComboBox()
        for store_name in self.store_names:
            self.store_combo.addItem(store_name)
        self.store_combo.currentIndexChanged.connect(self.update_selected_store)
        layout.addWidget(self.store_combo)

        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Nome")
        layout.addWidget(self.name_edit)

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

        self.perform_registration_button = QPushButton("Cadastrar cliente")
        self.perform_registration_button.clicked.connect(self.perform_registration)
        layout.addWidget(self.perform_registration_button)

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

    def update_selected_store(self, index):
        self.selected_store = self.store_names[index]

    def perform_registration(self) -> Customer:
        name = self.name_edit.text()
        if self.selected_store is not None:
            store = self.selected_store
        else:
            raise Exception("Python sucks")
        phones = self.phones

        customer = Customer(name, phones, store)
        print(customer)
        return customer
