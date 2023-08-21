from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from gui.blade_form import BladeRegistrationForm


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema Toguishi")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        self.registration_form = BladeRegistrationForm()
        layout.addWidget(self.registration_form)

        central_widget.setLayout(layout)
