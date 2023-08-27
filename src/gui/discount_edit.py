from decimal import Decimal
from PySide6.QtWidgets import QHBoxLayout, QLineEdit, QWidget


class DiscountEdit(QWidget):
    def __init__(self):
        super().__init__()
        price_layout = QHBoxLayout()

        self.discount_edit = QLineEdit()
        self.discount_edit.setPlaceholderText("Desconto")

        price_layout.addWidget(self.discount_edit)

        self.setLayout(price_layout)

    def get_discount(self) -> Decimal:
        discount = Decimal(self.discount_edit.text())
        return discount
