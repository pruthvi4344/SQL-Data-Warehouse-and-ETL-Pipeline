from pathlib import Path
import pandas as pd

def extract_raw_data(raw_dir: str = "data/raw") -> dict:
    raw_path = Path(raw_dir)
    return {
        "orders": pd.read_csv(raw_path / "orders.csv"),
        "customers": pd.read_csv(raw_path / "customers.csv"),
        "products": pd.read_csv(raw_path / "products.csv"),
        "regions": pd.read_csv(raw_path / "regions.csv"),
    }
