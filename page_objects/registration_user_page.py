from page_objects.base_page import BasePage
from page_objects.locators.registration_user_locator import RegistrationUserLocator
from randomaizer import random_string, random_email, random_telefone_number

class RegistrationUserPage(BasePage):
    def transition_to_Registration_User(self):
        self.click_element(RegistrationUserLocator.MI_ACCOUNT)
        self.click_element(RegistrationUserLocator.REGISTER_LINK)

    def verify_header(self):
        self.verify_element_presence(RegistrationUserLocator.HEADER_TEXT)

    def verify_first_name_input(self):
        self.verify_element_presence(RegistrationUserLocator.FIRST_NAME_INPUT)

    def verify_last_name_input(self):
        self.verify_element_presence(RegistrationUserLocator.LAST_NAME_INPUT)

    def verify_email_input(self):
        self.verify_element_presence(RegistrationUserLocator.EMAIL_INPUT)

    def verify_telephone_input(self):
        self.verify_element_presence(RegistrationUserLocator.TELEPHONE_INPUT)

    def verify_password_input(self):
        self.verify_element_presence(RegistrationUserLocator.PASSWORD_INPUT)

    def verify_confirm_password_input(self):
        self.verify_element_presence(RegistrationUserLocator.CONFIRM_PASSWORD_INPUT)

    def verify_check_box_policy(self):
        self.verify_element_presence(RegistrationUserLocator.CHECK_BOX_POLICY)

    def verify_policy_link(self):
        self.verify_element_presence(RegistrationUserLocator.POLICY_LINK)

    def veify_continue_button(self):
        self.verify_element_presence(RegistrationUserLocator.CONTINUE_BUTTON)

    def input_first_name(self):
        self.input_text(RegistrationUserLocator.FIRST_NAME_INPUT, random_string(7))

    def input_last_name(self):
        self.input_text(RegistrationUserLocator.LAST_NAME_INPUT, random_string(11))

    def input_email(self):
        self.input_text(RegistrationUserLocator.EMAIL_INPUT, random_email(7, 5))

    def input_telephone(self):
        self.input_text(RegistrationUserLocator.TELEPHONE_INPUT, random_telefone_number())

    def input_password(self, text):
        self.input_text(RegistrationUserLocator.PASSWORD_INPUT, text)

    def input_confirm_password(self, text):
        self.input_text(RegistrationUserLocator.CONFIRM_PASSWORD_INPUT, text)

    def click_check_box(self):
        self.click_element(RegistrationUserLocator.CHECK_BOX_POLICY)

    def click_button_continue(self):
        self.click_element(RegistrationUserLocator.CONTINUE_BUTTON)
