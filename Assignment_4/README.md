# Building Lambda Functions with API


### INTRODUCTION


INTRODUCTION
API1: Access
This API retrieves the EDGAR filings data from the S3 bucket
API2: Named entity recognition
This API takes a link to a file on S3 and:
Call Amazon Comprehend anonymize data to recognize the entities for anonymization
Store these on S3
API3: Implement masking, and anonymization functions.
This API masks the data 

Use pre-trained AlBert model trained on IMDB dataset to predict sentiment of each sentences of EDGAR dataset


### Input Data Sources

EDGAR Dataset which has call transcripts of 44 companies

### Output 

A streamlit application to display results of all the 3 APIs and display the prediction of AlBert model for sentiment prediction.

Annotation and Training Pipeline
Architecture

### Architecture

![](Architecture/Assignment_4.jpg)

### Process:
Read EDGAR dataset from S3 using lambda function
Recognize entities for anonymization 
Use Amazon Comprehend to anonymize and mask the data



### CLAAT Document
https://docs.google.com/document/d/1YWciTVYl467sJIL_mF_k4Y4WZ0Z657GnvAjOSVMuRA4/edit?usp=sharing
 
