import pytest
import allure
from selenium import webdriver
from data import URL


@allure.step('Open a new table in Firefox browser. Visit Yandex.Scooter. Close the browser')
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.fullscreen_window()
    driver.get(URL.BASE_SCOOTER_URL)
    yield driver
    driver.quit()

