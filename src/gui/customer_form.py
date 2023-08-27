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
from customer.store import Store
from db.db_manager import DBManager


class CustomerRegistrationForm(QWidget):
    def __init__(self, db_manager: DBManager):
        super().__init__()

        self.db_manager = db_manager
        self.phones = []
        self.selected_store = None

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.setup_store_section(layout)
        self.setup_name_section(layout)
        self.setup_phone_section(layout)
        self.setup_registration_section(layout)

    def setup_store_section(self, layout):
        self.store_label = QLabel("Loja:")
        layout.addWidget(self.store_label)

        self.store_combo = QComboBox()
        self.populate_store_combo()
        self.store_combo.currentIndexChanged.connect(self.update_selected_store)
        layout.addWidget(self.store_combo)

    def setup_name_section(self, layout):
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Nome")
        layout.addWidget(self.name_edit)

    def setup_phone_section(self, layout):
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

    def setup_registration_section(self, layout):
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
        selected_store = self.store_combo.itemData(index)
        self.selected_store = selected_store
        print("custumer form::", selected_store)

    def perform_registration(self) -> Customer:
        name = self.name_edit.text()
        if self.selected_store is not None:
            store = self.selected_store
        else:
            raise Exception("Selected store is nil")
        phones = self.phones
        customer = Customer(name, phones, store, self.db_manager)
        id = customer.save()
        print(f"customer[{id}]: {customer}")
        return customer

    def populate_store_combo(self):
        stores = self.db_manager.get_all_stores()
        for store in stores:
            store_object = Store(
                store["name"], store["address"], store["phones"], self.db_manager
            )
            self.store_combo.addItem(store["name"], userData=store_object)

    def update_store_combo(self):
        self.store_combo.clear()
        self.populate_store_combo()
