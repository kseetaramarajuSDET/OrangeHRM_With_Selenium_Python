import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.DashBoardPage import DashboardPage
from pages.JobPage import JobPage
from utilities.ReadConfig import ReadConfig
from pages.LoginPage import LoginPage
from utilities.customLogger import LogGen  # Import your logger utility
from selenium.webdriver.chrome.options import Options

# Initialize the logger for the conftest level
logger = LogGen.loggen()


@pytest.fixture(scope="function")
def setup(request):
    driver = None
    logger.info("--------- Starting WebDriver Setup ---------")

    try:
        # 1. Add Chrome Options to handle renderer lag

        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--headless")

        # 1️⃣ Create browser
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        logger.info("Chrome Driver launched successfully.")

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
        if driver is not None:
            driver.quit()
        raise e

    finally:
        if driver is not None:
            logger.info("Quitting WebDriver and closing browser.")
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
