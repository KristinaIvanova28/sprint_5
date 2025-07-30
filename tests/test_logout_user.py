from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from curl import *
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait


class TestLogoutUser:
    def test_logout_via_exit_button_in_account(self, driver, wait, pre_login):
        driver.get(login_page_url)
        pre_login()
        link_personal_acc = driver.find_element(*Locators.LINK_PERSONAL_ACC)
        driver.execute_script("arguments[0].click();", link_personal_acc)
        long_wait = WebDriverWait(driver, 20)
        long_wait.until(EC.url_contains("/account"))
        but_exit = long_wait.until(EC.element_to_be_clickable(Locators.BUT_EXIT))
        driver.execute_script("arguments[0].click();", but_exit)
        long_wait.until(EC.url_contains("/login"))
        assert long_wait.until(EC.visibility_of_element_located(Locators.BUT_ENTER))
        assert driver.current_url == login_page_url



