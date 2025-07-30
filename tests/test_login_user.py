from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from curl import *

class TestAuth:

    def test_user_can_login_via_enter_account_button(self, driver, wait, pre_login):
        wait.until(EC.element_to_be_clickable(Locators.BUT_ENTER_ACC)).click()
        pre_login()
        assert wait.until(EC.visibility_of_element_located(Locators.BUT_ORDER)).is_displayed()

    def test_user_can_login_via_link_person_account(self, driver, wait, pre_login):
        wait.until(EC.element_to_be_clickable(Locators.LINK_PERSONAL_ACC)).click()
        pre_login()
        assert wait.until(EC.visibility_of_element_located(Locators.BUT_ORDER)).is_displayed()

    def test_user_can_login_via_link_enter_by_register_site(self, driver, wait, pre_login):
        driver.get(register_page_url)
        wait.until(EC.element_to_be_clickable(Locators.LINK_LOGIN)).click()
        wait.until(EC.visibility_of_element_located(Locators.BUT_ENTER))
        pre_login()
        assert wait.until(EC.visibility_of_element_located(Locators.BUT_ORDER)).is_displayed()

    def test_user_can_login_via_link_enter_by_forgot_password_page_url(self, driver, wait, pre_login):
        driver.get(forgot_password_page_url)
        wait.until(EC.element_to_be_clickable(Locators.LINK_LOGIN)).click()
        wait.until(EC.visibility_of_element_located(Locators.BUT_ENTER))
        pre_login()
        assert wait.until(EC.visibility_of_element_located(Locators.BUT_ORDER)).is_displayed() 