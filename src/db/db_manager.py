import sqlite3

from customer.customer import Customer
from customer.store import Store


class DBManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("toguishi.db")
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self.setup_database()

    def setup_database(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                name TEXT,
                store_id INTEGER,
                FOREIGN KEY (store_id) REFERENCES stores (id)
            )
        """
        )

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS stores (
                id INTEGER PRIMARY KEY,
                name TEXT,
                address TEXT
            )
        """
        )

        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS phones ( 
                 id INTEGER PRIMARY KEY, 
                 store_id INTEGER, 
                 phone_number TEXT, 
                 FOREIGN KEY (store_id) REFERENCES stores (id)
            )
        """
        )

        self.connection.commit()

    def insert_customer(self, customer):
        self.cursor.execute("INSERT INTO customers (name) VALUES (?)", (customer.name,))
        customer_id = self.cursor.lastrowid
        self.connection.commit()
        return customer_id

    def insert_store(self, store):
        self.cursor.execute(
            "INSERT INTO stores (name, address) VALUES (?, ?)",
            (store.name, store.address),
        )
        store_id = self.cursor.lastrowid

        for phone in store.phones:
            self.cursor.execute(
                "INSERT INTO phones (store_id, phone_number) VALUES (?, ?)",
                (store_id, phone.number),
            )

        self.connection.commit()
        return store_id

    def get_all_customers(self):
        self.cursor.execute(
            """
            SELECT customers.id, customers.name AS customer_name, stores.id AS store_id, stores.name AS store_name, stores.address AS store_address
            FROM customers
            LEFT JOIN stores ON customers.store_id = stores.id
            """
        )
        customer_rows = self.cursor.fetchall()

        customers = []
        for customer_data in customer_rows:
            customer_phones = self.get_phones_for_store(customer_data["store_id"])
            store = Store(
                customer_data["store_name"],
                customer_data["store_address"],
                customer_phones,
            )
            customer = Customer(
                customer_data["customer_name"],
                customer_phones,
                store,
            )
            customers.append(customer)

        return customers

    def get_all_stores(self):
        self.cursor.execute("SELECT * FROM stores")
        store_rows = self.cursor.fetchall()

        stores_with_phones = []
        for store_data in store_rows:
            store_phones = self.get_phones_for_store(store_data["id"])
            store = Store(
                store_data["name"],
                store_data["address"],
                store_phones,
            )
            stores_with_phones.append(store)

        return stores_with_phones

    def get_phones_for_store(self, store_id):
        self.cursor.execute(
            "SELECT phone_number FROM phones WHERE store_id = ?", (store_id,)
        )
        phones = self.cursor.fetchall()
        return [phone["phone_number"] for phone in phones]

    def get_store_by_name(self, store_name):
        self.cursor.execute("SELECT * FROM stores WHERE name = ?", (store_name,))
        store_data = self.cursor.fetchone()

        if store_data:
            store_id = store_data["id"]
            store_name = store_data["name"]
            store_address = store_data["address"]
            store_phones = self.get_phones_for_store(store_id)

            return Store(store_name, store_address, store_phones)
        return None

    def get_customer_by_name(self, customer_name):
        self.cursor.execute(
            """
            SELECT customers.id, customers.name AS customer_name, stores.id AS store_id, stores.name AS store_name, stores.address AS store_address
            FROM customers
            LEFT JOIN stores ON customers.store_id = stores.id
            WHERE customers.name = ?
            """,
            (customer_name,),
        )
        customer_data = self.cursor.fetchone()

        if customer_data:
            customer_phones = self.get_phones_for_store(customer_data["store_id"])
            store = Store(
                customer_data["store_name"],
                customer_data["store_address"],
                customer_phones,
            )
            return Customer(
                customer_data["customer_name"],
                customer_phones,
                store,
            )
        return None

    def __del__(self):
        self.connection.close()
