from data import Users
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage
import allure
from conftest import driver


class TestOrderPage:
    @allure.title('Test "Place an order by a header button"')
    @allure.description('''1)Click on the order button;
                        2)Complete the 1st part of the form;
                        3)Complete the 2nd part of the form;
                        4)Confirm an order;
                        5)Wait for popup of an order's confirmation to show''')
    def test_order_by_header_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.accept_cookie()
        main_page.order_from_header()
        order_page.confirm_order(Users.user_1)
        assert order_page.show_order_completed_popup()

    @allure.title('Test "Place an order by a page button"')
    @allure.description('''1)Click on the order button;
                        2)Complete the 1st part of the form;
                        3)Complete the 2nd part of the form;
                        4)Confirm an order;
                        5)Wait for popup of an order's confirmation to show''')
    def test_order_by_page_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.accept_cookie()
        main_page.order_from_page()
        order_page.confirm_order(Users.user_2)
        assert order_page.show_order_completed_popup()
