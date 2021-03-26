import boto3
import json
import csv
import os

input_directory_path = r'C:\Users\adwai\Downloads\sec-edgar\sec-edgar\output'


def connect_aws():
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
    return  comprehend

def check_sentiments(content):
    final_String = ""
    list_statement = content.split('.')
    for line in list_statement:
        if len(line) > 0:
            abc = json.dumps(comprehend.detect_sentiment(Text=line, LanguageCode='en'), sort_keys=True, indent=4)
            pqr = json.loads(abc)
            if (pqr['Sentiment'] == 'MIXED' or pqr['Sentiment'] == 'NEUTRAL'):
                rows.append([line, 0.5])
                final_String = final_String + line + ',' + '0.5' + "\n"
            elif (pqr['Sentiment'] == 'NEGATIVE' or pqr['Sentiment'] == 'POSITIVE'):
                rows.append([line, pqr['SentimentScore']['Positive']])
                final_String = final_String + line + ',' + str(pqr['SentimentScore']['Positive']) + "\n"
    return final_String

def get_data_from_s3():
    s3 = boto3.resource('s3')
    bucket_name = 'edgarpipeline'
    my_bucket = s3.Bucket(bucket_name)
    output = ""

    for object_summary in my_bucket.objects.filter(Prefix="optimized_layer/"):
        body = object_summary.get()['Body'].read()
        output = output + str(body)
    return output

rows = []
final_String=""
comprehend = connect_aws()
content = get_data_from_s3()
final_String = check_sentiments(content)

client = boto3.client('s3')
client.put_object(Body=final_String, Bucket='edgarpipeline', Key='labelled_data/labelled_file.csv')
