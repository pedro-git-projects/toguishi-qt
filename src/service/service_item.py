from enum import Enum
from typing import Type
from decimal import Decimal

from item.item import Item


class ServiceItem:
    def __init__(
        self, category: Type[Enum], item: Item, inital_price: Decimal, discount: Decimal
    ):
        self.category = category
        self.item = item
        self.initial_price = inital_price
        self.discount = discount
        self.final_price = inital_price - discount
