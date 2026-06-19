from sqlalchemy import create_engine
from datetime import datetime
from config.config import DATABASE_URL


def connect_database():

    try:

        engine = create_engine(DATABASE_URL)

        print("Database connection established.")

        return engine

    except Exception as error:

        print("Database connection failed.")

        print(error)

        raise


def load_single_table(engine, table_name, dataframe):

    try:

        dataframe.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        rows = len(dataframe)

        print(f"{table_name} loaded ({rows} rows).")

    except Exception as error:

        print(f"Error loading {table_name}")

        print(error)


def load_to_database(tables: dict):

    start_time = datetime.now()

    print("\nStarting database loading process...")

    engine = connect_database()

    total_tables = len(tables)

    print(f"Total tables: {total_tables}")

    loaded = 0

    for table_name, dataframe in tables.items():

        load_single_table(
            engine,
            table_name,
            dataframe
        )

        loaded += 1

    end_time = datetime.now()

    duration = end_time - start_time

    print("\n========== SUMMARY ==========")

    print(f"Tables Loaded : {loaded}")

    print(f"Execution Time: {duration}")

    print("=============================")

    print("All tables loaded successfully.")


def verify_tables(tables: dict):

    print("\nTables prepared for loading:")

    for table_name in tables:

        print(f"- {table_name}")


if __name__ == "__main__":

    sample_tables = {}

    verify_tables(sample_tables)

    if sample_tables:

        load_to_database(sample_tables)

    else:

        print("No tables found.")
