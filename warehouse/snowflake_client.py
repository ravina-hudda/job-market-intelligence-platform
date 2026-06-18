import snowflake.connector

from ingestion.config.settings import settings

conn = snowflake.connector.connect(
    user=settings.snowflake.user,
    password=settings.snowflake.password,
    account=settings.snowflake.account,
    warehouse=settings.snowflake.warehouse,
    database=settings.snowflake.database,
    schema=settings.snowflake.schema
)