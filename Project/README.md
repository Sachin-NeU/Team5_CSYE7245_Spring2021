# CSYE7245 - Real time stock Prediction using Twitter Tweets and Historical Data


[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

**Team Members**<br />
Adwait Sathe <br />
Sachin <br />
Vivek Kulkarni <br />

#### Quick Links

##### Presentations <br />
[Project Proposal/Presentation](https://docs.google.com/document/d/1bA-ub0TiGgQjVOulephp--b_WJovU-EI6D1JA5N0jwc/edit#heading=h.n8d7ycbpbk04)<br />


##### Streamlit Application<br />
Follow instructions below to setup and deploy your own Streamlit Application<br />

[TS-Pipeline | WebApp](http://54.157.171.89:8501/)<br /> 


---

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)


## Introduction

Real time Data Pipeline for ingesting tweets of stocks from Twitter and finding the Sentiments of the Tweets which can be used for predicting Trend of Stock. Analyzing historical time-series stock prices and returns and predicting the nearby future stock prices using LSTM model.


## Architecture 

![alt text](https://github.com/catchvivek94/Team5_CSYE7245_Spring2021/blob/main/Project/images/architecture.jpg)

---


## Setup

The pipeline requires an Amazon Web Services account to deploy and run. The pipeline uses the folllowing AWS Services:

- Lambda 
- S3
- Comprehend
- CloudWatch
- EC2
- Kinesis Data Streams
- Kinesis Data Firehose

Signup for an AWS Account [here](https://portal.aws.amazon.com/billing/signup#/start)

Signup for an  Aplha API Account [here](https://www.alphavantage.co/)

Signup for an Twitter Developer Account [here](https://developer.twitter.com/en/apply-for-access)


### Clone

Clone this repo to your local machine using `https://github.com/catchvivek94/Team5_CSYE7245_Spring2021.git`


### Creating EC2 Instance

As lot of apps are going to run simultaneoulsly on the EC2 Instance(We need 4 vCPU EC2 instance) , choose t2.xlarge

Setup Security group inbound access as per below Image
![alt text](https://github.com/catchvivek94/Team5_CSYE7245_Spring2021/blob/main/Project/images/ec2_security.PNG)

Install pip and git on Ec2 using following commands

```
sudo yum -y install python-pip
yum install git
```
Install all Libraries necessary for project using requirement.txt File
```
pip install -r requirement.txt
```

### Create Kinsesis Data Stream
Go to the Amazon Kinesis console to sign up for the service and create an Amazon Kinesis Data Stream. 
```
Mention name of Data Stream in Field:- Data stream name(eg twitter_data)
Number of open shards:- 1
```

### Create Kinesis Data Firehose - Create delivery stream
Go to the Amazon Kinesis console to sign up for the service and create an Amazon Kinesis Data Firehose. 

```
Delivery stream name:- Name of the app(eg twitter_data_app)
Source:- Kinesis Data Stream
Kinesis data stream:- Data stream name(eg twitter_data)
Transform source records with AWS Lambda : Disabled
Data transformation : Disabled
Convert record format: Disabled
Destination:Amazon S3
S3 bucket :- Output Bucket
Buffer size :- 5 MiB
Buffer interval :- 60 sec
S3 compression and encryption: Disabled
```

### Structure of S3 Bucket

S3 Buckets is the main component where we would be storing all the stock data as well as Twitter Data. The structure looks like below
  
![alt text](https://github.com/catchvivek94/Team5_CSYE7245_Spring2021/blob/main/Project/images/s3_structure.PNG)


![alt text](https://github.com/catchvivek94/Team5_CSYE7245_Spring2021/blob/main/Project/images/s3.PNG)
    
---











### Building Streamlit Application 

Streamlit Application is used as a Front end for our pipeline.

### Deploying Streamlit App 

The Python code for this app can be found at `Streamlitapp/app.py`. This app is deployed on the EC2 Instance.

> Install required libraries

```
pip3 install streamlit
pip3 install boto3
```

> Run `app.py`

Run the WebApp by running `streamlit run app.py`. 


### Building Docker File
We have dockerized the application so that anyone can consume the application as they need.

Commands used to dockerize the application
```
sudo docker build -t [appname]:latest
sudo docker images
sudo docker run -p 8501:8501 mystapp:latest
```
![image](https://user-images.githubusercontent.com/59774725/116688307-8958af80-a984-11eb-8576-014fc9cb54c9.png)

### Training LSTM model using MLflow
MLflow is an open source platform for managing the end-to-end machine learning lifecycle. This project requires a Conda environment to run - install Conda on your machine from [here](https://conda.io/projects/conda/en/latest/user-guide/install/download.html)

#### Code related to MLflow:
* [`mlflow.tensorflow.autolog()`](https://www.mlflow.org/docs/latest/tracking.html#automatic-logging-from-tensorflow-and-keras-experimental):
This is an experimental api that logs ML model artifacts and TensorBoard metrics created by the `tf.estimator` we are using.
The TensorBoard metrics are logged during training of the model. By default, MLflow autologs every 100 steps.
The ML model artifact creation is handled during the call to `tf.estimator.export_saved_model()`.

* stock_prediction:
This is the main python file and is used to initiate MLflow run and manages all other python files and functions.





