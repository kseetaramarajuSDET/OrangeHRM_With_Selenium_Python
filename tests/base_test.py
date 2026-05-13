import pytest

from utilities.ReadConfig import ReadConfig
import os
from datetime import datetime


@pytest.mark.usefixtures("setup", "init_pages")
class Base_Test:
    # Getting the data from config file
    username = ReadConfig.get_config_data("common info", "username")
    password = ReadConfig.get_config_data("common info", "password")

    def take_screenshot(self, method_name):
        # Create screenshots folder if it doesn't exist
        if not os.path.exists("ScreenShots"):
            os.makedirs("ScreenShots")

        # Create a unique filename using timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_path = f"ScreenShots/{method_name}_{timestamp}.png"

        self.driver.save_screenshot(file_path)
        print(f"📸 Screenshot saved at: {file_path}")
