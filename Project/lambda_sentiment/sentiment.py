import boto3
import json
import string
import random

bucket_name = 'stockpriceteam5optimized'
s3_client = boto3.client('s3')
kwargs = {'Bucket': bucket_name}
response = s3_client.list_objects_v2(**kwargs)
all = response['Contents']
latest = max(all, key=lambda x: x['LastModified'])
latest_file = latest['Key']
stock_split = latest_file.split('/')

stock_location = '/'.join(stock_split[i] for i in range(0,len(stock_split)-1) )

s3 = boto3.resource('s3')

my_bucket = s3.Bucket(bucket_name)

result = {}
result['data'] = []
comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')

result = {}
result['data'] = []
for object_summary in my_bucket.objects.filter(Prefix=latest_file):
    body = object_summary.get()['Body'].read()
    string_body = body.decode("utf-8")
    final_dictionary = eval(string_body)

    for i in final_dictionary['data']:
        original_tweet = i['tweet']
        clean_tweet = i['clean_tweet']
        ts = i['ts']
        abc = json.dumps(comprehend.detect_sentiment(Text=clean_tweet, LanguageCode='en'), sort_keys=True, indent=4)
        pqr = json.loads(abc)
        sentiment = pqr['Sentiment']
        search_string= ""

        if sentiment == 'NEUTRAL':
            search_string = 'Neutral'
        elif sentiment == 'POSITIVE':
            search_string = 'Positive'
        elif sentiment == 'NEGATIVE':
            search_string = 'Negative'
        elif sentiment == 'MIXED':
            search_string = 'Mixed'
        score = pqr['SentimentScore'][search_string]

        result['data'].append({
            'tweet': original_tweet,
            'clean_tweet': clean_tweet,
            'sentiment':sentiment,
            'sentiment_score':score,
            'ts':ts
        })
print(result)
letters = string.ascii_letters
file =  ''.join(random.choice(letters) for i in range(10))
client = boto3.client('s3')
bucket_name_destination = 'stockpriceteam5business'
key =  stock_location + '/' + file + '.txt'
client.put_object(Body=str(result), Bucket=bucket_name_destination, Key=key)

