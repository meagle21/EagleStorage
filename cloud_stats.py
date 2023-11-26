import pandas as pd

class Cloud_Stats:

    def __init__(self, s3_data):
        self.ALL_DATA = s3_data

    def get_all_data(self):
        return self.ALL_DATA