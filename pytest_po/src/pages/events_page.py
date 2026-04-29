from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.components.event_card import EventCard
from src.components.header import Header

class EventsPage(BasePage):

    EVENT_CARDS = (By.CSS_SELECTOR, "mat-card.event-list-item")

    def get_event_cards(self):
        elements = self.find_all(self.EVENT_CARDS)
        return [EventCard(self.driver, el) for el in elements]

    def get_header(self):
        return Header(self.driver, self.driver)