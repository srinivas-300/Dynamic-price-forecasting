from pyspark.sql import SparkSession 
from pyspark.sql.functions import from_json , col
from pyspark.sql.types import StructType , IntegerType , StringType , DoubleType

# Initialize Spark session
spark = SparkSession.builder.appName("SalesDataProcessing").getOrCreate()

schema = StructType([
( "product_id" , IntegerType),
    ("store_id" , IntegerType),
    ("timestamp" , DoubleType),
    ("quantity_sold" , IntegerType)
])

df = (spark.readStream
      .format("kafka")
      .option("kafka.bootstrap.servers","*******")
      .option("subcribe","sales-data")
      .option("startingOffsets","earliest")
      .load())



sales_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")


# Write processed data to Azure Data Lake

sales_df.writeStream \
    .format("parquet") \
    .option("checkpointLocation", "/mnt/sales/checkpoints") \
    .option("path", "abfss://sales-data@yourdatalake.dfs.core.windows.net/processed/") \
    .trigger(processingTime="1 minute") \
    .start()

