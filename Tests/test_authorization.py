from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from element_locators import TestLocators
from conftest import driver

class TestAuthorization:
    def test_authorization_main_page(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        # вход по кнопке «Войти в аккаунт» на главной
        driver.find_element(*TestLocators.SIGN_IN_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_FIELD_AUTH).send_keys("Elena_Krylova_4_555@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_FIELD_AUTH).send_keys("1q2w3E4*")
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_authorization_personal_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        # вход через "Личный кабинет"
        driver.find_element(*TestLocators.ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_FIELD_AUTH).send_keys("Elena_Krylova_4_555@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_FIELD_AUTH).send_keys("1q2w3E4*")
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_authorization_registration(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        # вход через кнопку в форме регистрации
        driver.find_element(*TestLocators.LOGIN_LINK_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_FIELD_AUTH).send_keys("Elena_Krylova_4_555@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_FIELD_AUTH).send_keys("1q2w3E4*")
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_enter_forgot_password(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        # вход через кнопку в форме восстановления пароля
        driver.find_element(*TestLocators.LOGIN_LINK_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_FIELD_AUTH).send_keys("Elena_Krylova_4_555@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_FIELD_AUTH).send_keys("1q2w3E4*")
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'