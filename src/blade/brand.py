from enum import Enum, auto

from item.enum_meta import CustomEnumMeta


class BladeBrand(Enum, metaclass=CustomEnumMeta):
    ANDIS = auto()
    OSTER = auto()
    WAHL = auto()
    PET_GROOM = auto()
    PRECISION_EDGE = auto()

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"

    def __str__(self):
        words = self.name.split("_")
        capitalized_words = [word.capitalize() for word in words]
        return " ".join(capitalized_words)
