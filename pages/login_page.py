import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    
    USERNAME_FIELD = ("xpath", "//input[@name='name']")
    PASSWORD_FIELD = ("xpath", "//input[@name='password']")
    SUBMIT_BTN = ("xpath", "//button[@type='submit']")

    @allure.step("Login user")
    def login_user(self, username, password):

        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(username)
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BTN)).click()

        self.wait.until(EC.url_to_be(Links.TEST_SQLI))

    
    def get_jwt_from_cookie(self, cookie_name="token"):
        cookie = self.driver.get_cookie(cookie_name)
        return cookie["value"] if cookie else None

   
        