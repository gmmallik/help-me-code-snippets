"""
This file has basics on 
- Standard Libraries
- How to define a schema
- Read a file CSV Parquet
- Write a file CSV Parquet
- Transformation
- Add a column
"""
from pyspark.sql.functions import *
from pyspark.sql.types import *

"""
Good practice is to define a schema and not have Spark infer for Performance
Without a schema, Spark will launch couple of jobs: 
1) To read header, and 
2) Another to sample a good portion of the data
"""

# original input schema
jsonSchema = (
  StructType()
  .add("timestamp", TimestampType()) #event time at the source
  .add("deviceId", LongType())
  .add("deviceType", StringType())
  .add("signalStrength", DoubleType())
)

# Output schema
# modified schema with added columns since we are 
# doing some ETL (transforming and adding extra columns)
# this transformed data will be stored into parquet files
# from which an SQL table can be created for consumption or
# report generation
parquetSchema = (
  StructType()
  .add("timestamp", TimestampType()) #event time at the source
  .add("deviceId", LongType())
  .add("deviceType", StringType())
  .add("signalStrength", DoubleType())
  .add("INPUT_FILE_NAME", StringType()) #file name from which this data item was read
  .add("PROCESSED_TIME", TimestampType())) #time at the executor while processing
