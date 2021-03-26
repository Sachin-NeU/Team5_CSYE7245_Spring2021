import requests
from dataprocessing import datacleaning,removeStopwords,removePunctuation
import re
import boto3

input_data = {'ACFN':'2021','BLFS':'2021','BMMJ':'2021','CELTF':'2021','GHLD':'2021','IRIX':'2021', 'KGFHF':'2021','TME':'2021'}
api = "http://127.0.0.1:8000/call-transcripts/"


def processApi(api_String,code):

    response_input = requests.get(api_String)
    text = response_input.json()['transcript']
    input_string = datacleaning(text)

    list_statement = input_string.split('.')

    final_String = ""

    # for line in list_statement:
    #     score_output = requests.post("http://127.0.0.1:8000",line)
    #     score = score_output['input']['pred']
    #     final_String = final_String + line + ',' + score + "\n"

    key = "inference_data/" + code + "_data.csv"
    print(key)
#    client = boto3.client('s3')
#    client.put_object(Body=final_String, Bucket='edgarpipeline', Key='labelled_data/labelled_file.csv')


for i in input_data:
    code = i
    year = input_data.get(code)
    api_String = api + code + '/' + year
    processApi(api_String,code)

