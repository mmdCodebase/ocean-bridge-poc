import boto3
import os
from botocore.exceptions import NoCredentialsError
import json

def upload_file_to_s3(file, bucket_name, object_name):
    s3 = boto3.client('s3')
    try:
        s3.upload_fileobj(file, bucket_name, object_name)
    except NoCredentialsError:
        print("No AWS credentials found.")

def is_valid_json(data):
    try:
        json.loads(data)
        return True
    except json.JSONDecodeError:
        return False