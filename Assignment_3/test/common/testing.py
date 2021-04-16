from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
import pandas as pd

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
