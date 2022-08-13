from page_objects.base_page import BasePage
from page_objects.locators.main_page_locator import MainPageLocators

class MainPage(BasePage):
    def verify_top_menu(self):
        self.verify_element_presence(MainPageLocators.TOP_MENU)

    def verify_input_search(self):
        self.verify_element_presence(MainPageLocators.INPUT_SEARCH)

    def verify_button_search(self):
        self.verify_element_presence(MainPageLocators.BUTTON_SEARCH)

    def verify_button_basket(self):
        self.verify_element_presence(MainPageLocators.BASKET_BUTTON)

    def verify_logo(self):
        self.verify_element_presence(MainPageLocators.LOGO)

