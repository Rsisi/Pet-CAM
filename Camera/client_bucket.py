from google.cloud import storage
import os
import pyrebase

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'patronus-329903-c179acacf626.json'

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"


    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

bucket_name = 'patronus-329903.appspot.com'
filename = "1.jpg"
blob_name = 'image'
upload_blob(bucket_name,filename,blob_name)
