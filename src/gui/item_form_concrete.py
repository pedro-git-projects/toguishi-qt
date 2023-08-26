from PySide6.QtWidgets import (
    QButtonGroup,
    QStackedWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QRadioButton,
    QWidget,
)
from blade.blade import Blade
from dryer.dryer import Dryer

from gui.blade_form import BladeRegistrationForm
from gui.dryer_form import DryerRegistrationForm
from gui.scissors_form import ScissorsRegistrationForm
from item.item import Item
from scissors.scissors import Scissors


class ItemFormConcrete(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.setup_item_type_section(layout)
        self.setup_stacked_widget(layout)

        self.setLayout(layout)

    def setup_item_type_section(self, layout):
        item_type_layout = QHBoxLayout()

        self.item_type_label = QLabel("Item: ")
        self.dryer_radio = QRadioButton("Secador")
        self.blade_radio = QRadioButton("Lâmina")
        self.scissors_radio = QRadioButton("Tesoura")

        self.item_type_radio_group = QButtonGroup()
        self.item_type_radio_group.addButton(self.dryer_radio)
        self.item_type_radio_group.addButton(self.blade_radio)
        self.item_type_radio_group.addButton(self.scissors_radio)

        item_type_layout.addWidget(self.item_type_label)
        item_type_layout.addWidget(self.dryer_radio)
        item_type_layout.addWidget(self.blade_radio)
        item_type_layout.addWidget(self.scissors_radio)

        self.item_type_radio_group.buttonClicked.connect(self.update_selected_item_type)

        layout.addLayout(item_type_layout)

    def setup_stacked_widget(self, layout):
        self.stacked_widget = QStackedWidget()
        self.dryer_form = DryerRegistrationForm()
        self.blade_form = BladeRegistrationForm()
        self.scissors_form = ScissorsRegistrationForm()
        self.stacked_widget.addWidget(self.dryer_form)
        self.stacked_widget.addWidget(self.blade_form)
        self.stacked_widget.addWidget(self.scissors_form)

        layout.addWidget(self.stacked_widget)

    def update_selected_item_type(self, button):
        item_type = None
        if button == self.dryer_radio:
            item_type = "Dryer"
        elif button == self.blade_radio:
            item_type = "Blade"
        elif button == self.scissors_radio:
            item_type = "Scissors"

        if item_type:
            self.set_current_item_type(item_type)

    def set_current_item_type(self, item_type):
        if item_type == "Dryer":
            self.stacked_widget.setCurrentWidget(self.dryer_form)
        elif item_type == "Blade":
            self.stacked_widget.setCurrentWidget(self.blade_form)
        elif item_type == "Scissors":
            self.stacked_widget.setCurrentWidget(self.scissors_form)

    def get_selected_item_data(self) -> Item:
        current_form = self.stacked_widget.currentWidget()

        if isinstance(current_form, DryerRegistrationForm):
            return Dryer(*current_form.get_item_data())

        elif isinstance(current_form, BladeRegistrationForm):
            return Blade(*current_form.get_item_data())

        elif isinstance(current_form, ScissorsRegistrationForm):
            return Scissors(current_form.get_item_data())

        raise Exception("Impossible")
