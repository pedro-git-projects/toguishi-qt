from typing import List

from customer.phone import Phone
from customer.store import Store


class Customer:
    def __init__(self, name: str, phones: List[Phone], store: Store):
        self.name = name
        self.phones = phones
        self.store = store

    def __str__(self):
        phone_numbers = ", ".join(str(phone) for phone in self.phones)
        return f"nome: {self.name}, telefones: [{phone_numbers}], loja: {self.store}"

    def __repr__(self):
        phones_repr = ", ".join(repr(phone) for phone in self.phones)
        return f"Customer('{self.name}', [{phones_repr}], {self.store})"
