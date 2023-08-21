from enum import Enum

from item.enum_meta import CustomEnumMeta


class BladeModel(Enum, metaclass=CustomEnumMeta):
    CINQUENTA = None
    QUARENTA = None
    QUINZE = None
    DEZ = None
    NOVE = None
    SETE = None
    OITO = None
    OITO_E_MEIO = None
    SETE_F = None
    CINCO = None
    CINCO_F = None
    QUATRO = None
    QUATRO_F = None
    TRES = None
    TRES_F = None
    CINCO_OITAVOS = None
    CINCO_OITAVOS_F = None
    TRES_QUARTOS = None
    TRES_QUARTOS_F = None
    BRAVURA = None
    PRO6 = None
    PRO4 = None
    A8 = None
