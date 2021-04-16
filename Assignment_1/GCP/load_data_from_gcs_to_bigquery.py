from google.cloud import bigquery
import pandas as pd

## Prepare file before pushing it to BigQuery
df = pd.read_csv('CATALOG.csv')

df1 = df[df['time_utc'].str.contains("2019")]
catalogidlist = []
for ind in df1.index: 
     catalogidlist.append(df1['event_id'][ind])
        
cleanedList = [event_id for event_id in catalogidlist if str(event_id) != 'nan']

dfdetails = pd.read_csv('StormEvents_details-ftp_v1.0_d2019_c20210223.csv')

dfdetails = dfdetails[dfdetails['EVENT_ID'].isin(cleanedList)]

dffatalities = pd.read_csv('StormEvents_fatalities-ftp_v1.0_d2019_c20210223.csv')
dffatalities = dffatalities[dffatalities['EVENT_ID'].isin(cleanedList)]

dflocations = pd.read_csv('StormEvents_locations-ftp_v1.0_d2019_c20210223.csv')
dflocations = dflocations[dflocations['EVENT_ID1'].isin(cleanedList)]

firstset = pd.merge(df1, dfdetails, left_on='event_id', right_on='EVENT_ID')
secondset = pd.merge(firstset, dffatalities, left_on='event_id', right_on='EVENT_ID')
finalset = pd.merge(secondset, dflocations, left_on='event_id', right_on='EVENT_ID1')

finalset['time_utc'] = pd.to_datetime(df['time_utc'])
finalset.drop(['FATALITY_DATE','BEGIN_DATE_TIME','END_DATE_TIME'], axis=1,inplace=True)

finalset.to_csv('finalset.csv')
print(finalset.shape)

# Construct a BigQuery client object.
client = bigquery.Client(project='sevirdataflow')

# TODO(developer): Set table_id to the ID of the table to create.
table_id = "sevirdataflow.sevir_data.storm_event_data"

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1, autodetect=True,
)

with open('finalset.csv', "rb") as source_file:
    job = client.load_table_from_file(source_file, table_id, job_config=job_config)

job.result()  # Waits for the job to complete.

table = client.get_table(table_id)  # Make an API request.
print(
    "Loaded {} rows and {} columns to {}".format(
        table.num_rows, len(table.schema), table_id
    )
)