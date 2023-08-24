import sqlite3


class DBManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("toguishi.db")
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

    def __del__(self):
        self.connection.close()
