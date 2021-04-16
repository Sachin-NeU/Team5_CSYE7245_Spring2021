# Set up logging
import json
import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Import Boto 3 for AWS Glue
import boto3
client = boto3.client('glue')

# Variables for the job: 
glueJobName = "stormjoinjoin"

# Define Lambda function
def lambda_handler(event, context):
    response = client.start_job_run(JobName = glueJobName)
    print(glueJobName)
    print('## GLUE JOB RUN ID: ' + response['JobRunId'])
    return response