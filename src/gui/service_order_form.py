from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
)

from db.db_manager import DBManager
from gui.payment_widget import PaymentMethodWidget


class ServiceOrderForm(QWidget):
    def __init__(self, db_manager: DBManager):
        super().__init__()
        self.db_manager = db_manager
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setup_payment_method(layout)

    def setup_payment_method(self, layout):
        self.payment_method_combo = PaymentMethodWidget()
        layout.addWidget(self.payment_method_combo)
