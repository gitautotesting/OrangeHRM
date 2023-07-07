import time

import pytest

from PageObject.LoginPage import LoginPage
from TestCase.conftest import setup
from Utilities.ReadProperties import ReadConfig
from Utilities.Loggings import LogGenerator


class Test_Login:
    url = ReadConfig.application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    log = LogGenerator.loggen()

    @pytest.mark.regression
    def test_pagetitle_001(self, setup):
        self.driver = setup
        self.log.info('********************** test_pagetitle_001 **********************')
        self.driver.get(self.url)
        self.log.info('Opening url --->'+self.url)
        self.driver.maximize_window()
        time.sleep(2)
        act_title = self.driver.title
        if act_title == 'OrangeHRM':
            self.driver.close()
            self.log.info('Page title is matched  ' + act_title + '   ***** test_pagetitle_001 Passed *****')
            assert True
        else:
            self.driver.save_screenshot("D:\\Classes\\Framework_Practice\\Screenshots\\test_pagetitle_001.png")
            self.driver.close()
            self.log.error('Page title is does not matched   ' + act_title + '   ***** test_pagetitle_001 Failed *****')
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_002(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.log.info('*****************  test_login_002 *****************')
        time.sleep(3)
        lp = LoginPage(self.driver)
        lp.enter_username(self.username)
        self.log.info('Username --->   ' + self.username + '   ---entered')
        lp.enter_password(self.password)
        self.log.info('Password --->   ' + self.password + '  ---entered')
        time.sleep(3)
        lp.click_login()
        self.log.info('Clicked on Login Button')
        time.sleep(2)
        if lp.login_status():
            self.driver.close()
            self.log.info('Login Succesfull and *** test_login_002 Passed ***')
            assert True
        else:
            self.driver.save_screenshot("D:\\Classes\\Framework_Practice\\Screenshots\\test_login_002.png")
            self.driver.close()
            self.log.error('Login Failed and *** test_login_002 Failed ***')
            assert False


