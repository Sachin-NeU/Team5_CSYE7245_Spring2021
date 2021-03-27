import requests
from dataprocessing import datacleaning,removeStopwords,removePunctuation
import re
import boto3
import json

input_data = {'TME':'2021'}
api = "http://127.0.0.1:8000/call-transcripts/"


def processApi(api_String,code):

    response_input = requests.get(api_String)
    text = response_input.json()['transcript']
    input_string = datacleaning(text)

    list_statement = input_string.split('.')

    final_String = ""

    for line in list_statement:
        final_list = json.dumps(line)
        data = {"data": [final_list]}
        #final_list = json.dumps(statement_list_new)
        response_data = requests.post("http://localhost:5000/predict", json=data)
        score_output = response_data.json()
        #print(response_data['input'])
        score1 = score_output['pred']
        score = json.dumps(score1)
        final_String = final_String + line + ',' + score + "\n"
        #break
        key = "inference_data/" + code + "_data.csv"
        client = boto3.client('s3')
        client.put_object(Body=final_String, Bucket='edgarpdp', Key=key)

for i in input_data:
    code = i
    year = input_data.get(code)
    api_String = api + code + '/' + year
    processApi(api_String, code)

