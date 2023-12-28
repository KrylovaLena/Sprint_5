from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from element_locators import TestLocators
from conftest import driver

class TestDesidner:

    def test_bread_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.SAUCE_BUTTON).click()
        driver.find_element(*TestLocators.BREAD_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.BREAD_SECTION))
        assert driver.find_element(*TestLocators.ACTIVE_BUTTON).text == 'Булки'

    def test_sauce_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.SAUCE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.SAUCE_SECTION))
        assert driver.find_element(*TestLocators.ACTIVE_BUTTON).text == 'Соусы'

    def test_topping_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.TOPPING_BUTTON ).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.TOPPING_SECTION))
        assert driver.find_element(*TestLocators.ACTIVE_BUTTON).text == 'Начинки'