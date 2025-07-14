from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, 'user-name')
        self.password_input = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')
        self.login_error_message = (By.CSS_SELECTOR,
                                  '#login_button_container > div > form > div.error-message-container.error > h3')

    def open(self):
        self.driver.get('https://www.saucedemo.com/')

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def error_message(self):
        return self.driver.find_element(*self.login_error_message).text

    def logout(self):
        menu_button = self.driver.find_element(By.ID, 'react-burger-menu-btn')
        menu_button.click()

        logout_button = WebDriverWait(self.driver, 5)\
            .until(EC.visibility_of_element_located((By.ID, 'logout_sidebar_link')))

        logout_button.click()
