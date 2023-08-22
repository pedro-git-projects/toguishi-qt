from blade.blade import Blade
from blade.brand import BladeBrand
from blade.model import BladeModel
from gui.item_form import ItemFormBase

DEFECTS = ["cortante", "mola", "nylon", "pente", "parafusos", "soquete"]
DEFECTS = [defect.capitalize() for defect in DEFECTS]


class BladeRegistrationForm(ItemFormBase):
    def __init__(self):
        super().__init__(DEFECTS, BladeBrand, BladeModel)

    def perform_registration(self, brand, model, defects_dict):
        blade = Blade(brand, model, defects_dict)
        print("Lâmina registrada: ", blade)
