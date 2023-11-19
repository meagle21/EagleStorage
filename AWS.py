import boto3
from system_tasks import System_Tasks
import datetime

class AWS:
    
    def __init__(self):
        self.system_tasks = System_Tasks() #OBJECT
        self.SECRET_ACCESS_ID = self.system_tasks.get_aws_secret_access_key() #STRING
        self.ACCESS_KEY_ID = self.system_tasks.get_aws_access_key_id() #STRING
        self.BUCKET_NAME = self.system_tasks.get_s3_bucket_name() #STRING
        self.connection = boto3.client(service_name = "s3", region_name = "us-east-2",
                                       aws_access_key_id = self.get_access_key_id(), aws_secret_access_key = self.get_secret_access_id()
                                      ) #AWS SESSION WITH S3 BUCKET
        self.all_objects = self.set_all_objects() #LIST OF DICTIONARIES
        self.all_object_names_only = self.set_all_object_names() #LIST OF STRINGS

    def get_secret_access_id(self):
        return self.SECRET_ACCESS_ID

    def get_access_key_id(self):
        return self.ACCESS_KEY_ID

    def get_bucket_name(self):
        return self.BUCKET_NAME

    def get_connection(self):
        return self.connection

    def set_all_objects(self):
        objects_list = []
        objects_with_metadata = self.get_connection().list_objects(Bucket = self.get_bucket_name())["Contents"]
        for obj in objects_with_metadata:
            obj_data_dict = {"Name" : "", "LastModified" : "", "FileType" : ""}
            obj_data_dict["Name"] = rf"{obj['Key']}"
            obj_data_dict["LastModified"] = obj["LastModified"].ctime()
            obj_data_dict["FileType"] = self.system_tasks.get_aws_file_type(obj_data_dict["Name"])
            objects_list.append(obj_data_dict)
        return objects_list
    
    def get_all_objects(self):
        return self.all_objects

    def set_all_object_names(self):
        names = []
        for obj in self.get_all_objects():
            names.append(obj["Name"])
        return names

    def get_all_object_names(self):
        return self.all_object_names_only

    def file_name_check(self, upload_file_name):
        if(upload_file_name in self.get_all_object_names()):
            return False
        else:
            return True


    def upload_file_to_s3(self, upload_file, upload_file_name = []):
        '''Method uploads a file to S3 given an inputted file and an optional upload file name parameter'''
        if(upload_file_name == []): #if the user does not input an upload file name then set it to the name of the file being uploaded
            upload_file_name = upload_file
        file_name_check = self.file_name_check() #returns a boolean that says whether the file name already exists in S3
        try:
            response = self.get_connnection().upload_file(upload_file, self.get_bucket_name(), upload_file_name) #upload the file to S3 bucket
            self.set_all_objects() #reset the global variable to the new list, of objects, as this list has now been changed
            self.set_all_object_names() #reset the global variable to the new list of object names
            print(f"{upload_file_name} was successfully uploaded to S3.")
        except ClientError as e:
            logging.error(e)
            print("Failure")            

    def download_file_from_s3(self, file_name, download_path):
        '''Method downloads the requested file from S3 to a specified local directory.'''
        self.get_connection().download_file(self.get_bucket_name(), file_name, download_path)


        

