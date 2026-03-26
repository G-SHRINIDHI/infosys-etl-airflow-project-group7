import pandas as pd
import sqlite3

# Connect to database
conn = sqlite3.connect("infosys_etl.db")

# -------------------------
# LOAD ORDERS TABLE
# -------------------------

orders_df = pd.read_csv("data/List of Orders.csv")

# Rename columns to match table
orders_df.columns = ["order_id", "order_date", "customer_name", "state", "city"]

# Remove duplicates
orders_df.drop_duplicates(inplace=True)

# Load into database
orders_df.to_sql("orders", conn, if_exists="append", index=False)

print("Orders table loaded successfully!")

# -------------------------
# LOAD ORDER DETAILS TABLE
# -------------------------

details_df = pd.read_csv("data/Order Details.csv")

details_df.columns = ["order_id", "amount", "profit", "quantity", "category", "sub_category"]

details_df.drop_duplicates(inplace=True)

details_df.to_sql("order_details", conn, if_exists="append", index=False)

print("Order details table loaded successfully!")

# -------------------------
# LOAD SALES TARGET TABLE
# -------------------------

target_df = pd.read_csv("data/Sales target.csv")

target_df.columns = ["month", "category", "target"]

target_df.drop_duplicates(inplace=True)

target_df.to_sql("sales_target", conn, if_exists="append", index=False)

print("Sales target table loaded successfully!")

conn.close()
