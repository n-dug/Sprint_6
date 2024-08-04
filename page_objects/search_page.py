import allure
from page_objects.base_page import BasePage
from locators.search_page_locators import SearchPageLocators


class SearchPage(BasePage):
    @allure.step("Check for a visible main button at Dzen search page")
    def check_element_main_button(self):
        self.find_visible_element(SearchPageLocators.MAIN_BUTTON)
        self.check_element_displayed(SearchPageLocators.MAIN_BUTTON)
