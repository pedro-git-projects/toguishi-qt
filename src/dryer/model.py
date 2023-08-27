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
        match self:
            case DryerModel.MAXX:
                return "Maxx"
            case DryerModel.REX:
                return "Rex"
            case DryerModel.SUPER_DOIS_PONTO_ZERO:
                return "Super 2.0"
            case DryerModel.REVOLUTION:
                return "Revolution"
            case DryerModel.UNIQUE:
                return "Unique"
            case DryerModel.H_DOIS_OUT:
                return "H2Out"
            case DryerModel.TITA:
                return "Titã"
            case DryerModel.JET_BOX:
                return "JetBox"
            case DryerModel.PLENITUDE_SETE_PONTO_CINCO:
                return "Plenitude 7.5"
            case DryerModel.PLENITUDE_NOVE_PONTO_CINCO:
                return "Plenitude 9.5"
            case DryerModel.SUPER_TURBO:
                return "Super Turbo"
            case DryerModel.COMPACTO:
                return "Compacto"
            case DryerModel.MASTER:
                return "Master"
            case DryerModel.SUPER:
                return "Super"
            case DryerModel.BELLS_PLUS:
                return "Bells Plus"
            case DryerModel.TORNADO:
                return "Tornado"
            case DryerModel.SILENCIO:
                return "Silêncio"
