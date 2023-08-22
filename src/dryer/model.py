from enum import Enum, auto
from item.enum_meta import CustomEnumMeta


class DryerModel(Enum, metaclass=CustomEnumMeta):
    MAXX = auto()
    REX = auto()
    SUPER_DOIS_PONTO_ZERO = auto()
    REVOLUTION = auto()
    UNIQUE = auto()
    H_DOIS_OUT = auto()
    TITA = auto()
    JET_BOX = auto()
    PLENITUDE_SETE_PONTO_CINCO = auto()
    PLENITUDE_NOVE_PONTO_CINCO = auto()
    SUPER_TURBO = auto()
    COMPACTO = auto()
    MASTER = auto()
    SUPER = auto()
    BELLS_PLUS = auto()
    TORNADO = auto()
    SILENCIO = auto()

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"

    def __str__(self):
        words = self.name.split("_")
        capitalized_words = [word.capitalize() for word in words]
        return " ".join(capitalized_words)
