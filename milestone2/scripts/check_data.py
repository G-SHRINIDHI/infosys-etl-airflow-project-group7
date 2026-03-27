import sqlite3

DB_PATH = "/home/unix16/airflow/data/infosys.db"

def check_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print("\n--- RAW TABLE COUNTS ---")
    cursor.execute("SELECT COUNT(*) FROM orders")
    print("orders:", cursor.fetchone()[0])

    cursor.execute("SELECT COUNT(*) FROM order_details")
    print("order_details:", cursor.fetchone()[0])

    cursor.execute("SELECT COUNT(*) FROM sales_target")
    print("sales_target:", cursor.fetchone()[0])

    print("\n--- CLEAN TABLE COUNTS ---")
    cursor.execute("SELECT COUNT(*) FROM clean_orders")
    print("clean_orders:", cursor.fetchone()[0])

    cursor.execute("SELECT COUNT(*) FROM clean_order_details")
    print("clean_order_details:", cursor.fetchone()[0])

    cursor.execute("SELECT COUNT(*) FROM clean_sales_target")
    print("clean_sales_target:", cursor.fetchone()[0])

    conn.close()

    print("\nData validation completed.")

if __name__ == "__main__":
    check_data()