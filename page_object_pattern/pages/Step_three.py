from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from page_object_patern.pages.Base_page import BasePage
import unittest
from selenium.webdriver.common.action_chains import ActionChains


class Locators:
    """Locators reservation step three"""
    name = (By.ID, "imie2")
    surname = (By.ID, "nazwisko2")
    email = (By.ID, "email2a")
    phone = (By.NAME, "nr_kom")
    address = (By.ID, "adres")
    city = (By.ID, "miejscowosc")
    post_code = (By.ID, "kod_poczta")
    invoice = (By.ID, "faktura")
    all_consents = (By.ID, "regx")
    submit_step_three = (By.XPATH, "//input[@value='Zarezerwuj']")
    step_two_back = (By.XPATH, "//*[@id='reserve-form']//button")
    """Locators for assert"""
    assert_data_pickup = (By.CSS_SELECTOR, ".steppesTable .stTD:nth-child(2)")
    assert_pickup_location = (By.CSS_SELECTOR, ".steppesTable .stTD:nth-child(4)")
    assert_data_return = (By.CSS_SELECTOR, ".steppesTable .stTD:nth-child(6)")
    assert_return_location = (By.CSS_SELECTOR, ".steppesTable .stTD:nth-child(8)")
    assert_additional_driver = (By.ID, "sttd_a9")
    assert_child_seat = (By.ID, "sttd_a4")
    assert_booster_seat = (By.ID, "sttd_a5")
    assert_gps = (By.ID, "sttd_a3")
    assert_dirty_return = (By.ID, "sttd_o3")
    assert_zone_1 = (By.ID, "sttd_o15")
    assert_zone_2 = (By.ID, "sttd_o16")
    assert_zone_3 = (By.ID, "sttd_o17")
    assert_insurance_price = (By.ID, "sttd_o31")
    assert_insurance_name = (By.ID, "stth_o31")
    assert_car_name = (By.XPATH, "//div[@class='car-name']/strong")


