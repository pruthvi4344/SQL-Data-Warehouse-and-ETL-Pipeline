from etl.extract import extract_raw_data
from etl.transform import transform
from etl.load import load_to_database

def main():
    data = extract_raw_data()
    warehouse = transform(data)
    load_to_database(warehouse)

if __name__ == "__main__":
    main()
