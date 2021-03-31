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

class Item(BaseModel):
    last_name: str


app = FastAPI()


@app.post("/get_data")
def create_item( item: Item):
    last_name = item.last_name
    searchString = "select index_1 from tbl where " + 'last_name = ' + '\''  + last_name + '\''
    connection = connectSnowFlake()
    aa = selectFromSnowflake(searchString,connection)
    d = aa.to_dict(orient='records')
    json_records = json.dumps(d)
    print(json_records)
    return json_records



