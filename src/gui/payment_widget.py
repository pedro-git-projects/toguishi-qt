from PySide6.QtWidgets import QComboBox, QHBoxLayout, QLabel, QWidget

from service.payment import PaymentMethods


class PaymentMethodWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.payment_label = QLabel("Forma de pagamento:")
        self.payment_combo = QComboBox()
        layout = QHBoxLayout()
        for payment in PaymentMethods:
            self.payment_combo.addItem(str(payment))

        layout.addWidget(self.payment_label)
        layout.addWidget(self.payment_combo)
        self.setLayout(layout)

    def get_payment_method(self) -> PaymentMethods:
        selected_index = self.payment_combo.currentIndex()
        selected_payment = PaymentMethods(selected_index + 1)
        return selected_payment
