# 🧠 Property Analytics on AWS

---

## 🧭 Overview

**Description:**   
This project builds a batch ETL data pipeline to process property transaction data from multiple sources, creating a set of dimension and fact tables for analytics and reporting.

**Business Problem:**  
Real estate organizations often struggle to consolidate and analyze large property transaction datasets, including financial details, property characteristics, and location-based risk factors. This project enables automated processing of raw property data into curated tables for analytics, reporting, and decision-making.

**Objectives:**  
- Automate extraction, transformation, and loading (ETL) of large property datasets.
- Generate dimension tables (dim_property, dim_location, dim_customer_financials) and a fact table (fact_property_purchase).
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
- Data is extracted from various sources, which in this case, it is extracted from Kaggle dataset. 
- Ingested into S3 as raw data within the raw folder.  
- Handles large datasets by splitting into manageable chunks with the help of ```split_into_chunks.py```.
- Data categorized into `raw` (Bronze), `processed` (Silver), and `analytics` (Gold) zones.

**2. Transformation Layer:**  
- AWS Glue jobs clean and join data, and create Facts and Dimension Tables.  
- Schema evolution handled automatically.  
- Output stored as Parquet for efficient querying.

**3. Storage Layer:**  
- Raw data is stored in S3 buckets with lifecycle policies.  
- Versioning and encryption enabled (SSE-S3 / KMS).

**4. Warehouse / Analytics Layer:**
- Redshift or Athena queries used for BI and model training.  
- QuickSight dashboards visualize KPIs.

---

[//]: # (## ⚙️ Workflow Orchestration)

[//]: # ()
[//]: # (| **Tool** | **Role** |)

[//]: # (|-----------|-----------|)

[//]: # (| AWS Step Functions | Manage pipeline flow |)

[//]: # (| EventBridge | Schedule periodic runs |)

[//]: # (| SNS | Notify on success/failure |)

[//]: # (| CloudWatch | Monitor performance metrics |)

---

## 🔐 Security & Compliance

- IAM roles follow least privilege principle.  
- Encryption at rest (S3 KMS, Redshift encryption).  
- Encryption in transit (HTTPS, SSL).  
- Logging enabled via CloudTrail.  
- Compliance: GDPR / HIPAA as applicable.

---

## 🚀 Scalability & Performance

- Serverless services like Glue handle scaling automatically.  
- Partitioning and bucketing improve query performance.   
- Cost optimization via data compression and lifecycle rules and better coding quality.

---

## 🧰 Monitoring & Error Handling

| **Tool** | **Purpose** |
|-----------|-------------|
| CloudWatch Logs | Track ETL job status |
| SNS Alerts | Notify on failures |
| Dead-Letter Queues | Capture failed records |
| Glue Job Bookmarks | Ensure idempotent processing |

---

[//]: # (## 🔁 Deployment & CI/CD)

[//]: # ()
[//]: # (| **Tool** | **Function** |)

[//]: # (|-----------|--------------|)

[//]: # (| GitHub Actions / CodePipeline | CI/CD automation |)

[//]: # (| Terraform / CloudFormation | Infrastructure as Code |)

[//]: # (| S3 + Lambda Deployments | Serverless updates |)

[//]: # (| Environment Segregation | Dev → Staging → Prod |)

---

## 📊 Sample Data Schema

**Table:** `sales_data`  

|  Column  |  Type  |      Description      | 
|:--------:|:------:|:---------------------:|
| **order_id** | ```STRING``` | Unique transaction ID |
| **user_id** | ```STRING``` | Customer identifier |
| **product_id** | ```STRING``` | Product reference |
| **quantity** | ```INT``` | Quantity purchased |
| **total_price** | ```FLOAT``` | Total transaction amount |
| **timestamp** | ```TIMESTAMP``` | Purchase time |

---

## 📈 Sample Query (Redshift / Athena)

```sql
SELECT 
  product_id, 
  SUM(total_price) AS total_sales
FROM curated.sales_data
GROUP BY product_id
ORDER BY total_sales DESC
LIMIT 10;
```

## 🧱 Future Improvements
- Add data quality checks (Great Expectations, Deequ).
- Introduce Delta Lake or Iceberg for ACID transactions.
- Enable ML feature store integration.
- Add cost tracking via AWS Cost Explorer.

## 📂 Folder Structure
```plaintext
/project-root
 ├── /src                  # ETL scripts (Glue/Spark)
 ├── /infra                # IaC templates (Terraform/CloudFormation)
 ├── /notebooks            # Data exploration
 ├── /docs                 # Documentation & diagrams
 ├── README.md
 └── requirements.txt
```

## 📎 Appendix
- References:
  - AWS Glue Documentation
  - Redshift Best Practices
  - Data Lake Architecture (AWS Whitepaper)
- Contacts:
  - Data Engineer: [Your Name]
  - Email: [your.email@example.com]