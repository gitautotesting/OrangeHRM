from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException as ec


class LoginPage:
    textbox_username_name = By.NAME, 'username'
    textbox_password_name = By.NAME, 'password'
    button_login_XPATH = By.XPATH, "//button[@type='submit']"
    button_profile_XPATH = By.XPATH, "//p[@class='oxd-userdropdown-name']"
    button_logout_XPATH = By.XPATH, "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*LoginPage.textbox_username_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*LoginPage.textbox_password_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(*LoginPage.button_login_XPATH).click()

    def click_profile(self):
        self.driver.find_element(*LoginPage.button_profile_XPATH).click()

    def click_logout(self):
        self.driver.find_element(*LoginPage.button_logout_XPATH).click()

    def login_status(self):
        self.driver.implicitly_wait(5)
        try:
            self.driver.find_element(*LoginPage.button_profile_XPATH)
            return True
        except ec:
            return False
