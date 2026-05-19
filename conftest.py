import os

import pytest
from selenium import webdriver
# Import specific services
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from pages.DashBoardPage import DashboardPage
from pages.JobPage import JobPage
from utilities.ReadConfig import ReadConfig
from pages.LoginPage import LoginPage
from utilities.customLogger import LogGen  # Import your logger utility
from selenium.webdriver.chrome.options import Options

# Initialize the logger for the conftest level
logger = LogGen.loggen()


# This hook adds the custom --browser argument to the pytest command
def pytest_addoption(parser):
    logger.info("--------- Addoption Hook Running  ---------")
    parser.addoption("--browser", action="store", default="chrome",
                     help="Type in browser: chrome or firefox or edge")


@pytest.fixture(scope="function")
def setup(request):
    # Retrieve the browser name from the command line
    browser_name = request.config.getoption("--browser").lower()
    driver = None
    logger.info("--------- Starting WebDriver Setup ---------")
    logger.info(f"--------- Initializing {browser_name} browser ---------")

    # if browser_name == "edge":
    #     # Force webdriver-manager to ignore the internet entirely
    #     os.environ['WDM_LOCAL'] = '1'
    #     # Optional: Disable SSL verification if it's a proxy issue
    #     os.environ['WDM_SSL_VERIFY'] = '0'

    try:
        # 1️⃣ Create browser
        if browser_name == "chrome":
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)
        elif browser_name == "firefox":
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service)
        elif browser_name == "edge":
            try:
                # 1. Attempt automated download first
                service = EdgeService(EdgeChromiumDriverManager().install())
                driver = webdriver.Edge(service=service)
            except Exception as e:
                logger.warning("⚠️ Network block detected! Switching to the local manual driver fallback.")
                # 2. Local Fallback pointing directly to your new folder
                local_driver_path = os.path.abspath("./drivers/msedgedriver.exe")

                if not os.path.exists(local_driver_path):
                    logger.error(f"❌ Manual setup failed: msedgedriver.exe is missing at {local_driver_path}")
                    raise FileNotFoundError(f"Please check if msedgedriver.exe is in the drivers folder!")

                service = EdgeService(executable_path=local_driver_path)
                driver = webdriver.Edge(service=service)
        else:
            logger.warning(f"Browser '{browser_name}' not recognized. Launching Chrome as default.")
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)

        # 1. Add Chrome Options to handle renderer lag

        # chrome_options = Options()
        # chrome_options.add_argument("--disable-notifications")
        # chrome_options.add_argument("--disable-gpu")
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--headless")

        # 2️⃣ Browser configurations
        timeout = int(ReadConfig.get_config_data('common info', 'timeout'))
        driver.implicitly_wait(timeout)
        driver.set_page_load_timeout(30)
        driver.delete_all_cookies()
        logger.info(f"Browser configured with implicit wait: {timeout}s")

        # 3️⃣ Launch application
        base_url = ReadConfig.get_config_data('common info', 'baseURL')
        logger.info(f"Opening Application URL: {base_url}")
        driver.get(base_url)
        driver.maximize_window()
        logger.info("Browser window maximized.")

        # 4️⃣ Pass driver to the test class
        if request.cls is not None:
            request.cls.driver = driver

        yield driver

    except Exception as e:
        logger.error(f"Failed to initialize WebDriver: {str(e)}")
        raise e

    finally:
        if driver is not None:
            logger.info("Quitting WebDriver and closing browser.")
            logger.info(f"--------- {browser_name} Browser Closed ---------")
            driver.quit()
        logger.info("--------- WebDriver Setup Completed ---------")


@pytest.fixture(scope="function")
def init_pages(request, setup):
    """
    Initializes Page Objects and logs the initialization process.
    """
    logger.info(" ********** Initializing Page Objects **********")

    # This only initializes pages related to Job Pages
    request.cls.lp = LoginPage(setup)
    request.cls.dp = DashboardPage(setup)
    request.cls.jp = JobPage(setup)

    logger.info("Page Objects initialized and attached to the class instance.")
