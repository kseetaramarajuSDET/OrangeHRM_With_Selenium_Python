from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from utilities.ReadConfig import ReadConfig
from utilities.customLogger import LogGen  # 1. Import your logger
import os


class BasePage:
    # 2. Initialize logger at class level
    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver
        timeout_val = ReadConfig.get_config_data('common info', 'timeout')
        timeout = int(timeout_val) if timeout_val else 10
        self.wait = WebDriverWait(self.driver, timeout)
        self.actions = ActionChains(self.driver)

    # ================= WAIT METHODS =================

    def wait_for_visible(self, locator):
        self.logger.info(f"⏳ Waiting for visibility of element: {locator}")
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.logger.error(f"❌ Element not visible within timeout: {locator}")
            raise

    def wait_for_clickable(self, locator):
        self.logger.info(f"⏳ Waiting for element to be clickable: {locator}")
        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            self.logger.error(f"❌ Element not clickable within timeout: {locator}")
            raise

    def wait_for_presence(self, locator):
        self.logger.info(f"⏳ Waiting for presence of element: {locator}")
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            self.logger.error(f"❌ Element not present in DOM: {locator}")
            raise

    # ================= ACTION METHODS =================

    def type(self, locator, text):
        # We don't log passwords for security
        log_text = "****" if "password" in str(locator).lower() else text
        self.logger.info(f"⌨️ Typing '{log_text}' into {locator}")

        element = self.wait_for_visible(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        self.logger.info(f"🖱️ Clicking on element: {locator}")
        try:
            self.wait_for_clickable(locator).click()
        except Exception as e:
            self.logger.warning(f"⚠️ Standard click failed, attempting JS Click on {locator}")
            self.js_click(locator)

    def js_click(self, locator):
        self.logger.info(f"⚡ Executing JavaScript Click on: {locator}")
        element = self.wait_for_visible(locator)
        self.driver.execute_script("arguments[0].click();", element)

    # ================= STATE CHECKS =================

    def is_displayed(self, locator):
        self.logger.info(f"🔍 Checking visibility of: {locator}")
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            self.logger.warning(f"❓ Element {locator} is not displayed.")
            return False

    # ================= NAVIGATION & UTILS =================

    def navigate_to(self, url):
        self.logger.info(f"🌐 Navigating to URL: {url}")
        self.driver.get(url)

    def upload_file(self, locator, file_relative_path):
        self.logger.info(f"📁 Attempting to upload file: {file_relative_path}")
        try:
            element = self.wait_for_presence(locator)
            absolute_path = os.path.abspath(file_relative_path)
            element.send_keys(absolute_path)
            self.logger.info(f"✅ File uploaded successfully from: {absolute_path}")
        except Exception as e:
            self.logger.error(f"❌ Failed to upload file: {str(e)}")
            raise
