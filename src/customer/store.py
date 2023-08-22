from typing import List

from customer.phone import Phone


class Store:
    def __init__(self, name: str, address: str, phones: List[Phone]):
        self.name = name
        self.address = address
        self.phones = phones
