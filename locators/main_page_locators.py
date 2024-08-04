from selenium.webdriver.common.by import By


class MainPageLocators:
    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')  # Логотип "Яндекса"

    SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')  # Логотип "Самоката"

    SCOOTER_TEXT = (By.CLASS_NAME, 'Header_Disclaimer__3VEni')  # Текст "Учебный тренажер"

    HEADER_ORDER_BUTTON = (
    By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']")  # Кнопка "Заказать" в заголовке

    HOMEPAGE_ORDER_BUTTON = (
    By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']")  # Кнопка "Заказать" на странице

    FAQ = (By.CSS_SELECTOR, '.accordion')  # FAQ

    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')  # Кнопка "Принять куки"

    QUESTION_LOCATOR = (By.ID, 'accordion__heading-{}')  # Локатор для всех вопросов

    ANSWER_LOCATOR = (By.ID, 'accordion__panel-{}')  # Локатор для всех ответов