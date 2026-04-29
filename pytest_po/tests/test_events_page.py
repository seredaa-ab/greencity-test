import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pytest_po.src.pages.events_page import EventsPage


@allure.feature("Events Page")
class TestEvents:

    @allure.story("Open event details")
    def test_open_event_detail(self, driver):
        page = EventsPage(driver)

        with allure.step("Get events"):
            events = page.get_event_cards()
            assert len(events) > 0

        with allure.step("Open first event"):
            events[0].open_details()

    @allure.story("Open registration")
    def test_open_registration(self, driver):
        page = EventsPage(driver)
        header = page.get_header()

        with allure.step("Click registration"):
            header.open_registration()

    @allure.story("Redirect to home page via logo")
    def test_logo_redirect(self, driver):
        page = EventsPage(driver)
        header = page.get_header()

        with allure.step("Click logo"):
            header.click_logo()

        with allure.step("Verify redirect"):
            assert "#/greenCity" in driver.current_url

        with allure.step("Check main page element"):
            btn = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[contains(text(),'Почати формувати звичку')]")
                )
            )
            assert btn.is_displayed()