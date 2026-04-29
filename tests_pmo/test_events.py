import unittest
from selenium import webdriver

from tests_pmo.pages import EventsPage
from tests_pmo.pages.registration_page import RegistrationPage
from tests_pmo.pages import HomePage


class EventsPageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.greencity.cx.ua/#/greenCity/events")

        self.events = EventsPage(self.driver)
        self.registration = RegistrationPage(self.driver)
        self.home = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    # TC 1
    def test_open_event_detail(self):
        events = self.events.get_events()
        self.assertGreater(len(events), 0)

        self.events.open_first_event()

        detail = self.events.is_event_detail_opened()
        self.assertTrue(detail.is_displayed())

    # TC 2
    def test_registration_button(self):
        self.registration.open_form()
        self.registration.fill_form(
            "test@gmail.com",
            "TestUser",
            "Password1!"
        )

        self.assertTrue(self.registration.is_submit_enabled())

    # TC 3
    def test_logo_redirect(self):
        self.home.open_home()

        self.home.is_home_loaded()
        self.assertIn("#/greenCity", self.driver.current_url)

if __name__ == "__main__":
    unittest.main()