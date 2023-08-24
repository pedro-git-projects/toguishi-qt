from PySide6.QtCore import Qt
from PySide6.QtWidgets import QComboBox, QLabel, QVBoxLayout, QWidget

from customer.store import Store
from db.db_manager import DBManager

from service.category import Category
from service.payment import Payment


class ServiceItemForm(QWidget):
    def __init__(self, db_manager: DBManager):
        super().__init__()

        self.db_manager = db_manager

        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(layout)

        self.store_label = QLabel("Loja:")
        layout.addWidget(self.store_label)

        self.store_combo = QComboBox()
        layout.addWidget(self.store_combo)

        self.store_combo.currentIndexChanged.connect(self.update_selected_store)
        self.populate_store_combo()

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

    def populate_store_combo(self):
        stores = self.db_manager.get_all_stores()
        for store in stores:
            store_object = Store(
                store["name"], store["address"], [], self.db_manager
            )  # Assuming Store constructor parameters
            self.store_combo.addItem(store["name"], userData=store_object)

    def update_selected_store(self, index):
        selected_store = self.store_combo.itemData(index)
        print(selected_store)

    def update_store_combo(self):
        self.store_combo.clear()  # Clear the combo box
        self.populate_store_combo()
