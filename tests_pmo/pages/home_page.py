from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from tests_pmo.pages.base_page import BasePage


class HomePage(BasePage):

    LOGO = (By.CSS_SELECTOR, ".header_logo")
    START_BTN = (By.XPATH, "//button[contains(text(),'Почати формувати звичку')]")

    def open_home(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGO)
        ).click()

    def is_home_loaded(self):
        return self.wait.until(
            EC.presence_of_element_located(self.START_BTN)
        )