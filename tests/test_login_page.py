import pytest
from tests.base_test import Base_Test
from utilities.ExcelReaderUtility import ExcelReader
from utilities.ReadConfig import ReadConfig
from utilities.YamlReader import YamlReader


class Test_Login(Base_Test):

    def test_login_with_valid_credentials(self, request):
        self.logger.info("**** Starting: test_login_with_valid_credentials ****")

        self.logger.info(f"Entering username: {self.username}")
        self.lp.setUserName(self.username)

        self.logger.info(f"Entering password : {self.password}")
        self.lp.setPassword(self.password)

        self.logger.info("Clicking on Login button")
        self.lp.clickOnLogin()

        status = self.dp.is_header_Dashboard_present()

        if status:
            self.logger.info("✅ Login successful: Dashboard header displayed")
            assert True
        else:
            method_name = request.node.name
            self.take_screenshot(method_name)
            self.logger.error("❌ Login Failed: Dashboard header not found!")
            assert False

        self.logger.info("**** Finished: test_login_with_valid_credentials ****")

    test_data = YamlReader.read_loginData_from_Yaml_File("test-data/loginData.yml")

    @pytest.mark.parametrize("user, pwd, result", test_data)
    def test_login_with_valid_And_Invalid_credentials(self, user, pwd, result, request):
        self.logger.info(f"**** Starting Data Driven Test: User={user}, Expected={result} ****")

        self.lp.setUserName(user)
        self.lp.setPassword(pwd)
        self.lp.clickOnLogin()

        if result == "pass":
            status = self.dp.is_header_Dashboard_present()
            if status:
                self.logger.info(f"✅ Pass: Login worked as expected for user: {user}")
                assert True
            else:
                method_name = request.node.name
                self.take_screenshot(method_name)
                self.logger.error(f"❌ Fail: Expected SUCCESS but login failed for: {user}")
                assert False

        elif result == "fail":
            status = self.lp.is_error_msg_displayed()
            if status:
                self.logger.info(f"✅ Pass: Correctly showed error for invalid user: {user}")
                assert True
            else:
                method_name = request.node.name
                self.take_screenshot(method_name)
                self.logger.error(f"❌ Fail: Expected error message for {user} was NOT displayed")
                assert False

        self.logger.info("**** Finished Data Driven Test Case ****")

    # 1. Fetch data arrays from Excel dynamically
    # Passes file name and specific sheet tab name
    excel_data = ExcelReader.get_data_from_excel("Login_Data_Excel.xlsx", "Sheet1")

    @pytest.mark.parametrize("user, pwd, result", excel_data)
    def test_login_with_valid_And_Invalid_credentials(self, user, pwd, result, request):
        self.logger.info(f"**** Starting Data Driven Test: User={user}, Expected={result} ****")

        self.lp.setUserName(user)
        self.lp.setPassword(pwd)
        self.lp.clickOnLogin()

        if result == "pass":
            status = self.dp.is_header_Dashboard_present()
            if status:
                self.logger.info(f"✅ Pass: Login worked as expected for user: {user}")
                assert True
            else:
                method_name = request.node.name
                self.take_screenshot(method_name)
                self.logger.error(f"❌ Fail: Expected SUCCESS but login failed for: {user}")
                assert False

        elif result == "fail":
            status = self.lp.is_error_msg_displayed()
            if status:
                self.logger.info(f"✅ Pass: Correctly showed error for invalid user: {user}")
                assert True
            else:
                method_name = request.node.name
                self.take_screenshot(method_name)
                self.logger.error(f"❌ Fail: Expected error message for {user} was NOT displayed")
                assert False

        self.logger.info("**** Finished Data Driven Test Case ****")
