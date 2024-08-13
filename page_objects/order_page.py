import allure
from locators.order_page_locators import OrderPageLocators
from page_objects.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Send customer name')
    def send_name_to_name_input(self, text):
        self.send_text_to_field(OrderPageLocators.name_input_field, text)

    @allure.step('Send last name')
    def send_last_name_to_last_name_input(self, text):
        self.send_text_to_field(OrderPageLocators.last_name_input_field, text)

    @allure.step('Send delivery address')
    def send_address_to_address_input(self, text):
        self.send_text_to_field(OrderPageLocators.address_input_field, text)

    @allure.step('Send station')
    def send_subway_to_station_input(self, text):
        self.click_on_element(OrderPageLocators.station_input_field)
        self.send_text_to_field(OrderPageLocators.station_input_field, text)
        self.click_on_element(OrderPageLocators.chosen_station_field)

    @allure.step('Send phone number')
    def send_phone_number_to_number_input_field(self, text):
        self.send_text_to_field(OrderPageLocators.phone_number_input_field, text)

    @allure.step('Click on "Proceed" button of order form')
    def click_on_proceed_button(self):
        self.click_on_element(OrderPageLocators.proceed_button)

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
        self.click_on_element(OrderPageLocators.time_of_deliver_field)
        self.send_text_to_field(OrderPageLocators.time_of_deliver_field, text)

    @allure.step('Set rent time')
    def rent_time_choose(self):
        self.click_on_element(OrderPageLocators.rent_time_field)
        self.click_on_element(OrderPageLocators.chosen_rent_time_field)

    @allure.step('Set grey scooter color')
    def scooter_colour_choose(self):
        self.click_on_element(OrderPageLocators.scooter_grey_check_box)

    @allure.step('Send comment for courier')
    def send_comment_to_comment_input(self, text):
        self.send_text_to_field(OrderPageLocators.comment_for_courier_field, text)

    @allure.step('Click on "Order" button to complete order')
    def finish_order(self):
        self.click_on_element(OrderPageLocators.complete_order_button)

    @allure.step('Completely fill second part of order form')
    def complete_filling_of_order_form(self, text):
        self.send_deliver_date_to_delivery_input(text[6])
        self.rent_time_choose()
        self.scooter_colour_choose()
        self.send_comment_to_comment_input(text[7])
        self.finish_order()

    @allure.step('Click "Yes" button')
    def click_yes(self):
        self.click_on_element(OrderPageLocators.yes_button)

    @allure.step('Confirm an order')
    def confirm_order(self, user_1):
        self.fill_order_form(user_1)
        self.complete_filling_of_order_form(user_1)
        self.click_yes()

    @allure.step('Show popup of completed order')
    def show_order_completed_popup(self):
        return self.find_visible_element(OrderPageLocators.order_completed_popup).is_displayed()
