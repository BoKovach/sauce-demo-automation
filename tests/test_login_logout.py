import pytest
from pages.login_page import LoginPage
from utils.data_loader import load_login_data

login_data = load_login_data()


@pytest.mark.usefixtures("driver")
class TestLogInLogOut:

    @pytest.mark.login
    @pytest.mark.parametrize('data', login_data)
    def test_login_valid_data(self, driver, data):

        login = LoginPage(driver)
        login.open()
        login.login(data['username'], data['password'])

        if data['case'] == 'valid_login':
            assert driver.current_url == data['expected_url']

        elif data['case'] == 'locked':
            error = login.error_message().lower()
            assert error == data['expected_error'].lower()

        elif data['case'] == 'invalid':
            error = login.error_message().lower()
            assert error == data['expected_error'].lower()

        elif data['case'] == 'empty_user':
            error = login.error_message().lower()
            assert error == data['expected_error'].lower()

        elif data['case'] == 'empty_password':
            error = login.error_message().lower()
            assert error == data['expected_error'].lower()

    @pytest.mark.logout
    def test_logout(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login(login_data[0]['username'], login_data[0]['password'])

        assert driver.current_url == login_data[0]['expected_url']

        login.logout()

        assert driver.current_url == 'https://www.saucedemo.com/'
