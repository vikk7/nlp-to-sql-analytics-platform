from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd

from backend.config import (
    DB_USERNAME,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DB_NAME
)

# ==========================
# Database URL
# ==========================
DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{DB_USERNAME}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ==========================
# Create Database Engine
# ==========================
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)


# ==========================
# Execute SQL Query
# ==========================
def run_query(query: str):
    """
    Execute SQL query and return:
    (DataFrame, Error)
    """

    try:

        with engine.connect() as connection:
            df = pd.read_sql(text(query), connection)

        return df, None

    except SQLAlchemyError as e:

        return None, str(e)

    except Exception as e:

        return None, str(e)


# ==========================
# Test Database Connection
# ==========================
if __name__ == "__main__":

    query = "SELECT * FROM customers;"

    result, error = run_query(query)

    if error is None:

        print("\n✅ Query Executed Successfully\n")

        print(result)

    else:

        print("\n❌ Query Execution Failed\n")

        print(error)




 