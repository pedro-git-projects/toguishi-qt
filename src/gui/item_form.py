from enum import Enum
from typing import Type
from PySide6 import QtGui
from PySide6.QtGui import QPalette
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QListWidget,
    QVBoxLayout,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
)

from item.item import Item


class ItemFormBase(QWidget):
    def __init__(
        self, defects: list, brand_enum_class: Type[Enum], model_enum_class: Type[Enum]
    ):
        super().__init__()

        self.setWindowTitle("Registrar")
        self.defects = defects

        layout = QVBoxLayout()

        self.brand_label = QLabel("Marca:")
        self.brand_combobox = CustomEnumComboBox(brand_enum_class)

        self.model_label = QLabel("Modelo:")
        self.model_combobox = CustomEnumComboBox(model_enum_class)

        self.has_defect_checkbox = QCheckBox("Possui defeito")
        self.has_defect_checkbox.clicked.connect(self.update_defect_ui)

        self.defect_key_combobox = QComboBox()
        self.defect_key_combobox.addItems(self.defects)
        self.defect_description_edit = QLineEdit()

        self.add_defect_button = QPushButton("Adicionar defeito")
        self.add_defect_button.clicked.connect(self.add_defect)

        self.remove_defect_button = QPushButton("Remover defeito")
        self.remove_defect_button.clicked.connect(self.remove_defect)

        self.defects_list = QListWidget()

        self.register_button = QPushButton("Registrar")
        self.register_button.clicked.connect(self.register_item)

        layout.addWidget(self.brand_label)
        layout.addWidget(self.brand_combobox)

        layout.addWidget(self.model_label)
        layout.addWidget(self.model_combobox)

        layout.addWidget(self.has_defect_checkbox)
        layout.addWidget(self.defect_key_combobox)
        layout.addWidget(self.defect_description_edit)
        layout.addWidget(self.add_defect_button)
        layout.addWidget(self.remove_defect_button)
        layout.addWidget(self.defects_list)

        layout.addWidget(self.register_button)

        self.setLayout(layout)

        self.defects_list.clear()

    def add_defect(self):
        if self.has_defect_checkbox.isChecked():
            defect_key = self.defect_key_combobox.currentText().lower()
            defect_description = self.defect_description_edit.text()

            if self.validate_defect(defect_key, defect_description):
                defect_text = f"{defect_key}: {defect_description}"
                self.defects_list.addItem(defect_text)
                self.defect_description_edit.clear()
                self.reset_color()

                self.has_defect_checkbox.setChecked(True)
                self.has_defect_checkbox.setEnabled(False)
            else:
                self.defect_description_edit.setFocus()
        else:
            self.clear_defect_fields()

    def clear_defect_fields(self):
        self.defect_key_combobox.setCurrentIndex(0)
        self.defect_description_edit.clear()

    def update_defect_ui(self):
        is_checked = self.has_defect_checkbox.isChecked()
        self.defect_key_combobox.setEnabled(is_checked)
        self.defect_description_edit.setEnabled(is_checked)
        self.add_defect_button.setEnabled(is_checked)

        if self.defects_list.count() > 0:
            self.has_defect_checkbox.setChecked(True)
            self.has_defect_checkbox.setEnabled(False)

    def validate_defect(self, defect_key, defect_description):
        if not defect_key or not defect_description:
            self.set_error_color()
            return False
        return True

    def set_error_color(self):
        palette = self.defect_description_edit.palette()
        palette.setColor(QPalette.ColorRole.Base, "white")
        palette.setColor(QPalette.ColorRole.Highlight, "red")
        self.defect_description_edit.setPalette(palette)

    def reset_color(self):
        palette = self.defect_description_edit.palette()
        palette.setColor(QPalette.ColorRole.Base, "white")
        palette.setColor(
            QPalette.ColorRole.Highlight,
            QtGui.QColor.fromRgbF(0.188235, 0.549020, 0.776471, 1.000000),
        )
        self.defect_description_edit.setPalette(palette)

    def remove_defect(self):
        selected_item = self.defects_list.currentItem()
        if selected_item:
            self.defects_list.takeItem(self.defects_list.row(selected_item))

            if self.defects_list.count() == 0:
                self.has_defect_checkbox.setEnabled(True)

    def register_item(self):
        brand = self.brand_combobox.current_enum()
        model = self.model_combobox.current_enum()
        defects_dict = self.parse_defects()
        self.perform_registration(brand, model, defects_dict)

        self.defects_list.clear()
        self.has_defect_checkbox.setEnabled(False)
        self.defect_key_combobox.setEnabled(False)
        self.defect_description_edit.setEnabled(False)
        self.add_defect_button.setEnabled(False)

        self.has_defect_checkbox.setChecked(False)

        if self.defects_list.count() == 0:
            self.has_defect_checkbox.setEnabled(True)

    def parse_defects(self):
        defects_dict = {}
        for index in range(self.defects_list.count()):
            defect_item = self.defects_list.item(index)
            key, value = defect_item.text().split(":")
            defects_dict[key.strip()] = value.strip()
        return defects_dict

    # overload
    def showEvent(self, event):
        self.update_defect_ui()

    def perform_registration(self, brand, model, defects) -> Item:
        raise NotImplementedError("Subclasses must implement perform_registration")


class CustomEnumComboBox(QComboBox):
    def __init__(self, enum_class):
        super().__init__()

        self.enum_class = enum_class
        self.populate()

    def populate(self):
        for enum_item in self.enum_class:
            self.addItem(str(enum_item), enum_item)

    def current_enum(self):
        return self.itemData(self.currentIndex())
