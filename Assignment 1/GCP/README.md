# Building Data Pipeline for SEVIR Dataset in GCP

### INTRODUCTION

The goal is to develop a data pipeline to ingest, process and visualize  Storm EVent ImagRy (SEVIR) dataset using components in the AWS ecosystem

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

The output of the pipeline is stored in the s3 bucket for aws, the path would be mentioned in output component of Glue pipeline

### Architecture

Google Dataflow is used for data ingestion, transformation, integration and writing output to Google Storage and finally to Google BigQuery.

Google BigQuery is used to query data and Google Data Studio build visualalizations

![](images/'GCP pipeline architecture.jpg')


### Usage



#### Prerequites:
STEP 1 - You need a GCP account

STEP 2 - Download all three types of storm files and upload them to the S3 bucket

STEP 3 - In the Google Cloud Console, on the project selector page, select or create a Google Cloud project. 

STEP 4 - Make sure that billing is enabled for your Cloud project.

STEP 5 - Enable the BigQuery, Cloud Source Repositories, Dataflow, Google Storage, Data Studio and Datalab APIs

STEP 6 - Create Bucket in Cloud Storage and Dataset in BigQuery.


#### Python Scripts in Cloud Shell

STEP 1 - Open Cloud Shell and set your project. Create a virtual environment and install all the dependencies. 

STEP 2 - Create python script to connect to S3 bucket and download all the relevant files

STEP 3 - Create python script to load the files downloaded from S3 bucket and dump them as is to Google Cloud Storage bucket.

STEP 4 - Create python script to integrate the Storm and Weather data and load the final dataset in Big Query table.


#### BigQuery and DataFlow

STEP 1 - Create queries in Big Query

STEP 2 - Load the saved query in Dataflow and create visualizations


### CLAAT Document

https://docs.google.com/document/d/10nxtIU1BLjj-YgayO_XC6u9ABWcGvwdMrDSxi9pu_z0/edit#heading=h.ro8ivw5cavxe

 
