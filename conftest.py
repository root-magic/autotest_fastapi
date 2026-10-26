from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options as ChromeOptions



@pytest.fixture(scope="function", autouse=True)
def driver(request):

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()

