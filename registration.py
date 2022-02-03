from Homepage import Homepage
from ex_lib import read_locators
class RegistrationPage(Homepage):

    registration_locators = read_locators("registrationpage")

    def registration_select_male(self):
        # self.click_element(("id", "gender-male"))
        self.click_element(self.registration_locators["click_male"])

    def registration_select_female(self):
        # self.click_element(("id", "gender-female"))
        self.click_element(self.registration_locators["click_female"])

    def registration_enter_first_name(self, fname):
        # self.element_text(("id", "FirstName"), fname)
        self.element_text(self.registration_locators["txt_fname"], fname)

    def registration_enter_last_name(self, lname):
        # self.element_text(("id", "LastName"), lname)
        self.element_text(self.registration_locators["txt_lname"], lname)

    def registartion_enter_email(self, email):
        # self.element_text(("id", "Email"), email)
        self.element_text(self.registration_locators["txt_email"], email)

    def registration_enter_password(self, password):
        # self.element_text(("id", "Password"), password)
        self.element_text(self.registration_locators["txt_password"], password)

    def registration_enter_confirm_password(self, password):
        # self.element_text(("id", "ConfirmPassword"), password)
        self.element_text(self.registration_locators["txt_confirm"], password)

    def registration_click_register(self):
        # self.click_element(("name", "register-button"))
        self.click_element(self.registration_locators["click_register"])
