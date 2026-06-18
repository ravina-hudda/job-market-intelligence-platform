from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("JobMarketIntelligence")
    .getOrCreate()
)