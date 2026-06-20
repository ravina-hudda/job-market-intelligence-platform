# Job Market Intelligence Platform

An end-to-end Data Engineering platform that collects job market data from public APIs, processes it using PySpark, stores analytics-ready datasets in Snowflake, and visualizes insights through Streamlit dashboards. The entire pipeline is automated using Apache Airflow and containerized with Docker.
access here: https://job-market-intelligence-platform-ai.streamlit.app/
---

## Project Overview

The goal of this project is to build a production-style data platform that answers questions such as:

- Which job roles are currently in highest demand?
- Which companies are hiring the most?
- Which locations have the highest number of openings?
- How is the job market evolving over time?

The platform follows a modern Data Engineering architecture:

```text
Adzuna API
    ↓
Bronze Layer (Raw JSON)
    ↓
Silver Layer (Cleaned Jobs Data)
    ↓
Gold Layer (Business Aggregations)
    ↓
Snowflake Data Warehouse
    ↓
Streamlit Dashboard
```

---

## Architecture

```text
                +----------------+
                |   Adzuna API   |
                +--------+-------+
                         |
                         v
                +----------------+
                | Bronze Layer   |
                | Raw JSON Files |
                +--------+-------+
                         |
                         v
                +----------------+
                | Silver Layer   |
                | Cleaned Data   |
                +--------+-------+
                         |
          +--------------+--------------+
          |              |              |
          v              v              v
+----------------+ +----------------+ +----------------+
| Jobs By Role   | | Jobs By Company| | Jobs By Location|
+-------+--------+ +-------+--------+ +-------+--------+
        |                  |                  |
        +--------+---------+---------+--------+
                 |                   |
                 v
         +------------------+
         |    Snowflake     |
         | Data Warehouse   |
         +--------+---------+
                  |
                  v
         +------------------+
         | Streamlit        |
         | Dashboard        |
         +------------------+
```

---

# Tech Stack

### Data Ingestion
- Python
- Requests
- Adzuna Jobs API

### Data Processing
- Apache Spark
- PySpark
- Spark SQL

### Data Storage
- Snowflake

### Orchestration
- Apache Airflow
- Docker

### Dashboard
- Streamlit

### Development
- Git
- GitHub
- WSL Ubuntu
- VS Code

---

# Project Structure

```text
job-market-intelligence-platform/

├── airflow/
│   ├── dags/
│   │   └── job_market_pipeline.py
│   ├── docker-compose.yml
│   └── Dockerfile
│
├── ingestion/
│   ├── adzuna_client.py
│   └── main.py
│
├── pyspark_etl/
│   ├── spark_session.py
│   └── jobs/
│       ├── bronze_to_silver.py
│       ├── silver_to_gold_role.py
│       ├── silver_to_gold_company.py
│       └── silver_to_gold_location.py
│
├── warehouse/
│   ├── snowflake_client.py
│   ├── snowflake_config.py
│   ├── load_gold_role.py
│   ├── load_gold_company.py
│   └── load_gold_location.py
│
├── dashboard/
│   ├── app.py
│   ├── snowflake_reader.py
│   └── pages/
│       ├── role_analysis.py
│       ├── company_analysis.py
│       └── location_analysis.py
│
├── data/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
└── requirements.txt
```

---

# Data Pipeline

## 1. Data Ingestion

Job data is collected from the Adzuna API for multiple technology roles:

- Data Engineer
- Data Scientist
- Software Engineer
- Backend Developer
- Frontend Developer
- Full Stack Developer
- DevOps Engineer
- Cloud Engineer

Raw API responses are stored in the Bronze layer as JSON files.

Example:

```text
data/bronze/adzuna/
```

---

## 2. Silver Layer

The Bronze layer data is cleaned and standardized using PySpark.

Transformations include:

- Schema standardization
- Deduplication
- Null handling
- Field selection
- Data quality validation

Output:

```text
data/silver/jobs/
```

---

## 3. Gold Layer

Business-ready datasets are generated.

### Jobs By Role

```text
Role               Total Jobs
-----------------------------
Data Scientist         263
DevOps Engineer        255
Full Stack Developer   254
Backend Developer      253
Data Engineer          246
```

### Jobs By Company

Aggregates total jobs by hiring company.

### Jobs By Location

Aggregates total jobs by location.

Output:

```text
data/gold/
```

---

## 4. Snowflake Data Warehouse

Gold datasets are loaded into Snowflake.

Tables:

### JOBS_BY_ROLE

```sql
ROLE
TOTAL_JOBS
LAST_UPDATED
```

### JOBS_BY_COMPANY

```sql
COMPANY_NAME
TOTAL_JOBS
LAST_UPDATED
```

### JOBS_BY_LOCATION

```sql
LOCATION_NAME
TOTAL_JOBS
LAST_UPDATED
```

---

## 5. Dashboard

Interactive dashboard built using Streamlit.

Features:

- Role demand analysis
- Company hiring analysis
- Location hiring analysis
- Real-time Snowflake integration

Launch:

```bash
streamlit run dashboard/app.py
```

---

# Airflow Orchestration

The entire pipeline is automated using Apache Airflow.

DAG:

```text
ingestion
      ↓
bronze_to_silver
      ↓
 ┌──────────────┬──────────────┬──────────────┐
 │              │              │
gold_role   gold_company   gold_location
 │              │              │
load_role   load_company   load_location
```

Schedule:

```python
@hourly
```

Airflow automatically:

1. Fetches new jobs
2. Builds Silver layer
3. Generates Gold datasets
4. Loads Snowflake tables

---

# Running Locally

## Clone Repository

```bash
git clone <repo_url>
cd job-market-intelligence-platform
```

---

## Create Virtual Environment

```bash
python -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Ingestion

```bash
python -m ingestion.main
```

---

## Run ETL

```bash
python -m pyspark_etl.jobs.bronze_to_silver

python -m pyspark_etl.jobs.silver_to_gold_role

python -m pyspark_etl.jobs.silver_to_gold_company

python -m pyspark_etl.jobs.silver_to_gold_location
```

---

## Load Snowflake

```bash
python -m warehouse.load_gold_role

python -m warehouse.load_gold_company

python -m warehouse.load_gold_location
```

---

## Run Dashboard

```bash
streamlit run dashboard/app.py
```

---

## Run Airflow

```bash
cd airflow

docker compose up -d
```

Airflow UI:

```text
http://localhost:8080
```

Default Credentials:

```text
Username: admin
Password: admin
```

---

# Future Enhancements

- Resume Matching Engine
- RAG-powered Career Assistant
- Job Market Forecasting
- Kafka Streaming Pipeline
- CI/CD Deployment
- Cloud Deployment (Azure/AWS)

---

# Author

**Ravina Hudda**

B.Tech, IIT Roorkee  
Data Engineer | PySpark | Snowflake | Airflow | Azure Databricks
