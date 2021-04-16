import json
import boto3
def lambda_handler(event, context):
    # TODO implement
    
    tag = event['tag']
    def connect_to_aws():
        s3 = boto3.resource('s3')
        bucket_name = 'edgardataset'
        my_bucket = s3.Bucket(bucket_name)
        data = {}
        for object_summary in my_bucket.objects.filter(Prefix="raw_layer/"+tag):
            value =  object_summary.get()['Body'].read()
            return value
            
    
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
    
    text = str(connect_to_aws())
    result = json.dumps(comprehend.detect_entities(Text="Agenus Inc. (AGEN) CEO Garo Armen on Q4 2020 Results - Earnings Call Transcript", LanguageCode='en'), sort_keys=True, indent=4)
    result_loads = json.loads(result)
    result_loads_2 = json.dumps(result_loads)
    
    filetext = str(connect_to_aws())
    count = 0
    tt = ""
    for i in filetext.split('\\n'):
        print(i)
        result= json.dumps(comprehend.detect_entities(Text=i, LanguageCode='en'), sort_keys=True, indent=4)
        result_loads = json.loads(result)
        for j in result_loads["Entities"]:
            if j["Type"] == 'PERSON' or j["Type"] == 'ORGANIZATION' or j["Type"] == 'LOCATION' :
                tt = tt + str(j)
        count += 1
        if count == 3 :
            break
    client = boto3.client('s3')
    client.put_object(Body=tt, Bucket='edgardataset', Key='entites/result.txt')
        
    return result
