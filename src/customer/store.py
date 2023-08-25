from typing import List

from customer.phone import Phone
from db.db_manager import DBManager


class Store:
    def __init__(
        self, name: str, address: str, phones: List[Phone], db_manager: DBManager
    ):
        self.name = name
        self.address = address
        self.phones = phones
        self.db_manager = db_manager

    def __str__(self):
        phone_numbers = ", ".join(str(phone) for phone in self.phones)
        return (
            f"nome: {self.name}, endereço: {self.address} ,telefones: [{phone_numbers}]"
        )

    def __repr__(self):
        phones_repr = ", ".join(repr(phone) for phone in self.phones)
        return f"Customer('{self.name}', '{self.address}' ,[{phones_repr}], {self.db_manager})"

    def save(self):
        store_id = self.db_manager.insert_store(self)
        return store_id
