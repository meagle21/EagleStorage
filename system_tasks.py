import os, json

class System_Tasks:

    def __init__(self):
        self.CONFIG_FILENAME = "config_data.json"
        self.AWS_ACCESS_KEY_ID_KEY_NAME = "AWS_ACCESS_KEY_ID"
        self.AWS_SECRET_ACCESS_KEY_KEY_NAME = "AWS_SECRET_ACCESS_KEY"
        self.AWS_S3_BUCKET_NAME_KEY = "S3_BUCKET"
        self.ROOT_FOLDER = os.getcwd()
        self.CONFIG_FILE_PATH = self.set_config_file_path()
        self.FULL_CONFIG_FILE_DATA = self.set_config_file_all()
        self.AWS_ACCESS_KEY_ID = self.set_aws_access_key_id()
        self.AWS_SECRET_ACCESS_KEY = self.set_aws_secret_access_key()
        self.AWS_S3_BUCKET = self.set_s3_bucket_name()

    def get_root_folder(self):
        '''Get the file path of the root folder of the project.'''
        return self.ROOT_FOLDER

    def get_config_file_name(self):
        '''Get the configuration file name from the global variable list.'''
        return self.CONFIG_FILENAME

    def set_config_file_path(self):
        '''Set the configuration file file path based on the root folder path and config file name.'''
        return rf"{self.get_root_folder()}/{self.get_config_file_name()}"

    def set_config_file_all(self):
        '''Set the data from the configuration file.'''
        return json.load(open(self.CONFIG_FILE_PATH))[0]

    def get_config_file_all(self):
        return self.FULL_CONFIG_FILE_DATA

    def get_aws_access_key_id_key(self):
        return self.AWS_ACCESS_KEY_ID_KEY_NAME

    def set_aws_access_key_id(self):
        return self.get_config_file_all()[self.get_aws_access_key_id_key()]
    
    def get_aws_access_key_id(self):
        return self.AWS_ACCESS_KEY_ID

    def get_aws_secret_access_key_name(self):
        return self.AWS_SECRET_ACCESS_KEY_KEY_NAME

    def set_aws_secret_access_key(self):
        return self.get_config_file_all()[self.get_aws_secret_access_key_name()]

    def get_aws_secret_access_key(self):
        return self.AWS_SECRET_ACCESS_KEY

    def get_aws_s3_bucket_name_key(self):
        return self.AWS_S3_BUCKET_NAME_KEY

    def set_s3_bucket_name(self):
        return self.get_config_file_all()[self.get_aws_s3_bucket_name_key()]

    def get_s3_bucket_name(self):
        return self.AWS_S3_BUCKET

    def get_aws_file_type(self, file_name):
        file_extension = os.path.splitext(file_name)[1].replace(".", "")
        if(len(file_extension) == 0):
            file_extension = "folder"
        return file_extension

