from PySide6.QtWidgets import QComboBox, QLabel, QVBoxLayout, QWidget
from service.category import Category


class CategorySelector(QWidget):
    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.category_label = QLabel("Categoria:")
        self.category_combo = QComboBox()

        categories = list(Category)
        if categories:
            self.category_combo.setCurrentIndex(0)
            for category in categories:
                self.category_combo.addItem(str(category))

        layout.addWidget(self.category_label)
        layout.addWidget(self.category_combo)

    def get_selected_category(self) -> Category:
        selected_index = self.category_combo.currentIndex()
        selected_category = Category(selected_index + 1)
        return selected_category
