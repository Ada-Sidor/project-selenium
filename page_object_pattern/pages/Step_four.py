from selenium.webdriver.support.wait import WebDriverWait
from page_object_patern.pages.Base_page import BasePage
import unittest


class ReservationStepFour(BasePage, unittest.TestCase):
    """Page reservation step four"""

    def __init__(self, driver):
        super().__init__(driver)

    def _verify_page(self):
        WebDriverWait(self.driver, 3)

    def assert_h1(self):
        """Assert for navigation to the next page"""
        expected_url_prefix = "https://carfree.pl/pl/rezerwacja-krok4/"
        current_url = self.driver.current_url
        assert expected_url_prefix in current_url, f"Assertion error: Expected URL '{expected_url_prefix}' was not found."
        print(f"Assertion pass: Expected URL '{expected_url_prefix}' was found.")
