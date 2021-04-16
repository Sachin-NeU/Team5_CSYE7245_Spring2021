from fastapi import FastAPI, Header
from pydantic import BaseModel
from fastapi.security.api_key import APIKeyQuery, APIKeyCookie, APIKeyHeader, APIKey
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
import pandas as pd
import json
from fastapi import Security, Depends, FastAPI, HTTPException
from fastapi.security.api_key import APIKeyQuery, APIKeyCookie, APIKeyHeader, APIKey
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from starlette.status import HTTP_403_FORBIDDEN
from starlette.responses import RedirectResponse, JSONResponse
from typing import Optional


API_KEY = "1234567asdfgh"
API_KEY_NAME = "access_token"
COOKIE_DOMAIN = "localtest.me"

api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)
api_key_cookie = APIKeyCookie(name=API_KEY_NAME, auto_error=False)

def getdataFromSnowflake(searchString):
    connection = connectSnowFlake()
    aa = selectFromSnowflake(searchString,connection)
    d = aa.to_dict(orient='records')
    json_records = json.dumps(d)
    final_dictionary = json.loads(json_records)
    return final_dictionary

def connectSnowFlake():
    engine = create_engine(URL(
         account = 'doa03229.us-east-1',
         user = 'adwaitasathe',
         password = 'Boston1#',
         database = 'HEALTHCARE',
         schema = 'public',
         warehouse = 'COMPUTE_WH',
         role='ACCOUNTADMIN'
     ))
    return engine.connect()

def selectFromSnowflake(string, engine):
    return pd.read_sql_query(string, engine)


async def get_api_key(
    api_key_query: str = Security(api_key_query),
    api_key_header: str = Security(api_key_header),
    api_key_cookie: str = Security(api_key_cookie),
):

    if api_key_query == API_KEY:
        return api_key_query
    elif api_key_header == API_KEY:
        return api_key_header
    elif api_key_cookie == API_KEY:
        return api_key_cookie
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )
class Identifier(BaseModel):
    identfier_number: str

class Name(BaseModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name : str

class location(BaseModel):
    country: str
    statecode:str

app = FastAPI()


@app.post("/get_national_provider_identifier")
def get_identifier( Identifier: Identifier,api_key: APIKey = Depends(get_api_key)):
    identfier_number = Identifier.identfier_number
    searchString = "select * from healthcare_fraud where " + 'national_provider_identifier = ' + '\''  + identfier_number + '\''
    result = getdataFromSnowflake(searchString)
    return result

@app.post("/get_national_provider_identifier_key")
def get_identifier_for_key( Identifier: Identifier):
    identfier_number = Identifier.identfier_number
    searchString = "select * from healthcare_fraud where " + 'national_provider_identifier = ' + '\''  + identfier_number + '\''
    result = getdataFromSnowflake(searchString)
    return result
    
@app.get("/get_all")
def get_identifier():
    searchString = "select top 10 * from healthcare_fraud"
    result = getdataFromSnowflake(searchString)
    return result
    
@app.get("/get_by_identifier_top10")
def get_by_identifier_top10():
    searchString = "select top 10 * from healthcare_fraud where national_provider_identifier = 1891106191"
    result = getdataFromSnowflake(searchString)
    return result

@app.get("/get_by_lastname")
def get_by_lastname():
    searchString = "select top 10 * from healthcare_fraud where last_name = 'JONES'"
    result = getdataFromSnowflake(searchString)
    return result
    
@app.get("/get_by_country")
def get_by_country():
    searchString = "select top 10 * from healthcare_fraud where COUNTRY_CODE_OF_THE_PROVIDER = 'US'"
    result = getdataFromSnowflake(searchString)
    return result


@app.get("/{get_national_provider_identifier}")
async def read_item(get_national_provider_identifier):
    searchString = "select * from healthcare_fraud where " + 'national_provider_identifier = ' + '\''  + get_national_provider_identifier + '\''
    result = getdataFromSnowflake(searchString)
    return result

@app.post("/get_from_name")
def get_name( name: Name,api_key: APIKey = Depends(get_api_key)):
    first_name = name.first_name
    last_name = name.last_name
    middle_name = name.middle_name
    searchString = "select * from healthcare_fraud where " + 'last_name = ' + '\''  + last_name + '\' and first_name_of_the_provider = ' + '\''  + first_name + '\''
    if (middle_name != None):
        searchString = searchString + ' and MIDDLE_INITIAL_OF_THE_PROVIDER = ' + '\''  + middle_name + '\''
    result = getdataFromSnowflake(searchString)
    return result

@app.post("/get_from_location")
def get_location( location: location,api_key: APIKey = Depends(get_api_key)):
    country = location.country
    state = location.statecode
    searchString = "select * from healthcare_fraud where " + 'STATE_CODE_OF_THE_PROVIDER = ' + '\''  + state + '\' and COUNTRY_CODE_OF_THE_PROVIDER = ' + '\''  + country + '\''
    print(searchString)
    result = getdataFromSnowflake(searchString)
    return result

