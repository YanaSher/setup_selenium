from randomaizer import random_string, random_email
from page_objects.base_page import BasePage
from page_objects.locators.admin_system_page_locator import AdminSystemPageLocator

class AdminSystemPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.text_name = "Igor"

    def click_add_product_button(self):
        self.click_element(AdminSystemPageLocator.ADD_USER_BUTTON)

    #def input_user_name(self):
     #   self.input_text(AdminSystemPageLocator.INPUT_USER_NAME, self.text_name)

    def input_user_name(self, text):
        self.input_text(AdminSystemPageLocator.INPUT_USER_NAME, text)

    def input_first_name(self):
        self.input_text(AdminSystemPageLocator.FIRST_NAME_INPUT, random_string(7))

    def input_last_name(self):
        self.input_text(AdminSystemPageLocator.LAST_NAME_INPUT, random_string(11))

    def input_email(self):
        self.input_text(AdminSystemPageLocator.EMAIL_INPUT, random_email(7, 5))

    def input_password(self, text):
        self.input_text(AdminSystemPageLocator.PASSWORD_INPUT, text)

    def input_confirm_password(self, text):
        self.input_text(AdminSystemPageLocator.CONFIRM_PASSWORD_INPUT, text)

    def choise_user_group_demonstration(self):
        self.click_element(AdminSystemPageLocator.INPUT_USER_GROUP)
        self.click_element(AdminSystemPageLocator.CHOICE_GROUP_DEMONSTRATION)

    def choise_status_enabled(self):
        self.click_element(AdminSystemPageLocator.INPUT_STATUS)
        self.click_element(AdminSystemPageLocator.CHOISE_STATUS_ENABLED)

    def click_save_button(self):
        self.click_element(AdminSystemPageLocator.SAVE_BUTTON)

    def verify_success_message(self):
        success_message = self.get_text(AdminSystemPageLocator.SUCCESS_MESSAGE)
        success_message = success_message[:-2]
        assert success_message == "Success: You have modified users!"

    def click_check_box(self, username):
        self.click_element(AdminSystemPageLocator.CHECK_BOX_IN_USER_TABLE(username))

    def click_delete_user_button(self):
        self.click_element(AdminSystemPageLocator.DELETE_USER_BUTTON)

    def click_cancel_delete_user_button(self):
        self.click_element(AdminSystemPageLocator.CANSEL_BUTTON)

    def warning_success_message(self):
        success_message = self.get_text(AdminSystemPageLocator.SUCCESS_MESSAGE)
        success_message = success_message[:-2]
        assert success_message == "Warning: Username is already in use!"
