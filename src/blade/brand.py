from enum import Enum

from item.enum_meta import CustomEnumMeta



class BladeBrand(Enum, metaclass=CustomEnumMeta):
    ANDIS = None
    OSTER = None
    WAHL = None
    PET_GROOM = None
    PRECISION_EDGE = None
