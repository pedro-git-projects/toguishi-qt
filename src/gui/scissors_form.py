from dryer.dryer import Dryer
from gui.item_form import ItemFormBase
from item.item import Item
from scissors.brand import ScissorsBrand
from scissors.model import ScissorsModel

DEFECTS = []


class ScissorsRegistrationForm(ItemFormBase):
    def __init__(self):
        super().__init__(DEFECTS, ScissorsBrand, ScissorsModel)

    def perform_registration(self, brand, model, defects_dict) -> Item:
        dryer = Dryer(brand, model, defects_dict)
        print(dryer)
        return dryer

    def get_item_data(self):
        brand = self.brand_combobox.current_enum()
        model = self.model_combobox.current_enum()
        defects_dict = self.parse_defects()
        return brand, model, defects_dict
