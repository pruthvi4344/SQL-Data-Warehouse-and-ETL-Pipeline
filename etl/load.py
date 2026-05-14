from sqlalchemy import create_engine
from config.config import DATABASE_URL

def load_to_database(tables: dict):
    engine = create_engine(DATABASE_URL)
    for name, df in tables.items():
        df.to_sql(name, engine, if_exists="replace", index=False)
    print("All tables loaded successfully.")
