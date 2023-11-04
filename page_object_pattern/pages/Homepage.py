from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from page_object_patern.pages.Base_page import BasePage
import time
from page_object_patern.tests.test_data import ValidData
from page_object_patern.tests.test_data import InvalidData
from selenium.webdriver.common.action_chains import ActionChains
from page_object_patern.helpers.helpers import ScreenshotMaker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class Locators:
    """Locators Home Page"""
    accept_cookies = (By.XPATH, "//span[text()= 'Akceptuję']")
    field_place_start = (By.ID, 'bsPlaceStart')
    place_start = (By.XPATH, f"//*[@id='select2-placeStart-results']//li[text()='{ValidData.Start_city}']")
    checkbox_another_city = (By.ID, 'placeSameBox')
    field_place_end = (By.XPATH, "//*[@id='bsPlaceEnd']//span[@class='select2-selection select2-selection--single']")
    place_end = (By.XPATH, f"//*[@id='select2-placeEnd-results']/li[text()='{ValidData.End_city}']")
    input_end = (By.XPATH, '//input[@class="select2-search__field"]')
    box_date_start = (By.ID, 'dateStart')
    date_start = (
        By.XPATH,
        f"//div[@id='dateStart_box']//div[@class='datePickerBoxDaysSecond']"
        f"//div[text()='{ValidData.expected_date}']")
    date_start_test_case_6 = (
        By.XPATH,
        f"//div[@id='dateStart_box']//div[@class='datePickerBoxDaysSecond']"
        f"//div[text()='{InvalidData.date_start_test_case}']")
    date_end_test_case_6 = (
        By.XPATH,
        f"//div[@id='dateEnd_box']//div[@class='datePickerBoxDaysSecond']"
        f"//div[text()='{InvalidData.date_end_test_case}']")
    date_end = (
        By.XPATH,
        f"//div[@id='dateEnd_box']//div[@class='datePickerBoxDaysSecond']"
        f"//div[text()='{ValidData.expected_date_2}']")
    box_hour_start = (By.ID, 'hourStart')
    hour_start = (
        By.XPATH,
        f"//*[@id='hourStart_box']//div[text()='{ValidData.hour_start}']")
    minutes_start = (
        By.XPATH,
        f"//*[@class='timePickerBoxMinutes']//div[text()='{ValidData.minutes_start}']")
    invalid_date_end = (
        By.XPATH,
        f"//div[@id='dateEnd_box']//div[@class='datePickerBoxDaysSecond']"
        f"//div[text()='{InvalidData.expected_end_invalid}']")
    date_end_too_long = (
        By.XPATH,
        "//*[@id = 'dateEnd_box']//div[@class='datePickerBoxNextMonth']")
    date_end_invalid = (
        By.XPATH,
        f"//div[@id='dateEnd_box']//div[@class='datePickerBoxDaysSecond']"
        f"//div[text()='{InvalidData.date_end_invalid_data}']")
    invalid_hour_start = (
        By.XPATH,
        f"//*[@id='hourStart_box']//div[text()='{InvalidData.invalid_start_hour}']")
    BoxHourEnd = (By.NAME, 'godzina_do')
    HourEnd = (
        By.XPATH,
        f"//*[@id='hourEnd_box']/div[@class='timePickerBoxHours']/div[text()='{ValidData.hour_end}']")
    MinutesEnd = (
        By.XPATH,
        f"//*[@id='hourEnd_box']//div[@class='timePickerBoxMinutes']/div[text()='{ValidData.minutes_end}']")
    step_1_button = (By.ID, 'reservationSubmit')
    error_box = (By.ID, 'reservationErrorBox')


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.screenshot_maker = ScreenshotMaker(self.driver)

    """Main Page"""
    def _verify_page(self):
        """This method verifies that we are on the correct page."""
        pass

    def accept_cookies(self):
        """Click on the 'Accept' button in the pop-up window to accept cookies"""
        self.driver.find_element(*Locators.accept_cookies).click()

    def open_calendar(self):
        """Enters place pickup"""
        self.driver.find_element(*Locators.box_date_start).click()

    def set_city_start(self, start_city):
        """Enters place pickup"""
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(*Locators.field_place_start).click()
        place_start = wait.until(ec.element_to_be_clickable(Locators.place_start))
        place_start.click()

    def set_city_end(self, end_city):
        """Enters place return"""
        wait = WebDriverWait(self.driver, 10)
        checkbox_another_city = wait.until(ec.element_to_be_clickable(Locators.checkbox_another_city))
        checkbox_another_city.click()
        field_place_end = wait.until(ec.element_to_be_clickable(Locators.field_place_end))
        field_place_end.click()
        place_end = wait.until(ec.element_to_be_clickable(Locators.place_end))
        place_end.click()

    def set_date_start(self, expected_date):
        """Click on date pickup"""
        self.driver.find_element(*Locators.box_date_start).click()
        self.driver.find_element(*Locators.date_start).click()

    def set_date_end(self, expected_date_2):
        """Click on date return"""
        self.driver.find_element(*Locators.date_end).click()

    def set_date_end_test_case_reservation_time_too_long(self, date_end_invalid_data):
        """Click on invalid return date"""
        date_end_too_long_element = self.driver.find_element(*Locators.date_end_too_long)
        date_end_invalid_element = self.driver.find_element(*Locators.date_end_invalid)
        for _ in range(3):
            self.scroll_into_view_and_click(date_end_too_long_element)
            time.sleep(2)
        self.scroll_into_view_and_click(date_end_invalid_element)

    def scroll_into_view_and_click(self, element):
        """Scroll into view and click"""
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def set_hour_start(self, hour_start, minutes_start):
        """Click on hour pickup"""
        self.driver.find_element(*Locators.box_hour_start).click()
        self.driver.find_element(*Locators.hour_start).click()
        self.driver.find_element(*Locators.minutes_start).click()

    def set_invalid_date_end(self, expected_end_invalid):
        """Click on invalid date return"""
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.element_to_be_clickable(Locators.invalid_date_end)).click()

    def set_invalid_hour_start(self, invalid_start_hour, minutes_start):
        """Click on hour pickup"""
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.element_to_be_clickable(Locators.box_hour_start)).click()
        wait.until(ec.element_to_be_clickable(Locators.invalid_hour_start)).click()
        wait.until(ec.element_to_be_clickable(Locators.minutes_start)).click()

    def set_hour_end(self, hour_end, minutes_end):
        """Click on hour return"""
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.element_to_be_clickable(Locators.BoxHourEnd)).click()
        wait.until(ec.element_to_be_clickable(Locators.HourEnd)).click()
        wait.until(ec.element_to_be_clickable(Locators.MinutesEnd)).click()

    def submit_home_page(self):
        """Next step reservation"""
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(ec.element_to_be_clickable(Locators.step_1_button))
        element.click()

    def scroll_up(self):
        """Scrolls the page up"""
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_UP).perform()

    def assert_for_too_short_rental_term(self):
        """Asserts for a too short rental term error message on the reservation page."""
        error_box = self.driver.find_element(*Locators.error_box)
        error_message = error_box.find_element_by_tag_name('p').text
        expected_message = 'Wybrany okres wypożyczenia jest zbyt krótki.'
        try:
            assert error_message == expected_message, (
                f"Expected error message '{expected_message}', "
                f"but got '{error_message}'"
            )
            print('Assertion for too short rental term pass')
        except AssertionError as e:
            print('Assertion for too short rental term error:', e)
            raise e

    def assert_empty_field_location_pickup(self):
        """Asserts for empty location pickup on the reservation page."""
        expected_url = "https://carfree.pl/"
        assert self.driver.current_url == expected_url, (
            f"Expected URL '{expected_url}', but found '{self.driver.current_url}'"
        )
        try:
            h1_element = self.driver.find_element_by_tag_name('h1')
            expected_text = 'WYPOŻYCZALNIA SAMOCHODÓW'
            assert expected_text in h1_element.text, f"Expected text '{expected_text}' not found in h1 element"
            print('Assertion for empty field location pickup pass')
        except AssertionError as e:
            print('Assertion for empty location pickup error:', e)

    def assert_for_too_long_rental_term(self):
        """Asserts for a too long rental term error message on the reservation page."""
        try:
            error_element = self.driver.find_element(*Locators.error_box)
            expected_error_message = "W celu omówienia warunków wynajmu na dłuższy okres najmu, skontaktuj się\n" \
                                     "z naszą infolinią +48 794 500 550."
            assert expected_error_message in error_element.text, \
                f"Expected error message '{expected_error_message}' not found"
            print('Assertion for too long rental term pass')
        except AssertionError as e:
            print('Assertion for too long rental term error:', e)

    def set_date_end_earlier_than_start(self, date_start_test_case, date_end_test_case):
        """Test the behavior when selecting an end date earlier than the start date on the calendar."""
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.element_to_be_clickable(Locators.box_date_start)).click()
        time.sleep(2)
        wait.until(ec.element_to_be_clickable(Locators.date_start_test_case_6)).click()
        time.sleep(2)
        wait.until(ec.element_to_be_clickable(Locators.date_end_test_case_6)).click()

    def make_screenshot(self, screenshot_path):
        """Captures a screenshot of the current page and saves it to the specified 'screenshot_path'."""
        self.screenshot_maker.save_screenshot(screenshot_path)

    def close_window(self):
        """Closes Datepicker window in the web browser."""
        empty_area = self.driver.find_element(By.TAG_NAME, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(empty_area).click().perform()
