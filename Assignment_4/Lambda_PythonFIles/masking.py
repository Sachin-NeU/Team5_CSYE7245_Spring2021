import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    inputUri = event['inputUri']
    outputUri = event['outputUri']
    print(inputUri , "   ",outputUri)
    client = boto3.client('comprehend',region_name='us-east-1')
    response = client.start_pii_entities_detection_job(
        InputDataConfig={
            'S3Uri': 's3://edgardataset/raw_layer/AXU'
    },
        OutputDataConfig={
            'S3Uri': 's3://edgardataset/masked/'
    },
        Mode='ONLY_REDACTION',
        RedactionConfig={
            'PiiEntityTypes': ['ALL'],
            'MaskMode': 'MASK',
            'MaskCharacter': '*'
    },
        DataAccessRoleArn='arn:aws:iam::845270504212:role/comprehend',
        JobName='comprehend-test',
        LanguageCode='en',
        ClientRequestToken='string'
    )
    
    return {
        'statusCode': 200,
        'body': response
    }
