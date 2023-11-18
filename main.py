from AWS import AWS
from App import App
from system_tasks import System_Tasks

### INITIALIZE OBJECTS TO USE CUSTOM METHODS
AWS_Class = AWS()
App_Class = App()
System_Tasks = System_Tasks()

AWS_Class.upload_file("test.jpg")