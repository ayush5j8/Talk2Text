import boto3
import os
from dotenv import load_dotenv
from smart_open import open
import pandas as pd

load_dotenv()

bucket_name = 'talk2text'
output_path = f'{os.getcwd()}\\tmp\output\output_video.mp4'


class AWS:

    def connect_to_s3(self):
        s3 = boto3.resource(
            service_name='s3',
            region_name=os.getenv('REGION'),
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )
        return s3

    def upload_output(self):

        s3 = self.connect_to_s3()

        bucket = s3.Bucket(bucket_name)
        objs = list(bucket.objects.all())
        keys = [{'Key': obj.key} for obj in objs]

        if keys:
            bucket.delete_objects(Delete={'Objects': keys})
            print(f"All objects in {bucket_name} deleted successfully.")
        else:
            print(f"No objects in {bucket_name}.")

        s3.Bucket(bucket_name).upload_file(
            Filename=output_path, Key='Output_Video/output_video.mp4')
