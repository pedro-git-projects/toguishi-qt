from PySide6.QtWidgets import QListWidget, QListWidgetItem, QVBoxLayout, QWidget


class ItemListWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.v_layout = QVBoxLayout(self)
        self.list_widget = QListWidget()
        self.v_layout.addWidget(self.list_widget)
        self.setLayout(self.v_layout)

    def add_item(self, service_item):
        item_text = str(service_item)
        list_item = QListWidgetItem(item_text)
        self.list_widget.addItem(list_item)
