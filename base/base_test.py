import pytest

from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.check_user_page import SQLI

from config.data import Data

class BaseTest:

    register_page: RegisterPage
    login_page: LoginPage
    sqli_page: SQLI
    data: Data

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):

        request.cls.driver = driver
        request.cls.data = Data()
        
        request.cls.register_page = RegisterPage(driver)
        request.cls.login_page = LoginPage(driver)
        request.cls.sqli_page = SQLI(driver)

      
    
    

