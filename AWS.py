import boto3
from system_tasks import System_Tasks

class AWS:
    
    def __init__(self):
        self.system_tasks = System_Tasks()
        self.SECRET_ACCESS_ID = self.system_tasks.get_aws_secret_access_key()
        self.ACCESS_KEY_ID = self.system_tasks.get_aws_access_key_id()
        self.bucket_name = self.system_tasks.get_s3_bucket_name()
        self.connection = boto3.client(service_name = "s3", region_name = "us-east-2",
                                       aws_access_key_id = self.ACCESS_KEY_ID, aws_secret_access_key = self.SECRET_ACCESS_ID
                                      )

    def get_secret_access_id(self):
        return self.secret_access_id

    def get_access_key_id(self):
        return self.get_access_key_id

    def get_bucket_name(self):
        return self.bucket_name

    def get_connection(self):
        return self.connection

    def upload_file(self, upload_file, upload_file_name = []):
        connection = self.get_connection()
        if(upload_file_name == []):
            upload_file_name = upload_file
        try:
            response = connection.upload_file(upload_file, self.bucket_name, upload_file_name)
            print(f"{upload_file_name} was successfully uploaded to S3.")
        except ClientError as e:
            logging.error(e)
            print("Failure")
