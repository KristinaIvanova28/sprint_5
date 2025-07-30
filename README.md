
# Sprint_5: Автотесты для Stellar Burgers

Этот проект содержит автотесты для веб-приложения Stellar Burgers, написанные на Python с использованием Selenium WebDriver.

## Описание проекта

Проект тестирует следующую функциональность:
- Регистрация пользователя
- Вход в систему
- Переход в личный кабинет
- Переход из личного кабинета в конструктор
- Выход из аккаунта
- Раздел "Конструктор" (булки, соусы, начинки)

## Технологии

- Python 3.9+
- Selenium WebDriver
- pytest
- WebDriver Manager
- faker

## Структура проекта

- `tests/`: Содержит все тестовые файлы (`.py`).
- `locators/`: Содержит файлы с локаторами элементов страниц (`main_page_locators.py`, `login_page_locators.py` и т.д.).
- `data.py`: Содержит тестовые данные.
- `curl.py`: Файл с URL-адресами страниц.
- `tests/conftest.py`: Файл с фикстурами pytest (настройка драйвера, ожиданий).
- `requirements.txt`: Список зависимостей Python.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone <URL_вашего_репозитория>
   cd <название_папки_проекта>
2. Создайте виртуальное окружение:
    python -m venv .venv
3. Aктивируйте виртуальное окружение:
    Linux/macOS:
    source .venv/bin/activate
    Windows:
    .venv\Scripts\activate
4. Установите зависимости:
    pip install -r requirements.txt

## Запуск тестов

Запустить все тесты:
pytest tests/

Запустить все тесты с подробным выводом:
pytest tests/ -v

Запустить один конкретный тест:
pytest tests/папка_теста.py::КлассТеста::имя_метода_теста -v

Запустить тесты, подавляя предупреждение urllib3:
PYTHONWARNINGS="ignore::urllib3.exceptions.NotOpenSSLWarning" pytest tests/ -v 
