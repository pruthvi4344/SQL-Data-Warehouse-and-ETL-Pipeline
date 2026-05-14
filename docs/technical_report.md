# Technical Report

## Objective
Design and implement an enterprise-style ETL pipeline that loads retail data into a SQL data warehouse.

## Data Model
Star schema with:
- FactSales
- DimDate
- DimCustomer
- DimProduct
- DimRegion

## Data Quality Checks
- Duplicate removal
- Type conversion
- Referential integrity

## Performance Considerations
- Surrogate keys
- Indexing on foreign keys
- Partitioning fact tables (future)
