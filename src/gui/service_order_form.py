from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
    QRadioButton,
    QStackedWidget,
)

from db.db_manager import DBManager
from gui.add_item_dialog import AddItemDialog
from gui.customer_form import CustomerRegistrationForm
from gui.customer_selector import CustomerSelector
from gui.discount_edit import DiscountEdit
from gui.item_list import ItemListWidget
from gui.payment_widget import PaymentMethodWidget
from gui.store_form import StoreForm
from gui.store_selector import StoreSelector


# TODO: Check for phone joins in store database
class ServiceOrderForm(QWidget):
    def __init__(
        self,
        db_manager: DBManager,
        store_form: StoreForm,
        customer_form: CustomerRegistrationForm,
    ):
        super().__init__()
        self.db_manager = db_manager
        self.store_form = store_form
        self.customer_form = customer_form
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setup_selector_radios(layout)
        self.setup_stacked_widgets(layout)
        self.setup_payment_method(layout)
        self.setup_list(layout)
        self.setup_discount(layout)
        self.setup_submit_button(layout)

    def setup_discount(self, layout):
        self.discount_edit = DiscountEdit()
        layout.addWidget(self.discount_edit)

    def setup_list(self, layout):
        self.item_list_widget = ItemListWidget()
        layout.addWidget(self.item_list_widget)

        self.add_item_button = QPushButton("Adicionar Item")
        self.remove_item_button = QPushButton("Remover Item")

        layout.addWidget(self.add_item_button)
        layout.addWidget(self.remove_item_button)

        self.add_item_button.clicked.connect(self.open_item_dialog)
        self.remove_item_button.clicked.connect(self.remove_selected_item)

    def setup_payment_method(self, layout):
        self.payment_method_combo = PaymentMethodWidget()
        layout.addWidget(self.payment_method_combo)

    def setup_submit_button(self, layout):
        self.submit_button = QPushButton("Submit")
        layout.addWidget(self.submit_button)
        self.submit_button.clicked.connect(self.get_service_data)

    def setup_selector_radios(self, layout):
        radio_layout = QHBoxLayout()
        self.store_radio = QRadioButton("Loja")
        self.customer_radio = QRadioButton("Cliente")
        self.store_radio.toggled.connect(self.handle_radio_toggled)
        self.customer_radio.toggled.connect(self.handle_radio_toggled)

        radio_layout.addWidget(self.store_radio)
        radio_layout.addWidget(self.customer_radio)
        layout.addLayout(radio_layout)

    def setup_stacked_widgets(self, layout):
        self.stacked_widgets = QStackedWidget()

        self.store_combo = StoreSelector(self.db_manager, self.store_form)
        self.customer_combo = CustomerSelector(self.db_manager, self.customer_form)

        self.stacked_widgets.addWidget(self.store_combo)
        self.stacked_widgets.addWidget(self.customer_combo)

        layout.addWidget(self.stacked_widgets)

        self.stacked_widgets.setCurrentWidget(self.store_combo)

    def handle_radio_toggled(self):
        if self.store_radio.isChecked():
            self.stacked_widgets.setCurrentWidget(self.store_combo)
        elif self.customer_radio.isChecked():
            self.stacked_widgets.setCurrentWidget(self.customer_combo)

    def open_item_dialog(self):
        dialog = AddItemDialog(self.db_manager)
        dialog.service_item_form.submitted.connect(self.item_list_widget.add_item)
        dialog.exec_()

    def remove_selected_item(self):
        selected_item = self.item_list_widget.list_widget.currentItem()
        if selected_item:
            row = self.item_list_widget.list_widget.row(selected_item)
            self.item_list_widget.list_widget.takeItem(row)

    def get_service_data(self):
        items = self.item_list_widget.get_items()
        payment_method = self.payment_method_combo.get_payment_method()

        if self.store_radio.isChecked():
            selected_store = self.store_combo.get_selected_store()
            selected_customer = None
        elif self.customer_radio.isChecked():
            selected_customer = self.customer_combo.get_selected_customer()
            selected_store = None
        else:
            selected_store = None
            selected_customer = None
        discount = self.discount_edit.get_discount()
        print("SELECTED STORE::", selected_store)
        print("SELECTED CUSTOMER::", selected_customer)
        print(items, payment_method, selected_store, selected_customer, discount)
