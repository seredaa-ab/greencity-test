from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class EventsPage(BasePage):

    EVENT_CARDS = (By.CSS_SELECTOR, "mat-card.event-list-item")
    MORE_BTN = (By.CSS_SELECTOR, "button.secondary-global-button")
    EVENT_DETAIL = (By.CSS_SELECTOR, "app-event-details, .event-detail")

    def get_events(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(self.EVENT_CARDS)
        )

    def open_first_event(self):
        events = self.get_events()
        events[0].find_element(*self.MORE_BTN).click()

    def is_event_detail_opened(self):
        return self.wait.until(
            EC.presence_of_element_located(self.EVENT_DETAIL)
        )