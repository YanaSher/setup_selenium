import allure

from randomaizer import random_string, random_email, random_telefone_number
from page_objects.base_page import BasePage
from page_objects.locators.admin_customers_page_locator import AdminCustomersPageLocator



class AdminCustomerPage(BasePage):

    @allure.step("Нажатие кнопки - добавление кастомера")
    def click_add_customers_button(self):
        self.click_element(AdminCustomersPageLocator.ADD_CUSTOMERS_BUTTON)

    @allure.step("Ввод имени кастомера")
    def input_first_name(self, text):
        self.input_text(AdminCustomersPageLocator.FIRST_NAME_INPUT, text)

    @allure.step("Ввод фамилии кастомера")
    def input_last_name(self, text):
        self.input_text(AdminCustomersPageLocator.LAST_NAME_INPUT, text)

    @allure.step("Ввод фамилии кастомера")
    def input_email(self):
        self.input_text(AdminCustomersPageLocator.EMAIL_INPUT, random_email(7, 5))

    @allure.step("Ввод телефона кастомера")
    def input_telephone(self):
        self.input_text(AdminCustomersPageLocator.TELEPHONE_INPUT, random_telefone_number(11))

    @allure.step("Ввод почты кастомера")
    def input_incorrect_email(self):
        self.input_text(AdminCustomersPageLocator.EMAIL_INPUT, random_string(8))

    @allure.step("Ввод пароля кастомера")
    def input_password(self, text):
        self.input_text(AdminCustomersPageLocator.PASSWORD_INPUT, text)

    @allure.step("Повтор ввода пароля кастомера")
    def input_confirm_password(self, text):
        self.input_text(AdminCustomersPageLocator.CONFIRM_PASSWORD_INPUT, text)

    @allure.step("Нажатие кнопки сохранить")
    def click_save_button(self):
        self.click_element(AdminCustomersPageLocator.SAVE_BUTTON)

    @allure.step("Проверка появлени сообшения о том, что действия завершены успешно")
    def verify_success_message(self):
        success_message = self.get_text(AdminCustomersPageLocator.SUCCESS_MESSAGE)
        success_message = success_message[:-2]
        assert success_message == "Success: You have modified customers!"

    @allure.step("Ввод имени и фамилии кастомера в поиск")
    def find_customers_name(self, text):
        self.input_text(AdminCustomersPageLocator.INPUT_CUSTOMERS_NAME_IN_FILTER, text)

    @allure.step("Нажатие кнопки фильтра")
    def click_filter_button(self):
        self.click_element(AdminCustomersPageLocator.BUTTON_FILTER)

    @allure.step("Кликаем по чекбоксу")
    def click_check_box(self):
        self.click_element(AdminCustomersPageLocator.CHECK_BOX_IN_CUSTOMERS_TABLE)

    @allure.step("Нажать кнопку удалить")
    def click_delete_customers_button(self):
        self.click_element(AdminCustomersPageLocator.DELETE_CUSTOMERS_BUTTON)

    @allure.step("Проверка появления сообщения, о том, что форма заполнена неверно")
    def verify_warning_message(self):
        success_message = self.get_text(AdminCustomersPageLocator.SUCCESS_MESSAGE)
        success_message = success_message[:-2]
        assert success_message == "Warning: Please check the form carefully for errors!"

    @allure.step("Проверка появления сообщения, о том, что введена невалидная почта")
    def verify_error_message_email(self):
        success_message = self.get_text(AdminCustomersPageLocator.ERROR_MESSAGE)
        assert success_message == "E-Mail Address does not appear to be valid!"

    @allure.step("Проверка появления сообщения, о том, что введено невалидное имя")
    def verify_error_message_first_name(self):
        success_message = self.get_text(AdminCustomersPageLocator.ERROR_MESSAGE)
        assert success_message == "First Name must be between 1 and 32 characters!"

    @allure.step("Ввод имени превышающего ограничение в 32 символа")
    def input_long_first_name(self):
        self.input_text(AdminCustomersPageLocator.FIRST_NAME_INPUT, random_string(33))

    @allure.step("Проверка появления сообщения, о том, что введена невалидная фамилия")
    def verify_error_message_last_name(self):
        success_message = self.get_text(AdminCustomersPageLocator.ERROR_MESSAGE)
        assert success_message == "Last Name must be between 1 and 32 characters!"

    @allure.step("Ввод фамилии превышающей ограничение в 32 символа")
    def input_long_last_name(self):
        self.input_text(AdminCustomersPageLocator.LAST_NAME_INPUT, random_string(33))

    @allure.step("Проверка появления сообщения, о том, что введен невалидный телефон")
    def verify_error_message_telephone(self):
        success_message = self.get_text(AdminCustomersPageLocator.ERROR_MESSAGE)
        assert success_message == "Telephone must be between 3 and 32 characters!"

    @allure.step("Ввод слишком короткого телефоного номера, меньше 3 символов")
    def input_short_telephone(self):
        self.input_text(AdminCustomersPageLocator.TELEPHONE_INPUT, random_telefone_number(2))

    @allure.step("Ввод номера телефона превышающего ограничение в 32 символа")
    def input_long_telephone(self):
        self.input_text(AdminCustomersPageLocator.TELEPHONE_INPUT, random_telefone_number(33))

    @allure.step("Проверка появления сообщения, о том, что введён невалидный пароль")
    def verify_error_message_password(self, locator: tuple):
        try:
            success_message = self.get_text(AdminCustomersPageLocator.ERROR_MESSAGE)
            assert success_message == "Password must be between 4 and 20 characters!"
        except AssertionError:
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError("Cant find element by locator: {}".format(locator))

    @allure.step("Ввод слишком короткого пароля, меньше 4 символов")
    def input_shot_password(self):
        self.input_text(AdminCustomersPageLocator.PASSWORD_INPUT, random_string(3))

    @allure.step("Ввод пароля превышающего ограничение в 20 символов")
    def input_long_password(self):
        self.input_text(AdminCustomersPageLocator.PASSWORD_INPUT, random_string(21))

    @allure.step("Проверка появления сообщения, о том, что пароль и повтор пароля не совпадают")
    def verify_error_message_confirmation(self):
        success_message = self.get_text(AdminCustomersPageLocator.ERROR_MESSAGE)
        assert success_message == "Password and password confirmation do not match!"

    @allure.step("Ввод рандомного пароля в 12 символов")
    def input_random_password(self):
        self.input_text(AdminCustomersPageLocator.PASSWORD_INPUT, random_string(12))

    @allure.step("Ввод рандомного повтора пароля в 13 символов")
    def input_random_confirm_password(self):
        self.input_text(AdminCustomersPageLocator.CONFIRM_PASSWORD_INPUT, random_string(13))

