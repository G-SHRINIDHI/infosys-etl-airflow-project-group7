import sqlite3

# Create connection to database (this creates file if not exists)
conn = sqlite3.connect("infosys_etl.db")
cursor = conn.cursor()

# Create Orders Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id TEXT PRIMARY KEY,
    order_date TEXT,
    customer_name TEXT,
    state TEXT,
    city TEXT
)
""")

# Create Order Details Table
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

# Create Sales Target Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales_target (
    month TEXT,
    category TEXT,
    target REAL
)
""")

conn.commit()
conn.close()

print("Tables created successfully!")
