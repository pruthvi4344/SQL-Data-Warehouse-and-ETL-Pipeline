import pandas as pd

def build_date_dimension(order_dates):
    dates = pd.to_datetime(pd.Series(order_dates).drop_duplicates()).sort_values()
    dim = pd.DataFrame({"full_date": dates})
    dim["date_key"] = dim["full_date"].dt.strftime("%Y%m%d").astype(int)
    dim["day"] = dim["full_date"].dt.day
    dim["month"] = dim["full_date"].dt.month
    dim["quarter"] = dim["full_date"].dt.quarter
    dim["year"] = dim["full_date"].dt.year
    dim["weekday"] = dim["full_date"].dt.day_name()
    return dim

def transform(data):
    orders = data["orders"].copy()
    orders["order_date"] = pd.to_datetime(orders["order_date"])
    orders = orders.drop_duplicates()

    dim_date = build_date_dimension(orders["order_date"])
    dim_customer = data["customers"].drop_duplicates().reset_index(drop=True)
    dim_customer["customer_key"] = dim_customer.index + 1

    dim_product = data["products"].drop_duplicates().reset_index(drop=True)
    dim_product["product_key"] = dim_product.index + 1

    dim_region = data["regions"].drop_duplicates().reset_index(drop=True)
    dim_region["region_key"] = dim_region.index + 1

    fact = (
        orders
        .merge(dim_customer[["customer_id", "customer_key"]], on="customer_id")
        .merge(dim_product[["product_id", "product_key"]], on="product_id")
        .merge(dim_region[["region_id", "region_key"]], on="region_id")
    )
    fact["date_key"] = fact["order_date"].dt.strftime("%Y%m%d").astype(int)

    fact_sales = fact[
        ["order_id", "date_key", "customer_key", "product_key",
         "region_key", "sales", "quantity", "discount", "profit"]
    ]

    return {
        "dim_date": dim_date,
        "dim_customer": dim_customer,
        "dim_product": dim_product,
        "dim_region": dim_region,
        "fact_sales": fact_sales,
    }
