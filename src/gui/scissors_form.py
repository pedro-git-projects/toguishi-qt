from dryer.dryer import Dryer
from gui.item_form import ItemFormBase
from item.item import Item
from scissors.brand import ScissorsBrand
from scissors.model import ScissorsModel

DEFECTS = ["observação"]
DEFECTS = [defect.capitalize() for defect in DEFECTS]


class ScissorsRegistrationForm(ItemFormBase):
    def __init__(self):
        super().__init__(DEFECTS, ScissorsBrand, ScissorsModel)

    def perform_registration(self, brand, model, defects_dict) -> Item:
        dryer = Dryer(brand, model, defects_dict)
        print(dryer)
        return dryer

    def get_item_data(self):
        defects_dict = self.parse_defects()
        return defects_dict
