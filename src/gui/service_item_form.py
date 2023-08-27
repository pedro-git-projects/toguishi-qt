from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from db.db_manager import DBManager
from gui.category_selector import CategorySelector
from gui.item_form_concrete import ItemFormConcrete
from gui.price_widget import PriceWidget
from service.service_item import ServiceItem


class ServiceItemForm(QWidget):
    submitted = Signal(ServiceItem)

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
        self.setup_registration_button(layout)

    def setup_category_section(self, layout):
        self.category_selector = CategorySelector()
        layout.addWidget(self.category_selector)

    def setup_price_section(self, layout):
        self.price_widget = PriceWidget()
        layout.addWidget(self.price_widget)

    def setup_item_form(self, layout):
        self.item_form = ItemFormConcrete()
        layout.addWidget(self.item_form)

    def setup_registration_button(self, layout):
        self.registration_button = QPushButton("Registrar")
        self.registration_button.clicked.connect(self.perform_registration)
        layout.addWidget(self.registration_button)

    def perform_registration(self):
        selected_category = self.category_selector.get_selected_category()
        selected_item = self.item_form.get_selected_item_data()
        initial_price = self.price_widget.get_initial_price()
        discount = self.price_widget.get_discount()
        service_item = ServiceItem(
            selected_category, selected_item, initial_price, discount
        )
        print(service_item)
        print(service_item.item)
        self.submitted.emit(service_item)
