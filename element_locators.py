from selenium.webdriver.common.by import By


class TestLocators:
    # Для регистрации пользователя
    NAME_FIELD_FIRST = (By.XPATH, "(//input[@name= 'name'])[1]") # Поле ввода имени
    EMAIL_FIELD_FIRST = (By.XPATH, "(//input[@name= 'name'])[2]")  # Поле ввода email
    PASSWORD_FIELD_FIRST = (By.XPATH, "//input[@name= 'Пароль']")  # Поле ввода пароля
    REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")   # Кнопка "Зарегистрироваться"
    PASSWORD_ERROR_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']")  # Сообщение об некорректном пароле

    # Для авторизации пользователя
    EMAIL_FIELD_AUTH = (By.XPATH, ".//input[@name='name']")  # Поле ввода email
    PASSWORD_FIELD_AUTH = (By.XPATH, ".//input[@name='Пароль']")  # Поле ввода пароля
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")  # Кнопка Войти
    ACCOUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")  # Кнопка "Личный кабинет"
    SIGN_IN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    LOGIN_LINK_BUTTON = (By.XPATH, ".//a[@href='/login']")  # Кнопка Уже зарегистрированы? "Войти"

    # Для проверки перехода из личного кабинета в конструктор
    BUILDER_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")  # Кнопка "Конструктор"
    BUILDER_TITLE = (By.XPATH, ".//h1[text()='Соберите бургер']")  # Заголовок страницы Конструктор
    LOGO_BUTTON = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # Логотип Stellar Burgers

    # Для проверки выхода из аккаунта
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")  # Кнопка "Выход"

    # Для тестирования конструктора
    BREAD_BUTTON = (By.XPATH, ".//span[text()='Булки']")  # Кнопка "Булки"
    BREAD_SECTION = (By.XPATH, ".//h2[text()='Булки']")  # Раздел "Булки"
    SAUCE_BUTTON = (By.XPATH, ".//span[text()='Соусы']")  # Кнопка "Соус"
    SAUCE_SECTION = (By.XPATH, ".//h2[text()='Соусы']")  # Раздел "Соус"
    TOPPING_BUTTON = (By.XPATH, ".//span[text()='Начинки']")  # Кнопка "Начинки"
    TOPPING_SECTION = (By.XPATH, ".//h2[text()='Начинки']")  # Раздел "Начинки"
    ACTIVE_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]") # Текущая кнопка конструктора
