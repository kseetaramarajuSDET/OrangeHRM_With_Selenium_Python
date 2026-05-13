from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from utilities.ReadConfig import ReadConfig
import os


class BasePage:

    def __init__(self, driver):
        self.driver = driver

        # Get timeout from config
        timeout_val = ReadConfig.get_config_data('common info', 'timeout')
        timeout = int(timeout_val) if timeout_val else 10

        self.wait = WebDriverWait(self.driver, timeout)
        self.actions = ActionChains(self.driver)

    # ================= WAIT METHODS =================

    def wait_for_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise

    def wait_for_clickable(self, locator):
        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise

    def wait_for_presence(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise

    # ================= ACTION METHODS =================

    def type(self, locator, text):
        element = self.wait_for_visible(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        try:
            self.wait_for_clickable(locator).click()
        except Exception:
            # Fallback to JS click if normal click is intercepted
            self.js_click(locator)

    def js_click(self, locator):
        element = self.wait_for_visible(locator)
        self.driver.execute_script("arguments[0].click();", element)

    # ================= STATE CHECKS =================

    def is_displayed(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_enabled(self, locator):
        try:
            return self.wait_for_visible(locator).is_enabled()
        except Exception:
            return False

    # ================= NAVIGATION & UTILS =================

    def navigate_to(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_element(self, locator):
        # The * unpacking converts (By.ID, "val") into By.ID, "val"
        return self.driver.find_element(*locator)

    # File Uploading
    def upload_file(self, locator, file_relative_path):
        """
        Uploads a file by converting a relative path to an absolute path
        and sending it to the upload input element.
        """
        # 1. Wait for the hidden or visible input element
        # Use wait_for_presence because sometimes upload inputs are invisible
        element = self.wait_for_presence(locator)

        # 2. Get the absolute path (Selenium needs the full C:\... path)
        absolute_path = os.path.abspath(file_relative_path)

        # 3. Send the path to the element
        element.send_keys(absolute_path)
