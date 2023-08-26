from PySide6.QtWidgets import (
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from gui.blade_form import BladeRegistrationForm
from gui.dryer_form import DryerRegistrationForm
from gui.scissors_form import ScissorsRegistrationForm


class ItemFormConcrete(QWidget):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget()
        self.dryer_form = DryerRegistrationForm()
        self.blade_form = BladeRegistrationForm()
        self.scissors_form = ScissorsRegistrationForm()
        self.stacked_widget.addWidget(self.dryer_form)
        self.stacked_widget.addWidget(self.blade_form)
        self.stacked_widget.addWidget(self.scissors_form)

        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)

    def get_selected_item_data(self):
        current_form = self.stacked_widget.currentWidget()
        if isinstance(current_form, (DryerRegistrationForm, BladeRegistrationForm)):
            return current_form.get_item_data()

    def set_current_item_type(self, item_type):
        if item_type == "Dryer":
            self.stacked_widget.setCurrentWidget(self.dryer_form)
        elif item_type == "Blade":
            self.stacked_widget.setCurrentWidget(self.blade_form)
        elif item_type == "Scissors":
            self.stacked_widget.setCurrentWidget(self.scissors_form)
