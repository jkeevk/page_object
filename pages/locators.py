from selenium.webdriver.common.by import By


class ProductPageLocators:
    PROMO = '?promo=newYear'
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ALERT = (By.CSS_SELECTOR, '.alertinner')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'h1')
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, '.alertinner:nth-child(2) strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    ALERT_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")