from decimal import Decimal
from PySide6.QtWidgets import QHBoxLayout, QLineEdit, QWidget

class PriceWidget(QWidget): 
    def __init__(self):
        super().__init__()
        price_layout = QHBoxLayout()

        self.inital_price_edit = QLineEdit()
        self.inital_price_edit.setPlaceholderText("Preço")

        self.discount_edit = QLineEdit()
        self.discount_edit.setPlaceholderText("Desconto")

        price_layout.addWidget(self.inital_price_edit)
        price_layout.addWidget(self.discount_edit)

        self.setLayout(price_layout)

    def get_initial_price(self) -> Decimal:
            initial_price = Decimal(self.inital_price_edit.text())
            return initial_price 

    def get_discount (self) -> Decimal:
            discount = Decimal(self.discount_edit.text())
            return discount 
