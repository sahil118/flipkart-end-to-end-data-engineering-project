# Flipkart End To End Data Engineering Project
This project involves building an ETL (Extract, Transform, Load) data pipeline that extracts product data from the Flipkart API, transforms it into the desired format, and loads it into an AWS data store.

### Overview
This project involves building an ETL (Extract, Transform, Load) data pipeline that extracts product data from the Flipkart API, transforms it into the desired format, and loads it into an AWS data store.

### Architecture
![Architecture Diagram](https://github.com/sahil118/flipkart-end-to-end-data-engineering-project/blob/main/flipkart-project-architecture.png)

### About API/Dataset:
The Real-Time Flipkart API provides product details such as name, price, and ratings based on their popularity. [API Endpoint](https://rapidapi.com/opendatapoint-opendatapoint-default/api/real-time-flipkart-api/playground).

### Tools Utilized

1. **S3(Amazon Simple Storage Service):** Amazon S3, a scalable object storage service provided by Amazon Web Services (AWS). Buckets are used to store and organize data, such as documents, images, backups, logs, and other types of files.

2. **AWS Lambda :** AWS Lambda is a serverless compute service provided by Amazon Web Services (AWS) that allows you to run code without provisioning or managing servers. With AWS Lambda, you can upload your code, set triggers, and the service automatically executes the code in response to specific events, such as changes to data in an S3 bucket, updates in a DynamoDB table, or HTTP requests via Amazon API Gateway.

3. **Cloud Watch:** Amazon CloudWatch is a monitoring service by AWS that collects and analyzes data from AWS resources and applications in real time, providing insights into performance, health, and resource usage to ensure smooth operation.

4. **Glue Crawler :** AWS Glue Crawler is a service that automatically discovers and catalogs data in your AWS environment. It scans data stores (like Amazon S3, DynamoDB, or RDS), identifies the structure of the data, and creates metadata tables in the AWS Glue Data Catalog.

5. **Data Catalog :** AWS Glue Data Catalog is a fully managed, centralized metadata repository in AWS that stores information about data assets, such as their schema, location, and data types. It enables users to discover, organize, and manage metadata for data stored across various AWS services (e.g., Amazon S3, RDS, Redshift) and makes this metadata easily accessible for querying and processing by AWS services like Athena, Redshift Spectrum, and Glue.

6. **AWS Athena :** Amazon Athena is a serverless interactive query service that allows you to analyze data directly in Amazon S3 using standard SQL. It eliminates the need for setting up and managing servers, making it easy to run ad-hoc queries on large datasets stored in S3.

### Packages used 
```
import http.client
import json
import boto3
import os
from datetime import datetime
from io import StringIO
import pandas as pd 
```
### Project Implementation : 
Here is your project execution description, paraphrased and broken down step by step:

1. **Data Extraction**: Use **AWS Lambda** to extract data from the Flipkart API. Deploy the code and configure an **AWS CloudWatch** trigger to automate data extraction every hour.

2. **Store Raw Data**: Save the raw data to an **S3 bucket** for storage.

3. **Data Transformation**: Implement a transformation function within **AWS Lambda** to process the raw data. Set up an automated trigger to execute the transformation and store the transformed data in **S3**.

4. **Analytics Setup**: Use **AWS Glue Crawler** and the **AWS Glue Data Catalog** to build analytics tables based on the transformed data.

5. **Data Querying**: Use **AWS Athena** to query the transformed data for analysis. 
