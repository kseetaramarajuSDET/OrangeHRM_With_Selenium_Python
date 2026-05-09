import pytest
from utilities.ReadConfig import ReadConfig
from utilities.YamlReader import YamlReader


@pytest.mark.usefixtures("setup", "init_login_pages")
class Test_Login:
    # Getting the data from config file
    baseURL = ReadConfig.get_config_data("common info", "baseURL")
    username = ReadConfig.get_config_data("common info", "username")
    password = ReadConfig.get_config_data("common info", "password")

    def test_login_with_valid_credentials(self):
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickOnLogin()

        status = self.dp.is_header_Dashboard_present()
        assert status == True, "❌ Login Failed: Dashboard header not displayed!"

    test_data = YamlReader.read_loginData_from_Yaml_File("test-data/loginData.yml")

    @pytest.mark.parametrize("user, pwd, result", test_data)
    def test_login_with_valid_And_Invalid_credentials(self, user, pwd, result):
        self.lp.setUserName(user)
        self.lp.setPassword(pwd)
        self.lp.clickOnLogin()

        if result == "pass":
            status = self.dp.is_header_Dashboard_present()
            assert status == True, f"❌ Login Failed: for User : {user} Dashboard header not displayed!"
        elif result == "fail":
            status = self.lp.is_error_msg_displayed()
            assert status == True, f"❌ Failed: Expected FAILURE for {user}, but error was not shown!"
