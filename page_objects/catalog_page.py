from page_objects.base_page import BasePage
from page_objects.locators.catalog_page_locator import CatalogPageLocator


class CatalogPage(BasePage):
    path = "/camera"

    def open(self, url):
        self.browser.get(url + self.path)

    def verify_catalog_header(self):
        self.verify_element_presence(CatalogPageLocator.CATALOG_HEADER)

    def verify_header_text(self):
        self.verify_element_presence(CatalogPageLocator.HEADER_TEXT)

    def verify_list_view(self):
        self.verify_element_presence(CatalogPageLocator.LIST_VIEW)

    def verify_greed_view(self):
        self.verify_element_presence(CatalogPageLocator.GREED_VIEW)

    def verify_button_show(self):
        self.verify_element_presence(CatalogPageLocator.BUTTON_SHOW)

    def verify_button_sort_by(self):
        self.verify_element_presence(CatalogPageLocator.BUTTON_SORT_BY)

    def transition_to_Desktops(self):
        self.click_element(CatalogPageLocator.BUTTON_DESKTOPS)
        self.verify_element_presence(CatalogPageLocator.HEADER_DESKTOPS)

    def transition_to_Laptops_and_Notebooks(self):
        self.click_element(CatalogPageLocator.BUTTON_LAPTOPS_NOTEBOOKS)
        self.verify_element_presence(CatalogPageLocator.HEADER_LAPTOPS_NOTEBOOKS)

