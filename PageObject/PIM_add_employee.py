from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class PIM_page:
    button_menu_xpath = By.XPATH, '// *[ @ id = "app"] / div[1] / div[1] / header / div[1] / div[1] / i'
    button_PIM_xpath = By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='PIM']"
    button_add_emp_xpath = By.XPATH, "//button[normalize-space()='Add']"
    text_firstname_name = By.NAME, "firstName"
    text_middlename_name = By.NAME, "middleName"
    text_lastname_name = By.NAME, "lastName"
    text_empid_xpath = By.CLASS_NAME, "oxd-input"
    button_save_xpath = By.XPATH, "//button[@type='submit']"
    text_personal_details_xpath = By.XPATH, "//h6[normalize-space()='Personal Details']"

    def __init__(self, driver):
        self.driver = driver

    def clickonmenu(self):
        return self.driver.find_element(*PIM_page.button_menu_xpath).click()

    def clickonPIM(self):
        return self.driver.find_element(*PIM_page.button_PIM_xpath).click()

    def addemployee(self):
        return self.driver.find_element(*PIM_page.button_add_emp_xpath).click()

    def get_firstname(self, firstname):
        return self.driver.find_element(*PIM_page.text_firstname_name).send_keys(firstname)

    def get_middlename(self, middlename):
        return self.driver.find_element(*PIM_page.text_middlename_name).send_keys(middlename)

    def get_lastname(self, lastname):
        return self.driver.find_element(*PIM_page.text_lastname_name).send_keys(lastname)

    def get_empid(self, empid):
        return self.driver.find_element(*PIM_page.text_empid_xpath).send_keys(empid)

    def clickonsave(self):
        return self.driver.find_element(*PIM_page.button_save_xpath).click()

    def check_addemp_status(self):
        try:
            self.driver.implicitly_wait(5)
            self.driver.find_element(*PIM_page.text_personal_details_xpath)
            return True
        except ec:
            return False
