from selenium.webdriver.common.by import By


class MainPageLocators:
    YANDEX_LOGO = (By.XPATH, ".//a[contains(@class,'Header_LogoYandex')]")  # Логотип "Яндекса"

    SCOOTER_LOGO = (By.XPATH, ".//a[contains(@class,'Header_LogoScooter')]")  # Логотип "Самоката"

    SCOOTER_TEXT = (By.XPATH, ".//div[contains(@class,'Header_Disclaimer')]")  # Текст "Учебный тренажер"

    HEADER_ORDER_BUTTON = (
        By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']")  # Кнопка "Заказать" в заголовке

    HOMEPAGE_ORDER_BUTTON = (
        By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']")  # Кнопка "Заказать" на странице

    FAQ = (By.CSS_SELECTOR, '.accordion')  # FAQ

    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')  # Кнопка "Принять куки"

    QUESTION_LOCATOR = (By.ID, 'accordion__heading-{}')  # Локатор для всех вопросов

    ANSWER_LOCATOR = (By.ID, 'accordion__panel-{}')  # Локатор для всех ответов
