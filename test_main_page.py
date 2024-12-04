from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page() 


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()



@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("http://selenium1py.pythonanywhere.com/") 
    yield driver
    driver.quit()

def test_login_url(driver):
    login_page = LoginPage(driver)
    login_page.should_be_login_url()

def test_login_form(driver):
    login_page = LoginPage(driver)
    login_page.should_be_login_form()
def test_register_form(driver):
    login_page = LoginPage(driver)
    login_page.should_be_register_form()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()