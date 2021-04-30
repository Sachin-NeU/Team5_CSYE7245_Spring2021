# CSYE7245 - Real time stock Prediction using Twitter Tweets and Historical Data


[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

**Team Members**<br />
Adwait Sathe <br />
Sachin <br />
Vivek Kulkarni <br />

#### Quick Links

##### Presentations <br />
[Presentation](https://docs.google.com/document/d/1YMq5QQI7rR6wszhGaVp9iZlRndOikG59GAwNEQaf1f4/edit?usp=sharing)<br />
[Project Proposal](https://docs.google.com/document/d/1QRjOFOU81qru-dsCTIoF4OCbajMffB-vANqJgpZCjGs/edit?usp=sharing)<br />


##### Streamlit Application<br />
Follow instructions below to setup and deploy your own Streamlit Application<br />

[TS-Pipeline | WebApp](http://18.234.153.64:8501/)<br /> 

##### Test Cases<br />
[Document](https://docs.google.com/document/d/1fUBjMMH8iwD7WO291wInE3U9daDpmmAYEeFQTnxxT2w/edit?usp=sharing)

---

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [TestCases](#testcases)


## Introduction

Real time Data Pipeline for ingesting tweets of stocks from Twitter and Finding the Sentiments of the Tweets. Summarization is done using `LSTM` models based on the HuggingFace Pytorch transformers library to run extractive summarizations.

#### Architecture 

![alt text](https://github.com/holladileep/TS-Pipeline/blob/dev/img/CSYE7245_v2-2.png)

---


## Setup

The pipeline requires an Amazon Web Services account to deploy and run. The pipeline uses the folllowing AWS Services:

- Lambda 
- S3
- Comprehend
- CloudWatch
- EC2
- Simple Notification Servive (SNS)
- Kinesis Data Streams
- Kinesis Data Firehose

Signup for an AWS Account [here](https://portal.aws.amazon.com/billing/signup#/start)

Signup for an  Aplha API Account [here](https://www.alphavantage.co/)

Signup for an Twitter Developer Account [here](https://developer.twitter.com/en/apply-for-access)


### Clone

Clone this repo to your local machine using `https://github.com/catchvivek94/Team5_CSYE7245_Spring2021.git`
![alt text](https://github.com/holladileep/TS-Pipeline/blob/dev/img/CSYE7245_v2-2.png)


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
    
### Building Streamlit Application 

We have used Streamlit Application to interact with all the elements of the pipeline.

### Deploying Streamlit App 

The pipeline uses [Streamlit](https://www.streamlit.io/) for allowing the user to upload a file with URLs, enter a single URL or quicky summarize text and sentiments for a given text input. The app directly interacts with the built components on AWS and provides a GUI to run the pipeline without the need for the end-user to manually login to AWS Account and trigger the pipeline.

The Python code for this app can be found at `streamlit_webapp/app.py`. This app is deployed on the EC2 Instance.

> Install required libraries

```
pip3 install streamlit
pip3 install boto3
pip3 install pandas
pip3 install configparser
```

> Run `app.py`

Run the WebApp by running `streamlit run app.py`. 

### Deploying the AWS Batch Docker Container

The Python script for batch scraping URLs can be found in `scrape-batch/` directory. Copy contents of the directory on your machine. 

> Create new ECR Repository

Create a new repository on ECR with the following name `ts-pipeline1`

> Login to the repository

`aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <your_account_id>/ts-pipeline1`

> Build the Image

`docker build -t ts-pipeline1 .`

> Tag the image

`docker tag <your_ECR_repository_URL>/ts-pipeline1:latest`

> Push the image to ECR
`docker push <your_ECR_repository_URL>/ts-pipeline1:latest`

Create a new Compute Environment first followed by a Job Queue on the AWS Batch Console with the default configurations.
Create a Job Definition on the console and provide the ECR container ID created earlier as the input to the `container` attribute. The batch process is ready for execution

### DynamoDB

The pipleine requires three tables to be created on DynamoDB:

- `articles` Store the scraped data 
- `sentiments` Store sentiment scores
- `summary` Store generated summaries and scores

Create all tables from the DynamoDB console with `url` as the **Primary Key**. There is NO need to specify additional fields.

### Slack 

The pipeline delivers real-time notifications via Slack. All Python processes are designed to push notifications to Slack via the Web-Hook placed in the `config.ini` file. Step by step instructions to create an App and generate an incoming Web-Hook can be found [here](https://api.slack.com/messaging/webhooks).

Once the Web-Hook is generated, place the same inside the `config.ini` file for the key `webhook_url`.


## TestCases

All Test Cases have been documented [here](https://docs.google.com/document/d/1fUBjMMH8iwD7WO291wInE3U9daDpmmAYEeFQTnxxT2w/edit?usp=sharing)

Streamlit App can be accessed using this link: [TS-Pipeline | WebApp](http://18.234.153.64:8501/)
> :warning: The instance hosting the App has been shutdown

The pipeline can be tested with the sample `demo.txt` file present in the `tests` directory. Additonally any URL can be entered in the Streamlit app and results can be seen. 

Additionally, `POST` request can be made to the following URLs to receive a summarized response.

> :warning: `POST` requests made to the below API Endpoints do not work since the Flask Application is no longer running on EC2 Instance to avoid recurring AWS Charges. Replace the endpoints with your deployed Flask Application(s) to test the summarization models

> Model 1
```
POST http://18.234.153.64:5001/summarize?ratio=0.2
Content-type: text/plain
Body: <enter your text here>
```
> Model 2
```
POST http://3.87.77.113:5000/summarize?ratio=0.2
Content-type: text/plain
Body: <enter your text here>
```


![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)
