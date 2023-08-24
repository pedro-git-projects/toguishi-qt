from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QButtonGroup,
    QComboBox,
    QLabel,
    QRadioButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from customer.store import Store
from db.db_manager import DBManager
from gui.blade_form import BladeRegistrationForm
from gui.dryer_form import DryerRegistrationForm

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

        self.category_combo.currentIndexChanged.connect(self.update_selected_category)

        self.payment_label = QLabel("Forma de pagamento:")
        layout.addWidget(self.payment_label)

        self.payment_combo = QComboBox()
        for payment in Payment:
            self.payment_combo.addItem(str(payment))
        layout.addWidget(self.payment_combo)

        self.item_type_label = QLabel("Item: ")
        layout.addWidget(self.item_type_label)

        self.item_type_radio_group = QButtonGroup()
        self.dryer_radio = QRadioButton("Secador")
        self.blade_radio = QRadioButton("Lâmina")
        self.blade_radio = QRadioButton("Tesoura")
        self.item_type_radio_group.addButton(self.dryer_radio)
        self.item_type_radio_group.addButton(self.blade_radio)

        layout.addWidget(self.dryer_radio)
        layout.addWidget(self.blade_radio)

        self.stacked_widget = QStackedWidget()
        layout.addWidget(self.stacked_widget)

        self.dryer_form = DryerRegistrationForm()
        self.blade_form = BladeRegistrationForm()

        self.stacked_widget.addWidget(self.dryer_form)
        self.stacked_widget.addWidget(self.blade_form)

        self.item_type_radio_group.buttonClicked.connect(self.update_selected_item_type)

    def update_selected_category(self):
        selected_index = self.category_combo.currentIndex()
        selected_category = Category(selected_index + 1)

    def populate_store_combo(self):
        stores = self.db_manager.get_all_stores()
        for store in stores:
            store_object = Store(store["name"], store["address"], [], self.db_manager)
            self.store_combo.addItem(store["name"], userData=store_object)

    def update_selected_store(self, index):
        selected_store = self.store_combo.itemData(index)
        print(selected_store)

    def update_store_combo(self):
        self.store_combo.clear()
        self.populate_store_combo()

    def update_selected_item_type(self, button):
        if button == self.dryer_radio:
            self.stacked_widget.setCurrentWidget(self.dryer_form)
        elif button == self.blade_radio:
            self.stacked_widget.setCurrentWidget(self.blade_form)

    def get_selected_item_data(self):
        current_form = self.stacked_widget.currentWidget()
        if isinstance(current_form, DryerRegistrationForm):
            data = current_form.get_item_data()
            print(data)
        elif isinstance(current_form, BladeRegistrationForm):
            data = current_form.get_item_data()
            print(data)
        else:
            pass
