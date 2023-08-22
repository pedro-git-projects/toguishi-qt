from PySide6.QtWidgets import QMainWindow, QTabWidget, QVBoxLayout, QWidget

from gui.blade_form import BladeRegistrationForm
from gui.dryer_form import DryerRegistrationForm


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema Toguishi")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        tab_widget = QTabWidget()

        self.blade_form = BladeRegistrationForm()
        self.dryer_form = DryerRegistrationForm()

        tab_widget.addTab(self.blade_form, "lâminas")
        tab_widget.addTab(self.dryer_form, "secadores")

        layout = QVBoxLayout()
        layout.addWidget(tab_widget)

        central_widget.setLayout(layout)
