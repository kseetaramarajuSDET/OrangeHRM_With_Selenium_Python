import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.DashBoardPage import DashboardPage
from utilities.ReadConfig import ReadConfig
from pages.LoginPage import LoginPage


@pytest.fixture(scope="function")
def setup(request):
    driver = None

    try:
        # 1️⃣ Create browser (Initializing WebDriver)
        # You can add logic here to choose browser from config later
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        print(" Chrome Driver Launched Successfully !! ")

        # 2️⃣ Browser configurations
        # Taking timeout from config using your universal method
        timeout = int(ReadConfig.get_config_data('common info', 'timeout'))
        driver.implicitly_wait(timeout)

        driver.set_page_load_timeout(30)

        driver.delete_all_cookies()

        # 3️⃣ Launch application
        base_url = ReadConfig.get_config_data('common info', 'baseURL')
        driver.get(base_url)
        print(" URL Launched Successfully !! ")
        driver.maximize_window()

        # 4️⃣ Pass driver to the test class (Like DriverManager)
        if request.cls is not None:
            request.cls.driver = driver

        # --- THE TEST RUNS HERE ---
        yield driver
        # --------------------------

    except Exception as e:
        if driver is not None:
            driver.quit()
        raise e

    finally:
        # 🛑 Only quit if driver was actually initialized
        if driver is not None:
            driver.quit()


@pytest.fixture(scope="function")
def init_login_pages(request, setup):
    # This only initializes pages related to Login/Dashboard
    request.cls.lp = LoginPage(setup)
    request.cls.dp = DashboardPage(setup)
