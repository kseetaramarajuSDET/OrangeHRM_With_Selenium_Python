from pages.BasePage import BasePage
from utilities.ReadConfig import ReadConfig
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    input_username_xpath = (By.XPATH, "//input[@placeholder='Username']")
    input_password_xpath = (By.XPATH, "//input[@placeholder='Password']")
    button_login_xpath = (By.XPATH, "//button[normalize-space()='Login']")
    login_invalid_msg = (By.XPATH, "//p[text()='Invalid credentials']")

    def __init__(self, driver):
        super().__init__(driver)

    def setUserName(self, username):
        self.type(self.input_username_xpath, username)

    def setPassword(self, password):
        self.type(self.input_password_xpath, password)

    def clickOnLogin(self):
        self.click(self.button_login_xpath)

    def is_error_msg_displayed(self):
        return self.is_displayed(self.login_invalid_msg)
