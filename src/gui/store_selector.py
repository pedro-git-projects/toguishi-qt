from PySide6.QtWidgets import QComboBox, QLabel, QVBoxLayout, QWidget

from customer.store import Store
from db.db_manager import DBManager
from gui.store_form import StoreForm


class StoreSelector(QWidget):
    def __init__(self, db_manager: DBManager, store_form: StoreForm):
        super().__init__()

        self.db_manager = db_manager
        self.store_form = store_form
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.store_label = QLabel("Loja:")
        self.store_combo = QComboBox()

        stores = self.db_manager.get_all_stores()
        for store in stores:
            self.store_combo.addItem(store["name"])

        layout.addWidget(self.store_label)
        layout.addWidget(self.store_combo)

    def get_selected_store(self) -> Store:
        selected_index = self.store_combo.currentIndex()
        if selected_index >= 0:
            selected_store_name = self.store_combo.itemText(selected_index)
            store = self.db_manager.get_store_by_name(selected_store_name)
            if store:
                return Store(
                    store["name"], store["address"], store["phones"], self.db_manager
                )
        raise Exception("is fucked")

    def populate_store_combo(self):
        stores = self.db_manager.get_all_stores()
        for store in stores:
            store_object = Store(
                store["name"], store["address"], store["phones"], self.db_manager
            )
            self.store_combo.addItem(store["name"], userData=store_object)

    # slot
    def update_store_combo(self):
        self.store_combo.clear()
        self.populate_store_combo()
