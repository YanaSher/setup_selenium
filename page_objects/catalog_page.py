import allure

from page_objects.base_page import BasePage
from page_objects.locators.catalog_page_locator import CatalogPageLocator


class CatalogPage(BasePage):
    path = "/camera"

    def open(self, url):
        self.browser.get(url + self.path)

    @allure.step("Проверка наличия заголовка")
    def verify_catalog_header(self):
        self.verify_element_presence(CatalogPageLocator.CATALOG_HEADER)

    @allure.step("Проверка соответствия названия заголовка - Cameras")
    def verify_header_text(self):
        self.verify_element_presence(CatalogPageLocator.HEADER_TEXT)

    @allure.step("Наличие элемента - отображение LIST")
    def verify_list_view(self):
        self.verify_element_presence(CatalogPageLocator.LIST_VIEW)

    @allure.step("Наличие элемента - отображение Greed")
    def verify_greed_view(self):
        self.verify_element_presence(CatalogPageLocator.GREED_VIEW)

    @allure.step("Наличие элемента - кнопка Show")
    def verify_button_show(self):
        self.verify_element_presence(CatalogPageLocator.BUTTON_SHOW)

    @allure.step("Наличие элемента - кнопка сортировки")
    def verify_button_sort_by(self):
        self.verify_element_presence(CatalogPageLocator.BUTTON_SORT_BY)

    @allure.step("Открытие каталога DESKTOPS")
    def transition_to_Desktops(self):
        self.click_element(CatalogPageLocator.BUTTON_DESKTOPS)
        self.verify_element_presence(CatalogPageLocator.HEADER_DESKTOPS)

    @allure.step("Открытие каталога LAPTOPS, NOTEBOOKS")
    def transition_to_Laptops_and_Notebooks(self):
        self.click_element(CatalogPageLocator.BUTTON_LAPTOPS_NOTEBOOKS)
        self.verify_element_presence(CatalogPageLocator.HEADER_LAPTOPS_NOTEBOOKS)
