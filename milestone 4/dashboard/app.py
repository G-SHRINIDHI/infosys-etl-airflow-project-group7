import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import os

# -------------------------------
# DATABASE PATH (FIXED ✅)
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "data", "infosys.db")


# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Infosys ETL Dashboard", layout="wide")

st.title("📊 Infosys ETL Dashboard (Milestone 4)")
st.write("Interactive dashboard built using Streamlit for analyzing cleaned ETL data.")

# -------------------------------
# LOAD DATA FROM SQLITE
# -------------------------------
@st.cache_data
def load_data():
    if not os.path.exists(DB_PATH):
        st.error("❌ Database not found. Please run Airflow pipeline first.")
        return None, None, None

    conn = sqlite3.connect(DB_PATH)

    try:
        orders = pd.read_sql("SELECT * FROM clean_orders", conn)
        details = pd.read_sql("SELECT * FROM clean_order_details", conn)
        target = pd.read_sql("SELECT * FROM clean_sales_target", conn)
    except Exception as e:
        st.error(f"❌ Error loading data: {e}")
        return None, None, None
    finally:
        conn.close()

    # Convert date
    orders["order_date"] = pd.to_datetime(orders["order_date"], errors="coerce")

    return orders, details, target


orders_df, details_df, target_df = load_data()

# Stop if data not loaded
if orders_df is None:
    st.stop()

# -------------------------------
# MERGE TABLES
# -------------------------------
merged_df = pd.merge(details_df, orders_df, on="order_id", how="inner")

# -------------------------------
# SIDEBAR FILTERS
# -------------------------------
st.sidebar.header("🔍 Filters")

state_filter = st.sidebar.multiselect(
    "Select State",
    options=sorted(merged_df["state"].dropna().unique()),
    default=sorted(merged_df["state"].dropna().unique())
)

category_filter = st.sidebar.multiselect(
    "Select Category",
    options=sorted(merged_df["category"].dropna().unique()),
    default=sorted(merged_df["category"].dropna().unique())
)

min_date = merged_df["order_date"].min()
max_date = merged_df["order_date"].max()

date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date)
)

# -------------------------------
# APPLY FILTERS (SAFE COPY ✅)
# -------------------------------
filtered_df = merged_df[
    (merged_df["state"].isin(state_filter)) &
    (merged_df["category"].isin(category_filter)) &
    (merged_df["order_date"] >= pd.to_datetime(date_range[0])) &
    (merged_df["order_date"] <= pd.to_datetime(date_range[1]))
].copy()

# -------------------------------
# KPI METRICS
# -------------------------------
st.subheader("📌 Key Performance Indicators (KPIs)")

total_orders = filtered_df["order_id"].nunique()
total_sales = filtered_df["amount"].sum()
total_profit = filtered_df["profit"].sum()
total_quantity = filtered_df["quantity"].sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Orders", total_orders)
col2.metric("Total Sales Amount", f"{total_sales:,.2f}")
col3.metric("Total Profit", f"{total_profit:,.2f}")
col4.metric("Total Quantity", int(total_quantity))

# -------------------------------
# VISUALIZATIONS
# -------------------------------
st.subheader("📊 Visualizations")

colA, colB = st.columns(2)

# SALES BY CATEGORY
with colA:
    st.write("### 🟦 Sales by Category")
    sales_by_cat = filtered_df.groupby("category")["amount"].sum().sort_values(ascending=False)

    fig, ax = plt.subplots()
    sales_by_cat.plot(kind="bar", ax=ax)
    ax.set_xlabel("Category")
    ax.set_ylabel("Sales Amount")
    st.pyplot(fig)

# PROFIT BY STATE
with colB:
    st.write("### 🟩 Profit by State (Top 10)")
    profit_by_state = filtered_df.groupby("state")["profit"].sum().sort_values(ascending=False).head(10)

    fig, ax = plt.subplots()
    profit_by_state.plot(kind="bar", ax=ax)
    ax.set_xlabel("State")
    ax.set_ylabel("Profit")
    st.pyplot(fig)

# -------------------------------
# MONTHLY SALES TREND
# -------------------------------
st.write("### 📈 Monthly Sales Trend")

filtered_df["month"] = filtered_df["order_date"].dt.to_period("M").astype(str)
monthly_sales = filtered_df.groupby("month")["amount"].sum()

fig, ax = plt.subplots()
monthly_sales.plot(kind="line", marker="o", ax=ax)
ax.set_xlabel("Month")
ax.set_ylabel("Sales Amount")
plt.xticks(rotation=45)
st.pyplot(fig)

# -------------------------------
# TOP CUSTOMERS
# -------------------------------
st.write("### 👤 Top 10 Customers by Sales")

top_customers = filtered_df.groupby("customer_name")["amount"].sum().sort_values(ascending=False).head(10)

fig, ax = plt.subplots()
top_customers.plot(kind="bar", ax=ax)
ax.set_xlabel("Customer Name")
ax.set_ylabel("Sales Amount")
plt.xticks(rotation=45)
st.pyplot(fig)

# -------------------------------
# TARGET VS ACTUAL SALES
# -------------------------------
st.write("### 🎯 Category Target vs Actual Sales")

actual_sales = filtered_df.groupby("category")["amount"].sum().reset_index()
actual_sales.columns = ["category", "actual_sales"]

target_sales = target_df.groupby("category")["target"].sum().reset_index()
target_sales["category"] = target_sales["category"].str.lower()

compare_df = pd.merge(target_sales, actual_sales, on="category", how="inner")

fig, ax = plt.subplots()
ax.bar(compare_df["category"], compare_df["target"], label="Target")
ax.bar(compare_df["category"], compare_df["actual_sales"], label="Actual Sales", alpha=0.7)

ax.set_xlabel("Category")
ax.set_ylabel("Amount")
ax.set_title("Target vs Actual Sales by Category")
plt.xticks(rotation=45)
ax.legend()
st.pyplot(fig)

# -------------------------------
# DATA PREVIEW
# -------------------------------
st.subheader("📄 Cleaned Data Preview")
st.dataframe(filtered_df.head(50))

st.success("✅ Dashboard loaded successfully!")