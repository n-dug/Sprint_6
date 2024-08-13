from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT_FIELD = (By.XPATH, "//input[@placeholder = '* Имя']")  # Поле ввода имени
    LAST_NAME_INPUT_FIELD = (By.XPATH, "//input[@placeholder = '* Фамилия']")  # Поле ввода фамилии
    ADDRESS_INPUT_FIELD = (By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']")  # Поле ввода адреса
    STATION_INPUT_FIELD = (By.XPATH, "//input[@placeholder = '* Станция метро']")  # Поле ввода станции метро
    CHOSEN_STATION_FIELD = (By.XPATH, ".//div[text() = 'Университет']")  # Поле с выбранной станцией
    PHONE_NUMBER_INPUT_FIELD = (By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']")  # Поле ввода номера телефона
    PROCEED_BUTTON = (By.XPATH, "//button[text() = 'Далее']")  # Кнопка "Далее"
    TIME_OF_DELIVER_FIELD = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")  # Поле ввода даты доставки
    RENT_TIME_FIELD = (By.XPATH, ".//span[@class='Dropdown-arrow']")  # Список времени аренды
    CHOSEN_RENT_TIME_FIELD = (By.XPATH, ".//div[text() = 'трое суток']")  # Поле с выбранным временем
    SCOOTER_GREY_CHECK_BOX = (By.ID, 'grey')  # Чек-бокс выбора серого цвета
    COMMENT_FOR_COURIER_FIELD = (By.XPATH, ".//input[@placeholder= 'Комментарий для курьера']")  # Поле комментария
    COMPLETE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Назад']/parent::div/button[text()='Заказать']")  # Кнопка "Заказать"
    YES_BUTTON = (By.XPATH, ".//button[contains(text(),'Да')]")  # Кнопка "Да" на форме подтверждения заказа
    ORDER_COMPLETED_POPUP = (By.XPATH, ".//div[text() = 'Заказ оформлен']")  # Ответный текст "Заказ оформлен"
