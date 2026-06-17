from pathlib import Path
import pandas as pd

# extracting the raw data
def extract_raw_data(raw_dir: str = "data/raw") -> dict:
    """
    Extract all raw datasets from CSV files.

    Returns:
        Dictionary containing DataFrames.
    """

    raw_path = Path(raw_dir)

    datasets = {}

    files = {
        "orders": "orders.csv",
        "customers": "customers.csv",
        "products": "products.csv",
        "regions": "regions.csv",
        "suppliers": "suppliers.csv",
        "employees": "employees.csv",
        "payments": "payments.csv",
        "shipments": "shipments.csv"
    }

    for name, filename in files.items():

        file_path = raw_path / filename

        if file_path.exists():

            datasets[name] = pd.read_csv(file_path)

            print(f"Loaded {filename}")

        else:

            print(f"{filename} not found")

    return datasets

# extracting raw data
def extract_orders(raw_dir="data/raw"):

    return pd.read_csv(
        Path(raw_dir) / "orders.csv"
    )

# extract customer data
def extract_customers(raw_dir="data/raw"):

    return pd.read_csv(
        Path(raw_dir) / "customers.csv"
    )

# extract products data
def extract_products(raw_dir="data/raw"):

    return pd.read_csv(
        Path(raw_dir) / "products.csv"
    )

# extract regions data
def extract_regions(raw_dir="data/raw"):

    return pd.read_csv(
        Path(raw_dir) / "regions.csv"
    )

# extract supplier data
def extract_suppliers(raw_dir="data/raw"):

    return pd.read_csv(
        Path(raw_dir) / "suppliers.csv"
    )

# extract employees data
def extract_employees(raw_dir="data/raw"):

    return pd.read_csv(
        Path(raw_dir) / "employees.csv"
    )


def extract_payments(raw_dir="data/raw"):

    return pd.read_csv(
        Path(raw_dir) / "payments.csv"
    )


def extract_shipments(raw_dir="data/raw"):

    return pd.read_csv(
        Path(raw_dir) / "shipments.csv"
    )


if __name__ == "__main__":

    data = extract_raw_data()

    print("\nDatasets Loaded:\n")

    for dataset_name, dataframe in data.items():

        print(f"{dataset_name}: {len(dataframe)} rows")
