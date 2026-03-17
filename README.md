\# AV Fleet Telemetry Analytics



!\[Python](https://img.shields.io/badge/Python-3.x-blue)

!\[SQL](https://img.shields.io/badge/SQL-Analytics-orange)

!\[ClickHouse](https://img.shields.io/badge/ClickHouse-Database-yellow)

!\[Data Engineering](https://img.shields.io/badge/Data-Engineering-green)

\## Overview

This project demonstrates a simplified data engineering and analytics pipeline for autonomous vehicle telemetry data.

The goal is to simulate how telemetry signals from vehicles can be ingested, transformed, stored, and analyzed to generate fleet monitoring insights.

The project includes a Python ETL pipeline, a ClickHouse schema, and an analytics layer built with SQL queries.



\## Architecture



Vehicle Telemetry Data  

↓  

Python ETL Pipeline  

↓  

ClickHouse Database  

↓  

SQL Analytics Layer  

↓  

Fleet Monitoring KPIs  



\## Repository Structure



AV-fleet-telemetry-analytics  

├── analytics → telemetry KPI calculations  

├── etl → Python ETL scripts  

├── sql → SQL analytics queries  

├── schema.docx → database schema  

└── README.md  



\## ETL Pipeline



The ETL layer processes telemetry data using Python. It ingests raw signals, transforms them into structured datasets, and prepares them for analytics.



\## Database



Telemetry data is stored in ClickHouse, a columnar database optimized for analytics and large-scale telemetry workloads.



\## Example SQL Query



```sql

SELECT

vehicle\_id,

AVG(speed) AS avg\_speed,

COUNT(\*) AS telemetry\_points

FROM telemetry\_data

GROUP BY vehicle\_id

ORDER BY avg\_speed DESC;

Technologies



Python

SQL

ClickHouse

Git \& GitHub



Author



Othmane Mouadi

MS Data Science Student

Autonomous vehicle testing \& telemetry analytics


