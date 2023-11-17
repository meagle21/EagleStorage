import boto3

class AWS:
    
    def __init__(self):
        self.secret_access_id = ""

    def get_secret_access_id(self):
        return self.secret_access_id