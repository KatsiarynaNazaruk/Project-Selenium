import pytest
import random

from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
from .pages.locators import ProductPageLocators
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    item_page = ProductPage(browser, link)
    item_page.open()
    item_page.add_to_basket()
    # item_page.solve_quiz_and_get_code()
    item_page.check_item_name()
    item_page.check_price()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    basket_page = BasketPage(browser, link)
    basket_page.open()
    basket_page.open_basket()
    basket_page.is_basket_empty()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    item_page = ProductPage(browser, link)
    item_page.open()
    item_page.add_to_basket()
    item_page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        chislo = random.randint(
            0, 1000
        )  # генерация случайного числа для логина и пароля пользователя
        email = (
            "email" + str(chislo * chislo) + "@email" + str(chislo) + ".com"
        )  # генерация логина
        password = "qwe123qwe" + str(chislo * chislo)  # генерация пароля
        page_login = LoginPage(browser, link)
        page_login.open()
        page_login.register_new_user(email, password)
        page_base = BasePage(browser, link)
        page_base.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        item_page = ProductPage(browser, link)
        item_page.open()
        item_page.add_to_basket()
        item_page.check_item_name()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        item_page = ProductPage(browser, link)
        item_page.open()
        item_page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
