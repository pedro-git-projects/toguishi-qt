from PySide6.QtCore import Qt
from PySide6.QtWidgets import QComboBox, QLabel, QVBoxLayout, QWidget

from service.category import Category
from service.payment import Payment


class ServiceItemForm(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(layout)

        self.category_label = QLabel("Categoria:")
        layout.addWidget(self.category_label)

        self.category_combo = QComboBox()
        for category in Category:
            self.category_combo.addItem(str(category))
        layout.addWidget(self.category_combo)

        self.selected_category_label = QLabel()
        layout.addWidget(self.selected_category_label)

        self.category_combo.currentIndexChanged.connect(self.update_selected_category)

        self.payment_label = QLabel("Forma de pagamento:")
        layout.addWidget(self.payment_label)

        self.payment_combo = QComboBox()
        for payment in Payment:
            self.payment_combo.addItem(str(payment))
        layout.addWidget(self.payment_combo)

    def update_selected_category(self):
        selected_index = self.category_combo.currentIndex()
        selected_category = Category(selected_index + 1)
        self.selected_category_label.setText(
            f"Selected Category: {selected_category.name}"
        )
