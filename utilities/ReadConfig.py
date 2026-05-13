import configparser
import os
import logging
from utilities.customLogger import LogGen

# Initialize the parser
config = configparser.RawConfigParser()
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Configurations', 'config.ini'))
config.read(path)


class ReadConfig:
    # Initialize logger for the utility
    logger = LogGen.loggen()

    @staticmethod
    def get_config_data(section, key):
        """
        A universal method to get data from any section and any key with logging.
        """
        try:
            value = config.get(section, key)
            # Optional: Log the fetch (Avoid logging sensitive info like passwords in production)
            if "password" not in key.lower():
                ReadConfig.logger.info(f"⚙️ Config Read: [{section}] -> {key} = {value}")
            else:
                ReadConfig.logger.info(f"⚙️ Config Read: [{section}] -> {key} = ********")

            return value

        except Exception as e:
            ReadConfig.logger.error(f"❌ Configuration Error: Could not find Section: [{section}] with Key: '{key}'")
            ReadConfig.logger.error(f"Actual Exception: {str(e)}")
            return None
