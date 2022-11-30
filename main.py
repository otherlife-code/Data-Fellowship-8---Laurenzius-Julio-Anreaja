
# Import libraries
from google.cloud import storage
import urllib.request

# Define variables
project_id = 'data-fellowship-batch-8'
bucket_name = 'datafellowship-batch8'
destination_blob_name = 'Practice_Test_TOEFL_CMEDIA.pdf'
source_file_name = 'https://penerbitcmedia.com/download1/Practice_Test_TOEFL_CMEDIA.pdf'
storage_client = storage.Client.from_service_account_json('data-fellowship-batch-8-5e438235246e')

# Define upload function
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    file = urllib.request.Request(source_file_name, headers={'User-Agent': 'Chrome/107.0.0.0'})   
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    name = urllib.request.urlopen(file).read()
    blob.upload_from_string(name, content_type='application/pdf')
    print("File uploaded Done!")

# Run the function
upload_blob(bucket_name, source_file_name, destination_blob_name)

