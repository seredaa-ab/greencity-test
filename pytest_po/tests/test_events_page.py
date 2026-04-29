import allure
from src.pages.events_page import EventsPage


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