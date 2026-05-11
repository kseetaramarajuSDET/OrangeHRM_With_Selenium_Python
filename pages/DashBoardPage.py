from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class DashboardPage(BasePage):
    header_Dashboard_xpath = (By.XPATH, "//h6[normalize-space()='Dashboard']")
    anchor_Admin_xpath = (By.XPATH, "//span[text()='Admin']/parent::a")

    def __init__(self, driver):
        super().__init__(driver)

    def is_header_Dashboard_present(self):
        return self.is_displayed(self.header_Dashboard_xpath)

    def click_anchor_Admin(self):
        self.click(self.anchor_Admin_xpath)
