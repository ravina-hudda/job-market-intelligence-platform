# dashboard/snowflake_reader.py

import pandas as pd
import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))
from warehouse.snowflake_client import conn


def get_roles_df() -> pd.DataFrame:

    query = """
    SELECT *
    FROM JOBS_BY_ROLE
    ORDER BY TOTAL_JOBS DESC
    """

    return pd.read_sql(query, conn)


def get_companies_df() -> pd.DataFrame:

    query = """
    SELECT *
    FROM JOBS_BY_COMPANY
    ORDER BY TOTAL_JOBS DESC
    """

    return pd.read_sql(query, conn)


def get_locations_df() -> pd.DataFrame:

    query = """
    SELECT *
    FROM JOBS_BY_LOCATION
    ORDER BY TOTAL_JOBS DESC
    """

    return pd.read_sql(query, conn)