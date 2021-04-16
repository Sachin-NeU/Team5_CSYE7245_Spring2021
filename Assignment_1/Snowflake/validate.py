from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(URL(
    account = 'lra33674.us-east-1',
    user = 'patelvidhic',
    password = 'Ilove@9515',
    database = 'STORMEVENTDATABASE',
    schema = 'public',
    warehouse = 'COMPUTE_WH',
    role='ACCOUNTADMIN'
))


connection = engine.connect()

df = pd.read_sql_query("SELECT * FROM STORM_EVENT", engine)
print(df.head())
