from enum import Enum, auto


class Payment(Enum):
    DINHEIRO = auto()
    PIX_PF = auto()
    PIX_PJ = auto()
    PIX_C6_PF = auto()
    PIX_C6_PJ = auto()
    MERCADO_PAGO = auto()
    PIX_HK = auto()
    DEB_HK = auto()
    PIX_ALY = auto()
    PIX_MAI = auto()
    PIX_NU_PF = auto()
    PIX_NU_PJ = auto()
    PAG_SEGURO = auto()

    def __str__(self):
        words = self.name.split("_")
        capitalized_words = [word.capitalize() for word in words]
        return " ".join(capitalized_words)
