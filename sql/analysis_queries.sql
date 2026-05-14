SELECT year, SUM(sales) AS total_revenue
FROM fact_sales f
JOIN dim_date d ON f.date_key = d.date_key
GROUP BY year
ORDER BY year;
