import allure
from locators.main_page_locators import MainPageLocators
from page_objects.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Click on Yandex logo')
    def yandex_logo_click(self):
        self.click_on_element(MainPageLocators.YANDEX_LOGO)

    @allure.step('Click on Scooter logo')
    def scooter_logo_click(self):
        self.click_on_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Click on "Order" header button')
    def order_from_header(self):
        self.click_on_element(MainPageLocators.HEADER_ORDER_BUTTON)

    @allure.step('Check for "Training simulator" header text')
    def check_main_title(self):
        return self.find_visible_element(MainPageLocators.SCOOTER_TEXT).is_displayed()

    @allure.step('Click on "Accept cookies" button')
    def accept_cookie(self):
        self.find_visible_element(MainPageLocators.COOKIE_BUTTON)
        self.click_on_element(MainPageLocators.COOKIE_BUTTON)

    @allure.step('Click "Order" page button')
    def order_from_page(self):
        self.scroll_to_locator(MainPageLocators.HOMEPAGE_ORDER_BUTTON)
        self.check_element_displayed(MainPageLocators.HOMEPAGE_ORDER_BUTTON)
        self.click_on_element(MainPageLocators.HOMEPAGE_ORDER_BUTTON)

    @allure.step('Scroll to FAQ')
    def scroll_to_faq(self):
        self.scroll_to_locator(MainPageLocators.FAQ)

    @allure.step('Click on FAQ questions')
    def click_on_question(self, num):
        formatted_q_locator = self.formatting_locator(MainPageLocators.QUESTION_LOCATOR, num)
        self.click_on_element(formatted_q_locator)

    @allure.step('Get answers from FAQ')
    def get_answers_text(self, num):
        formatted_a_locator = self.formatting_locator(MainPageLocators.ANSWER_LOCATOR, num)
        text = self.get_text_of_element(formatted_a_locator)
        return text

    def click_on_question_and_get_answer(self, num):
        self.click_on_question(num)
        return self.get_answers_text(num)

    @staticmethod
    def check_answer(result, expected):
        return result == expected
