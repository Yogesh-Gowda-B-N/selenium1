from Homepage import Homepage
from ex_lib import read_locators
class LoginPage(Homepage):

    login_locators = read_locators('loginpage')

    def login_enter_email(self, email):
        # self.element_text(("id", "Email"), email)
        self.element_text(self.login_locators["txt_email"], email)
    def login_enter_password(self, password):
        # self.element_text(("id", "Password"), password)
        self.element_text(self.login_locators["txt_password"], password)
    def login_click_login(self):
        # self.click_element(("xpath", "//input[@value='Log in']"))
        self.click_element(self.login_locators["btn_login"])