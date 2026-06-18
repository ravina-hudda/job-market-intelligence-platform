from ingestion.config.settings import settings

SNOWFLAKE_OPTIONS = {
    "sfURL":
        f"{settings.snowflake.account}.snowflakecomputing.com",

    "sfUser":
        settings.snowflake.user,

    "sfPassword":
        settings.snowflake.password,

    "sfDatabase":
        settings.snowflake.database,

    "sfSchema":
        settings.snowflake.schema,

    "sfWarehouse":
        settings.snowflake.warehouse
}