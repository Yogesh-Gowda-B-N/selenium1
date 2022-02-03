from seleniumwrapper1 import SeleniumWrapper
from ex_lib import read_locators
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from time import  sleep

class Homepage(SeleniumWrapper):

    homepage_locators = read_locators("homepage")
    def home_click_register(self):
        self.click_element(("link text", "Register"))
        self.click_element(self.homepage_locators["click_register"])


    def home_click_login(self):
        self.click_element(("link text", "Log in"))
        self.click_element(self.homepage_locators["click_login"])

    #positive scenario
    def is_user_logged_in(self, email):
        _xpath = f"//a[text()= '{email}']"
        for _ in range(10):
            try:
                print(f'Trying to find an element with email {email}')
                return self.driver.find_element_by_xpath(_xpath).is_displayed()
            except NoSuchElementException:
                sleep(1)
                continue
        return False