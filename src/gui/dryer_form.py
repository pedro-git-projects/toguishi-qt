from dryer.brand import DryerBrand
from dryer.dryer import Dryer
from dryer.model import DryerModel
from gui.item_form import ItemFormBase

DEFECTS = [
    "carcaça",
    "tampa do filtro",
    "filtro",
    "tela do filtro",
    "motor",
    "chave LDL",
    "cabo",
    "mangueira",
    "bico",
    "abraçadeira",
    "parafuso",
    "carvão",
    "redutor de assovio",
    "hélice de aluminio",
    "luva do motor",
    "anel de vedação",
]
DEFECTS = [defect.capitalize() for defect in DEFECTS]


class DryerRegistrationForm(ItemFormBase):
    def __init__(self):
        super().__init__(DEFECTS, DryerBrand, DryerModel)

    def perform_registration(self, brand, model, defects_dict):
        dryer = Dryer(brand, model, defects_dict)
        print("Lâmina registrada: ", dryer)
