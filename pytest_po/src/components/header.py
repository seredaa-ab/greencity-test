from selenium.webdriver.common.by import By
from pytest_po.src.components.base_component import BaseComponent
from selenium.webdriver.support import expected_conditions as EC

class Header(BaseComponent):

    SIGN_UP_BTN = (By.CSS_SELECTOR, ".header_sign-up-btn")
    LOGO = (By.CSS_SELECTOR, ".header_logo")

    def open_registration(self):
        self.wait.until(
            EC.element_to_be_clickable(self.SIGN_UP_BTN)
        ).click()

    def click_logo(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGO)
        ).click()