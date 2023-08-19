from enum import EnumMeta


class CustomEnumMeta(EnumMeta):
    def __getitem__(cls, name):
        return cls.__members__[name]
