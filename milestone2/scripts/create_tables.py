import sqlite3
import os

DB_PATH = "/home/unix16/airflow/data/infosys.db"

def create_tables():
    os.makedirs("/home/unix16/airflow/data", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    # Raw tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id TEXT PRIMARY KEY,
        order_date TEXT,
        customer_name TEXT,
        state TEXT,
        city TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS order_details (
        order_id TEXT,
        amount REAL,
        profit REAL,
        quantity INTEGER,
        category TEXT,
        sub_category TEXT,
        FOREIGN KEY(order_id) REFERENCES orders(order_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales_target (
        month TEXT,
        category TEXT,
        target REAL
    )
    """)

    # Clean tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clean_orders (
        order_id TEXT PRIMARY KEY,
        order_date TEXT,
        customer_name TEXT,
        state TEXT,
        city TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clean_order_details (
        order_id TEXT,
        amount REAL,
        profit REAL,
        quantity INTEGER,
        category TEXT,
        sub_category TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clean_sales_target (
        month TEXT,
        category TEXT,
        target REAL
    )
    """)

    conn.commit()
    conn.close()

    print("Tables created successfully (raw + clean).")

if __name__ == "__main__":
    create_tables()