from pages.product_page import ProductPage
import pytest


# @pytest.mark.parametrize(
#     "link",
#     [
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#         pytest.param(
#             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#             marks=pytest.mark.xfail,
#         ),
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
#     ],
# )
# def test_guest_can_add_product_to_basket(browser, link):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.add_product_to_cart()

# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"): 
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.add_product_to_cart()
#     product_page.should_not_be_success_message()

# def test_guest_cant_see_success_message(browser, link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"): 
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.should_not_be_success_message() 
    
# def test_message_disappeared_after_adding_product_to_basket(browser, link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"): 
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.add_product_to_cart()
#     product_page.success_message_should_be_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()