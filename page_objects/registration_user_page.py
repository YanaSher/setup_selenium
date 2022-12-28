import allure

from page_objects.base_page import BasePage
from page_objects.locators.registration_user_locator import RegistrationUserLocator
from randomaizer import random_string, random_email, random_telefone_number


class RegistrationUserPage(BasePage):
    @allure.step("Переход к странице регистрации юзера")
    def transition_to_Registration_User(self):
        self.click_element(RegistrationUserLocator.MI_ACCOUNT)
        self.click_element(RegistrationUserLocator.REGISTER_LINK)

    @allure.step("Проверка наличия заголовка")
    def verify_header(self):
        self.verify_element_presence(RegistrationUserLocator.HEADER_TEXT)

    @allure.step("Проверка наличия поля ввода имени")
    def verify_first_name_input(self):
        self.verify_element_presence(RegistrationUserLocator.FIRST_NAME_INPUT)

    @allure.step("Проверка наличия поля ввода фамилии")
    def verify_last_name_input(self):
        self.verify_element_presence(RegistrationUserLocator.LAST_NAME_INPUT)

    @allure.step("Проверка наличия поля ввода почты")
    def verify_email_input(self):
        self.verify_element_presence(RegistrationUserLocator.EMAIL_INPUT)

    @allure.step("Проверка наличия поля ввода телефона")
    def verify_telephone_input(self):
        self.verify_element_presence(RegistrationUserLocator.TELEPHONE_INPUT)

    @allure.step("Проверка наличия поля ввода пароля")
    def verify_password_input(self):
        self.verify_element_presence(RegistrationUserLocator.PASSWORD_INPUT)

    @allure.step("Проверка наличия поля ввода подтверждения пароля")
    def verify_confirm_password_input(self):
        self.verify_element_presence(RegistrationUserLocator.CONFIRM_PASSWORD_INPUT)

    @allure.step("Проверка наличия чекбокса принятия политики конфидициальности")
    def verify_check_box_policy(self):
        self.verify_element_presence(RegistrationUserLocator.CHECK_BOX_POLICY)

    @allure.step("Проверка наличия ссылки на политики")
    def verify_policy_link(self):
        self.verify_element_presence(RegistrationUserLocator.POLICY_LINK)

    @allure.step("Проверка наличия кнопки продолжения")
    def veify_continue_button(self):
        self.verify_element_presence(RegistrationUserLocator.CONTINUE_BUTTON)

    @allure.step("Ввод имени")
    def input_first_name(self):
        self.input_text(RegistrationUserLocator.FIRST_NAME_INPUT, random_string(7))

    @allure.step("Ввод фамилии")
    def input_last_name(self):
        self.input_text(RegistrationUserLocator.LAST_NAME_INPUT, random_string(11))

    @allure.step("Ввод почты")
    def input_email(self):
        self.input_text(RegistrationUserLocator.EMAIL_INPUT, random_email(7, 5))

    @allure.step("Ввод телефонного номера")
    def input_telephone(self):
        self.input_text(RegistrationUserLocator.TELEPHONE_INPUT, random_telefone_number(11))

    @allure.step("Ввод пароля")
    def input_password(self, text):
        self.input_text(RegistrationUserLocator.PASSWORD_INPUT, text)

    @allure.step("Ввод подтверждения пароля")
    def input_confirm_password(self, text):
        self.input_text(RegistrationUserLocator.CONFIRM_PASSWORD_INPUT, text)

    @allure.step("Клик по чекбоксу политики")
    def click_check_box(self):
        self.click_element(RegistrationUserLocator.CHECK_BOX_POLICY)

    @allure.step("Нажатие кнопки продолжение")
    def click_button_continue(self):
        self.click_element(RegistrationUserLocator.CONTINUE_BUTTON)
