from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from curl import *
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait


class TestLogoutUser:
    def test_logout_via_exit_button_in_account(self, driver, wait, pre_login):
        print(f"1. Открываем страницу логина: {login_page_url}")
        driver.get(login_page_url)
        pre_login()
        print("3. Вход выполнен.")
        print(f"4. Текущий URL после pre_login(): {driver.current_url}")
        print("5. Ищем ссылку 'Личный Кабинет'...")
        link_personal_acc = driver.find_element(*Locators.LINK_PERSONAL_ACC)
        print("6. Ссылка 'Личный Кабинет' найдена. Пытаемся кликнуть...")
        try:
            link_personal_acc.click()
        except ElementClickInterceptedException:
            print("Стандартный клик по ссылке 'Личный Кабинет' перехвачен. Пробуем JS-клик.")
            driver.execute_script("arguments[0].click();", link_personal_acc)
        print("7. Клик по ссылке 'Личный Кабинет' выполнен.")
        print(f"8. Текущий URL после клика по 'Личный Кабинет': {driver.current_url}")
        long_wait = WebDriverWait(driver, 20)
        print("9. Ожидаем URL, содержащий '/account'...")
        long_wait.until(EC.url_contains("/account"))
        print("10. Переход в /account подтвержден.")
        long_wait = WebDriverWait(driver, 20) 
        but_exit = long_wait.until(EC.element_to_be_clickable(Locators.BUT_EXIT))
        try:
            but_exit.click()
        except ElementClickInterceptedException:
            print("Стандартный клик по кнопке 'Выход' перехвачен. Пробуем JS-клик.")
            driver.execute_script("arguments[0].click();", but_exit)
        assert wait.until(EC.visibility_of_element_located(Locators.BUT_ENTER))
        assert driver.current_url == login_page_url 
