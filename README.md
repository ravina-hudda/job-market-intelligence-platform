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
