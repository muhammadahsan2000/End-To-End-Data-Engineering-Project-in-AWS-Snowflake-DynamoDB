# End-To-End-Data-Engineering-Project-in-AWS-Snowflake-DynamoDB

#Overview:
This project demonstrates an end-to-end real-time data pipeline that fetches weather data from an API, stores it in DynamoDB, streams it to Amazon S3, and loads it into Snowflake for analysis. The architecture ensures automated, scalable, and reliable data processing using AWS Lambda, DynamoDB Streams, and Snowflake.

https://github.com/muhammadahsan2000/End-To-End-Data-Engineering-Project-in-AWS-Snowflake-DynamoDB/blob/b465197bb0a2f72a5a0d79436804ca9b6b50b84d/de-proj.PNG

#Workflow & Architecture:
1️⃣ Weather Data Ingestion (Lambda & API Call)

A Lambda function is triggered on a schedule (via Amazon EventBridge or CloudWatch).
It fetches real-time weather data from an external Weather API for multiple cities.
The weather data is then stored in AWS DynamoDB.

2️⃣ Streaming Data from DynamoDB to S3 (Lambda & Streams)

DynamoDB Streams capture new data insertions in real-time.
A second Lambda function processes these stream records.
The Lambda function converts the data into CSV format and writes it to an S3 bucket.

3️⃣ Loading Data into Snowflake

A trusted connection is established between AWS S3 and Snowflake using STS (Secure Token Service).
Snowflake automatically ingests data from S3 into structured tables.
The ingested data is now ready for analysis, reporting, and visualization in Snowflake.

#Technology Stack
AWS Services: Lambda, DynamoDB, S3, DynamoDB Streams, STS
Database: Snowflake
Programming: Python (for Lambda functions)
Other Tools: Pandas (for data processing), Boto3 (AWS SDK)


#Setup & Deployment
1️⃣ Create an AWS Lambda function to fetch weather data and store it in DynamoDB.
2️⃣ Enable DynamoDB Streams and configure a Lambda trigger to process new records.
3️⃣ Store processed data in Amazon S3 in CSV format.
4️⃣ Configure Snowflake to load data from S3 using external stages.
5️⃣ Run SQL queries in Snowflake to analyze the weather dataset.
