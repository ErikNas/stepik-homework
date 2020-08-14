import pytest
import time
from selenium import webdriver


class TestShop:

    def is_element_present(self, browser):
        try:
            browser.implicitly_wait(10)
            browser.find_element_by_css_selector(".btn-add-to-basket")
            return True
        except:
            return False

    def test_check_basket_button(self, browser):

        browser.get(
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        time.sleep(30)
        assert self.is_element_present(browser) == True, "basket button not found"
