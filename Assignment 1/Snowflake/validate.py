from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(URL(
    account = 'soa94276',
    user = 'vivekkulkarni',
    password = '*********',
    database = 'SEVIRDB',
    schema = 'public',
    warehouse = 'SEVIRDATA',
    role='ACCOUNTADMIN'
))


connection = engine.connect()

df = pd.read_sql_query("SELECT * FROM data3files", engine)
print(df.head())
