from typing import List

from customer.phone import Phone
from customer.store import Store



class Client:
    def __init__(self, name: str, phones: List[Phone], store: Store):
        self.name = name
        self.phones = phones 
        self.store = store
