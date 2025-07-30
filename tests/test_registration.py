from selenium.webdriver.support import expected_conditions as EC

from tests.helper import *
from locators import Locators
from curl import *

class TestRegistration:

    def test_successful_registration(self, driver, wait):
        name, email, password = generate_registration_data()
        driver.get(register_page_url)
        wait.until(EC.visibility_of_element_located(Locators.BUT_REGISTER))
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.BUT_REGISTER).click()
        wait.until(EC.url_contains("/login"))

        assert driver.current_url==login_page_url

    def test_registration_with_short_password_shows_error_message(self, driver, wait):
        name, email, password = generate_registration_data_short_password()
        driver.get(register_page_url)
        wait.until(EC.visibility_of_element_located(Locators.BUT_REGISTER))
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.BUT_REGISTER).click()

        assert driver.current_url==register_page_url
        assert wait.until(EC.visibility_of_element_located(Locators.ERROR_MESS)).is_displayed()
        