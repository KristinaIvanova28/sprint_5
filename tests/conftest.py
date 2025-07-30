import pytest
import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from curl import *
from data import Credentials
from locators import Locators

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1200,600")
    browser = webdriver.Chrome(options=options)
    browser.get(main_page_url)
    yield browser
    browser.quit()

@pytest.fixture(scope='function')
def wait(driver):
    return WebDriverWait(driver, 5)


@pytest.fixture(scope='function')
def pre_login(driver, wait):
    def login():
        # Ожидаем поля
        wait.until(EC.visibility_of_element_located(Locators.EMAIL))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        wait.until(EC.element_to_be_clickable(Locators.BUT_ENTER)).click()
    return login


