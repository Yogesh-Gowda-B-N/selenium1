from selenium.webdriver import Chrome
from time import sleep
from pytest import fixture

@fixture
def setup():
    driver = Chrome(r"C:\Users\user\PycharmProjects\training1\drivers\chromedriver")
    driver.maximize_window()
    driver.get("http://demowebshop.tricentis.com/")
    sleep(2)
    yield driver
    driver.close()