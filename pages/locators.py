from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_EMPTY = (By.CSS_SELECTOR, ".basket_items")
    BASKET_MSG = (By.CSS_SELECTOR, "#content_inner p")
    SEE_BASKET = (By.CSS_SELECTOR, ".btn-group a")
    

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    FORM_REG = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PWD_REG = (By.CSS_SELECTOR, "#id_registration-password1")
    PWD_REG_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REG = (By.NAME,"registration_submit")

class ProductPageLocators():
    ADD_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_ADDED = (By.CLASS_NAME, "alertinner")
    PRICE_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")
    PRICE_BOOK = (By.CSS_SELECTOR, ".product_main .price_color")
    BOOK_NAME_PAGE = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_NAME_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > div:nth-of-type(1) strong")
    