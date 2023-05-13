# Apple-Stock-Data-Warehouse
Using ETL to collect data of Apple stock and save it in a data warehouse.

### Columns
date,open,high,low,close,volume

### Steps
1) Collect Data i.e. Extract part of ETL pipeline. <br>
  a) Data from 2013 to 2018 downloaded from kaggle named as AAP_kaggle.csv.<br>
  b) Data from 2018 to 2023 May 12 scraped from yahoo finance website named as AAPL_scraped.csv.<br>
  c) Data after May 12 will be taken from the yfianace API.<br>
2) Transform the collected data individually. Remove nulls. Remove unwanted columns like Stock Symbol. Convert data to required format. e.g. Convert date to datetime format. This is transform part of the ETL pipeline<br>
3)Combine the transformed data into a single csv file named merged.csv.

  
