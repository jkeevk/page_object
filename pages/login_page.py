from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import LoginPageLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Проверка, что URL содержит 'login'."""
        current_url = self.driver.current_url
        assert "login" in current_url, f"Expected 'login' in URL, but got {current_url}"

    def should_be_login_form(self):
        """Проверка наличия формы логина на странице."""
        login_form = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.LOGIN_FORM)
        )
        assert login_form.is_displayed(), "Login form is not displayed"

    def should_be_register_form(self):
        """Проверка наличия формы регистрации на странице."""
        register_form = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.REGISTER_FORM)
        )
        assert register_form.is_displayed(), "Register form is not displayed"