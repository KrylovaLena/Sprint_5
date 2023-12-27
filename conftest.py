import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    # Создаём экземпляр веб-драйвера Chrome
    driver = webdriver.Chrome()
    # Возвращаем экземпляр драйвера
    yield driver
    # Закрываем браузер после выполнения теста
    driver.quit()