from selenium.webdriver.common.by import By
from pytest_po.src.components.base_component import BaseComponent


class EventCard(BaseComponent):

    MORE_BTN = (By.CSS_SELECTOR, "button.secondary-global-button")

    def open_details(self):
        self.root.find_element(*self.MORE_BTN).click()