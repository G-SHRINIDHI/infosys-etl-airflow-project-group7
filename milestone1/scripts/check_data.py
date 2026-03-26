import sqlite3

conn = sqlite3.connect("infosys_etl.db")
cursor = conn.cursor()

# Count rows in each table
cursor.execute("SELECT COUNT(*) FROM orders")
print("Total Orders:", cursor.fetchone()[0])

cursor.execute("SELECT COUNT(*) FROM order_details")
print("Total Order Details:", cursor.fetchone()[0])

cursor.execute("SELECT COUNT(*) FROM sales_target")
print("Total Sales Targets:", cursor.fetchone()[0])

conn.close()
