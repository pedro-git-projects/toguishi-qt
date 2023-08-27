from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
    QRadioButton,
    QStackedWidget,
)

from db.db_manager import DBManager
from gui.customer_form import CustomerRegistrationForm
from gui.customer_selector import CustomerSelector
from gui.payment_widget import PaymentMethodWidget
from gui.store_form import StoreForm
from gui.store_selector import StoreSelector


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
        self.setup_payment_method(layout)
        self.setup_selector_radios(layout)
        self.setup_stacked_widgets(layout)

    def setup_payment_method(self, layout):
        self.payment_method_combo = PaymentMethodWidget()
        layout.addWidget(self.payment_method_combo)

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

