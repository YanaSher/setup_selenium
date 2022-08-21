from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def verify_element_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def click_element(self, locator: tuple):
        element = self.verify_element_presence(locator)
        #        element = self.browser.find_element(locator)
        element.click()

    def selection_from_drop_down_menu(self, locator_1: tuple, locator_2: tuple):
        self.click_element(locator_1)
        self.click_element(locator_2)

    def get_text(self, locator: tuple):
        element_text = self.verify_element_presence(locator).text
        return element_text

    def input_text(self, locator: tuple, text):
        element_text = self.verify_element_presence(locator)
        element_text.clear()
        element_text.send_keys(text)

    def alert_delete_product(self, browser):
        alert = Alert(browser)
        alert.accept()
