import boto3
import json
from fastapi import HTTPException

def download_file_from_s3(bucket_name, object_name):
    s3 = boto3.client('s3')
    try:
        response = s3.get_object(Bucket=bucket_name, Key=object_name)
        content = response['Body'].read().decode('utf-8')
        return content
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"File not found: {e}")