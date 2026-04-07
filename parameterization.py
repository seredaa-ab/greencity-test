from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec # noqa
def test_registration_invalid_passwords(self):
    wait = self.wait

    test_data = ["123", "abcdef", "PASSWORD", "12345678"]

    register_btn = wait.until(
        Ec.element_to_be_clickable((By.CSS_SELECTOR, ".header_sign-up-btn"))
    )
    register_btn.click()

    form = wait.until(
        Ec.visibility_of_element_located((By.CSS_SELECTOR, "form.form-content-container"))
    )

    for password in test_data:
        password_input = form.find_element(By.CSS_SELECTOR, "input[formcontrolname='password']")
        confirm_input = form.find_element(By.CSS_SELECTOR, "input[formcontrolname='repeatPassword']")

        self.driver.execute_script(f"arguments[0].value = '{password}';", password_input)
        self.driver.execute_script(f"arguments[0].value = '{password}';", confirm_input)

        self.driver.execute_script("arguments[0].dispatchEvent(new Event('blur'));", password_input)

        self.assertIn("ng-invalid", password_input.get_attribute("class"))