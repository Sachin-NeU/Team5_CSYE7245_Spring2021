from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client(project='sevirdataflow')

# TODO(developer): Set table_id to the ID of the table to create.
table_id = "sevirdataflow.sevir_data.CATALOG"

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1, autodetect=True,
)

with open('/home/sachinkumar1037/sevir/CATALOG.csv', "rb") as source_file:
    job = client.load_table_from_file(source_file, table_id, job_config=job_config)

job.result()  # Waits for the job to complete.

table = client.get_table(table_id)  # Make an API request.
print(
    "Loaded {} rows and {} columns to {}".format(
        table.num_rows, len(table.schema), table_id
    )
)