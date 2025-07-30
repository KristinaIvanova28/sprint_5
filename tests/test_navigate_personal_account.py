from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from curl import *


class TestNavigatePersonalAccount:

    def test_user_can_navigate_to_account_from_main_page_url(self, driver, wait, pre_login):
        driver.get(login_page_url)
        pre_login()
        wait.until(EC.element_to_be_clickable(Locators.LINK_PERSONAL_ACC)).click()
        wait.until(EC.visibility_of_element_located(Locators.BUT_SAVE))
        assert driver.current_url == profile_page_url

    def test_user_can_navigate_to_main_page_from_account_via_constructor_link(self, driver, wait, pre_login):
        driver.get(login_page_url)
        pre_login()
        driver.find_element(*Locators.LINK_PERSONAL_ACC).click()
        wait.until(EC.element_to_be_clickable(Locators.LINK_CONSTRUCT)).click()
        assert driver.current_url == main_page_url

    def test_user_can_navigate_to_main_page_from_account_via_logo_link(self, driver, wait, pre_login):
        driver.get(login_page_url)
        pre_login()
        driver.find_element(*Locators.LINK_PERSONAL_ACC).click()
        wait.until(EC.element_to_be_clickable(Locators.LINK_LOGO)).click()
        assert driver.current_url == main_page_url

