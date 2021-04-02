import pytest
import json
import requests

from fastapi.security.api_key import APIKeyQuery, APIKeyCookie, APIKeyHeader, APIKey

API_KEY = "1234567asdfgh"
API_KEY_NAME = "access_token"
COOKIE_DOMAIN = "localtest.me"

def test_get_all_check_status_code_equals_200():
     response = requests.get("http://127.0.0.1:8000/get")
     assert response.status_code == 200
     
def test_post_headers_body_json():
    url = 'http://127.0.0.1:8000/get_national_provider_identifier_key'
    
    # Additional headers.
    headers = {'Content-Type': 'application/json' } 
    
    # Body
    payload = {"identfier_number": "1891106191"}
    
    # convert dict to json string by json.dumps() for body data. 
    resp = requests.post(url, headers=headers, data=json.dumps(payload))       
    
    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    resp_body = resp.json()
    
    # print response full body as text
    print(resp.text)
    
def test_get_all_check_status_code_equals_200_identifier():
     response = requests.get("http://127.0.0.1:8000/1891106191")
     assert response.status_code == 200
     
