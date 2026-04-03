# 📊 Milestone 4: Dashboards & Deployment (Weeks 7–8)

## 🎯 Objective

The objective of Milestone 4 is to design and implement an interactive dashboard for visualizing ETL pipeline outputs and to prepare the system for deployment, enabling real-time monitoring and data-driven analysis.

This milestone focuses on:

- Developing dashboards using Streamlit  
- Testing performance on production-scale datasets  
- Deploying the dashboard for real-time access  

---

## 🌐 Live Dashboard

👉 Access the deployed Streamlit dashboard here:  
🔗 https://infosy-82mu22cfxzaj3mjlwmoxtc.streamlit.app/

---

## 1. Dashboard Development (Streamlit)

### ✅ Tool Used
- Streamlit (Python-based interactive dashboard framework)

### ✅ Data Source

The dashboard reads data from the cleaned ETL output stored in the SQLite database:

- `clean_orders`  
- `clean_order_details`  
- `clean_sales_target`  

**Database Path:**

/home/unix16/airflow/data/infosys.db


---

### ✅ Dashboard Features Implemented

#### 📌 KPI Metrics
The dashboard displays the following key performance indicators:

- Total Orders  
- Total Sales Amount  
- Total Profit  
- Total Quantity  

---

#### 📌 Visualizations

The dashboard includes multiple analytical charts:

- Sales by Category (Bar Chart)  
- Profit by State (Top 10) (Bar Chart)  
- Monthly Sales Trend (Line Chart)  
- Top 10 Customers by Sales (Bar Chart)  
- Category Target vs Actual Sales Comparison (Bar Chart)  

---

#### 📌 Filters

Interactive filters are provided for dynamic data exploration:

- Filter by State  
- Filter by Category  
- Filter by Date Range  

---

## 2. Production-Scale Dataset Testing

### ✅ Purpose

To evaluate dashboard performance under large-scale data conditions similar to real-world production environments.

### ✅ Approach

- Increased dataset size by replicating rows using Pandas  
- Tested dashboard responsiveness and chart rendering performance  

### ✅ Outcome

- Dashboard handled increased data volume efficiently  
- Visualizations loaded correctly without performance issues  

---

## 3. Deployment

### ✅ Deployment Platform
- Streamlit Cloud  

### ✅ Deployment Steps

1. Push dashboard code to GitHub repository  
2. Log in to Streamlit Cloud  
3. Connect GitHub repository  
4. Select the entry file:

milestone4/dashboard/app.py

5. Deploy the application  

---

## ⚙️ How to Run Milestone 4 Locally

### Step 1: Navigate to dashboard folder
```bash
cd milestone4/dashboard
```
### Step 2: Install dependencies
```bash
pip install -r requirements.txt
```
### Step 3: Run the application
```bash
streamlit run app.py
```
## 📂 Folder Structure
```bash
milestone4/
   dashboard/
      app.py
      requirements.txt
      streamlit cloud dashboard link.md
   README.md
```
## 🏁 Conclusion

Milestone 4 successfully delivers an interactive and scalable dashboard solution for visualizing ETL pipeline outputs.

Enables real-time data analysis
Provides interactive filtering and KPI monitoring
Supports large-scale dataset handling
Successfully deployed using Streamlit Cloud

This milestone demonstrates the final integration of data engineering and data visualization components in a real-world workflow.

