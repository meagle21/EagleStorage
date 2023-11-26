import os, json

class System_Tasks:

    def __init__(self):
        self.DATA_DICT_SECRET_ACCESS_KEY_KEY = "secret_access_key_key"
        self.DATA_DICT_ACCESS_KEY_KEY = "access_key_key"
        self.S3_BUCKET_NAME_KEY = "s3_bucket_name"
        self.ROOT_FOLDER = os.getcwd()
        self.ICONS_FOLDER = rf"/static"
        self.CONFIG_FILENAME = self.set_configuration_file()
        self.CONFIG_FILE_PATH = self.set_config_file_path()
        self.FULL_CONFIG_FILE_DATA = self.set_config_file_all()
        self.CONFIG_DATA_DICT = self.set_config_data_dict_key_pairs()
        self.AWS_ACCESS_KEY_ID = self.set_aws_access_key_id()
        self.AWS_SECRET_ACCESS_KEY = self.set_aws_secret_access_key()
        self.AWS_S3_BUCKET = self.set_s3_bucket_name()
        self.AVAILABLE_FILE_TYPES = self.set_available_file_types()

    def set_configuration_file(self):
        """This method finds the configuration file in the parent folder."""
        json_file = ".json"
        files = os.listdir(self.get_root_folder())
        for file in files:
            if(os.path.splitext(file)[-1] == json_file):
                return file
        exception_message = f"There needs to be a .json configuration file in the folder: {self.get_root_folder()}!"
        raise Exception(exception_message)
    
    def get_config_data_dict(self):
        return self.CONFIG_DATA_DICT
    
    def get_data_dict_secret_access_key_key(self):
        return self.DATA_DICT_SECRET_ACCESS_KEY_KEY
    
    def get_data_dict_access_key_key(self):
        return self.DATA_DICT_ACCESS_KEY_KEY
    
    def get_data_dict_s3_bucket_name(self):
        return self.S3_BUCKET_NAME_KEY

    def set_config_data_dict_key_pairs(self):
        """Set the variables for the configuration data dictionary, this makes errors in config file more dynamic"""
        access_key_key = self.get_data_dict_access_key_key()
        secret_access_key_key = self.get_data_dict_secret_access_key_key()
        s3_bucket_name = self.get_data_dict_s3_bucket_name()
        template_dict = {access_key_key : "", 
                         secret_access_key_key : "" , 
                         s3_bucket_name : ""} 
        keys_needed = list(template_dict.keys()) #get the keys that are needed in the configuration file
        config_file = self.get_config_file_all() #read the configuration file in 
        config_file_keys = list(config_file.keys()) #get the keys that are in the configuration file
        for config_key in config_file_keys: #iterate over them
            lowered_config_key = config_key.lower() #lower case to standardize for the if statements
            if(("access_key" in lowered_config_key) and ("secret" not in lowered_config_key)): #see if there's an access key
                template_dict[access_key_key] = config_file[config_key] #if found, set it in the template dictionary
                keys_needed.remove(access_key_key) #remove from list of keys needed
            elif("secret_access_key" in lowered_config_key): #look for secret access key
                template_dict[secret_access_key_key] = config_file[config_key] #set it in the template dictionary
                keys_needed.remove(secret_access_key_key) #remove from list of keys needed
            elif("s3" in lowered_config_key): #look for s3 bucket name key
                template_dict[s3_bucket_name] = config_file[config_key] #if found, set it in the template dictionary
                keys_needed.remove(s3_bucket_name) #remove from keys needed
        if(len(keys_needed) > 0): #if the list is not empty, meaning a key was not found containing the right keywords
            keys_needed_as_string = "" #variable to store the list of keys needed to string
            for key in keys_needed: #iterate over keys needed
                keys_needed_as_string += (key + ", ") #comma deliminate
            keys_needed_as_string = keys_needed_as_string[:-2] #since the commma and space come at end of iteration, remove from the list element of the string
            exception_message = f"You are missing the following keys from your configuration file, please add: {keys_needed_as_string} to the file to continue." #generate exception
            raise Exception(exception_message) #throw exception to tell user which key they are missing in their configuration file
        else:
            return template_dict #if the keys needed list is empty, meaning all necessary keys were found, return the template dictionary to set global variable

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

    def set_aws_access_key_id(self):
        return self.get_config_data_dict()[self.get_data_dict_access_key_key()]
    
    def get_aws_access_key_id(self):
        return self.AWS_ACCESS_KEY_ID

    def set_aws_secret_access_key(self):
        return self.get_config_data_dict()[self.get_data_dict_secret_access_key_key()]

    def get_aws_secret_access_key(self):
        return self.AWS_SECRET_ACCESS_KEY

    def set_s3_bucket_name(self):
        return self.get_config_data_dict()[self.get_data_dict_s3_bucket_name()]

    def get_s3_bucket_name(self):
        return self.AWS_S3_BUCKET

    def get_aws_file_type(self, file_name):
        file_extension = os.path.splitext(file_name)[1].replace(".", "")
        if(len(file_extension) == 0):   
            file_extension = "folder"
        return file_extension
    
    def get_aws_file_parent_folder(self, file_name):
        file_name_split = file_name.split(r"/") #split the file path
        parent_folder_path = '' #this is a string that will store the praent folder once it has been found
        for potential_whitespace_element in file_name_split: #folder paths have a white space at the end, we want to remove these for the iteration
            if(len(potential_whitespace_element) == 0):
                file_name_split.remove(potential_whitespace_element)
        for split_path in file_name_split[:-1]: #for each split path in the split file name, indexing away from -1 removed te file name 
            parent_folder_path += rf"{split_path}/" #create the parent folder path as a string, excluding the filename
        return parent_folder_path[:-1] #this removes the trailing backslash
    
    def get_icons_folder_path(self):
        return self.ICONS_FOLDER

    def set_available_file_types(self):
        return os.listdir(rf"{self.get_root_folder()}/{self.get_icons_folder_path()}")
    
    def get_available_file_types(self):
        return self.AVAILABLE_FILE_TYPES

    def get_icon_path(self, file_type):
        for available_type in self.get_available_file_types():
            if(file_type in available_type.split(".")[0]):
                return rf"{self.get_icons_folder_path()}/{available_type}"
        return rf"{self.get_icons_folder_path()}/{'not_found.png'}"
        
