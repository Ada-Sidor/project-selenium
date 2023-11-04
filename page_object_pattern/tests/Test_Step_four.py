from page_object_patern.tests.base_test import BaseTest
from page_object_patern.tests.test_data import ValidData
from page_object_patern.pages.Homepage import HomePage
from page_object_patern.pages.Step_one import ReservationStepOne
from page_object_patern.pages.Step_two import ReservationStepTwo
from page_object_patern.pages.Step_three import ReservationStepThree
from page_object_patern.pages.Step_four import ReservationStepFour
import time
from page_object_patern.tests.test_data import InvalidData


class StepFourPageTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.Step_one = ReservationStepOne(self.driver)
        self.Homepage = HomePage(self.driver)
        self.Homepage.accept_cookies()

    def test_case_6_reservation_without_account_invalid_data_date_end_earlier_than_start(self):
        date_start_test_case = InvalidData.date_start_test_case
        date_end_test_case = InvalidData.date_start_test_case
        start_city = ValidData.Start_city
        segment = ValidData.segment
        car = ValidData.car
        submit = ValidData.submit
        hour_start = ValidData.hour_start
        hour_end = ValidData.hour_end
        minutes_start = ValidData.minutes_start
        minutes_end = ValidData.minutes_end
        time.sleep(2)
        self.Homepage.set_city_start(start_city)
        time.sleep(2)
        self.Homepage.set_date_end_earlier_than_start(date_start_test_case, date_end_test_case)
        time.sleep(2)
        self.Homepage.close_window()
        time.sleep(1)
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
        self.Step_two = ReservationStepTwo(self.driver)
        self.driver.implicitly_wait(10)
        self.Step_two.select_additional_options()
        time.sleep(2)
        self.Step_two.payments_options()
        time.sleep(2)
        self.Step_two.submit_step_two()
        time.sleep(7)
        name = ValidData.name
        surname = ValidData.surname
        email = ValidData.email
        address = ValidData.address
        city = ValidData.city
        post_code = ValidData.post_code
        self.Step_three = ReservationStepThree(self.driver)
        self.Step_three.enter_name(name)
        time.sleep(1)
        self.Step_three.enter_surname(surname)
        time.sleep(1)
        self.Step_three.enter_email(email)
        time.sleep(1)
        self.Step_three.enter_address(address)
        time.sleep(1)
        self.Step_three.enter_city(city)
        time.sleep(1)
        self.Step_three.enter_post_code(post_code)
        time.sleep(1)
        self.Step_three.select_invoice()
        time.sleep(1)
        self.Step_three.select_all_consents()
        time.sleep(1)
        self.Step_three.select_invoice()
        time.sleep(3)
        self.Step_three.assert_step_home_page("2023-09-20 19:30", "Bielsko Biała - Miasto", "2023-09-26 10:45",
                                              "Bielsko Biała - Miasto")
        self.Step_three.assert_step_one(ValidData.car)
        self.Step_three.assert_step_two_combined("60 PLN", "114 PLN", "114 PLN", "114 PLN", "50 PLN", "199 PLN",
                                                 "399 PLN", "499 PLN", "Pakiet Ochrony Premium (P)", "540 PLN")
#       self.Step_three.submit_page_three()
        self.Step_four = ReservationStepFour(self.driver)
#        self.Step_four.assert_h1()

    def test_case_7_four_step_reservation_without_account_valid_data(self):
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
        self.driver.implicitly_wait(5)
        time.sleep(1)
        self.Homepage.set_city_start(start_city)
        time.sleep(1)
        self.Homepage.set_city_end(end_city)
        time.sleep(1)
        self.Homepage.set_date_start(date_start)
        time.sleep(1)
        self.Homepage.set_date_end(date_end)
        time.sleep(1)
        self.Homepage.set_hour_start(hour_start, minutes_start)
        time.sleep(1)
        self.Homepage.set_hour_end(hour_end, minutes_end)
        time.sleep(1)
        self.Homepage.submit_home_page()
        time.sleep(1)
        self.Step_one = ReservationStepOne(self.driver)
        self.Step_one.car_list(segment, car)
        time.sleep(1)
        self.Step_one.submit_step_one(submit)
        time.sleep(1)
        self.Step_two = ReservationStepTwo(self.driver)
        self.Step_two.select_additional_options()
        time.sleep(1)
        self.Step_two.payments_options()
        time.sleep(1)
        self.Step_two.submit_step_two()
        time.sleep(7)
        name = ValidData.name
        surname = ValidData.surname
        email = ValidData.email
        address = ValidData.address
        city = ValidData.city
        post_code = ValidData.post_code
        self.Step_three = ReservationStepThree(self.driver)
        time.sleep(1)
        self.Step_three.enter_name(name)
        time.sleep(1)
        self.Step_three.enter_surname(surname)
        time.sleep(1)
        self.Step_three.enter_email(email)
        time.sleep(1)
        self.Step_three.enter_address(address)
        time.sleep(1)
        self.Step_three.enter_city(city)
        time.sleep(1)
        self.Step_three.enter_post_code(post_code)
        time.sleep(1)
        self.Step_three.select_invoice()
        time.sleep(1)
        self.Step_three.select_all_consents()
        time.sleep(1)
        self.Step_three.select_invoice()
        time.sleep(3)
        self.Step_three.assert_step_home_page("2023-09-28 19:30", "Bielsko Biała - Miasto", "2023-09-30 10:45",
                                              "Wrocław")
        self.Step_three.assert_step_one(ValidData.car)
        self.Step_three.assert_step_two_combined(
            "20 PLN", "38 PLN", "38 PLN", "38 PLN", "50 PLN", "199 PLN", "399 PLN", "499 PLN",
            "Pakiet Ochrony Premium (P)", "180 PLN")
#        self.Step_three.submit_page_three()
        self.Step_four = ReservationStepFour(self.driver)
#        self.Step_four.assert_h1()

    def tearDown(self):
        self.driver.quit()
