import pytest

from tests.base_test import Base_Test
from utilities.ReadConfig import ReadConfig
from utilities.YamlReader import YamlReader


class Test_Login(Base_Test):

    def test_login_with_valid_credentials(self, request):
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickOnLogin()

        status = self.dp.is_header_Dashboard_present()
        if status == True:
            assert True
        else:
            method_name = request.node.name
            self.take_screenshot(method_name)
            assert False
            print("❌ Login Failed: Dashboard header not displayed!")

    test_data = YamlReader.read_loginData_from_Yaml_File("test-data/loginData.yml")

    @pytest.mark.parametrize("user, pwd, result", test_data)
    def test_login_with_valid_And_Invalid_credentials(self, user, pwd, result, request):
        self.lp.setUserName(user)
        self.lp.setPassword(pwd)
        self.lp.clickOnLogin()

        if result == "pass":
            status = self.dp.is_header_Dashboard_present()
            if status == True:
                assert True
            else:
                method_name = request.node.name
                self.take_screenshot(method_name)
                print(f"❌ Login Failed: for User : {user} Dashboard header not displayed!")
                assert False
        elif result == "fail":
            status = self.lp.is_error_msg_displayed()
            if status == True:
                assert True
            else:
                method_name = request.node.name
                self.take_screenshot(method_name)
                print(f"❌ Failed: Expected FAILURE for {user}, but error was not shown!")
                assert False
