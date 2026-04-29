import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.greencity.cx.ua/#/greenCity/events")
    driver.maximize_window()
    yield driver
    driver.quit()