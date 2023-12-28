from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from element_locators import TestLocators
from conftest import driver
import pytest
import random


class TestRegistration:
    def test_user_registration_correct(self, driver):
        # Генерируем случайные данные для регистрации
        name = "Elena Krylova"
        email_domain = random.choice(["gmail.com", "yandex.ru", "mail.com"])
        random_number = random.randint(100, 999)
        email = f"Elena_Krylova_4_{random_number}@{email_domain}"
        password = "1q2w3E4*"

        # Выполняем регистрацию пользователя
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*TestLocators.NAME_FIELD_FIRST).send_keys(name)
        driver.find_element(*TestLocators.EMAIL_FIELD_FIRST).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_FIELD_FIRST).send_keys(password)
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_contains("site/login"))

        # Проверяем, что успешно зарегистрированы и перенаправлены на другую страницу
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_user_registration_password_not_correct(self, driver):
        # Выполняем регистрацию пользователя
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*TestLocators.NAME_FIELD_FIRST).send_keys("Elena Krylova6")
        driver.find_element(*TestLocators.EMAIL_FIELD_FIRST).send_keys("Elena_Krylova_4_666@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_FIELD_FIRST).send_keys("12345")
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()

        # Проверяем, что получаем сообщение об ошибке 'Некорректный пароль'
        assert driver.find_element(*TestLocators.PASSWORD_ERROR_MESSAGE).text == "Некорректный пароль"

    def test_user_registration_not_name(self, driver):
        # Генерируем случайные данные для регистрации
        name = ""
        email_domain = random.choice(["gmail.com", "yandex.ru", "mail.com"])
        random_number = random.randint(100, 999)
        email = f"Elena_Krylova_4_{random_number}@{email_domain}"
        password = "1q2w3E4*"

        # Выполняем регистрацию пользователя
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*TestLocators.NAME_FIELD_FIRST).send_keys(name)
        driver.find_element(*TestLocators.EMAIL_FIELD_FIRST).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_FIELD_FIRST).send_keys(password)
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()

        # Проверяем, что пользователь не зарегистрирован и остался на той же странице
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

    def test_user_registration_email_not_correct(self, driver):
            # Генерируем случайные данные для регистрации
        name = ""
        random_number = random.randint(100, 999)
        email = f"Elena_Krylova_4_{random_number}"
        password = "1q2w3E4*"

        # Выполняем регистрацию пользователя
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*TestLocators.NAME_FIELD_FIRST).send_keys(name)
        driver.find_element(*TestLocators.EMAIL_FIELD_FIRST).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_FIELD_FIRST).send_keys(password)
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()

        # Проверяем, что пользователь не зарегистрирован и остался на той же странице
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'