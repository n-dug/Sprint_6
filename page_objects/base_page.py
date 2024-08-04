from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):  # Получение текущего URL
        return self.driver.current_url

    def find_visible_element(self, locator):  # Поиск видимого элемента
        WebDriverWait(
            self.driver, 5).until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def get_text_of_element(self, locator):  # Получить текст из элемента
        return self.find_visible_element(locator).text

    def check_element_displayed(self, locator):  # Проверка отображения элемента
        return self.find_visible_element(locator).is_displayed()

    def check_element_clickable(self, locator):  # Проверка возможности клика по элементу
        return WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(locator))

    def click_on_element(self, locator):  # Клик по элементу
        self.check_element_clickable(locator)
        self.find_visible_element(locator).click()

    def send_text_to_field(self, locator, text):  # Заполнение поля значением
        self.find_visible_element(locator).send_keys(text)

    def scroll_to_locator(self, locator):  # Скролл к элементу
        element = self.find_visible_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_to_the_new_tab(self):  # Открыть новую вкладку
        self.driver.switch_to.window(self.driver.window_handles[1])

    def formatting_locator(self, locator, num):  # Форматирование универсального локатора
        method, locator = locator
        locator = locator.format(num)
        return (method, locator)
