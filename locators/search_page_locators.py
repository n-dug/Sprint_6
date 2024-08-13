from selenium.webdriver.common.by import By


class SearchPageLocators:
    MAIN_BUTTON = (By.XPATH, ".//span[text() = 'Главная']")  # Кнопка "Главная" Яндекс.Дзена (иконка "дом")
