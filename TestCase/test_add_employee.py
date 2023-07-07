import random
import string
import time
import pytest

from PageObject.PIM_add_employee import PIM_page
from Utilities.ReadProperties import ReadConfig
from Utilities.Loggings import LogGenerator
from PageObject.LoginPage import LoginPage
from PageObject.PIM_add_employee import PIM_page


# ************** To Generate random Data ******************
def random_generator(size=3, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class Test_add_employee:
    url = ReadConfig.application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    firstname = ReadConfig.get_firstname()
    middlename = ReadConfig.get_middlename()
    lastname = ReadConfig.get_lastname()
    emp_id = random_generator()

    log = LogGenerator.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_add_employee_003(self, setup):
        self.log.info("******** test_add_employee_003 started ***********")
        self.driver = setup
        self.driver.get(self.url)
        time.sleep(5)
        self.log.info('**** Opening Url ***** ')
        self.lp = LoginPage(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.log.info(f"Entered the username as {self.username} and password as {self.password}")
        self.lp.click_login()
        time.sleep(3)
        self.log.info('Login Sucessfull')

        self.ae = PIM_page(self.driver)
        # self.ae.clickonmenu()
        # self.log.info('***** Clicked on Menu button ********')
        self.ae.clickonPIM()
        time.sleep(2)
        self.log.info("****** Clicked on PIM Tab *******")
        self.ae.addemployee()
        time.sleep(2)
        self.log.info("****** Clicked on Add button  *******")
        self.ae.get_firstname(self.firstname)
        self.ae.get_middlename(self.middlename)
        self.ae.get_lastname(self.lastname)
        self.ae.get_empid(self.emp_id)
        print(self.emp_id)
        self.log.info(f'***** Employee details filled ***** {self.firstname} -- {self.middlename} -- {self.lastname} -- {self.emp_id}')
        self.ae.clickonsave()
        time.sleep(2)

        if self.ae.check_addemp_status() == True:
            self.log.info('****Employee added sucesfully ******')
            assert True
        else:
            self.log.error("Employee details not added succesfully")
            self.driver.save_screenshot("D:\\Classes\\Framework_Practice\\Screenshots\\test_add_employee_003.png")
            time.sleep(2)
            assert False
        self.driver.close()





