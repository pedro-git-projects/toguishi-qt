from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import List, Type
from customer.customer import Customer

from service.service_item import ServiceItem


class ServiceOrder:
    def __init__(
        self,
        items: List[ServiceItem],
        payment_method: Type[Enum],
        discount: Decimal,
        customer: Customer,
    ):
        self.date = datetime.now()
        self.items = items
        self.amount = len(items)

        initial_price = Decimal(0.0)
        for item in self.items:
            initial_price = initial_price + item.final_price

        self.initial_price = initial_price
        self.discount = discount
        self.final_price = initial_price - discount
        self.payment_method = payment_method
        self.customer = customer
