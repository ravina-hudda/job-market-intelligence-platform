# job-market-intelligence-platform
-------------------------------------------------------------------------------------------
Real-time Job Market Intelligence Platform built using PySpark, Kafka, PostgreSQL, FastAPI, RAG, and Forecasting. Analyzes live job market trends, skill demand, salary insights, and provides AI-powered career recommendations.

-------------------------------------------------------------------------------------------
Architecture:
-------------------------------------------------------------------------------------------
Job APIs (Adzuna/The Muse)
          |
          v
    Kafka Producer
          |
          v
      Kafka Topic
          |
          v
Spark Structured Streaming
          |
    +-----+------+
    |            |
    v            v
 Bronze      PostgreSQL
    |
    v
 Silver
    |
    v
 Gold
    |
    v
 Streamlit Dashboard
    |
    v
 Resume Matcher + RAG
    |
    v
 Forecasting


-------------------------------------------------------------------------------------------
 PHASE 1:
-------------------------------------------------------------------------------------------
 Real Job API
      ↓
Kafka
      ↓
Spark
      ↓
Postgres


-------------------------------------------------------------------------------------------
Project Folder Structure:
-------------------------------------------------------------------------------------------
job-market-intelligence/

├── data/
│
├── producer/
│   └── job_producer.py
│
├── spark/
│   └── streaming_job.py
│
├── warehouse/
│   └── postgres.sql
│
├── docker/
│
├── docs/
│
├── requirements.txt
│
└── README.md

-----------------------------------------------------------------------------------------------
Design Decisions for Phase one
-----------------------------------------------------------------------------------------------

✓ Source: Adzuna
✓ Scope: Tech Jobs
✓ Bronze: Store raw API response
✓ Storage: One file per API call
✓ Naming: Timestamp-based
✓ Error Handling: Log and fail gracefully
✓ Secrets: .env
✓ Client: AdzunaClient
✓ Client Responsibility: API communication only
✓ Return Type: Parsed JSON
✓ Role Looping: main.py orchestrates
✓ Config Validation: Fail fast at startup

-----------------------------------------------------------------------------------------------
