# Building Data Pipeline for SEVIR Dataset using Snowflake

### INTRODUCTION

The goal is to develop a data pipeline to ingest, process and visualize  Storm EVent ImagRy (SEVIR) dataset using components in the Snowflake and Apache Superset

### DATA SOURCES
#### Input Data Sources

1 - Storm data has 3 types of csv files 
     
     StormEvents_details
     StormEvents_fatalities
     StormEvents_locations

The location of the Files are :- https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/


2 - SEVIR contains two major components:

Catalog: A CSV file with rows describing the metadata of an event 
Data Files: A set of HDF5 files containing events for a certain sensor type
      
	  Catalog Location   : https://s3.console.aws.amazon.com/s3/buckets/sevir?prefix=data%2F&region=us-west-2
      Data Files Location: https://s3.console.aws.amazon.com/s3/object/sevir?region=us-west-2&prefix=CATALOG.csv

The satellite image data is captured by 5 sensors, each sensor have a folder in s3 bucket and images are saved as h5 files

#### Output Data 

The output of the pipeline is stored in the snowflake table which is then access by Apache Superset


### Usage

#### Snowflake Steps to load the data
STEP 1 - You need a Snowflake account where your used

Comamnds to follow to create the stages and copy data to it

STEP 2 - create or replace stage <stagename>;

STEP 3 - create or replace file format <format_name> type = 'csv' field_delimiter = ',';

STEP 4 - put file://<filepath>.csv <stagename>;

STEP 5 - create or replace table <tablename> ( <add all the columns and data types> )

STEP 6 - copy into <tablename> from <stagename>;

STEP 7 - Resolve all the data type issues as snowflake does not handle all the normal data types like dattime2

#### Apache Superset

STEP 1 - pip install --upgrade snowflake-sqlalchemy

STEP 2 - Use this as connection string snowflake://vivekkulkarni:*****@soa94276.US-West/SEVIRDB?role=ACCOUNTADMIN&warehouse=SEVIRDATA

STEP 3 - Create New Charts and add them to the dashboards


### CLAAT Document

https://docs.google.com/document/d/10nxtIU1BLjj-YgayO_XC6u9ABWcGvwdMrDSxi9pu_z0/edit#heading=h.ro8ivw5cavxe

 
