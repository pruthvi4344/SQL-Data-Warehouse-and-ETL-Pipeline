# Retail Data Warehouse and ETL Pipeline

A production-style SQL Data Warehouse and ETL project built with Python, Pandas, and PostgreSQL.

## Business Problem
Retail companies receive raw CSV files from multiple systems. This project cleans, transforms, and loads the data into a star-schema warehouse for reporting and BI dashboards.

## Architecture
Raw CSV Files → Extract → Transform → Star Schema → Analytical SQL Queries → Power BI/Tableau

## Technology Stack
- Python
- Pandas
- SQLAlchemy
- PostgreSQL
- Docker
- Pytest

## Project Structure
```text
sql-data-warehouse-etl/
├── data/raw/
├── etl/
├── sql/
├── tests/
├── docs/
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Setup
```bash
docker compose up -d
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python -m etl.main
```

## Testing
```bash
pytest
```

## Sample Insights
- Revenue by year
- Top-performing product categories
- Regional sales trends

## Future Enhancements
- Incremental loading
- Slowly Changing Dimensions (SCD Type 2)
- Airflow scheduling
- Data quality dashboards
