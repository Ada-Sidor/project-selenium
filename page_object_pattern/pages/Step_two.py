from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from page_object_patern.pages.Base_page import BasePage
from page_object_patern.pages.Step_three import ReservationStepThree
import unittest
from selenium.webdriver.support import expected_conditions as ec
from page_object_patern.helpers.helpers import ScreenshotMaker


class Locators:
    """Locators reservation step two"""

    """Options protection package"""
    Option_0 = (By.ID, "o_0")
    Option_1 = (By.ID, "o_1")
    Option_2 = (By.ID, "o_2")
    Option_3 = (By.ID, "o_3")

    """Additional options"""
    Option_4 = (By.XPATH, "//*[@id='optionBox_4']//div[text()='+']")
    Option_5 = (By.XPATH, "//*[@id='optionBox_5']//div[text()='+']")
    Option_6 = (By.XPATH, "//*[@id='optionBox_6']//div[text()='+']")
    Option_7 = (By.XPATH, "//*[@id='optionBox_7']//div[text()='+']")
    Option_8 = (By.ID, "o_8")
    Option_9 = (By.ID, "o_9")
    Option_10 = (By.ID, "o_10")
    Option_11 = (By.ID, "o_11")
    Option_12 = (By.ID, "o_12")

    """Options payment method"""
    Payment_1 = (By.ID, "payment_1")
    Payment_2 = (By.CSS_SELECTOR, "input[type='radio'][value='2'][name='platnosc']")
    Payment_3 = (
        By.XPATH,
        f'//input[@name="platnosc" and @value="3" and following-sibling::label[text()="przelew tradycyjny"]]')

    """Go to the next page or return to the previous page"""
    step_3_button = (By.XPATH, "//*[@id='krok2-next']//input")
    step_one_back = (By.XPATH, "//*[@id='reserve-form']//button")


class ReservationStepTwo(BasePage, unittest.TestCase):
    """Page reservation step two"""
    def _verify_page(self): WebDriverWait(self.driver, 3)

    def select_additional_options(self):
        """Select insurance package."""
        self.driver.find_element(*Locators.Option_2).click()
        """Select additional options."""
        self.driver.find_element(*Locators.Option_4).click()
        self.driver.find_element(*Locators.Option_5).click()
        self.driver.find_element(*Locators.Option_6).click()
        self.driver.find_element(*Locators.Option_7).click()
        checkbox1 = self.driver.find_element(*Locators.Option_8)
        self.driver.execute_script("arguments[0].click();", checkbox1)
        checkbox2 = self.driver.find_element(*Locators.Option_9)
        self.driver.execute_script("arguments[0].click();", checkbox2)
        checkbox3 = self.driver.find_element(*Locators.Option_10)
        self.driver.execute_script("arguments[0].click();", checkbox3)
        checkbox4 = self.driver.find_element(*Locators.Option_11)
        self.driver.execute_script("arguments[0].click();", checkbox4)
        checkbox5 = self.driver.find_element(*Locators.Option_12)
        self.driver.execute_script("arguments[0].click();", checkbox5)

    def payments_options(self):
        """Select payment option"""
        self.driver.find_element(*Locators.Payment_2).click()

    def submit_step_two(self):
        """"Click the button to proceed to the next reservation step"""
        self.driver.find_element(*Locators.step_3_button).click()
        return ReservationStepThree(self.driver)

    def click_back(self):
        """Click the button to proceed to the previous reservation step."""
        self.driver.find_element(*Locators.step_one_back).click()
        pass

    def assert_empty_payment_option(self):
        """Asserts for an empty payment option."""
        expected_url_prefix = "https://carfree.pl/pl/rezerwacja-krok2/"
        current_url = self.driver.current_url
        assert expected_url_prefix in current_url, (
            f"Assertion error: Expected URL '{expected_url_prefix}' "
            f"was not found."
        )
        print(f"Assertion pass: Expected URL '{expected_url_prefix}' was found.")

    def assert_empty_insurance_option(self):
        """Assertions for not selecting an insurance option."""
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(ec.alert_is_present())
        expected_message = "Aby kontynuować musisz wybrać swój Pakiet Ochronny."
        assert expected_message in alert.text, (
            f"Assertion error: Expected message '{expected_message}' "
            "was not found in the alert."
        )
        print(f"Assertion pass: Expected message '{expected_message}' was found in the alert.")
        alert.accept()

    def make_screenshot(self, screenshot_path):
        """Captures a screenshot of the current page and saves it to the specified 'screenshot_path'."""
        self.screenshot_maker = ScreenshotMaker(self.driver)
        self.screenshot_maker.save_screenshot(screenshot_path)
