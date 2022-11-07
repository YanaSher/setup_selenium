import logging
import allure

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.logger = logging.getLogger(type(self).__name__)
        # настройка обработчика и форматировщика
        file_handler = logging.FileHandler(f"logs/{self.browser.test_name}.log")
        file_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
        # добавление обработчика к логгеру
        self.logger.addHandler(file_handler)
        self.logger.setLevel(level=self.browser.log_level)

    def verify_element_presence(self, locator: tuple):
        try:
            self.logger.info(f"Wait {locator} to be visibility")
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.logger.info(f"Element {locator} is not visibility")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def click_element(self, locator: tuple):
        element = self.verify_element_presence(locator)
        self.logger.info(f"Click element {locator}")
        element.click()

    def selection_from_drop_down_menu(self, locator_1: tuple, locator_2: tuple):
        self.click_element(locator_1)
        self.click_element(locator_2)

    def get_text(self, locator: tuple):
        self.logger.info("Get text".format(locator))
        element_text = self.verify_element_presence(locator).text
        return element_text

    def input_text(self, locator: tuple, text):
        self.logger.info("Input {} in input {}".format(locator, text))
        element_text = self.verify_element_presence(locator)
        element_text.clear()
        element_text.send_keys(text)

    def alert_delete_product(self, browser):
        self.logger.info("Accept alert delete product")
        alert = Alert(browser)
        alert.accept()
