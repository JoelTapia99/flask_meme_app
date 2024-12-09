import boto3
import os
from dotenv import load_dotenv

load_dotenv()


def s3_config():
    return boto3.client('s3',
                        region_name=os.getenv('AWS_S3_REGION'),
                        aws_access_key_id=os.getenv('AWS_S3_ACCESS_KEY'),
                        aws_secret_access_key=os.getenv('AWS_S3_SECRET_ACCESS_KEY')
                        )
