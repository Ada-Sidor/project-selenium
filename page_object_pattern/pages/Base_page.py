from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert


class BasePage:
    """Base class"""
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(driver, 10)
        self._verify_page_()
        self.alert = Alert(self.driver)

    def _verify_page_(self):
        """This method verifies that we are on the correct page."""
        return
