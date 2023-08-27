from PySide6.QtWidgets import QMainWindow, QTabWidget, QVBoxLayout, QWidget
from db.db_manager import DBManager
from gui.csv_loader import CSVLoaderWidget

from gui.customer_form import CustomerRegistrationForm
from gui.service_order_form import ServiceOrderForm
from gui.store_form import StoreForm


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.db_manager = DBManager()

        self.setWindowTitle("Sistema Toguishi")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        tab_widget = QTabWidget()

        self.store_form = StoreForm(self.db_manager)
        self.customer_form = CustomerRegistrationForm(self.db_manager)
        self.service_order_form = ServiceOrderForm(
            self.db_manager, self.store_form, self.customer_form
        )
        self.csv_loader = CSVLoaderWidget()

        self.store_form.store_saved.connect(self.customer_form.update_store_combo)
        self.store_form.store_saved.connect(
            self.service_order_form.store_combo.update_store_combo
        )
        self.customer_form.customer_saved.connect(
            self.service_order_form.customer_combo.update_customer_combo
        )

        tab_widget.addTab(self.store_form, "Loja")
        tab_widget.addTab(self.customer_form, "Cliente")
        tab_widget.addTab(self.service_order_form, "Ordem de Serviço")
        tab_widget.addTab(self.csv_loader, "Carregar CSV")

        layout = QVBoxLayout()
        layout.addWidget(tab_widget)

        central_widget.setLayout(layout)
