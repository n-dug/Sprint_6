import allure
import pytest
from data import AnswersList, URL
from page_objects.main_page import MainPage
from conftest import driver
from page_objects.search_page import SearchPage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class TestMainPage:
    @allure.title('Click on Scooter logo leading to its main page"')
    @allure.description('''1)Click on order button
                        2)Click on scooter logo
                        3)Compare URLs and check visibility of the title''')
    def test_click_on_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.order_from_header()
        main_page.scooter_logo_click()
        current_url = main_page.get_current_url()
        title_displayed = main_page.check_main_title()
        assert current_url == URL.BASE_SCOOTER_URL and title_displayed

    @allure.title('Click on Yandex logo leading to Yandex Dzen main page"')
    @allure.description('''1)Click on "Yandex" logo
                        2)Switch to new browser tab
                        3)Comparing expected and current URL's and confirm "Main" button appears''')
    def test_click_on_yandex_logo(self, driver):
        main_page = MainPage(driver)
        search_page = SearchPage(driver)
        main_page.yandex_logo_click()
        main_page.switch_to_the_new_tab()
        WebDriverWait(driver, 5).until(ec.url_to_be(URL.SEARCH_DZEN_URL))
        assert search_page.check_element_main_button

    @allure.title('Matching FAQ: current and expected answer texts')
    @allure.description('''1)Scroll to FAQ;
                           2)Click on question;
                           3)Get an answer text;
                           4)Compare current and expected texts''')
    @pytest.mark.parametrize('num, expected_result',
                             [
                                 (0, AnswersList.answers_text[0]),
                                 (1, AnswersList.answers_text[1]),
                                 (2, AnswersList.answers_text[2]),
                                 (3, AnswersList.answers_text[3]),
                                 (4, AnswersList.answers_text[4]),
                                 (5, AnswersList.answers_text[5]),
                                 (6, AnswersList.answers_text[6]),
                                 (7, AnswersList.answers_text[7]),
                             ]
                             )
    def test_questions(self, driver, num, expected_result):
        main_page = MainPage(driver)
        main_page.accept_cookie()
        main_page.scroll_to_faq()
        result = main_page.click_on_question_and_get_answer(num)
        assert main_page.check_answer(result, expected_result)
