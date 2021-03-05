import download_file_from_s3
from google.cloud import storage
import apache_beam as beam
import datetime

bucket = storage.Client().bucket('gcp-sevir-bucket')

blob = bucket.blob('CATALOG.csv')

blob.upload_from_filename('/home/sachinkumar1037/sevir/CATALOG.csv')

job_name = 'sevir-dataflow' + '-' + datetime.datetime.now().strftime('%y%m%d-%H%M%S')

OUTPUT_DIR = 'gs://gcp-sevir-bucket'
    
options = {
    'staging_location': 'gs://gcp-sevir-bucket/staging',
    'temp_location': 'gs://gcp-sevir-bucket/tmp',
    'job_name': job_name,
    'project': 'sevirdataflow',
    'max_num_workers': 3,   # CHANGE THIS IF YOU HAVE MORE QUOTA
    'no_save_main_session': True,
    'region': 'us-east1',
    #'aws_access_key_id': '', 
    #'aws_secret_access_key': ''
}
opts = beam.pipeline.PipelineOptions(flags=[], **options)
RUNNER = 'DataflowRunner'
p = beam.Pipeline(RUNNER, options=opts)
qry = 'SELECT  FROM sevirdataflow.sevir_data.storm_event_data'
(p 
         | 'Read input file' >> beam.io.ReadFromText('CATALOG.csv')
        )
 
job = p.run()