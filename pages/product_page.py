from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoAlertPresentException 
import math
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage): 

    def add_product_to_cart(self):
        # self.should_have_promo_in_url()
        self.should_be_basket_button()
        self.click_add_to_cart_button()
        self.solve_quiz_and_get_code()
        self.should_have_success_alert()
        self.product_name_should_match_the_one_added()
        self.product_price_should_match_original_product_price()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def success_message_should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is not disappeared"

    def should_have_promo_in_url(self):
        """Проверка наличия промо-кода в URL."""
        assert ProductPageLocators.PROMO in self.browser.current_url, \
            'Promo code "newYear" is missing'

    def should_be_basket_button(self):
        """Проверка наличия кнопки корзины на странице."""
        basket_button = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ProductPageLocators.BASKET_LINK)
        )
        assert basket_button.is_displayed(), "Basket button is not displayed"


    def click_add_to_cart_button(self):
        """Нажатие на кнопку добавления в корзину."""
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        add_to_cart_button.click()


    def should_have_success_alert(self):
        """Проверка наличия уведомления об успешном добавлении в корзину."""
        assert self.is_element_present(*ProductPageLocators.ALERT), \
            'Alert is not presented'
        
    def product_name_should_match_the_one_added(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        alert_product_name = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME).text
        assert product_name == alert_product_name, \
            'Product name doesn\'t match the one added to cart'

    def product_price_should_match_original_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        alert_product_price = self.browser.find_element(*ProductPageLocators.ALERT_PRICE).text
        assert product_price == alert_product_price, \
            'Product price doesn\'t match original product price'

    def solve_quiz_and_get_code(self):
        """Решение капчи и получение кода."""
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