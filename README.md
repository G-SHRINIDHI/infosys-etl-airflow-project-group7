# 🚀 E-Commerce ETL Pipeline & Analytics Dashboard
The e-commerce domain is widely used in data engineering projects because:

- High volume of transactional data  
- Multiple related tables (orders, products, customers)  
- Supports real-world business analysis (sales, profit, trends)  
- Ideal for demonstrating **ETL pipelines and dashboard analytics**

This makes it suitable for building scalable and practical data workflows.

---

## 🌐 Live Dashboard

🔗 **Streamlit Dashboard:**  
https://infosy-82mu22cfxzaj3mjlwmoxtc.streamlit.app/

---

## 🏗️ System Architecture


Raw CSV Data
     ↓
ETL Scripts (Python + Pandas)
     ↓
SQLite Database (Structured Storage)
     ↓
Apache Airflow (Pipeline Orchestration)
     ↓
Streamlit Dashboard (Visualization Layer)


---

## 🛠️ Technology Stack

| Layer                  | Technology Used      |
|------------------------|----------------------|
| Data Processing        | Python, Pandas       |
| Database               | SQLite               |
| Orchestration          | Apache Airflow       |
| Visualization          | Streamlit, Matplotlib|
| Deployment             | Streamlit Cloud      |

---

## 📂 Project Structure


```bash
├── data/ # Raw CSV datasets
├── milestone1/ # Data ingestion & setup
├── milestone2/ # Data cleaning & transformation
├── milestone3/ # Airflow ETL pipeline
├── milestone4/
│ └── dashboard/ # Streamlit dashboard
├── README.md
├── LICENSE
```


---

## 🔄 ETL Pipeline (All Milestones)

### 🔹 Milestone 1: Data Ingestion & Setup
- Created SQLite database  
- Loaded raw CSV files into structured tables  
- Tables: `orders`, `order_details`, `sales_target`  

---

### 🔹 Milestone 2: Data Cleaning & Transformation
- Removed duplicate records  
- Standardized column formats  
- Ensured data consistency and quality  

---

### 🔹 Milestone 3: ETL Pipeline using Airflow
- Designed DAG for workflow orchestration  
- Task flow:

create_tables → load_data → check_data

- Enabled structured pipeline execution  

---

### 🔹 Milestone 4: Dashboard & Deployment
- Built interactive dashboard using Streamlit  
- Integrated with cleaned database  
- Deployed using Streamlit Cloud  

---

## ⚙️ Why Apache Airflow?

Apache Airflow is used for **workflow orchestration and automation**.

### Key Advantages:

✔ **Task Scheduling**  
- Enables execution of pipelines at defined intervals (e.g., daily, hourly)  

✔ **Automation**  
- Eliminates manual execution of scripts  
- Ensures repeatable and reliable workflows  

✔ **Task Dependency Management**  
- Executes tasks in correct sequence  
- Prevents data inconsistencies  

✔ **Logging**  
- Tracks execution status of each task  
- Helps in debugging failures  

✔ **Alerts & Monitoring**  
- Provides visibility into pipeline health  
- Can be extended to trigger alerts on failures  

---

## 📊 Dashboard & Analytics (Key Focus)

### Why Streamlit?

Streamlit is used for building dashboards because:

✔ Simple and fast development  
✔ Real-time interactivity  
✔ Seamless integration with Python  
✔ Ideal for data-driven applications  

---

## 📈 Dashboard Features

### 🔹 Interactive Filters
- State selection  
- Category selection  
- Date range filtering  

### 🔹 Key Performance Indicators (KPIs)
- Total Orders  
- Total Sales Amount  
- Total Profit  
- Total Quantity  

### 🔹 Visualizations
- Sales by Category  
- Profit by State (Top 10)  
- Monthly Sales Trends  
- Top Customers by Sales  
- Target vs Actual Comparison  

### 🔹 Data Preview
- Displays cleaned dataset  
- Enables direct data inspection  

---

## 📊 Results & Insights

The dashboard enables:

- Identification of high-performing product categories  
- Analysis of profit distribution across states  
- Tracking monthly sales trends  
- Comparison of actual vs target sales  
- Customer-level performance insights  

These insights support **data-driven decision-making** in a business context.

---

## 🔁 Automation, Scheduling & Monitoring

Although currently manually triggered, the system is designed for:

### ✔ Automation
- Airflow DAG can automate ETL pipeline execution  

### ✔ Scheduling
- Can be configured using cron expressions (e.g., daily runs)  

### ✔ Logging
- Airflow logs track each task execution  
- Helps in debugging and monitoring  

### ✔ Alerts (Extendable)
- Can be integrated with email/notifications for failures  

---

## 🧩 Data Model

The system follows a **relational database design**:

- `orders` → Order-level data  
- `order_details` → Product-level data  
- `sales_target` → Target metrics  

### Relationship:
- One-to-Many  
(One order contains multiple products)

---

## 🧪 Execution Guide

### Run ETL Pipeline
```bash
cd milestone1/scripts
python create_tables.py
python load_data.py
python check_data.py
```

### Run Dashboard
```bash
cd milestone4/dashboard
streamlit run app.py
```
## 📈 Key Achievements
Built a complete ETL pipeline from scratch
Integrated multiple data engineering tools
Developed an interactive analytics dashboard
Ensured data quality and consistency
Prepared system for scalable automation

## 👥 Team Members
```bash
Shrinidhi
Shreya
Sruthi
```

## 📜 License

This project is licensed under the MIT License.

## 🙏 Acknowledgement

This project was developed as part of the Infosys Springboard Internship Program, focusing on real-world applications of data engineering and analytics.
