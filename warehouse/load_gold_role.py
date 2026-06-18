from pyspark_etl.spark_session import spark
from warehouse.snowflake_config import (
    SNOWFLAKE_OPTIONS
)

gold_df = spark.read.parquet(
    "data/gold/jobs_by_role"
)

gold_df.printSchema()

gold_df.show(truncate=False)

(
    gold_df.write
    .format("snowflake")
    .options(**SNOWFLAKE_OPTIONS)
    .option(
        "dbtable",
        "JOBS_BY_ROLE"
    )
    .mode("overwrite")
    .save()
)

print(
    "Successfully loaded JOBS_BY_ROLE"
)