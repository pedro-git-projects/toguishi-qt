import sqlite3


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
        self.cursor.execute("SELECT * FROM customers")
        customers = self.cursor.fetchall()
        return customers

    def get_all_stores(self):
        self.cursor.execute("SELECT * FROM stores")
        stores = self.cursor.fetchall()

        stores_with_phones = []
        for store_row in stores:
            store = dict(store_row)
            store_id = store["id"]
            store["phones"] = self.get_phones_for_store(store_id)
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
        store = self.cursor.fetchone()
        return dict(store) if store else None

    def get_customer_by_name(self, customer_name):
        self.cursor.execute("SELECT * FROM customers WHERE name = ?", (customer_name,))
        customer = self.cursor.fetchone()
        return dict(customer) if customer else None

    def __del__(self):
        self.connection.close()
