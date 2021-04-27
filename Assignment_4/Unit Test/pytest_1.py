import pytest
import json
import requests

from fastapi.security.api_key import APIKeyQuery, APIKeyCookie, APIKeyHeader, APIKey

API_KEY = "1234567asdfgh"
API_KEY_NAME = "access_token"
COOKIE_DOMAIN = "localtest.me"


url1 = "https://i4q6ts5eic.execute-api.us-east-1.amazonaws.com/team_5_134/api-1"
url2 = "https://i4q6ts5eic.execute-api.us-east-1.amazonaws.com/team_5_134/api-2"
url3 = "https://i4q6ts5eic.execute-api.us-east-1.amazonaws.com/team_5_134/api-3"

headers = {'Accept': 'application/json', 'Authorization': 'eyJraWQiOiJIZzJDZDdYRzFFc3FQaWltU1NjcjRqUXBZcHVUXC81MTNpc3V4VW9DOUNWUT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxMTQ1MjVna203NnV2dHZndHFsdTkxbWx1cyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoidGVhbTUtY3N5ZTcyNDUtc2VydmVyLWlkXC9sYW1iZGEtaW52b2tlIiwiYXV0aF90aW1lIjoxNjE5MTEwMDE0LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9mRFFoVTBKaWEiLCJleHAiOjE2MTkxOTY0MTQsImlhdCI6MTYxOTExMDAxNCwidmVyc2lvbiI6MiwianRpIjoiZmRjMjNhZmItNzlmMS00ZDE0LWJmNzgtYTgyNmE5NTQyZDgyIiwiY2xpZW50X2lkIjoiMTE0NTI1Z2ttNzZ1dnR2Z3RxbHU5MW1sdXMifQ.dD0gKuzS04aYoq2H4WGAxZp4wkd5dR0mYWJw78vEPVzlVp7szPxloJTJyxAT4VWUdD7T_V3seedJGHUzcNx6hPjaIQimXIYOh5616-nakAH3x6_vceLzPr3Bvh04ucoKi2k97q3x5gHp648lLtzQya_L4y_BMDFlYGPsxADtKXjOWIPEp7IdUX59QZoBHcasRiSMyfWZQOK6pPgFa2NJZeg-n04u-dqWC5LuawVkCZETq86zaw_r7ky2PIRa3tFxyI02gT_iZoKkHmfZxHDiT1hgJwX6QFJBrNl0aTWtKPZNGsfz1g43Qp5sMkhhSjcFoVVf_cWAI6Y0N86FGUvW3Q'}




def test_get_api1_status_code_equals_200():     
     params = {"tag": "AGEN"}
     req = requests.get(url1, headers=headers , params=params)
     assert req.status_code == 200
     
def test_get_api2_status_code_equals_200():     
     params = {"tag": "AGEN"}
     req = requests.get(url2, headers=headers , params=params)
     assert req.status_code == 200
     
def test_get_api3_status_code_equals_200():     
     params = {"inputUri": 's3://edgardataset/raw_layer/AGEN/', "outputUri":'s3://edgardataset/masked/'}
     req = requests.get(url3, headers=headers , params=params)
     assert req.status_code == 200

def test_get_api4_status_code_equals_200():     
     params = {"inputUri": 's3://edgardataset/raw_layer/AGEN/', "outputUri":'s3://edgardataset/masked/'}
     req = requests.get(url3, params=params)
     assert req.status_code == 401
     
def test_get_api5_status_code_equals_200():     
     params = {"tag": "AGEN"}
     req = requests.get(url2,  params=params)
     assert req.status_code == 401
     
def test_get_api6_status_code_equals_200():     
     params = {"inputUri": 's3://edgardataset/raw_layer/AGEN/', "outputUri":'s3://edgardataset/masked/'}
     req = requests.get(url3,  params=params)
     assert req.status_code == 401