from typing import Dict
from dryer.brand import DryerBrand
from dryer.model import DryerModel
from item.item import Item


class Dryer(Item):
    def __init__(self, brand: DryerBrand, model: DryerModel, defects=None):
        super().__init__()
        self._brand = brand
        self._model = model
        self._defects = defects if defects else {}

    def __repr__(self) -> str:
        return f"Dryer({self.brand!r}, {self.model!r}, {self._defects!r})"

    def __str__(self) -> str:
        defect_str = str(self._defects)
        return (
            f"Marca: {self.brand.name} "
            f"Modelo: {self.model.name} "
            f"Defeitos: {defect_str}"
        )

    @property
    def brand(self):
        return self._brand

    @property
    def model(self):
        return self._model

    def get_defects(self) -> Dict[str, str]:
        return self._defects
