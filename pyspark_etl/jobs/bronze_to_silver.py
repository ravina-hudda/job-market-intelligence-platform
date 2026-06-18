from pyspark_etl.spark_session import spark
from pyspark.sql.functions import col, explode, to_timestamp

bronze_df = spark.read.option("multiLine","true").json("data/bronze/adzuna/*.json")

# bronze_df.printSchema()

jobs_df = bronze_df.select(
    col("ingestion_timestamp"),
    col("source"),
    col("role"),
    col("page"),
    explode(
        col("response.results")
    ).alias("job")
)
# jobs_df.printSchema()
# jobs_df.show(truncate=False)

silver_df = jobs_df.select(
    col("job.id").alias("job_id"),
    col("job.title").alias("title"),
    col("role"),
    col("page"),
    col("job.company.display_name")
        .alias("company_name"),

    col("job.location.display_name")
        .alias("location_name"),

    col("job.category.label")
        .alias("category"),

    col("job.contract_time")
        .alias("contract_time"),

    to_timestamp(col("job.created"))
        .alias("created"),

    col("job.latitude")
        .alias("latitude"),

    col("job.longitude")
        .alias("longitude"),

    col("job.salary_is_predicted")
        .alias("salary_is_predicted"),

    col("job.description")
        .alias("description"),

    col("job.redirect_url")
        .alias("redirect_url"),

    col("ingestion_timestamp"),

    col("source")
)

# silver_df.printSchema()

# silver_df.show(
#     truncate=False
# )
silver_df = silver_df.dropDuplicates(
    ["job_id"]
)
silver_df.write \
    .mode("overwrite") \
    .parquet(
        "data/silver/jobs"
    )
silver_validation_df = spark.read.parquet(
    "data/silver/jobs"
)
print(
    f"Total Jobs: {silver_validation_df.count()}"
)

print(
    f"Unique Jobs: "
    f"{silver_validation_df.select('job_id').distinct().count()}"
)
silver_validation_df.printSchema()

silver_validation_df.show(
    truncate=False
)