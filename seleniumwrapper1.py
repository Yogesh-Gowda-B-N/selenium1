from wait import wait


class SeleniumWrapper:
    def __init__(self, driver):
        self.driver = driver

    @wait
    def element_text(self, locator, value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    @wait
    def click_element(self, locator):
        self.driver.find_element(*locator).click()