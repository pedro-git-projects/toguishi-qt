from PySide6.QtWidgets import QMainWindow, QTabWidget, QVBoxLayout, QWidget

from gui.blade_form import BladeRegistrationForm
from gui.dryer_form import DryerRegistrationForm
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

        tab_widget.addTab(self.blade_form, "lâminas")
        tab_widget.addTab(self.dryer_form, "secadores")
        tab_widget.addTab(self.store_form, "loja")

        layout = QVBoxLayout()
        layout.addWidget(tab_widget)

        central_widget.setLayout(layout)
