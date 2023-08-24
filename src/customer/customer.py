from typing import List

from customer.phone import Phone
from customer.store import Store
from db.db_manager import DBManager


class Customer:
    def __init__(
        self, name: str, phones: List[Phone], store: Store, db_manager: DBManager
    ):
        self.name = name
        self.phones = phones
        self.store = store
        self.db_manager = db_manager

    def __str__(self):
        phone_numbers = ", ".join(str(phone) for phone in self.phones)
        return f"nome: {self.name}, telefones: [{phone_numbers}], loja: {self.store}"

    def __repr__(self):
        phones_repr = ", ".join(repr(phone) for phone in self.phones)
        return (
            f"Customer('{self.name}', [{phones_repr}], {self.store}, {self.db_manager})"
        )

    def save(self):
        customer_id = self.db_manager.insert_customer(self)
        return customer_id
