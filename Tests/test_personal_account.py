from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from element_locators import TestLocators
from conftest import driver

class TestSwitching :
    def test_clicking_on_the_personal_account_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(*TestLocators.EMAIL_FIELD_AUTH).send_keys("Elena_Krylova_4_555@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_FIELD_AUTH).send_keys("1q2w3E4*")
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.ACCOUNT_BUTTON))
        driver.find_element(*TestLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    def test_clicking_on_the_builder_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(*TestLocators.EMAIL_FIELD_AUTH).send_keys("Elena_Krylova_4_555@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_FIELD_AUTH).send_keys("1q2w3E4*")
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.ACCOUNT_BUTTON))
        driver.find_element(*TestLocators.ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.BUILDER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        assert driver.find_element(*TestLocators.BUILDER_TITLE).text == 'Соберите бургер'

    def test_clicking_on_logo(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(*TestLocators.EMAIL_FIELD_AUTH).send_keys("Elena_Krylova_4_555@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_FIELD_AUTH).send_keys("1q2w3E4*")
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.ACCOUNT_BUTTON))
        driver.find_element(*TestLocators.ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.LOGO_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        assert driver.find_element(*TestLocators.BUILDER_TITLE).text == 'Соберите бургер'

    def test_logout_clicking_on_the_exit_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(*TestLocators.EMAIL_FIELD_AUTH).send_keys("Elena_Krylova_4_555@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_FIELD_AUTH).send_keys("1q2w3E4*")
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.ACCOUNT_BUTTON))
        driver.find_element(*TestLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.LOGOUT_BUTTON))
        driver.find_element(*TestLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
