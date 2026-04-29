from selenium.webdriver.common.by import By
from src.components.base_component import BaseComponent

class Header(BaseComponent):

    SIGN_UP_BTN = (By.CSS_SELECTOR, ".header_sign-up-btn")

    def open_registration(self):
        self.click(self.SIGN_UP_BTN)