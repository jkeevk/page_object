
from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    
    def should_not_cant_see_basket_product(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY), "basket is not empty"

    def should_cant_see_message_not_basket_product(self):
        basket_msg = self.browser.find_element(*BasketPageLocators.BASKET_MSG)
        basket_message = basket_msg.text
        print(f"basket_message: {basket_message}")
        assert "Ваша корзина пуста" in basket_message or "Your basket is empty" in basket_message, "basket is not empty"
        
