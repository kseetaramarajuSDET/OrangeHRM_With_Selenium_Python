import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utilities.ReadConfig import ReadConfig


@pytest.fixture(scope="function")
def setup(request):
    driver = None

    try:
        # 1️⃣ Create browser (Initializing WebDriver)
        # You can add logic here to choose browser from config later
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        # 2️⃣ Browser configurations
        # Taking timeout from config using your universal method
        timeout = int(ReadConfig.get_config_data('common info', 'timeout'))
        driver.implicitly_wait(timeout)

        driver.set_page_load_timeout(30)

        driver.delete_all_cookies()

        driver.maximize_window()

        # 3️⃣ Launch application
        base_url = ReadConfig.get_config_data('common info', 'baseURL')
        driver.get(base_url)

        # 4️⃣ Pass driver to the test class (Like DriverManager)
        if request.cls is not None:
            request.cls.driver = driver

        # --- THE TEST RUNS HERE ---
        yield driver
        # --------------------------

    except Exception as e:
        if driver:
            driver.quit()
        raise e

    finally:
        driver.quit()
