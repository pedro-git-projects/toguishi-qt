from PySide6.QtWidgets import (
    QButtonGroup,
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QRadioButton,
    QVBoxLayout,
    QWidget,
)

from db.db_manager import DBManager
from gui.item_form_concrete import ItemFormConcrete

from service.category import Category
from service.payment import Payment


class ServiceItemForm(QWidget):
    def __init__(self, db_manager: DBManager):
        super().__init__()
        self.db_manager = db_manager

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.setup_item_type_section(layout)
        #        self.setup_stacked_widget(layout)
        self.setup_item_form(layout)
        self.setup_category_section(layout)
        self.setup_price_section(layout)

    def setup_category_section(self, layout):
        self.category_label = QLabel("Categoria:")
        self.category_combo = QComboBox()
        self.category_combo.currentIndexChanged.connect(self.update_selected_category)
        for category in Category:
            self.category_combo.addItem(str(category))

        layout.addWidget(self.category_label)
        layout.addWidget(self.category_combo)

    def setup_price_section(self, layout):
        price_layout = QHBoxLayout()

        self.inital_price_edit = QLineEdit()
        self.inital_price_edit.setPlaceholderText("Preço")

        self.discount_edit = QLineEdit()
        self.discount_edit.setPlaceholderText("Desconto")

        price_layout.addWidget(self.inital_price_edit)
        price_layout.addWidget(self.discount_edit)

        layout.addLayout(price_layout)

    def setup_payment_section(self, layout):
        self.payment_label = QLabel("Forma de pagamento:")
        self.payment_combo = QComboBox()
        for payment in Payment:
            self.payment_combo.addItem(str(payment))

        layout.addWidget(self.payment_label)
        layout.addWidget(self.payment_combo)

    def setup_item_type_section(self, layout):
        item_type_layout = QHBoxLayout()

        self.item_type_label = QLabel("Item: ")
        self.dryer_radio = QRadioButton("Secador")
        self.blade_radio = QRadioButton("Lâmina")
        self.scissors_radio = QRadioButton("Tesoura")

        self.item_type_radio_group = QButtonGroup()
        self.item_type_radio_group.addButton(self.dryer_radio)
        self.item_type_radio_group.addButton(self.blade_radio)
        self.item_type_radio_group.addButton(self.scissors_radio)

        item_type_layout.addWidget(self.item_type_label)
        item_type_layout.addWidget(self.dryer_radio)
        item_type_layout.addWidget(self.blade_radio)
        item_type_layout.addWidget(self.scissors_radio)

        self.item_type_radio_group.buttonClicked.connect(self.update_selected_item_type)

        layout.addLayout(item_type_layout)

    def setup_item_form(self, layout):
        self.item_form = ItemFormConcrete()
        layout.addWidget(self.item_form)

    def update_selected_category(self):
        selected_index = self.category_combo.currentIndex()
        selected_category = Category(selected_index + 1)

    def update_selected_item_type(self, button):
        if button == self.dryer_radio:
            self.item_form.set_current_item_type("Dryer")
        elif button == self.blade_radio:
            self.item_form.set_current_item_type("Blade")
        elif button == self.scissors_radio:
            self.item_form.set_current_item_type("Scissors")
