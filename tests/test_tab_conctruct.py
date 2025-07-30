from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestTabConstruct:

    def test_switch_tab_sauces_to_tab_bread_current(self, driver, wait):
        driver.find_element(*Locators.TAB_SAUCES).click()
        wait.until(EC.visibility_of_element_located(Locators.SAUCES))
        driver.find_element(*Locators.TAB_BREAD).click()
        wait.until(EC.visibility_of_element_located(Locators.BREAD))
        current_tab = wait.until(EC.visibility_of_element_located(Locators.CURRENT_TAB))
        assert current_tab.text == 'Булки'

    def test_switch_tab_bread_to_tab_sauces_current(self, driver, wait):
        driver.find_element(*Locators.TAB_SAUCES).click()
        wait.until(EC.visibility_of_element_located(Locators.SAUCES))
        current_tab = wait.until(EC.visibility_of_element_located(Locators.CURRENT_TAB))
        assert current_tab.text == 'Соусы'

    def test_switch_tab_bread_to_tab_toppings_current(self, driver, wait):
        driver.find_element(*Locators.TAB_TOPPINGS).click()
        wait.until(EC.visibility_of_element_located(Locators.TOPPINGS))
        current_tab = wait.until(EC.visibility_of_element_located(Locators.CURRENT_TAB))
        assert current_tab.text == 'Начинки' 