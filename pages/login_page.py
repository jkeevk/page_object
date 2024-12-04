from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login link is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_REG), "Login registration is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL)
        email_field.send_keys(email)
        password1 = self.browser.find_element(*LoginPageLocators.PWD_REG)
        password1.send_keys(password)
        password2 = self.browser.find_element(*LoginPageLocators.PWD_REG_CONFIRM)
        password2.send_keys(password)
        btn_reg = self.browser.find_element(*LoginPageLocators.BUTTON_REG)
        btn_reg.click()