from randomaizer import random_string
from page_objects.base_page import BasePage
from page_objects.locators.admin_producte_page_locator import AdminProductePageLocator


class AdminProductPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        #       self.text_name = random_string(10)
        self.text_name = "NjaiFas"

    def click_add_product_button(self):
        self.click_element(AdminProductePageLocator.ADD_PRODYCT_BUTTON)

    def input_product_name(self):
        self.input_text(AdminProductePageLocator.INPUT_PRODUCT_NAME, self.text_name)

    def input_meta_tag_title(self):
        self.input_text(AdminProductePageLocator.INPUT_MEGA_TAG_TITLE, random_string(8))

    def click_tab_data(self):
        self.click_element(AdminProductePageLocator.DATA_TAB)

    def input_model(self):
        self.input_text(AdminProductePageLocator.INPUT_MODEL, random_string(5))

    def click_save_button(self):
        self.click_element(AdminProductePageLocator.SAVE_BUTTON)

    def verify_success_message(self):
        success_message = self.get_text(AdminProductePageLocator.SUCCESS_MESSAGE)
        success_message = success_message[:-2]
        assert success_message == "Success: You have modified products!"

    def find_product_name(self):
        self.input_text(AdminProductePageLocator.INPUT_PRODUCT_NAME_IN_FILTER, self.text_name)

    def click_filter_button(self):
        self.click_element(AdminProductePageLocator.BUTTON_FILTER)

    def click_check_box(self):
        self.click_element(AdminProductePageLocator.CHECK_BOX_IN_PRODUCT_TABLE)

    def click_delete_product_button(self):
        self.click_element(AdminProductePageLocator.DELETE_PRODUCT_BUTTON)
