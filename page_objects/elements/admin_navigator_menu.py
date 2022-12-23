from page_objects.base_page import BasePage
from page_objects.locators.admin_navigator_menu_locator import AdminNavigatorMenuLocator


class AdminNavigatorMenu(BasePage):
    def click_catalog_menu(self):
        self.click_element(AdminNavigatorMenuLocator.MENU_CATALOG)

    def click_product_catalog(self):
        self.click_element(AdminNavigatorMenuLocator.GATALOG_PRODUCT)

    def open_products_catalog(self):
        self.click_catalog_menu()
        self.click_product_catalog()
