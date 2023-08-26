from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
)

from db.db_manager import DBManager
from gui.category_selector import CategorySelector
from gui.item_form_concrete import ItemFormConcrete

from service.payment import Payment


class ServiceItemForm(QWidget):
    def __init__(self, db_manager: DBManager):
        super().__init__()
        self.db_manager = db_manager

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.setup_category_section(layout)
        self.setup_item_form(layout)
        self.setup_price_section(layout)

    def setup_category_section(self, layout):
        self.category_selector = CategorySelector()
        layout.addWidget(self.category_selector)

    def setup_price_section(self, layout):
        price_layout = QHBoxLayout()

        self.inital_price_edit = QLineEdit()
        self.inital_price_edit.setPlaceholderText("Preço")

        self.discount_edit = QLineEdit()
        self.discount_edit.setPlaceholderText("Desconto")

        price_layout.addWidget(self.inital_price_edit)
        price_layout.addWidget(self.discount_edit)

        layout.addLayout(price_layout)

    def setup_payment_section(self, layout):
        self.payment_label = QLabel("Forma de pagamento:")
        self.payment_combo = QComboBox()
        for payment in Payment:
            self.payment_combo.addItem(str(payment))

        layout.addWidget(self.payment_label)
        layout.addWidget(self.payment_combo)

    def setup_item_form(self, layout):
        self.item_form = ItemFormConcrete()
        layout.addWidget(self.item_form)

    def perform_registration(self):
        selected_category = self.category_selector.get_selected_category()
        selected_item = self.item_form.get_selected_item_data()
        print(selected_category)
        print(selected_item)
