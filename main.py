from AWS import AWS
from App import App
from system_tasks import System_Tasks

### INITIALIZE OBJECTS TO USE CUSTOM METHODS
AWS_Class = AWS()
App_Class = App()
System_Tasks = System_Tasks()


### THIS CODE SNIPPET CAN BE USED TO UPLOAD A FILE TO S3
#file_to_upload = "test.jpg"
#file_name_in_s3 = "CareerStuff/test_v2.jpg" #can be kept commented out if need be, the parameter is optional
#AWS_Class.upload_file_to_s3(file_to_upload, file_name_in_s3)

### THIS CODE SNIPPET CAN BE USED TO PRINT A LIST OF ALL OBJECTS IN THE S3 BUCKET
objects = AWS_Class.get_all_object_names()
print(objects)