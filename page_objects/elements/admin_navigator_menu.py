from page_objects.base_page import BasePage
from page_objects.locators.admin_navigator_menu_locator import AdminNavigatorMenuLocator


class AdminNavigatorMenu(BasePage):
    def click_catalog_menu(self):
        self.click_element(AdminNavigatorMenuLocator.MENU_CATALOG)

    def click_product_catalog(self):
        self.click_element(AdminNavigatorMenuLocator.GATALOG_PRODUCT)

    def click_system_menu(self):
        self.click_element(AdminNavigatorMenuLocator.MENU_SYSTEM)

    def click_users_menu(self):
        self.click_element(AdminNavigatorMenuLocator.SYSTEM_USERS)

    def click_users_catalog(self):
        self.click_element(AdminNavigatorMenuLocator.USERS_USERS)

    def open_products_catalog(self):
        self.click_catalog_menu()
        self.click_product_catalog()

    def open_users_catalog(self):
        self.click_system_menu()
        self.click_users_menu()
        self.click_users_catalog()
