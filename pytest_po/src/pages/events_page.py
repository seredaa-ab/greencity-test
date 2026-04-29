from selenium.webdriver.common.by import By
from pytest_po.src.pages.base_page import BasePage
from pytest_po.src.components.event_card import EventCard
from pytest_po.src.components.header import Header

class EventsPage(BasePage):

    EVENT_CARDS = (By.CSS_SELECTOR, "mat-card.event-list-item")

    def get_event_cards(self):
        elements = self.find_all(self.EVENT_CARDS)
        return [EventCard(self.driver, el) for el in elements]

    def get_header(self):
        return Header(self.driver)