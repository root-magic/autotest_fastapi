import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

import json

class SQLI(BasePage):

    PAGE_URL = Links.TEST_SQLI

    USER_CHECK_FIELD = ("xpath", "//input[@name='input']")
    SUBMIT_BTN = ("xpath", "//input[@type='submit']")

    @allure.step("Sqli test")
    def sqli_test(self, payload):

        self.wait.until(EC.element_to_be_clickable(self.USER_CHECK_FIELD)).send_keys(payload)
        

        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BTN)).click()


        body = self.wait.until(EC.visibility_of_element_located(("tag name", "body")))
        response_text = body.text

        return json.loads(response_text)