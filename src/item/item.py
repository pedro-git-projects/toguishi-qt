from abc import ABC, abstractmethod
from typing import Dict


class Item(ABC):
    @property
    @abstractmethod
    def brand(self):
        pass

    @property
    @abstractmethod
    def model(self):
        pass

    @abstractmethod
    def get_defects(self) -> Dict[str, bool]:
        pass
