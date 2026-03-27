# 🧹 Milestone 2: Data Cleaning & Transformation (Weeks 3–4)

---

## 🎯 Objective
The objective of Milestone 2 is to implement **data preparation workflows** by applying cleaning rules and transformation logic on the raw dataset using **Python (Pandas)**.  
The cleaned data is stored into new tables in the SQLite database for further automation in Milestone 3.

---

##  Tasks Implemented

### ✅ 1. Data Cleaning Rules
The following data cleaning rules were applied:

- Removed duplicate records  
- Removed null values from important columns  
- Converted numeric columns into correct numeric format  
- Converted date column into standard datetime format  
- Standardized text columns using `.strip()` and `.lower()`  
- Removed invalid records such as:
  - quantity ≤ 0  
  - amount < 0  

---

##  2. Transformation Implementation (Pandas)

### 📌 Scripts Used
All cleaning and transformation logic is implemented using Python scripts inside:

- `scripts/`

### 📌 Raw Tables Used
Raw tables loaded from CSV files:

- `orders`
- `order_details`
- `sales_target`

### 📌 Clean Tables Generated
After applying transformations, the following cleaned tables are created:

- `clean_orders`
- `clean_order_details`
- `clean_sales_target`

---

##  3. Testing & Validation
The pipeline was tested manually by executing the scripts and validating:

- Correct row counts after cleaning  
- Duplicate and null removal  
- Proper conversion of numeric and date fields  
- Successful creation of cleaned tables  

Validation is performed using:

- `scripts/check_data.py`

---

## ⚙️ How to Run Milestone 2

Navigate to the scripts folder:

```bash
cd milestone2/scripts
````

Run scripts in this order:

```bash
python create_tables.py
python load_data.py
python transform_data.py
python check_data.py
```


## 📂 Folder Structure

```
milestone2/
   scripts/
      create_tables.py
      load_data.py
      transform_data.py
      check_data.py
   README.md
```

## 🏁 Conclusion

Milestone 2 successfully implements complete **data cleaning and transformation workflows** using Pandas.
The cleaned dataset is stored into SQLite clean tables, which will be used in Milestone 3 for automation using Apache Airflow.



