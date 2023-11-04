from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from page_object_patern.pages.Base_page import BasePage
from page_object_patern.tests.test_data import ValidData
from page_object_patern.pages.Step_two import ReservationStepTwo


class Locators:
    """Locators reservation step one"""
    type_car = (By.XPATH, f"//*[@class='katSwitchGroup']//button[text()='{ValidData.segment}']")
    car_name = (By.XPATH, f"//*[@class='carlistGrid']//div[text()='{ValidData.car}']")
    step_2_button = (By.XPATH, f"//*[@id='csLink_{ValidData.submit}']")


class ReservationStepOne(BasePage):
    """Page reservation step one"""
    def __init__(self, driver):
        super().__init__(driver)

    def car_list(self, segment, car):
        """Select the type and click on the car model."""
        self.driver.find_element(*Locators.type_car).click()
        self.driver.find_element(*Locators.car_name).click()

    def submit_step_one(self, submit):
        """"Click the button to proceed to the next reservation step"""
        self.driver.find_element(*Locators.step_2_button).click()
        return ReservationStepTwo(self.driver)
