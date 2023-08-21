from typing import Dict
from blade.brand import BladeBrand
from blade.model import BladeModel
from item.item import Item


class Blade(Item):
    def __init__(self, brand: BladeBrand, model: BladeModel, defects=None):
        self._brand = brand
        self._model = model
        self._defects = defects if defects else {}

    def __repr__(self) -> str:
        return f"Blade({self.brand!r}, {self.model!r}, {self._defects!r})"

    def __str__(self) -> str:
        defect_str = str(self._defects)
        return (
            f"Marca: {self.brand.name}\t "
            f"Modelo: {self.model.name}\t "
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
