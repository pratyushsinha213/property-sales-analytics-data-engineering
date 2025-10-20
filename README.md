# 🧠 Property Analytics on AWS

---

## 🧭 Overview

**Description:**   
This project builds a batch ETL data pipeline to process property transaction data from multiple sources, creating a set of dimension and fact tables for analytics and reporting.

**Business Problem:**  
Real estate organizations often struggle to consolidate and analyze large property transaction datasets, including financial details, property characteristics, and location-based risk factors. This project enables automated processing of raw property data into curated tables for analytics, reporting, and decision-making.

**Objectives:**  
- Automate extraction, transformation, and loading (ETL) of large property datasets.
- Generate dimension tables (`dim_property`, `dim_location`, `dim_customer_financials`) and a fact table (`fact_property_purchase`).
- Store processed data in a format suitable for analytics (Parquet).
- Enable further consumption by BI tools or ML models for property value predictions and investment analysis.

---

## ☁️ Cloud Architecture

**Architecture Diagram:**  
_Add your architecture diagram here (use Lucidchart, Draw.io, or CloudCraft)._  
![Architecture Diagram](path/to/architecture_diagram.png)

**High-Level Flow:**  
Raw CSV Data → ETL Pipeline (Spark / PySpark) → Dimension & Fact Tables → Parquet Output → Analytics Dashboard

---

## 🧩 Cloud Components Used

| **Service**       | **Purpose**                                            |
|-------------------|--------------------------------------------------------|
| Amazon S3         | Storage of raw CSV files and processed Parquet tables  |
| AWS Glue / Spark  | ETL transformations (cleaning, joining, deduplication) |
| AWS Lambda        | Automation for triggering ETL pipelines                |
| Amazon Redshift   | Data warehouse for analytics                           |
| CloudWatch        | Monitoring and alerting                                |
| Amazon Athena     | Analytics and querying layer                           |
| Amazon Quicksight | Dashboard generation based on Athena queries           |

---

## 🔄 Data Flow and Processing Steps

**1. Ingestion Layer:**
  - Reads CSV files from raw data folder (./raw-data).
  - Handles large datasets by splitting into manageable chunks.

**2. Cleaning Layer:**
  - Drops unnecessary columns (e.g., previous_owners).
  - Standardizes column names for consistency.

**3. Dimension Tables Creation:**
  - dim_property: Includes property characteristics (property_type, furnishing_status, rooms, bathrooms, garage, garden, property_size_sqft).
  - dim_location: Includes location and risk metrics (country, city, crime_cases_reported, legal_cases_on_property, neighbourhood_rating, connectivity_score).
  - dim_customer_financials: Includes financial metrics of customers (customer_salary, loan_amount, loan_tenure_years, monthly_expenses, emi_to_income_ratio).

**4. Fact Table Creation:**
  - Joins the three dimension tables with the main dataset.
  - Includes keys referencing dimensions and metrics (property_id, price, down_payment, decision).

**5. Storage Layer:**
  - Writes dimension tables in overwrite mode.
  - Writes fact table in append mode.
  - All output stored in Parquet format in ./processed-data.

**5. Warehouse / Analytics Layer:****
  - Redshift or Athena queries used for BI and model training.  
  - QuickSight dashboards visualize KPIs.

---

## ⚙️ Workflow Orchestration


| **Tool**               | **Role**                                             |
|:-----------------------|:-----------------------------------------------------|
| PySpark / SparkSession | Executes ETL transformations in a distributed manner |
| Python scripts         | Automates reading, cleaning, and writing of data     |
| SNS                    | Notify on success/failure                            |
| CloudWatch             | Monitor performance metrics                          |

---

## 🔐 Security & Compliance
- Data stored in S3 or Redshift can be encrypted using SSE-KMS or Redshift encryption.
- IAM roles ensure least-privilege access for ETL processes.
- Logging via CloudWatch or Spark logs for auditability.
- Compliance with data privacy policies for financial and personal property information.

---

## 🚀 Scalability & Performance
- Uses PySpark for distributed processing of large datasets.
- Handles large CSV files by splitting them into smaller chunks.
- Dimension tables deduplicated to reduce storage overhead.
- Output Parquet format optimized for query performance in analytics.

---

## 🧰 Monitoring & Error Handling

| **Tool**           | **Purpose**                                        |
|:-------------------|:---------------------------------------------------|
| Spark Logs         | Track ETL job progress and errors                  | 
| Console Prints     | Status messages for file processing and time taken |  
| Retry Mechanism    | Rerun failed file processing                       |
| Glue Job Bookmarks | Ensure idempotent processing                       |


---

## 🧱 Future Improvements
- Integrate with AWS Glue Catalog for automated schema management.
- Implement real-time ingestion via Kinesis or Kafka for live property updates.
- Add data quality validation using Great Expectations.
- Integrate with ML models for property price prediction or risk scoring.
- Deploy CI/CD pipelines to automate ETL deployment and monitoring.

## 📂 Folder Structure
```plaintext
/property-sales-analytics-data-engineering/
├── raw-data
│ ├── global_house_purchase_dataset.csv     # Dataset to be worked upon
│ └── split_into_chunks.py                  # Python script to split large csv file into chunks
├── etl_pipeline.py                         # Python script to run the ETL pipeline
└── README.md
```

## 📎 Appendix
### References:
1. PySpark Documentation: https://spark.apache.org/docs/latest/api/python/
2. AWS S3 & Glue Best Practices: https://docs.aws.amazon.com/glue/latest/dg/best-practices.html
3. Data Lake Architecture Whitepaper: https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/building-data-lakes.pdf