from pyspark_etl.spark_session import spark
from pyspark.sql.functions import count, current_timestamp

silver_df = spark.read.parquet(
    "data/silver/jobs"
)

gold_df = (
    silver_df
    .groupBy("role")
    .agg(
        count("*").alias("total_jobs")
    )
    .withColumn(
        "last_updated",
        current_timestamp()
    )
)

gold_df.show(truncate=False)

gold_df.write \
    .mode("overwrite") \
    .parquet(
        "data/gold/jobs_by_role"
    )