import time
from page_object_patern.tests.test_data import ValidData
from page_object_patern.pages.Homepage import HomePage
from page_object_patern.pages.Step_one import ReservationStepOne
from page_object_patern.pages.Step_two import ReservationStepTwo
from page_object_patern.tests.base_test import BaseTest


class StepTwoPageTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.Step_one = ReservationStepOne(self.driver)
        self.Homepage = HomePage(self.driver)
        start_city = ValidData.Start_city
        end_city = ValidData.End_city
        date_start = ValidData.expected_date
        date_end = ValidData.expected_date_2
        hour_start = ValidData.hour_start
        hour_end = ValidData.hour_end
        minutes_start = ValidData.minutes_start
        minutes_end = ValidData.minutes_end
        segment = ValidData.segment
        car = ValidData.car
        submit = ValidData.submit
        self.driver.implicitly_wait(10)
        self.Homepage.accept_cookies()
        time.sleep(2)
        self.Homepage.set_city_start(start_city)
        time.sleep(2)
        self.Homepage.set_city_end(end_city)
        time.sleep(2)
        self.Homepage.set_date_start(date_start)
        time.sleep(2)
        self.Homepage.set_date_end(date_end)
        time.sleep(2)
        self.Homepage.set_hour_start(hour_start, minutes_start)
        time.sleep(1)
        self.Homepage.set_hour_end(hour_end, minutes_end)
        time.sleep(2)
        self.Homepage.submit_home_page()
        time.sleep(2)
        self.Step_one = ReservationStepOne(self.driver)
        self.Step_one.car_list(segment, car)
        time.sleep(2)
        self.Step_one.submit_step_one(submit)
        time.sleep(2)

    def test_case_4_two_step_reservation_empty_insurance_option(self):
        self.Step_two = ReservationStepTwo(self.driver)
        self.Step_two.payments_options()
        time.sleep(2)
        self.Step_three = self.Step_two.submit_step_two()
        time.sleep(2)
        self.Step_two.assert_empty_insurance_option()
        time.sleep(2)

    def test_case_5_two_step_reservation_empty_payment_option(self):
        self.Step_two = ReservationStepTwo(self.driver)
        self.Step_two.submit_step_two()
        time.sleep(2)
        self.Step_two.assert_empty_payment_option()
        time.sleep(2)
        self.Step_two.make_screenshot("test_case_5_two_step_reservation_empty_payment_option.png")

    def tearDown(self):
        self.driver.quit()