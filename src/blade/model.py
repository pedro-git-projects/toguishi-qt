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

    def __str__(self):
        match self:
            case BladeModel.CINQUENTA:
                return "50"
            case BladeModel.QUARENTA:
                return "40"
            case BladeModel.QUINZE:
                return "15"
            case BladeModel.DEZ:
                return "10"
            case BladeModel.NOVE:
                return "9"
            case BladeModel.SETE:
                return "7"
            case BladeModel.OITO:
                return "8"
            case BladeModel.OITO_E_MEIO:
                return "8.5"
            case BladeModel.SETE_F:
                return "7F"
            case BladeModel.CINCO:
                return "5"
            case BladeModel.CINCO_F:
                return "5F"
            case BladeModel.QUATRO:
                return "4"
            case BladeModel.QUATRO_F:
                return "4F"
            case BladeModel.TRES:
                return "3"
            case BladeModel.TRES_F:
                return "3F"
            case BladeModel.CINCO_OITAVOS:
                return "5/8"
            case BladeModel.CINCO_OITAVOS_F:
                return "5/8F"
            case BladeModel.TRES_QUARTOS:
                return "3/4"
            case BladeModel.TRES_QUARTOS_F:
                return "3/4F"
            case BladeModel.BRAVURA:
                return "Bravura"
            case BladeModel.PRO6:
                return "Pro 6"
            case BladeModel.PRO4:
                return "Pro 4"
            case BladeModel.A8:
                return "A8"

