import allure
from locators.order_page_locators import OrderPageLocators
from page_objects.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Send customer name')
    def send_name_to_name_input(self, text):
        self.send_text_to_field(OrderPageLocators.NAME_INPUT_FIELD, text)

    @allure.step('Send last name')
    def send_last_name_to_last_name_input(self, text):
        self.send_text_to_field(OrderPageLocators.LAST_NAME_INPUT_FIELD, text)

    @allure.step('Send delivery address')
    def send_address_to_address_input(self, text):
        self.send_text_to_field(OrderPageLocators.ADDRESS_INPUT_FIELD, text)

    @allure.step('Send station')
    def send_subway_to_station_input(self, text):
        self.click_on_element(OrderPageLocators.STATION_INPUT_FIELD)
        self.send_text_to_field(OrderPageLocators.STATION_INPUT_FIELD, text)
        self.click_on_element(OrderPageLocators.CHOSEN_STATION_FIELD)

    @allure.step('Send phone number')
    def send_phone_number_to_number_input_field(self, text):
        self.send_text_to_field(OrderPageLocators.PHONE_NUMBER_INPUT_FIELD, text)

    @allure.step('Click on "Proceed" button of order form')
    def click_on_proceed_button(self):
        self.click_on_element(OrderPageLocators.PROCEED_BUTTON)

    @allure.step('Complete 1st part of order form')
    def fill_order_form(self, user_1):
        self.send_name_to_name_input(user_1[1])
        self.send_last_name_to_last_name_input(user_1[2])
        self.send_address_to_address_input(user_1[3])
        self.send_subway_to_station_input(user_1[4])
        self.send_phone_number_to_number_input_field(user_1[5])
        self.click_on_proceed_button()

    @allure.step('Set delivery date')
    def send_deliver_date_to_delivery_input(self, text):
        self.click_on_element(OrderPageLocators.TIME_OF_DELIVER_FIELD)
        self.send_text_to_field(OrderPageLocators.TIME_OF_DELIVER_FIELD, text)

    @allure.step('Set rent time')
    def rent_time_choose(self):
        self.click_on_element(OrderPageLocators.RENT_TIME_FIELD)
        self.click_on_element(OrderPageLocators.CHOSEN_RENT_TIME_FIELD)

    @allure.step('Set grey scooter color')
    def scooter_colour_choose(self):
        self.click_on_element(OrderPageLocators.SCOOTER_GREY_CHECK_BOX)

    @allure.step('Send comment for courier')
    def send_comment_to_comment_input(self, text):
        self.send_text_to_field(OrderPageLocators.COMMENT_FOR_COURIER_FIELD, text)

    @allure.step('Click on "Order" button to complete order')
    def finish_order(self):
        self.click_on_element(OrderPageLocators.COMPLETE_ORDER_BUTTON)

    @allure.step('Completely fill second part of order form')
    def complete_filling_of_order_form(self, text):
        self.send_deliver_date_to_delivery_input(text[6])
        self.rent_time_choose()
        self.scooter_colour_choose()
        self.send_comment_to_comment_input(text[7])
        self.finish_order()

    @allure.step('Click "Yes" button')
    def click_yes(self):
        self.click_on_element(OrderPageLocators.YES_BUTTON)

    @allure.step('Confirm an order')
    def confirm_order(self, user_1):
        self.fill_order_form(user_1)
        self.complete_filling_of_order_form(user_1)
        self.click_yes()

    @allure.step('Show popup of completed order')
    def show_order_completed_popup(self):
        return self.find_visible_element(OrderPageLocators.ORDER_COMPLETED_POPUP).is_displayed()
