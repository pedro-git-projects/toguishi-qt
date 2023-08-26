from typing import Dict
from item.item import Item
from scissors.brand import ScissorsBrand
from scissors.model import ScissorsModel


class Scissors(Item):
    def __init__(self):
        super().__init__()
        self._brand = ScissorsBrand.NONE
        self._model = ScissorsModel.NONE
        self._defects = {}

    def __repr__(self) -> str:
        return f"Blade({self.brand!r}, {self.model!r}, {self._defects!r})"

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
