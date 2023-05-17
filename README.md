# Apple-Stock-Data-Warehouse
Using ETL to collect data of Apple stock and save it in a data warehouse.

### Columns
date,open,high,low,close,volume

### Steps
1) Collect Data i.e. Extract part of ETL pipeline. <br>
    a) Data from 2013 to 2018 downloaded from kaggle named as AAP_kaggle.csv.<br>
    b) Data from 2018 to 2023 May 12 scraped from yahoo finance website named as AAPL_scraped.csv.<br>
    c) Data after May 12 will be taken from the yfianace API.<br>
2) Transform the collected data individually. Remove nulls. Remove unwanted columns like Stock Symbol. Convert data to required format. e.g. Convert date to datetime    format. This is transform part of the ETL pipeline<br>
3) Combine the transformed data into a single csv file named merged.csv.
4) A new csv file named latest.csv is produced every month which contains the data of the latest month. Combine it by transforming the columns to the required          format. The whole data is again added to the merged.csv file.
5) The part of running the code generating latest.csv(latest.ipynb) is scheduled using Task Shecduler.
6) Export the data to SSMS to create a Data Warehouse.
7) Automation using SSMS was not feasible so use Telend for automation.



  #### Using AWS
  1) Load the Data Into S3 buckets.
  2) Use AWS Glue's Crawler and Glue Job for Transformation of Data.
  3) Use Athena for quering the transformed data in the form of warehouse using SQL.
  4) Use Quicksight to visualize the data stored in Data Warehouse.
  5) Use Lambda function and Cloudwatch for automation. 
  

#### The detailed documentation is present in Documentation.pdf.

#### -By: Anushil Timsina
