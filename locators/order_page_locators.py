from selenium.webdriver.common.by import By


class OrderPageLocators:
    name_input_field = (By.XPATH, "//input[@placeholder = '* Имя']")  # Поле ввода имени
    last_name_input_field = (By.XPATH, "//input[@placeholder = '* Фамилия']")  # Поле ввода фамилии
    address_input_field = (By.XPATH,  "//input[@placeholder = '* Адрес: куда привезти заказ']")  # Поле ввода адреса
    station_input_field = (By.XPATH, "//input[@placeholder = '* Станция метро']")  # Поле ввода станции метро
    chosen_station_field = (By.XPATH, ".//div[text() = 'Университет']")  # Поле с выбранной станцией
    phone_number_input_field = (By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']")  # Поле ввода номера телефона
    proceed_button = (By.XPATH, "//button[text() = 'Далее']")  # Кнопка "Далее"
    time_of_deliver_field = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")  # Поле ввода даты доставки
    rent_time_field = (By.XPATH, ".//span[@class='Dropdown-arrow']")  # Список времени аренды
    chosen_rent_time_field = (By.XPATH, ".//div[text() = 'трое суток']")  # Поле с выбранным временем
    scooter_grey_check_box = (By.ID, 'grey')  # Чек-бокс выбора серого цвета
    comment_for_courier_field = (By.XPATH, ".//input[@placeholder= 'Комментарий для курьера']")  # Поле комментария
    complete_order_button = (By.XPATH, ".//button[text()='Назад']/parent::div/button[text()='Заказать']")  # Кнопка "Заказать"
    yes_button = (By.XPATH, ".//button[contains(text(),'Да')]")  # Кнопка "Да" на форме подтверждения заказа
    order_completed_popup = (By.XPATH, ".//div[text() = 'Заказ оформлен']")  # Ответный текст "Заказ оформлен"
