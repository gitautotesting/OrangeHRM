import time

import pytest

from PageObject.LoginPage import LoginPage
from TestCase.conftest import setup
from Utilities.ReadProperties import ReadConfig
from Utilities.Loggings import LogGenerator
from Utilities import XLUtils
from selenium.webdriver.support import expected_conditions as ec


class Test_Login_DDT:
    url = ReadConfig.application_url()
    filename = 'D:\\Classes\\Framework_Practice\\Test_data\\Login_Data.xlsx'
    sheetname = 'Logindata'
    # username = ReadConfig.get_username()
    # password = ReadConfig.get_password()
    log = LogGenerator.loggen()
    result_lst = []

    @pytest.mark.regression
    def test_login_DDT_001(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.log.info('*****************  test_login_DDT_001  *****************')
        time.sleep(3)
        self.lp = LoginPage(self.driver)
        row_count = XLUtils.getrowcount(self.filename, self.sheetname)
        print('The Total number of rows is : ', row_count)

        for r in range(2, row_count+1):
            username = XLUtils.readdata(self.filename, self.sheetname, r, 1)
            password = XLUtils.readdata(self.filename, self.sheetname, r, 2)
            exp_result = XLUtils.readdata(self.filename, self.sheetname, r, 3)
            self.lp.enter_username(username)
            self.lp.enter_password(password)
            self.log.info('Entering Username as --> '+username+ ' and password as --> '+password)
            self.lp.click_login()
            time.sleep(2)

            if self.lp.login_status() == True:
                self.log.info('Login Sucessful with given credentials Username -->'+username+ 'password -->'+password )
                if exp_result == 'Pass':
                    self.log.info("++++++++++  Positive test case Passed +++++++++++++")
                    self.lp.click_profile()
                    self.lp.click_logout()
                    time.sleep(2)
                    self.result_lst.append('Pass')
                elif exp_result == 'Fail':
                    self.log.info('+++++++++ Login succesful with invalid credentials +++++++++')
                    self.lp.click_profile()
                    self.lp.click_logout()
                    time.sleep(2)
                    self.result_lst.append('Fail')

            elif self.lp.login_status() == False:
                if exp_result == 'Fail':
                    self.log.info('Logout failed with invalid credentials')
                    time.sleep(2)
                    self.result_lst.append('Pass')
                elif exp_result == 'Pass':
                    self.log.info('++++++++++ Login Failed with Valid credential ++++++++')
                    time.sleep(2)
                    self.result_lst.append('Fail')

        if 'Fail' not in self.result_lst:
            self.log.info('+++++++++++++++ The test case test_login_DDT_001 Passed')
            assert True
        else:
            self.log.error('++++++++++++Test case --- test_login_DDT_001 Failed ++++++++++++')
            assert False
        self.driver.quit()
    log.info("++++++++++ END of test_login_DDT_001 ++++++++++++")
    log.info('+++++++++ Test_Login_DDT ++++++++++++++++++')
