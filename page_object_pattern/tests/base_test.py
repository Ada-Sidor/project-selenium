import unittest
from page_object_patern.pages.Homepage import HomePage
from selenium import webdriver


class BaseTest(unittest.TestCase):
    def setUp(self):
        """Preconditions"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://carfree.pl")
        self.Homepage = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()
