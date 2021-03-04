import download_file_from_s3
from google.cloud import storage

bucket = storage.Client().bucket('gcp-sevir-bucket')

blob = bucket.blob('CATALOG.csv')

blob.upload_from_filename('/home/sachinkumar1037/sevir/CATALOG.csv')
