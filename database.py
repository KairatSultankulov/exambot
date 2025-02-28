import sqlite3


class Database:
    def __init__(self, path):
        self.path = path
        self.create_tables()

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    category TEXT,
                    size TEXT,
                    price TEXT,
                    product_id TEXT,
                    photo TEXT
                )
            ''')
            conn.commit()

    def add_product(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''
                INSERT INTO products (name, category, size, price, product_id, photo) 
                VALUES (?, ?, ?, ?, ?, ?)
                ''',
                (data['name'], data['category'], data['size'], data['price'], data['product_id'], data['photo'])
            )
            conn.commit()

    def get_products(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name, category, size, price, product_id, photo FROM products")
            return cursor.fetchall()

    def add_order(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''
                INSERT INTO orders (product_id, size, quantity, phone) 
                VALUES (?, ?, ?, ?)
                ''',
                (data['product_id'], data['size'], data['quantity'], data['phone'])
            )
            conn.commit()
