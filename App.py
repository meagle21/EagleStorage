#import eel
from system_tasks import System_Tasks

class App:

    def __init__(self):
        self.SYSTEM_TASKS = System_Tasks()
        self.WEB_APP_FOLDER = self.SYSTEM_TASKS.get_root_folder() + "\\" + "WebApp"
        #eel.init(self.WEB_APP_FOLDER0)

    def get_web_app_folder(self):
        return self.WEB_APP_FOLDER
