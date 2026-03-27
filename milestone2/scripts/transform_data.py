import pandas as pd
import sqlite3

DB_PATH = "/home/unix16/airflow/data/infosys.db"

def transform_data():
    print("Transformation started...")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Clear existing cleaned tables
    cursor.execute("DELETE FROM clean_order_details")
    cursor.execute("DELETE FROM clean_orders")
    cursor.execute("DELETE FROM clean_sales_target")
    conn.commit()

    # ----------------------------
    # CLEAN ORDERS
    # ----------------------------
    orders_df = pd.read_sql("SELECT * FROM orders", conn)

    orders_df.dropna(subset=["order_id"], inplace=True)

    orders_df["order_date"] = pd.to_datetime(orders_df["order_date"], errors="coerce")
    orders_df.dropna(subset=["order_date"], inplace=True)

    orders_df["customer_name"] = orders_df["customer_name"].astype(str).str.strip()
    orders_df["state"] = orders_df["state"].astype(str).str.strip().str.lower()
    orders_df["city"] = orders_df["city"].astype(str).str.strip().str.lower()

    orders_df.drop_duplicates(subset=["order_id"], inplace=True)

    orders_df.to_sql("clean_orders", conn, if_exists="append", index=False)
    print("clean_orders table created successfully.")

    # ----------------------------
    # CLEAN ORDER DETAILS
    # ----------------------------
    details_df = pd.read_sql("SELECT * FROM order_details", conn)

    details_df["amount"] = pd.to_numeric(details_df["amount"], errors="coerce")
    details_df["profit"] = pd.to_numeric(details_df["profit"], errors="coerce")
    details_df["quantity"] = pd.to_numeric(details_df["quantity"], errors="coerce")

    details_df.dropna(inplace=True)

    details_df = details_df[details_df["quantity"] > 0]
    details_df = details_df[details_df["amount"] >= 0]

    details_df["category"] = details_df["category"].astype(str).str.strip().str.lower()
    details_df["sub_category"] = details_df["sub_category"].astype(str).str.strip().str.lower()

    details_df.drop_duplicates(inplace=True)

    details_df.to_sql("clean_order_details", conn, if_exists="append", index=False)
    print("clean_order_details table created successfully.")

    # ----------------------------
    # CLEAN SALES TARGET
    # ----------------------------
    target_df = pd.read_sql("SELECT * FROM sales_target", conn)

    target_df["target"] = pd.to_numeric(target_df["target"], errors="coerce")
    target_df["category"] = target_df["category"].astype(str).str.strip().str.lower()
    target_df["month"] = target_df["month"].astype(str).str.strip()

    target_df.dropna(inplace=True)
    target_df.drop_duplicates(inplace=True)

    target_df.to_sql("clean_sales_target", conn, if_exists="append", index=False)
    print("clean_sales_target table created successfully.")

    conn.commit()
    conn.close()

    print("Transformation completed successfully.")

if __name__ == "__main__":
    transform_data()