##### Intalling the spark in google colab-----

pip intall pyspark

from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder \
    .appName("Colab PySpark Setup") \
    .getOrCreate()

# Test Spark by creating a simple DataFrame
data = [("Upen", 1), ("John", 2), ("Alice", 3)]
df = spark.createDataFrame(data, ["Name", "ID"])
df.show()

##### Now uploading the file from local directory to google colab (eg. example.csv)--------

from google.colab import files
uploaded = files.upload()

##### Reading the file and Understanding the Sturcture of Schema------

df = spark.read.csv("train.csv", header=True, inferSchema=True)
df.show(5)
df.printSchema()

df.printSchema()
df.columns
df.describe().show()


##### Now cleaning the raw data (REMOVING THE UNWANTED AND NULL DATA)----


from pyspark.sql.functions import to_timestamp, unix_timestamp, col, when

# Set legacy time parser policy
spark.conf.set("spark.sql.legacy.timeParserPolicy", "LEGACY") # Added this line to set legacy time parser

# Replace 'NaN' or missing strings with nulls
df = df.replace('NaN', None)

# Convert time columns to timestamp
df = df.withColumn("Time_Orderd_ts", to_timestamp("Time_Orderd", "HH:mm"))

# Drop rows where time data is missing
df = df.na.drop(subset=["Time_Orderd_ts", "Time_Order_picked"])

# Calculate delivery duration in minutes (from order time to pickup time)
df = df.withColumn("Order_to_Pickup_Minutes",
                   (unix_timestamp("Time_Order_picked") - unix_timestamp("Time_Orderd_ts")) / 60)

# Show a few cleaned rows
df.select("Time_Orderd", "Time_Order_picked", "Order_to_Pickup_Minutes").show(5)


#### Now some basic analysis -----


# Average delivery person age by city
df.groupBy("City").avg("Delivery_person_Age").show()

# Average pickup delay by traffic conditions
df.groupBy("Road_traffic_density").avg("Order_to_Pickup_Minutes").show()

# Count orders by order type
df.groupBy("Type_of_order").count().show()

# Average delivery time by weather conditions
df.groupBy("Weatherconditions").avg("Order_to_Pickup_Minutes").show()

# Average delivery time by vehicle condition
df.groupBy("Vehicle_condition").avg("Order_to_Pickup_Minutes").show()

# Delivery time comparison by festival
df.groupBy("Festival").avg("Order_to_Pickup_Minutes").show()



