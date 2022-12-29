import allure

from page_objects.base_page import BasePage
from page_objects.locators.main_page_locator import MainPageLocators


class MainPage(BasePage):
    @allure.step("Проверка наличия меню")
    def verify_top_menu(self):
        self.verify_element_presence(MainPageLocators.TOP_MENU)

    @allure.step("Проверка наличия строки поиска")
    def verify_input_search(self):
        self.verify_element_presence(MainPageLocators.INPUT_SEARCH)

    @allure.step("Проверка наличия кнопки поиска")
    def verify_button_search(self):
        self.verify_element_presence(MainPageLocators.BUTTON_SEARCH)

    @allure.step("Проверка наличия кнопки корзины")
    def verify_button_basket(self):
        self.verify_element_presence(MainPageLocators.BASKET_BUTTON)

    @allure.step("Проверка наличия лого")
    def verify_logo(self):
        self.verify_element_presence(MainPageLocators.LOGO)

    @allure.step("Смена валюты на EURO")
    def selection_euro(self):
        self.selection_from_drop_down_menu(MainPageLocators.FORM_CURRENCY, MainPageLocators.EURO_CURRENCY)

    @allure.step("Смена валюты на GBP")
    def selection_gbp(self):
        self.selection_from_drop_down_menu(MainPageLocators.FORM_CURRENCY, MainPageLocators.GBP_CURRENCY)

    @allure.step("Смена валюты на USD")
    def selection_usd(self):
        self.selection_from_drop_down_menu(MainPageLocators.FORM_CURRENCY, MainPageLocators.USD_CURRENCY)

    @allure.step("Проверка, что валюта сменилась")
    def verify_chosen_valut(self, symbol):
        currency_symbol = self.get_text(MainPageLocators.CURRENCY_SYMBOL)
        assert currency_symbol == symbol
