from decimal import Decimal

from item.item import Item
from service.category import Category


class ServiceItem:
    def __init__(
        self, category: Category, item: Item, inital_price: Decimal, discount: Decimal
    ):
        self.category = category
        self.item = item
        self.initial_price = inital_price
        self.discount = discount
        self.final_price = inital_price - discount

    def __repr__(self) -> str:
        return f"ServiceItem({repr(self.category)}, {repr(self.item)}, {repr(self.initial_price)}, {repr(self.discount)})"

    def __str__(self) -> str:
        return f"{str(self.category)}, {str(self.item)}, {str(self.initial_price)}, {str(self.discount)}"
