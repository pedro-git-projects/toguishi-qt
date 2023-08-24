from PySide6.QtWidgets import QMainWindow, QTabWidget, QVBoxLayout, QWidget

from gui.blade_form import BladeRegistrationForm
from gui.customer_form import CustomerRegistrationForm
from gui.dryer_form import DryerRegistrationForm
from gui.service_item_form import ServiceItemForm
from gui.store_form import StoreForm


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema Toguishi")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        tab_widget = QTabWidget()

        self.blade_form = BladeRegistrationForm()
        self.dryer_form = DryerRegistrationForm()
        self.store_form = StoreForm()
        self.customer_form = CustomerRegistrationForm()
        self.service_item_form = ServiceItemForm()

        tab_widget.addTab(self.blade_form, "Lâminas")
        tab_widget.addTab(self.dryer_form, "Secadores")
        tab_widget.addTab(self.store_form, "Loja")
        tab_widget.addTab(self.customer_form, "Cliente")
        tab_widget.addTab(self.service_item_form, "Item de Serviço")

        layout = QVBoxLayout()
        layout.addWidget(tab_widget)

        central_widget.setLayout(layout)
