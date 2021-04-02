import pytest
import json
import requests


def test_get_all_check_status_code_equals_200():
     response = requests.get("http://127.0.0.1:8000/get")
     assert response.status_code == 200
     
def test_post_headers_body_json():
    url = 'http://127.0.0.1:8000/get_data'
    
    # Additional headers.
    headers = {'Content-Type': 'application/json' } 
    
    # Body
    payload = {"last_name": "JONES"}
    
    # convert dict to json string by json.dumps() for body data. 
    resp = requests.post(url, headers=headers, data=json.dumps(payload))       
    
    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    resp_body = resp.json()
    
    # print response full body as text
    print(resp.text)