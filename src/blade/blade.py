from typing import Dict
from blade.brand import BladeBrand
from blade.model import BladeModel
from item.item import Item


class Blade(Item):
    def __init__(self, brand: BladeBrand, model: BladeModel, defects=None):
        self._brand = brand
        self._model = model
        self._defects = defects if defects else {}

    @property
    def brand(self):
        return self._brand

    @property
    def model(self):
        return self._model

    def get_defects(self) -> Dict[str, bool]:
        return self._defects
