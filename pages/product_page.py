from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        try:
            self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
            return True
        except NoSuchElementException:
            return False
            
    def get_product_name(self):
        try:
            return str(self.browser.find_element(*ProductPageLocators.ITEM_NAME).text)
        except NoSuchElementException:
            return None

    def check_item_name(self):
        result = self.get_success_message_after_add_product_to_basket()
        product = self.get_product_name()
        assert result == product, 'Product does not match with expected'

    def get_success_message_after_add_product_to_basket(self):
        WebDriverWait(self.browser, 20).until(expected_conditions.presence_of_element_located(ProductPageLocators.SUCCESS_MESSAGE))
        try:
            return str(self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text)
        except NoSuchElementException:
            return None


    def get_price(self):
        try:
            return str(self.browser.find_element(*ProductPageLocators.PRICE).text)
        except NoSuchElementException:
            return None

    def get_price_from_message(self):
        WebDriverWait(self.browser, 20).until(expected_conditions.presence_of_element_located(ProductPageLocators.PRICE_MESSAGE))
        try:
            return str(self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE).text)
        except NoSuchElementException:
            return None

    def check_price(self):
        price = self.get_price()
        price_message = self.get_price_from_message()
        assert price == price_message, 'Price does not match with expected'