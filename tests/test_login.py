import pytest
from selenium import webdriver

from pages.LoginPage import LoginPage
from utilities.ReadConfig import ReadConfig
from selenium.webdriver import WebDriver

class LoginTest():
    # Getting the data from config file
    baseURL = ReadConfig.get_config_data("common info", "baseURL")
    username = ReadConfig.get_config_data("common info", "username")
    password = ReadConfig.get_config_data("common info", "password")

    def test_login_with_valid_credentials(self):

