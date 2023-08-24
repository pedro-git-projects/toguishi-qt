from typing import List

from customer.phone import Phone


class Store:
    def __init__(self, name: str, address: str, phones: List[Phone]):
        self.name = name
        self.address = address
        self.phones = phones

    def __str__(self):
        phone_numbers = ", ".join(str(phone) for phone in self.phones)
        return (
            f"nome: {self.name}, endereço: {self.address} ,telefones: [{phone_numbers}]"
        )

    def __repr__(self):
        phones_repr = ", ".join(repr(phone) for phone in self.phones)
        return f"Customer('{self.name}', '{self.address}' ,[{phones_repr}])"
