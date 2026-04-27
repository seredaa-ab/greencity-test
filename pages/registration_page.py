from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class RegistrationPage(BasePage):

    SIGN_UP_BTN = (By.CSS_SELECTOR, ".header_sign-up-btn")
    FORM = (By.CSS_SELECTOR, "form.form-content-container")

    EMAIL = (By.CSS_SELECTOR, "input[formcontrolname='email']")
    NAME = (By.CSS_SELECTOR, "input[formcontrolname='firstName']")
    PASSWORD = (By.CSS_SELECTOR, "input[formcontrolname='password']")
    REPEAT_PASSWORD = (By.CSS_SELECTOR, "input[formcontrolname='repeatPassword']")
    SUBMIT_BTN = (By.CSS_SELECTOR, "button.greenStyle")

    def open_form(self):
        self.wait.until(
            EC.element_to_be_clickable(self.SIGN_UP_BTN)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(self.FORM)
        )

    def fill_form(self, email, name, password):
        form = self.wait.until(
            EC.visibility_of_element_located(self.FORM)
        )

        form.find_element(*self.EMAIL).send_keys(email)
        form.find_element(*self.NAME).send_keys(name)
        form.find_element(*self.PASSWORD).send_keys(password)
        form.find_element(*self.REPEAT_PASSWORD).send_keys(password)

    def is_submit_enabled(self):
        btn = self.wait.until(
            EC.presence_of_element_located(self.SUBMIT_BTN)
        )
        return btn.is_enabled()

    def is_password_error_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_LABEL)
        ).is_displayed()