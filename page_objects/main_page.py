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

    # смена валюты
    def selection_euro(self):
        self.selection_from_drop_down_menu(MainPageLocators.FORM_CURRENCY, MainPageLocators.EURO_CURRENCY)

    def selection_gbp(self):
        self.selection_from_drop_down_menu(MainPageLocators.FORM_CURRENCY, MainPageLocators.GBP_CURRENCY)

    def selection_usd(self):
        self.selection_from_drop_down_menu(MainPageLocators.FORM_CURRENCY, MainPageLocators.USD_CURRENCY)

    def verify_chosen_valut(self, symbol):
        currency_symbol = self.get_text(MainPageLocators.CURRENCY_SYMBOL)
        assert currency_symbol == symbol
