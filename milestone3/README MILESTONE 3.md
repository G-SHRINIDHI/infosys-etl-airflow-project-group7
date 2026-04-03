
# Milestone 3: Orchestration & Monitoring (Weeks 5–6)

## Objective
To automate and monitor the ETL pipeline using **Apache Airflow** by implementing:
- DAG scheduling  
- Logging  
- Alerting system  

---

## 1. DAG Configuration & Scheduling
- Created an Airflow DAG named **infosys_etl_pipeline**
- Defined task sequence:

```

create_tables → load_data → transform_data → check_data

```

- Used **BashOperator** to execute Python scripts.
- Configured scheduling using a cron expression to run every **2 minutes**:

```

*/2 * * * *

````

The ETL pipeline is automated using scheduling in Apache Airflow, where the DAG is configured to run every 2 minutes using a cron expression.

- Enabled retry mechanism to handle failures automatically.

### ✅ Outcome
- Pipeline runs automatically without manual intervention  
- Tasks execute in correct dependency order  
- Failed tasks are retried automatically  

---

## 2. Logging Implementation

### ✅ Purpose
- Track execution of each step  
- Maintain history of pipeline runs  
- Help in debugging errors  

### ✅ Implementation
- Added logging in all scripts using:

```python
import logging
logging.basicConfig(level=logging.INFO)
````

* Logged key events such as:

  * Start of execution
  * Table creation
  * Data loading
  * Data transformation
  * Completion

### ✅ Example Logs

```
Transformation started
Clean Orders table created!
Clean Order Details table created!
Clean Sales Target table created!
Transformation completed
```

* Logs are stored in:

```
~/airflow/logs/
```

### ✅ Outcome

* Complete execution history is maintained
* Easy debugging and monitoring

---

## 3. Alerts Integration (Email Notifications)

### ✅ Purpose

* Notify user when a task fails or retries
* Reduce need for manual monitoring

### ✅ Implementation

* Configured email alerts in DAG:

```python
'email': ['mshr3ya@gmail.com'],
'email_on_failure': True,
'email_on_retry': True
```

* Configured Gmail SMTP using:

  * 2-Factor Authentication
  * App Password

* Created Airflow SMTP connection (**smtp_default**) for successful email delivery.

### ✅ Testing

* Manually triggered a failure in the pipeline
* Verified:

  * Task failure in Airflow UI
  * Alert triggered in logs
  * Email notification received successfully

### ✅ Outcome

* Alerts are triggered automatically on failure
* Email notifications successfully received

---

## 🔹 4. Monitoring via Airflow UI

Used Airflow Web UI to:

* Monitor DAG runs
* Check task status (success/failure)
* View logs for each task

### ✅ Outcome

* Real-time monitoring of pipeline
* Easy identification of errors

---

## Conclusion

In this milestone, the ETL pipeline was successfully:

* Automated using Airflow DAG scheduling (every 2 minutes)
* Monitored using logging and Airflow UI
* Enhanced with email alerts for failure detection

This ensures a reliable, automated, and monitored data pipeline system.

---

##  One-line Summary

**The pipeline is automated using Airflow to run every 2 minutes, with logging for tracking and email alerts for failure monitoring.**

