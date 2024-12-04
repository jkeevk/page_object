from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

class ProductPage(BasePage):
    
    def should_be_add_product_to_cart(self):
        self.should_be_add_to_basket_button()
        link = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        link.click()
        self.solve_quiz_and_get_code()
        self.should_be_added_book_name_message()
        self.should_be_correct_book_name()
        self.should_be_correct_book_price()

    def add_to_basket(self):
        self.should_be_add_to_basket_button()
        link = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        link.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET), "Button add to basket is not on the page"

    def solve_quiz_and_get_code(self):
        WebDriverWait(self.browser, 5).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
        
    def should_be_added_book_name_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED), "product is not added to basket"
    
    def should_be_correct_book_price(self):
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET)
        price_basket_text = price_basket.text
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK)
        price_book_text = price_book.text
        print(f"basket_price: {price_basket_text}, book_price: {price_book_text}")
        assert price_basket_text == price_book_text, "the price of the product in the basket does not match the price of the product"
        
    def should_be_correct_book_name(self):
        book_name_page = self.browser.find_element(*ProductPageLocators.BOOK_NAME_PAGE)
        book_name_page_text = book_name_page.text
        book_name_message = self.browser.find_element(*ProductPageLocators.BOOK_NAME_MESSAGE)
        book_name_message_text = book_name_message.text
        print(f"book name page: {book_name_page_text}, book name message: {book_name_message_text}")
        assert book_name_page_text == book_name_message_text, "The name of the product in the message matches the added"


    def should_not_be_success_message_after_adding_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        link.click()
        assert self.is_not_element_present(*ProductPageLocators.BASKET_PRODUCT_NAME), "element visible"

    def should_not_cant_see_success_message(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        assert self.is_not_element_present(*ProductPageLocators.BASKET_PRODUCT_NAME), "element visible"
                                   
    def should_not_be_success_message_disappeared(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        link.click()
        assert self.is_disappeared(*ProductPageLocators.BASKET_PRODUCT_NAME), "element visible"