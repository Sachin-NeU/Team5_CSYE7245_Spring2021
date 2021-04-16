from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
import pandas as pd
import boto3

d =['index_1', 'national_provider_identifier','last_name','first_name_of_the_provider','middle_initial_of_the_provider','credentials_of_the_provider','gender_of_the_provider','entity_type_of_the_provider','street_address_1_of_the_provider','street_address_2_of_the_provider','city_of_the_provider','zip_code_of_the_provider','state_code_of_the_provider','country_code_of_the_provider','provider_type','medicare_participation_indicator','place_of_service','hcpcs_code','hcpcs_description','hcpcs_drug_indicator','number_of_services','number_of_medicare_beneficiaries','number_of_distinct_medicare_beneficiary','average_medicare_allowed_amount','average_submitted_charge_amount','average_medicare_payment_amount','average_medicare_standardized_amount']
s3 = boto3.client('s3')
path = "s3://fastapiteam5/Healthcare_Providers.csv"
df = pd.read_csv(path,names=d,skiprows=[0])
df = df.astype(str)
df = df.fillna('')

engine = create_engine(URL(
     account = 'doa03229.us-east-1',
     user = 'adwaitasathe',
     password = 'Boston1#',
     database = 'HEALTHCARE',
     schema = 'public',
     warehouse = 'COMPUTE_WH',
     role='ACCOUNTADMIN'
 ))

connection = engine.connect()

df.to_sql('TBL', con=engine, index=False,if_exists='append',chunksize=16000)

connection.close()
engine.dispose()


