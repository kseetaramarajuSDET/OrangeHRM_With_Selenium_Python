import pytest
from utilities.ReadConfig import ReadConfig
import os
from datetime import datetime
from utilities.customLogger import LogGen


@pytest.mark.usefixtures("setup", "init_pages")
class Base_Test:
    # Initialize the logger once for the whole class
    # This is a class-level logger shared by all inheriting test classes
    logger = LogGen.loggen()

    # Getting the data from config file
    username = ReadConfig.get_config_data("common info", "username")
    password = ReadConfig.get_config_data("common info", "password")

    def take_screenshot(self, method_name):
        """
        Captures a screenshot and records the event in the automation logs.
        """
        self.logger.info(f"📸 Attempting to capture screenshot for method: {method_name}")

        try:
            # Create screenshots folder if it doesn't exist
            if not os.path.exists("ScreenShots"):
                os.makedirs("ScreenShots")
                self.logger.info("Directory 'ScreenShots' created successfully.")

            # Create a unique filename using timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_path = f"ScreenShots/{method_name}_{timestamp}.png"

            # Perform the screenshot capture
            self.driver.save_screenshot(file_path)

            # Log the success
            self.logger.info(f"✅ Screenshot successfully saved at: {file_path}")

        except Exception as e:
            # Log any failure that occurs during the screenshot process
            self.logger.error(f"❌ Failed to capture screenshot for {method_name}. Exception: {str(e)}")
