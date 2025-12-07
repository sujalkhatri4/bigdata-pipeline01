# spark_job.py
# Simple PySpark-style data processing job

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("BigDataJob").getOrCreate()

data = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
columns = ["Name", "Age"]

df = spark.createDataFrame(data, columns)
df.show()

spark.stop()
