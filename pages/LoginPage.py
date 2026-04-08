from utilities.ReadConfig import ReadConfig


class LoginPage:
    input_username_xpath = "//input[@placeholder='Username']"
    input_password_xpath = "//input[@placeholder='Password']"
    button_login_xpath = "//button[normalize-space()='Login']"

    # Getting the data from config file
    baseURL = ReadConfig.get_config_data("common info", "baseURL")
    username = ReadConfig.get_config_data("common info", "username")
    password = ReadConfig.get_config_data("common info", "password")

    def __init__(self, driver):
        self.driver = driver
