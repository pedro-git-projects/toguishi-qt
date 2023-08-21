from enum import Enum, auto

from item.enum_meta import CustomEnumMeta


class BladeModel(Enum, metaclass=CustomEnumMeta):
    CINQUENTA = auto()
    QUARENTA = auto()
    QUINZE = auto()
    DEZ = auto()
    NOVE = auto()
    SETE = auto()
    OITO = auto()
    OITO_E_MEIO = auto()
    SETE_F = auto()
    CINCO = auto()
    CINCO_F = auto()
    QUATRO = auto()
    QUATRO_F = auto()
    TRES = auto()
    TRES_F = auto()
    CINCO_OITAVOS = auto()
    CINCO_OITAVOS_F = auto()
    TRES_QUARTOS = auto()
    TRES_QUARTOS_F = auto()
    BRAVURA = auto()
    PRO6 = auto()
    PRO4 = auto()
    A8 = auto()

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"
