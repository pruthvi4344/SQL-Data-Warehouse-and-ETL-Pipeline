
-- total revenue by year
SELECT
    d.year,
    SUM(f.sales) AS total_revenue

FROM fact_sales f

JOIN dim_date d

ON f.date_key = d.date_key

GROUP BY d.year

ORDER BY d.year;



-- this query is for monthly revenue
SELECT

    d.year,

    d.month,

    SUM(f.sales) AS monthly_revenue

FROM fact_sales f

JOIN dim_date d

ON f.date_key = d.date_key

GROUP BY

    d.year,

    d.month

ORDER BY

    d.year,

    d.month;


-------------------------------------------------
-- 3. Top 10 Products
-------------------------------------------------

SELECT

    p.product_name,

    SUM(f.sales) AS total_sales

FROM fact_sales f

JOIN dim_product p

ON f.product_key = p.product_key

GROUP BY p.product_name

ORDER BY total_sales DESC

LIMIT 10;


-------------------------------------------------
-- 4. Top Customers
-------------------------------------------------

SELECT

    c.customer_name,

    SUM(f.sales) AS total_spent

FROM fact_sales f

JOIN dim_customer c

ON f.customer_key = c.customer_key

GROUP BY c.customer_name

ORDER BY total_spent DESC

LIMIT 10;


-------------------------------------------------
-- 5. Sales by Region
-------------------------------------------------

SELECT

    r.region_name,

    SUM(f.sales) AS total_sales

FROM fact_sales f

JOIN dim_region r

ON f.region_key = r.region_key

GROUP BY r.region_name

ORDER BY total_sales DESC;


-------------------------------------------------
-- 6. Average Order Value
-------------------------------------------------

SELECT

    AVG(sales) AS average_order_value

FROM fact_sales;


-------------------------------------------------
-- 7. Total Orders
-------------------------------------------------

SELECT

    COUNT(*) AS total_orders

FROM fact_sales;


-------------------------------------------------
-- 8. Best Performing Year
-------------------------------------------------

SELECT

    d.year,

    SUM(f.sales) AS yearly_sales

FROM fact_sales f

JOIN dim_date d

ON f.date_key = d.date_key

GROUP BY d.year

ORDER BY yearly_sales DESC

LIMIT 1;


-------------------------------------------------
-- 9. Best Performing Month
-------------------------------------------------

SELECT

    d.month,

    SUM(f.sales) AS monthly_sales

FROM fact_sales f

JOIN dim_date d

ON f.date_key = d.date_key

GROUP BY d.month

ORDER BY monthly_sales DESC

LIMIT 1;


-------------------------------------------------
-- 10. Revenue by Product Category
-------------------------------------------------

SELECT

    p.category,

    SUM(f.sales) AS total_revenue

FROM fact_sales f

JOIN dim_product p

ON f.product_key = p.product_key

GROUP BY p.category

ORDER BY total_revenue DESC;


-------------------------------------------------
-- 11. Customer Count by Region
-------------------------------------------------

SELECT

    r.region_name,

    COUNT(c.customer_key) AS customer_count

FROM dim_customer c

JOIN dim_region r

ON c.region_key = r.region_key

GROUP BY r.region_name

ORDER BY customer_count DESC;


-------------------------------------------------
-- 12. Dashboard Summary
-------------------------------------------------

SELECT

    COUNT(*) AS transactions,

    SUM(sales) AS total_sales,

    AVG(sales) AS average_sales,

    MAX(sales) AS highest_sale,

    MIN(sales) AS lowest_sale

FROM fact_sales;
