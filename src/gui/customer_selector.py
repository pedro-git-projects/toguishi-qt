from PySide6.QtWidgets import QComboBox, QLabel, QVBoxLayout, QWidget
from customer.customer import Customer

from db.db_manager import DBManager
from gui.customer_form import CustomerRegistrationForm


class CustomerSelector(QWidget):
    def __init__(self, db_manager: DBManager, customer_form: CustomerRegistrationForm):
        super().__init__()

        self.db_manager = db_manager
        self.customer_form = customer_form
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.customer_label = QLabel("Cliente:")
        self.customer_combo = QComboBox()

        customers = self.db_manager.get_all_customers()
        for customer in customers:
            self.customer_combo.addItem(customer["name"])

        layout.addWidget(self.customer_label)
        layout.addWidget(self.customer_combo)

    def get_selected_customer(self) -> Customer:
        selected_index = self.customer_combo.currentIndex()
        if selected_index >= 0:
            selected_name = self.customer_combo.itemText(selected_index)
            customer = self.db_manager.get_store_by_name(selected_name)
            if customer:
                return Customer(
                    customer["name"],
                    customer["phones"],
                    customer["store"],
                )
        raise Exception("is fucked")

    def populate_customer_combo(self):
        customers = self.db_manager.get_all_customers()
        for customer in customers:
            customer_object = Customer(
                customer["name"],
                customer["phones"],
                customer["store"],
                self.db_manager,
            )
            self.customer_combo.addItem(customer["name"], userData=customer_object)

    # slot
    def update_customer_combo(self):
        self.customer_combo.clear()
        self.populate_customer_combo()
