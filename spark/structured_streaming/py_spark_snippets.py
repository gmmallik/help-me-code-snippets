from pyspark.sql.functions import *
from pyspark.sql.types import *



# original input schema
jsonSchema = (
  StructType()
  .add("timestamp", TimestampType()) #event time at the source
  .add("deviceId", LongType())
  .add("deviceType", StringType())
  .add("signalStrength", DoubleType())
)

"""
reading from a data stream
Spark streaming has 2 processing modes
1) micro-batch processing {Reads data in chunks ~100ms}
2) Continues streaming {enables low (~1 ms) end-to-end latency with at-least-once fault-tolerance guarantees}
"""

inputDF = ( spark 
        .readStream 
        .schema(jsonSchema) 
        .option("maxFilesPerTrigger", 1)  #slow it down for tutorial. 1 file read, simulate like reading from kafka topic
        .option("badRecordsPath", bad_records_path) #any bad records will go here
        .json(sensor_path) #the source
        .withColumn("INPUT_FILE_NAME", input_file_name()) #maintain file path
        .withColumn("PROCESSED_TIME", current_timestamp()) #add a processing timestamp at the time of processing
        .withWatermark("PROCESSED_TIME", "1 minute") #optional: window for out of order data
        )

# Read text from socket
socketDF = spark \
    .readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()

socketDF.isStreaming()    # Returns True for DataFrames that have streaming sources

socketDF.printSchema()

# Read all the csv files written atomically in a directory
userSchema = StructType().add("name", "string").add("age", "integer")
csvDF = spark \
    .readStream \
    .option("sep", ";") \
    .schema(userSchema) \
    .csv("/path/to/directory")  # Equivalent to format("csv").load("/path/to/directory")

# Write Stream to Parquet File Sink
query = (inputDF
         .writeStream
         .format("parquet") #our sink to save it for posterity or batch queries if needed
         .option("path", output_path)
         .option("checkpointLocation", checkpoint_path) # add checkpointing for resiliency
         .outputMode("append")
         .queryName("devices") #optionally a query name over write to issue queries against
         .trigger(processingTime='5 seconds')
         .start() 
        )