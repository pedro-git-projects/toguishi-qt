from enum import Enum, auto


class Category(Enum):
    AFIACAO = auto()
    REPOSICAO = auto()
    TAXA = auto()
    VENDA = auto()

    def __str__(self):
        match self:
            case Category.AFIACAO:
                return "Afiação"
            case Category.REPOSICAO:
                return "Reposição"
            case Category.TAXA:
                return "Taxa"
            case Category.VENDA:
                return "Venda"
