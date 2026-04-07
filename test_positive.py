import unittest
import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EventsPageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.greencity.cx.ua/#/greenCity/events")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

# TC Positive 1: Відкриття детальної сторінки події
    def test_open_event_detail(self):
        wait = self.wait

        # 1. Чекаємо картки подій
        event_cards = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "mat-card.event-list-item"))
        )
        self.assertGreater(len(event_cards), 0, "Події не завантажились")

        # 2. Клікаємо "Більше"
        more_button = event_cards[0].find_element(By.CSS_SELECTOR, "button.secondary-global-button")
        more_button.click()

        # 3. Перевірка відкриття деталей
        event_detail = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "app-event-details, .event-detail"))
        )
        self.assertTrue(event_detail.is_displayed())

# TC Positive 2: Успішна активація кнопки реєстрації
    def test_registration_button(self):
        wait = self.wait

        # 1. Відкрити форму
        register_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".header_sign-up-btn"))
        )
        register_btn.click()

        # 2. Чекаємо форму
        form = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "form.form-content-container"))
        )

        # 3. Знаходимо інпути
        email_input = form.find_element(By.CSS_SELECTOR, "input[formcontrolname='email']")
        name_input = form.find_element(By.CSS_SELECTOR, "input[formcontrolname='firstName']")
        password_input = form.find_element(By.CSS_SELECTOR, "input[formcontrolname='password']")
        confirm_input = form.find_element(By.CSS_SELECTOR, "input[formcontrolname='repeatPassword']")

        # 4. Вводимо валідні дані
        def fill_input(driver, element, value):
            driver.execute_script("arguments[0].value = arguments[1];", element, value)
            driver.execute_script("arguments[0].dispatchEvent(new Event('input'));", element)
            driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", element)

        fill_input(self.driver, email_input, "testemail@gmail.com")
        fill_input(self.driver, name_input, "TestUser")
        fill_input(self.driver, password_input, "Password1!")
        fill_input(self.driver, confirm_input, "Password1!")

        # тригеримо Angular
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('input'));", password_input)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('input'));", confirm_input)

        # 5. Перевірка, що кнопка стала активною
        submit_btn = form.find_element(By.CSS_SELECTOR, "button.greenStyle")
        self.assertTrue(submit_btn.is_enabled(), "Кнопка не активувалась")
        submit_btn.click()
        print(submit_btn.get_attribute("disabled"))

#  TC Positive 3: Перехід на головну через логотип
    def test_logo_redirect(self):
        wait = self.wait

        # 1. Клік по логотипу
        logo = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".header_logo"))
        )
        logo.click()

        # 2. Перевірка URL (надійніше ніж title)
        wait.until(lambda d: "#/greenCity" in d.current_url)

        # 3. Перевірка елемента головної сторінки
        start_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(), 'Почати формувати звичку')]")
            )
        )
        self.assertTrue(start_button.is_displayed())


if __name__ == "__main__":
    unittest.main()