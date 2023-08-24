from blade.blade import Blade
from blade.brand import BladeBrand
from blade.model import BladeModel
from gui.item_form import ItemFormBase
from item.item import Item

DEFECTS = ["cortante", "mola", "nylon", "pente", "parafusos", "soquete"]
DEFECTS = [defect.capitalize() for defect in DEFECTS]


class BladeRegistrationForm(ItemFormBase):
    def __init__(self):
        super().__init__(DEFECTS, BladeBrand, BladeModel)

    def perform_registration(self, brand, model, defects_dict) -> Item:
        blade = Blade(brand, model, defects_dict)
        return blade

    def get_item_data(self):
        brand = self.brand_combobox.current_enum()
        model = self.model_combobox.current_enum()
        defects_dict = self.parse_defects()
        return brand, model, defects_dict
