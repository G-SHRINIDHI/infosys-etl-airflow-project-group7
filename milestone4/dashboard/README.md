# 📊 Milestone 4: Dashboards & Deployment (Weeks 7–8)

## 🎯 Objective
The objective of Milestone 4 is to build an interactive dashboard for the ETL pipeline outputs and finalize deployment for real-time monitoring and analysis.

This milestone focuses on:
- Building dashboards using **Streamlit**
- Testing performance on production-scale datasets
- Deploying the dashboard framework

##  1. Dashboard Development (Streamlit)

### ✅ Tool Used
- Streamlit (Python-based dashboard framework)

### ✅ Data Source
The dashboard reads data from the cleaned ETL output stored in the SQLite database:

- `clean_orders`
- `clean_order_details`
- `clean_sales_target`

Database used:
```
/home/unix16/airflow/data/infosys.db

```

### ✅ Dashboard Features Implemented

#### 📌 KPI Metrics
The following key metrics are displayed:
- Total Orders
- Total Sales Amount
- Total Profit
- Total Quantity

#### 📌 Visualizations
The dashboard includes the following charts:
- Sales by Category (Bar Chart)
- Profit by State (Top 10) (Bar Chart)
- Monthly Sales Trend (Line Chart)
- Top 10 Customers by Sales (Bar Chart)
- Category Target vs Actual Sales Comparison (Bar Chart)

#### 📌 Filters
Interactive filters were implemented for better analysis:
- Filter by State
- Filter by Category
- Filter by Date Range

---

##  2. Production-Scale Dataset Testing

### ✅ Purpose
To ensure the dashboard performs efficiently on large datasets similar to production environments.

### ✅ Approach
- Dataset size was increased by replicating rows using Pandas.
- Dashboard responsiveness and chart loading time were tested.

### ✅ Outcome
The dashboard was successfully tested for scalability and was able to load and visualize large datasets.

---

##  3. Deployment

### ✅ Deployment Platform
- Streamlit Cloud (Recommended)

### ✅ Deployment Steps
1. Push the dashboard code to the GitHub repository.
2. Login to Streamlit Cloud.
3. Connect the GitHub repository.
4. Select the Streamlit entry file:
```

milestone4/dashboard/app.py

````
5. Deploy the application.

---

## ⚙️ How to Run Milestone 4 Locally

Navigate to the dashboard folder:

```bash
cd milestone4/dashboard
````

Install required dependencies:

```bash
pip install -r requirements.txt
```

Run the dashboard:

```bash
streamlit run app.py
```

---

## 📂 Folder Structure

```
milestone4/
   dashboard/
      app.py
      requirements.txt
   README.md
```

---

## 🏁 Conclusion

Milestone 4 successfully implements an interactive Streamlit dashboard to visualize and monitor the cleaned ETL pipeline output.
The dashboard supports KPI monitoring, interactive filtering, visual insights, production-scale testing, and deployment readiness.

