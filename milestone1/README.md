📘 Milestone 1 – Basic ETL Pipeline
📌 Objective

The objective of this milestone is to implement a basic ETL (Extract, Load, Validate) pipeline using Python and SQLite. This process is executed manually without automation.

📂 Project Structure
milestone1/
│
├── dag/
│   └── etl_pipeline_dag.py     # Optional DAG (for demonstration)
│
├── scripts/
│   ├── create_tables.py       # Creates database tables
│   ├── load_data.py           # Loads CSV data into database
│   └── check_data.py          # Validates data using SQL queries
│
└── README.md
🔄 Workflow
create_tables.py → load_data.py → check_data.py
⚙️ Implementation Details
1️⃣ Create Tables (create_tables.py)
Connects to SQLite database (infosys_etl.db)
Creates tables:
orders
order_details
sales_target
Uses CREATE TABLE IF NOT EXISTS
2️⃣ Load Data (load_data.py)
Reads CSV files using pandas
Renames columns to match schema
Removes duplicate records
Inserts data into database tables
3️⃣ Validate Data (check_data.py)
Executes SQL queries
Counts records in each table
Displays results in terminal
▶️ How to Run

Run the scripts in the following order:

python create_tables.py
python load_data.py
python check_data.py
📊 Expected Output
Tables are created successfully
Data is loaded into database
Record counts are displayed:
Total Orders
Total Order Details
Total Sales Targets
⚠️ Note on DAG
The DAG file (etl_pipeline_dag.py) is included only for demonstration
Automation using Airflow is fully implemented in Milestone 3
📝 Conclusion

This milestone builds the foundation of the ETL pipeline by manually creating tables, loading data, and validating results using Python scripts.

🚀 Future Scope
Data cleaning and transformation (Milestone 2)
Automation and scheduling using Airflow (Milestone 3)
