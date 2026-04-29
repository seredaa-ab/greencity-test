from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseComponent:
    def __init__(self, driver, root=None):
        self.driver = driver
        self.root = root if root else driver
        self.wait = WebDriverWait(driver, 20)

    def find(self, locator):
        return self.root.find_element(*locator)

    def find_all(self, locator):
        return self.root.find_elements(*locator)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()