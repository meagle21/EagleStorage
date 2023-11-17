import os
#from dotenv import load_dotenv


class System_Tasks:

    def __init__(self):
        self.ROOT_FOLDER = os.getcwd()

    def get_root_folder(self):
        return self.ROOT_FOLDER