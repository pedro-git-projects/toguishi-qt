from PySide6.QtWidgets import (
    QComboBox,
    QListWidget,
    QListWidgetItem,
    QVBoxLayout,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
)
from blade.brand import BladeBrand
from blade.model import BladeModel
from blade.blade import Blade


class BladeRegistrationForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registrar Lâmina")

        layout = QVBoxLayout()

        self.brand_label = QLabel("Marca:")
        self.brand_combobox = CustomEnumComboBox(BladeBrand)

        self.model_label = QLabel("Modelo:")
        self.model_combobox = CustomEnumComboBox(BladeModel)

        self.defects_label = QLabel("Defeitos:")
        self.defects_edit = QLineEdit()

        self.add_defect_button = QPushButton("Adicionar defeito")
        self.add_defect_button.clicked.connect(self.add_defect)

        self.remove_defect_button = QPushButton("Remover defeito")
        self.remove_defect_button.clicked.connect(self.remove_defect)

        self.defects_list = QListWidget()

        self.register_button = QPushButton("Registrar Lâmina")
        self.register_button.clicked.connect(self.register_blade)

        layout.addWidget(self.brand_label)
        layout.addWidget(self.brand_combobox)
        layout.addWidget(self.model_label)
        layout.addWidget(self.model_combobox)
        layout.addWidget(self.defects_label)
        layout.addWidget(self.defects_edit)
        layout.addWidget(self.add_defect_button)
        layout.addWidget(self.remove_defect_button)
        layout.addWidget(self.defects_list)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

        self.defects = []

    def add_defect(self):
        defect_text = self.defects_edit.text()
        if defect_text:
            self.defects.append(defect_text)
            self.update_defects_list()
            self.defects_edit.clear()

    def remove_defect(self):
        selected_item = self.defects_list.currentItem()
        if selected_item:
            self.defects.remove(selected_item.text())
            self.defects_list.takeItem(self.defects_list.row(selected_item))

    def update_defects_list(self):
        self.defects_list.clear()
        for defect in self.defects:
            item = QListWidgetItem(defect)
            self.defects_list.addItem(item)

    def register_blade(self):
        brand = self.brand_combobox.current_enum()
        model = self.model_combobox.current_enum()
        defects_dict = self.parse_defects()
        blade = Blade(brand, model, defects_dict)
        print("Lâmina registrada:", blade)
        self.defects = []
        self.update_defects_list()

    def parse_defects(self):
        defects_dict = {}
        for defect in self.defects:
            parts = defect.split(":")
            if len(parts) == 2:
                key, value = parts
                defects_dict[key.strip()] = value.strip()
        return defects_dict


class CustomEnumComboBox(QComboBox):
    def __init__(self, enum_class):
        super().__init__()

        self.enum_class = enum_class
        self.populate()

    def populate(self):
        for enum_item in self.enum_class:
            self.addItem(enum_item.name, enum_item)

    def current_enum(self):
        return self.itemData(self.currentIndex())
