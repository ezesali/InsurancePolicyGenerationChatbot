import boto3
import os
from decouple import config

s3 = boto3.Session(
    aws_access_key_id = config('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key = config('AWS_SECRET_ACCESS_KEY'),
)

bucket_name = config('BUCKET_NAME')
prefix = 'queplan_insurance/'

s3_client = s3.client('s3')


# Create a list to store the downloaded file paths
local_file_paths = []

# Use the list_objects method to retrieve a list of S3 object keys that match the prefix
response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

# Loop through the objects in the response and download each file to the local dataset folder
for obj in response['Contents']:
    if obj['Key'] != prefix:
        file_key = obj['Key']
        file_name = os.path.basename(file_key)
        
        local_file_path = os.path.join('dataset', file_name)
        
        with open(local_file_path, 'wb') as f:
            s3_client.download_fileobj(bucket_name, file_key, f)
        local_file_paths.append(local_file_path)