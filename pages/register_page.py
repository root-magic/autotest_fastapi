import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

import time
class RegisterPage(BasePage):

    PAGE_URL = Links.REGISTER_PAGE

    USERNAME_FIELD = ("xpath", "//input[@name='name']")
    PASSWORD_FIELD = ("xpath", "//input[@name='password']")

    ERR_MSG = ("xpath", "//div[@id='wrapper']/p")
    SUBMIT_BTN = ("xpath", "//button[@type='submit']")


    @allure.step("Register user")
    def register_user(self, username, password):

        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(username)
       
        
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)
       
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BTN)).click()
       
        self.wait.until(EC.url_to_be(Links.LOGIN_PAGE))

        
    def existing_user(self, username, password):

        with allure.step(f"User - {username} is exist"):

            self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(username)
            self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

            self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BTN)).click()


            self.wait.until(EC.text_to_be_present_in_element(self.ERR_MSG, 'User is already exist'))



