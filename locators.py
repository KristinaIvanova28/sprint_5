from selenium.webdriver.common.by import By

class Locators:

    # локаторы для главной страницы авторизованный:
    BUT_ORDER = (By.XPATH, "//button[text()='Оформить заказ']") # кнопка "Оформить заказ"
    
    # локаторы на главной странице неавторизованной:
    BUT_ENTER_ACC = (By.XPATH, "//button[text()='Войти в аккаунт']") # кнопка "Войти в аккаунт"
    LINK_PERSONAL_ACC = (By.XPATH, "//a[@href = '/account']") # ссылка "Личный кабинет" идентична для всех страниц
    LINK_CONSTRUCT = (By.XPATH, ".//p[text() = 'Конструктор']") # ссылка "Конструктор" идентична для всех страниц
    LINK_LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']//a") #логотип "Stellar Burger" идентична для всех страниц

    # локаторы для страницы авторизации:
    EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input") # поле ввода емаил для страницы авторизации и регистрации
    PASSWORD = (By.NAME, "Пароль") #поле ввода пароля для страницы авторизации и регистрации
    BUT_ENTER = (By.XPATH, "//button[text()='Войти']")  # кнопка "Войти"
    LINK_REG = (By.XPATH, "//a [@href='/register']") # ссылка "Зарегистрироваться"
    LINK_FORGOT_PASS = (By.XPATH, "//a[@href = '/forgot-password']") # ссылка "Восстановить пароль"

    # локаторы для страницы регистрации:
    NAME = (By.NAME, "name") # поле ввода "Имя"
    BUT_REGISTER = (By.XPATH, "//button[text()='Зарегистрироваться']") #кнопка "Зарегистрироваться"
    LINK_LOGIN = (By.XPATH, "//a[@href = '/login']") # ссылка "Войти"

    ERROR_MESS = (By.CLASS_NAME, 'input__error') # сообщение об ошибке при регистрации с коротким паролем

    # локаторы для страницы Личный кабинет:
    BUT_EXIT = (By.XPATH, "//button[text()='Выход']") # кнопка "Выход"
    BUT_SAVE = (By.XPATH, "//button[text()='Сохранить']") # конпка "Сохранить"

    # локаторы для раздела Конструктор:
    TAB_BREAD = (By.XPATH, "//span[text()='Булки']") # переход на вкладку Булки в разделеа Конструктор
    TAB_SAUCES = (By.XPATH, "//span[text()='Соусы']") # переход на вкладку Соусы в разделе Конструктор
    TAB_TOPPINGS = (By.XPATH, "//span[text()='Начинки']") # переход на вкладку Начинки в разделеа Конструктор

    CURRENT_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]") # выбранная вкладка в Разделе Конструктор
    BREAD = (By.XPATH, '//h2[text()="Булки"]//following-sibling::ul') # список булок
    SAUCES = (By.XPATH, '//h2[text()="Соусы"]//following-sibling::ul') # список соусов
    TOPPINGS = (By.XPATH, '//h2[text()="Начинки"]//following-sibling::ul') # список начинок











