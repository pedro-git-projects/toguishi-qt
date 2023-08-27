from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
)

from db.db_manager import DBManager
from gui.payment_widget import PaymentMethodWidget
from gui.store_form import StoreForm
from gui.store_selector import StoreSelector


class ServiceOrderForm(QWidget):
    def __init__(self, db_manager: DBManager, store_form: StoreForm):
        super().__init__()
        self.db_manager = db_manager
        self.store_form = store_form
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setup_payment_method(layout)
        self.setup_store_combo(layout)

    def setup_payment_method(self, layout):
        self.payment_method_combo = PaymentMethodWidget()
        layout.addWidget(self.payment_method_combo)

    def setup_store_combo(self, layout):
        self.store_combo = StoreSelector(self.db_manager, self.store_form)
        layout.addWidget(self.store_combo)
