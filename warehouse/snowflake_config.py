import snowflake.connector

from warehouse.snowflake_config import (
    SNOWFLAKE_OPTIONS
)

conn = snowflake.connector.connect(
    user=SNOWFLAKE_OPTIONS["user"],
    password=SNOWFLAKE_OPTIONS["password"],
    account=SNOWFLAKE_OPTIONS["account"],
    warehouse=SNOWFLAKE_OPTIONS["warehouse"],
    database=SNOWFLAKE_OPTIONS["database"],
    schema=SNOWFLAKE_OPTIONS["schema"]
)