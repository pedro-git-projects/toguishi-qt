from PySide6.QtWidgets import QMainWindow, QTabWidget, QVBoxLayout, QWidget
from db.db_manager import DBManager

from gui.blade_form import BladeRegistrationForm
from gui.customer_form import CustomerRegistrationForm
from gui.dryer_form import DryerRegistrationForm
from gui.service_item_form import ServiceItemForm
from gui.store_form import StoreForm


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.db_manager = DBManager()

        self.setWindowTitle("Sistema Toguishi")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        tab_widget = QTabWidget()

        self.blade_form = BladeRegistrationForm()
        self.dryer_form = DryerRegistrationForm()
        self.store_form = StoreForm(self.db_manager)
        self.customer_form = CustomerRegistrationForm(self.db_manager)
        self.service_item_form = ServiceItemForm(self.db_manager)

        self.store_form.store_saved.connect(self.service_item_form.update_store_combo)
        self.store_form.store_saved.connect(self.customer_form.update_store_combo)


        tab_widget.addTab(self.blade_form, "Lâminas")
        tab_widget.addTab(self.dryer_form, "Secadores")
        tab_widget.addTab(self.store_form, "Loja")
        tab_widget.addTab(self.customer_form, "Cliente")
        tab_widget.addTab(self.service_item_form, "Item de Serviço")

        layout = QVBoxLayout()
        layout.addWidget(tab_widget)

        central_widget.setLayout(layout)
