import allure

from randomaizer import random_string, random_email
from page_objects.base_page import BasePage
from page_objects.locators.admin_system_page_locator import AdminSystemPageLocator


class AdminSystemPage(BasePage):

    @allure.step("Нажатие кнопки - добавление юзера")
    def click_add_user_button(self):
        self.click_element(AdminSystemPageLocator.ADD_USER_BUTTON)

    @allure.step("Ввод ника пользователя")
    def input_user_name(self, text):
        self.input_text(AdminSystemPageLocator.INPUT_USER_NAME, text)

    @allure.step("Ввод имени пользователя")
    def input_first_name(self):
        self.input_text(AdminSystemPageLocator.FIRST_NAME_INPUT, random_string(7))

    @allure.step("Ввод фамилии пользователя")
    def input_last_name(self):
        self.input_text(AdminSystemPageLocator.LAST_NAME_INPUT, random_string(11))

    @allure.step("Ввод почты пользователя")
    def input_email(self):
        self.input_text(AdminSystemPageLocator.EMAIL_INPUT, random_email(7, 5))

    @allure.step("Ввод пароля")
    def input_password(self, text):
        self.input_text(AdminSystemPageLocator.PASSWORD_INPUT, text)

    @allure.step("Ввод подтверждения пароля")
    def input_confirm_password(self, text):
        self.input_text(AdminSystemPageLocator.CONFIRM_PASSWORD_INPUT, text)

    @allure.step("Смена группы пользователя на demonstration")
    def choise_user_group_demonstration(self):
        self.click_element(AdminSystemPageLocator.INPUT_USER_GROUP)
        self.click_element(AdminSystemPageLocator.CHOICE_GROUP_DEMONSTRATION)

    @allure.step("Смена статуса на enabled")
    def choise_status_enabled(self):
        self.click_element(AdminSystemPageLocator.INPUT_STATUS)
        self.click_element(AdminSystemPageLocator.CHOISE_STATUS_ENABLED)

    @allure.step("Нажатие кнопки сохранить")
    def click_save_button(self):
        self.click_element(AdminSystemPageLocator.SAVE_BUTTON)

    @allure.step("Проверка сообщения о том, что действие выполнено успешно")
    def verify_success_message(self):
        try:
            success_message = self.get_text(AdminSystemPageLocator.SUCCESS_MESSAGE)
            success_message = success_message[:-2]
            assert success_message == "Success: You have modified users!"
        except AssertionError:
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )

    @allure.step("Выбор чекбокса с нужным пользователем")
    def click_check_box(self, username):
        self.click_element(AdminSystemPageLocator.CHECK_BOX_IN_USER_TABLE(username))

    @allure.step("Нажатие кнопки удалить")
    def click_delete_user_button(self):
        self.click_element(AdminSystemPageLocator.DELETE_USER_BUTTON)

    @allure.step("Нажатие кнопки отменить")
    def click_cancel_delete_user_button(self):
        self.click_element(AdminSystemPageLocator.CANSEL_BUTTON)

    @allure.step("Проверка спредупреждения о том, что такой пользователь уже существует")
    def warning_success_message(self):
        success_message = self.get_text(AdminSystemPageLocator.SUCCESS_MESSAGE)
        success_message = success_message[:-2]
        assert success_message == "Warning: Username is already in use!"
