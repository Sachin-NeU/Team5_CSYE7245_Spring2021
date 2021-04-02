from fastapi import FastAPI
from pydantic import BaseModel
#from test.common.testing import connectSnowFlake,selectFromSnowflake
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
import pandas as pd
import json

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

class Identifeir(BaseModel):
    identfier_number: str

class Name(BaseModel):
    first_name: str
    last_name : str

app = FastAPI()

def getdataFromSnowflake(searchString):
    connection = connectSnowFlake()
    aa = selectFromSnowflake(searchString,connection)
    d = aa.to_dict(orient='records')
    json_records = json.dumps(d)
    final_dictionary = json.loads(json_records)
    print(final_dictionary)
    return final_dictionary

@app.post("/get_national_provider_identifier")
def get_identifier( identifeir: Identifeir):
    identfier_number = identifeir.identfier_number
    searchString = "select * from healthcare_fraud where " + 'national_provider_identifier = ' + '\''  + identfier_number + '\''
    result = getdataFromSnowflake(searchString)
    return result

@app.post("/get_from_name")
def get_identifier( name: Name):
    first_name = name.first_name
    last_name = name.last_name
    searchString = "select * from healthcare_fraud where " + 'last_name = ' + '\''  + last_name + '\' and first_name_of_the_provider = ' + '\''  + first_name + '\''
    result = getdataFromSnowflake(searchString)
    return result




