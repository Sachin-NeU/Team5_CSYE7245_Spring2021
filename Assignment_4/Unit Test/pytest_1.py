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

headers = {'Accept': 'application/json', 'Authorization': 'eyJraWQiOiJIZzJDZDdYRzFFc3FQaWltU1NjcjRqUXBZcHVUXC81MTNpc3V4VW9DOUNWUT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxMTQ1MjVna203NnV2dHZndHFsdTkxbWx1cyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoidGVhbTUtY3N5ZTcyNDUtc2VydmVyLWlkXC9sYW1iZGEtaW52b2tlIiwiYXV0aF90aW1lIjoxNjE4NTk4OTYxLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9mRFFoVTBKaWEiLCJleHAiOjE2MTg2ODUzNjEsImlhdCI6MTYxODU5ODk2MSwidmVyc2lvbiI6MiwianRpIjoiZWEwNzYyNTAtMzRiNC00ZWNiLWJhMmQtM2ViMmVmMmM5NzA3IiwiY2xpZW50X2lkIjoiMTE0NTI1Z2ttNzZ1dnR2Z3RxbHU5MW1sdXMifQ.dpFAVRdPLkgfv72I_3IILrkX4ctNSPjYGLv4m8aduvSs3wl8aKXtSzsC0uJz1twV7f-f5jL_8CNSLt3YWutRPAkAB4nEBZFQUlpiGB_XBmdLPKLaWvRbhDQrcAATV43sw0V64Z3zH7fHfAn6Lsz0aROj1GZQlM548pCWUWdNnzrQpyWBlwI0xHgeOnyGYd6b2qs7SfHLRuDvi2Gkj9YDxMDxdnL05NayUEovty9M8YkiuAunll6JDJ9O8Cy4ylOpEMfodYL7C6bjADb7YKEVJLJSLYkKZ98dhoCZZ2wf0ad-4EzyPNJzgczWIN5MMT1ChElECEc4JlbATUZj-UV6gw'}




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
     req = requests.get(url3, headers=headers , params=params)
     assert req.status_code == 200
     
def test_get_api5_status_code_equals_200():     
     params = {"inputUri": 's3://edgardataset/raw_layer/AGEN/', "outputUri":'s3://edgardataset/masked/'}
     req = requests.get(url3, headers=headers , params=params)
     assert req.status_code == 200
     
     
def test_get_api6_status_code_equals_200():     
     params = {"inputUri": 's3://edgardataset/raw_layer/AGEN/', "outputUri":'s3://edgardataset/masked/'}
     req = requests.get(url3, headers=headers , params=params)
     assert req.status_code == 200
     
