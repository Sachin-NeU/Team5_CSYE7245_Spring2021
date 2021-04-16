import boto3

session = boto3.session.Session(aws_access_key_id='---',
              aws_secret_access_key='---')

# Your Bucket goes here
bucket_name = 'sevir'

# Your S3 Path goes here
filename = 'CATALOG.csv'

# Connect to Boto3
#s3 = boto3.resource(service_name='s3',region_name='us-east-1')
s3 = boto3.client('s3', aws_access_key_id='bla' , aws_secret_access_key='bla')
s3.download_file(bucket_name,filename,filename)




