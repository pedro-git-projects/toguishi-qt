from enum import Enum, auto

from item.enum_meta import CustomEnumMeta


class ScissorsModel(Enum, metaclass=CustomEnumMeta):
    NONE = auto()

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"

    def __str__(self):
        words = self.name.split("_")
        capitalized_words = [word.capitalize() for word in words]
        return " ".join(capitalized_words)
