import pytest
from utilities.ReadConfig import ReadConfig


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
