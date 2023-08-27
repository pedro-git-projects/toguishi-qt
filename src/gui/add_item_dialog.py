from PySide6.QtWidgets import QDialog, QVBoxLayout

from db.db_manager import DBManager
from gui.service_item_form import ServiceItemForm


class AddItemDialog(QDialog):
    def __init__(self, db_manager: DBManager):
        super().__init__()
        self.db_manager = db_manager

        self.service_item_form = ServiceItemForm(self.db_manager)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.addWidget(self.service_item_form)
        self.service_item_form.registration_button.clicked.connect(self.accept)
