class ValidData:
    """Home page"""
    Start_city = "Bielsko Biała - Miasto, podstawienie pod adres"
    End_city = "Wrocław, Dworzec Główny PKP"
    expected_date = "28"
    expected_date_2 = "30"
    hour_start = "19"
    minutes_start = "30"
    hour_end = '10'
    minutes_end = '45'

    """Page one"""
    segment = 'Van/Bus'
    car = 'Toyota Proace City Long -7os.'
    submit = '14'

    """Page three"""
    name = 'Adam'
    surname = 'Kowalski'
    email = 'adamkowalis@gmail.com'
    phone = '111 111 111'
    address = 'Kolorowa 22/2'
    city = 'Poznan'
    post_code = "00-000"


class InvalidData:
    """Data test case 6 """
    date_start_test_case = "25"
    date_end_test_case = "20"

    """Test case 3 homepage reservation short"""
    expected_end_invalid = "29"
    invalid_start_hour = '23'
    """Test case 1 homepage reservation time too long"""
    date_end_invalid_data = '30'
