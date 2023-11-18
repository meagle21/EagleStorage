import os
import json

class System_Tasks:

    def __init__(self):
        self.ROOT_FOLDER = os.getcwd()
        self.CONFIG_FILENAME = "config_data.json"
        self.CONFIG_FILE_PATH = self.set_config_file_path()
        self.FULL_CONFIG_FILE_DATA = self.set_config_file_all()
        self.AWS_ACCESS_KEY_ID = self.set_aws_access_key_id()
        self.AWS_SECRET_ACCESS_KEY = self.set_aws_secret_access_key()
        self.AWS_S3_BUCKET = self.set_s3_bucket_name()

    def get_root_folder(self):
        return self.ROOT_FOLDER

    def get_config_file_name(self):
        return self.CONFIG_FILENAME

    def set_config_file_path(self):
        root_folder = self.get_root_folder()
        config_filename = self.get_config_file_name()
        return root_folder + "//" + config_filename

    def set_config_file_all(self):
        return json.load(open(self.CONFIG_FILE_PATH))[0]

    def get_config_file_all(self):
        return self.FULL_CONFIG_FILE_DATA

    def set_aws_access_key_id(self):
        aws_access_key_id = "AWS_ACCESS_KEY_ID"
        return self.get_config_file_all()[aws_access_key_id]
    
    def get_aws_access_key_id(self):
        return self.AWS_ACCESS_KEY_ID

    def set_aws_secret_access_key(self):
        aws_secret_access_key = "AWS_SECRET_ACCESS_KEY"
        return self.get_config_file_all()[aws_secret_access_key]

    def get_aws_secret_access_key(self):
        return self.AWS_SECRET_ACCESS_KEY

    def set_s3_bucket_name(self):
        s3_bucket = "S3_BUCKET"
        return self.get_config_file_all()[s3_bucket]

    def get_s3_bucket_name(self):
        return self.AWS_S3_BUCKET