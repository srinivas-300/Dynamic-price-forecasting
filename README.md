# Dynamic-price-forecasting

Architectural flow diagram:

[ Kafka (Azure Event Hubs) ]
        |
        v
[ Azure Data Lake (Raw Data) ]
        |
        v
[ PySpark (Databricks - Streaming Processing) ]
        |
        v
[ Facebook Prophet (Forecasting) ]


Steps for deployment:

1) Setup events hub in azure portal for kafka streaming for the producer.py

2) Setup azure data lake gen1 / gen2 for data storage 

3) Setup a cluster in databricks, use the workspace to extract the data that was published by the producer.py, transform the data and load the data to the data lake that was setup previously

4) Now run the forecast notebook in the same data bricks cluster using the data that was previously stored in data lake and schedule jobs
