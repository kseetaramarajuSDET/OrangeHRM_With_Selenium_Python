import configparser
import os

config = configparser.RawConfigParser()
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Configurations', 'config.ini'))
config.read(path)


class ReadConfig:

    @staticmethod
    def get_config_data(section, key):
        """
        A universal method to get data from any section and any key.
        """
        try:
            return config.get(section, key)
        except Exception as e:
            print(f"Error: Could not find Section: [{section}] with Key: '{key}'")
            return None
