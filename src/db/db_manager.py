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
        self.connection.commit()
        return store_id

    def get_all_customers(self):
        self.cursor.execute("SELECT * FROM customers")
        customers = self.cursor.fetchall()
        return customers

    def get_all_stores(self):
        self.cursor.execute("SELECT * FROM stores")
        stores = self.cursor.fetchall()
        return stores

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
