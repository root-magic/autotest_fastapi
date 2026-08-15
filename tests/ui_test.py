import allure
from base.base_test import BaseTest
import pytest


@allure.feature("Testing functions")
class TestSite(BaseTest):

    @allure.title("Testing auth and sqli endpoints")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_auth(self):

        self.register_page.open()
        self.register_page.is_opened()
        self.register_page.register_user(self.data.username, self.data.password)
        

        self.register_page.open()
        self.register_page.is_opened()
        self.register_page.existing_user(self.data.username, self.data.password)

        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.login_user(self.data.username, self.data.password)

       

    def test_sqli(self):

        self.register_page.open()
        self.register_page.is_opened()
        self.register_page.register_user(self.data.username, self.data.password)

        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.login_user(self.data.username, self.data.password)
        jwt_token = self.login_page.get_jwt_from_cookie()
        print("JWT:", jwt_token)


        self.sqli_page.open()
        self.sqli_page.is_opened()
        result = self.sqli_page.sqli_test("' OR 1=1--")

        self.sqli_page.make_screen("sqli")

        print(result)
        assert result["match"] is True, f"Injection doesnt worked: {result}" 
       

