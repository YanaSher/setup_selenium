from page_objects.base_page import BasePage
from page_objects.locators.registration_user_locator import RegistrationUserLocator


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
