# Team5_CSYE7245_Spring2021


###INTRODUCTION

The goal is to develop a data pipeline to ingest, process and visualize  Storm EVent ImagRy (SEVIR) dataset using components in the AWS ecosystem

###DATA SOURCES
####Input Data Sources

1 - Storm data has 3 types of csv files 
     
     StormEvents_details
     StormEvents_fatalities
     StormEvents_locations

The location of the Files are :- https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/


2 - SEVIR contains two major components:
Catalog: A CSV file with rows describing the metadata of an event
Data Files: A set of HDF5 files containing events for a certain sensor type
      Catalog Location : https://sevir.undefined/CATALOG.csv
      Data Files Location: s3://sevir/data/

The satellite image data is captured by 5 sensors, each sensor have a folder in s3 bucket and images are saved as h5 files

####Output Data 

The output of the pipeline is stored in the s3 bucket for aws and google storage bucket for GCP, the path would be mentioned in output component of Glue pipeline