class ReservationStepThree(BasePage, unittest.TestCase):
    """Page reservation step three"""
    def _verify_page(self):
        WebDriverWait(self.driver, 3)

    def enter_name(self, name):
        """Enters name"""
        self.driver.find_element(*Locators.name).send_keys(name)

    def enter_surname(self, surname):
        """Enters surname"""
        self.driver.find_element(*Locators.surname).send_keys(surname)

    def enter_email(self, email):
        """Enters email"""
        self.driver.find_element(*Locators.email).send_keys(email)

    def enter_phone(self, phone):
        """Enters phone"""
        self.driver.find_element(*Locators.phone).send_keys(phone)

    def enter_address(self, address):
        """Enters address"""
        self.driver.find_element(*Locators.address).send_keys(address)

    def enter_city(self, city):
        """Enters city"""
        self.driver.find_element(*Locators.city).send_keys(city)

    def enter_post_code(self, post_code):
        """Enters post code"""
        self.driver.find_element(*Locators.post_code).send_keys(post_code)

    def select_invoice(self):
        """Enters invoice"""
        self.driver.find_element(*Locators.invoice).click()

    def submit_page_three(self):
        """"Click the button to proceed to the next reservation step"""
        element = self.driver.find_element(*Locators.submit_step_three)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element.click()

    def select_all_consents(self):
        """Select all consents"""
        self.driver.find_element(*Locators.all_consents).click()

    def step_two_back(self):
        """Click the button to proceed to the previous reservation step."""
        self.driver.find_element(*Locators.step_two_back).click()

    def get_element_text(self, locator):
        element = self.driver.find_element(*locator)
        return element.text

    def assert_step_home_page(self, expected_value, expected_value2, expected_value3, expected_value4):
        """Asserts for Home page reservation"""
        actual_value_data_odbioru = self.get_element_text(Locators.assert_data_pickup)
        assert actual_value_data_odbioru == expected_value, (
            f"Assertion error: Data odbioru - expected: {expected_value}, "
            f"actual: {actual_value_data_odbioru}")
        print(
            f"Assertion Homepage pass: Data odbioru - expected: {expected_value}, "
            f"actual: {actual_value_data_odbioru}")
        actual_value_miejsce_odbioru = self.get_element_text(Locators.assert_pickup_location)
        assert actual_value_miejsce_odbioru == expected_value2, (
            f"Assertion error: Miejsce odbioru - expected: {expected_value2}, "
            f"actual: {actual_value_miejsce_odbioru}")
        print(
            f"Assertion Homepage pass: Miejsce odbioru - expected: {expected_value2},"
            f"actual: {actual_value_miejsce_odbioru}")

        actual_value_data_zwrotu = self.get_element_text(Locators.assert_data_return)
        assert actual_value_data_zwrotu == expected_value3, (
            f"Assertion error: Data zwrotu - expected: {expected_value3}, "
            f"actual: {actual_value_data_zwrotu}")
        print(
            f"Assertion Homepage pass: Data zwrotu - expected: {expected_value3},"
            f"actual: {actual_value_data_zwrotu}")

        actual_value_miejsce_zwrotu = self.get_element_text(Locators.assert_return_location)
        assert actual_value_miejsce_zwrotu == expected_value4, (
            f"Assertion error: Miejsce zwrotu - expected: {expected_value4}, "
            f"actual: {actual_value_miejsce_zwrotu}")
        print(
            f"Assertion Homepage pass: Miejsce zwrotu - expected: {expected_value4},"
            f"actual: {actual_value_miejsce_zwrotu}")

    def assert_step_two_combined(self, expected_additional_driver, expected_child_seat, expected_booster_seat,
                                 expected_gps, expected_dirty_return, expected_zone_1, expected_zone_2,
                                 expected_zone_3, expected_insurance_name, expected_price_insurance):
        """Asserts for step two reservation"""
        actual_value_additional_driver = self.get_element_text(Locators.assert_additional_driver)
        if actual_value_additional_driver == expected_additional_driver:
            print(f"Assertion Step two reservation pass: Dodatkowy kierowca - expected: {expected_additional_driver}")
        else:
            print(
                f"Assertion Step two reservation error: Dodatkowy kierowca - expected: {expected_additional_driver}, "
                f"actual: {actual_value_additional_driver}")
        actual_value_child_seat = self.get_element_text(Locators.assert_child_seat)
        if actual_value_child_seat == expected_child_seat:
            print(f"Assertion Step two reservation pass: Fotelik - expected: {expected_child_seat}")
        else:
            print(
                f"Assertion Step two reservation error: Fotelik - expected: {expected_child_seat}, "
                f"actual: {actual_value_child_seat}"
            )
        actual_value_booster_seat = self.get_element_text(Locators.assert_booster_seat)
        if actual_value_booster_seat == expected_booster_seat:
            print(f"Assertion Step two reservation pass: Podkladka - expected: {expected_booster_seat}")
        else:
            print(f"Assertion Step two reservation error: Podkladka - expected: {expected_booster_seat},"
                  f"actual: {actual_value_booster_seat}")
        actual_value_gps = self.get_element_text(Locators.assert_gps)
        if actual_value_gps == expected_gps:
            print(f"Assertion Step two reservation pass: GPS - expected: {expected_gps}")
        else:
            print(f"Assertion Step two reservation error: GPS - expected: {expected_gps}, actual: {actual_value_gps}")
        actual_value_dirty_return = self.get_element_text(Locators.assert_dirty_return)
        if actual_value_dirty_return == expected_dirty_return:
            print(f"Assertion Step two reservation pass: Zwrot brudnego samochodu - expected: {expected_dirty_return}")
        else:
            print(f"Assertion Step two reservation error: Zwrot brudnego samochodu - expected: {expected_dirty_return},"
                  f"actual: {actual_value_dirty_return}")
        actual_value_zone_1 = self.get_element_text(Locators.assert_zone_1)
        if actual_value_zone_1 == expected_zone_1:
            print(f"Assertion Step two reservation pass: Strefa 1 - expected: {expected_zone_1}")
        else:
            print(f"Assertion Step two reservation error: Strefa 1 - expected: {expected_zone_1},"
                  f"actual: {actual_value_zone_1}")
        actual_value_zone_2 = self.get_element_text(Locators.assert_zone_2)
        if actual_value_zone_2 == expected_zone_2:
            print(f"Assertion Step two reservation pass: Strefa 2 - expected: {expected_zone_2}")
        else:
            print(f"Assertion Step two reservation error: Strefa 2 - expected: {expected_zone_2},"
                  f"actual: {actual_value_zone_2}")
        actual_value_zone_3 = self.get_element_text(Locators.assert_zone_3)
        if actual_value_zone_3 == expected_zone_3:
            print(f"Assertion Step two reservation pass: Strefa 3 - expected: {expected_zone_3}")
        else:
            print(f"Assertion Step two reservation error: Strefa 3 - expected: {expected_zone_3}, "
                  f"actual: {actual_value_zone_3}")
        actual_insurance_name = self.get_element_text(Locators.assert_insurance_name)
        if actual_insurance_name == expected_insurance_name:
            print(f"Assertion Step two reservation pass: Insurance name - expected: {expected_insurance_name}")
        else:
            print(f"Assertion Step two reservation error: Insurance name - expected: {expected_insurance_name},"
                  f"actual: {actual_insurance_name}")
        actual_price_insurance = self.get_element_text(Locators.assert_insurance_price)
        if actual_price_insurance == expected_price_insurance:
            print(f"Assertion Step two reservation pass: Insurance price - expected: {expected_price_insurance}")
        else:
            print(f"Assertion Step two reservation error: Insurance price - expected: {expected_price_insurance},"
                  f"actual: {actual_price_insurance}")

    def assert_step_one(self, car):
        """Asserts for step one reservation"""
        text = self.get_element_text(Locators.assert_car_name)
        assert text.lower() == car.lower(), (
            f"Assertion Step one reservation error: Element with the name '{car}' "
            "not found"
        )
        print(f"Assertion Step one reservation pass: Found an element with the name '{car}'")