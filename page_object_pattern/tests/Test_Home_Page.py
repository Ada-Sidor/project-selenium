import time
from page_object_patern.tests.base_test import BaseTest
from page_object_patern.tests.test_data import ValidData
from page_object_patern.tests.test_data import InvalidData


class HomePageTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.Homepage.accept_cookies()

    def test_case_1_reservation_without_aaccount_reservation_period_is_too_long(self):
        start_city = ValidData.Start_city
        date_start = ValidData.expected_date
        date_end_invalid_data = InvalidData.date_end_invalid_data
        time.sleep(2)
        self.Homepage.set_city_start(start_city)
        time.sleep(2)
        self.Homepage.set_date_start(date_start)
        time.sleep(2)
        self.Homepage.set_date_end_test_case_reservation_time_too_long(date_end_invalid_data)
        time.sleep(2)
        self.Homepage.scroll_up()
        time.sleep(1)
        self.Homepage.submit_home_page()
        time.sleep(2)
        self.Homepage.assert_for_too_long_rental_term()
        time.sleep(2)
        self.Homepage.screenshot_maker._create_screenshot_folder_if_does_not_exist()
        self.Homepage.make_screenshot("test_case_1_test_case_reservation_without_aaccount_reservation_period_is_too_long.png")

    def test_case_2_reservation_without_account_required_pickup_field_is_empty(self):
        self.Homepage.submit_home_page()
        self.Homepage.make_screenshot("test_case_2_reservation_without_account_required_pickup_field_is_empty.png")
        self.Homepage.assert_empty_field_location_pickup()
        time.sleep(2)
        self.driver.quit()

    def test_case_3_reservation_without_account_reservation_period_is_too_short(self):
        expected_end_invalid = InvalidData.expected_end_invalid
        invalid_start_hour = InvalidData.invalid_start_hour
        minutes_start = ValidData.minutes_start
        expected_date = ValidData.expected_date
        start_city = ValidData.Start_city
        hour_end = ValidData.hour_end
        minutes_end = ValidData.minutes_end
        self.Homepage.set_city_start(start_city)
        time.sleep(2)
        self.Homepage.set_date_start(expected_date)
        time.sleep(2)
        self.Homepage.set_invalid_date_end(expected_end_invalid)
        time.sleep(2)
        self.Homepage.set_invalid_hour_start(invalid_start_hour, minutes_start)
        time.sleep(2)
        self.Homepage.set_hour_end(hour_end, minutes_end)
        time.sleep(2)
        self.Homepage.submit_home_page()
        time.sleep(2)
        self.Homepage.make_screenshot("test_case_3_reservation_without_account_reservation_period_is_too_short.png")
        self.Homepage.assert_for_too_short_rental_term()
        time.sleep(2)
        self.driver.quit()

    def tearDown(self):
        self.driver.quit()
