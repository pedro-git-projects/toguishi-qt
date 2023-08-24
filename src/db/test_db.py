from customer.customer import Customer
from customer.phone import Phone
from customer.store import Store
from db.db_manager import DBManager
import pytest


@pytest.fixture
def db_manager():
    return DBManager()


def test_customer_save(db_manager):
    store = Store(
        "Focinho Feliz", "Asa Norte SQN 216 BL A", [Phone("(61)986792020")], db_manager
    )
    store.save()
    customer = Customer("João da Silva", [Phone("(61)93213459")], store, db_manager)
    customer_id = customer.save()
    assert customer_id is not None


def test_store_save(db_manager):
    store = Store(
        "Focinho Feliz", "Asa Norte SQN 216 BL A", [Phone("(61)986792020")], db_manager
    )
    store_id = store.save()
    assert store_id is not None


def test_get_store_by_name(db_manager):
    store = Store(
        "Focinho Feliz", "Asa Norte SQN 216 BL A", [Phone("(61)986792020")], db_manager
    )
    store.save()
    retrieved_store = db_manager.get_store_by_name("Focinho Feliz")
    assert retrieved_store is not None
    assert retrieved_store["name"] == "Focinho Feliz"


def test_get_customer_by_name(db_manager):
    store = Store(
        "Focinho Feliz", "Asa Norte SQN 216 BL A", [Phone("(61)986792020")], db_manager
    )
    store.save()
    customer = Customer("João da Silva", [Phone("(61)93213459")], store, db_manager)
    customer.save()

    retrieved_customer = db_manager.get_customer_by_name("João da Silva")
    assert retrieved_customer is not None
    assert retrieved_customer["name"] == "João da Silva"
