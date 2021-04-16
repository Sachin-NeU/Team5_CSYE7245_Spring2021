import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    def connect_to_aws():
        tag = event['tag']
        s3 = boto3.resource('s3')
        bucket_name = 'edgardataset'
        my_bucket = s3.Bucket(bucket_name)
        data = {}
        for object_summary in my_bucket.objects.filter(Prefix="raw_layer/"+tag):
            value =  object_summary.get()['Body'].read()
            data['output'] = value
            return value
            
    result = connect_to_aws()    
    return {
        'statusCode': 200,
        'body': result
    }
