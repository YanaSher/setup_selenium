import allure
from page_objects.base_page import BasePage
from page_objects.locators.login_admin_page_locator import AdminPageLocator
from page_objects.elements.login_form import LoginForm


class AdminPage(BasePage):
    path = "/admin"

    @allure.step("Открываем страницу админки")
    def open(self, url):
        self.browser.get(url + self.path)

    @allure.step("Проверка отображения элемента - поле ввода имени пользователя")
    def verify_user_input(self):
        self.verify_element_presence(AdminPageLocator.USERNAME_INPUT)

    @allure.step("Проверка отображения элемента - поле ввода пароля")
    def verify_password_input(self):
        self.verify_element_presence(AdminPageLocator.PASSWORD_INPUT)

    @allure.step("Проверка отображения элемента - кнопка подтверждения")
    def verify_submit_button(self):
        self.verify_element_presence(AdminPageLocator.SUBMIT_BUTTON)

    @allure.step("Проверка отображения элемента - ссылкаесли забыли пароль")
    def verify_forgotten_pasword(self):
        self.verify_element_presence(AdminPageLocator.FORGOTTEN_PASSWORD)

    @allure.step("Проверка отображения элемента -ссылки opencart")
    def verify_opencart_link(self):
        self.verify_element_presence(AdminPageLocator.OPENCART_LINK)

    @allure.step("Авторизация на странице админа")
    def login_admin(self, username, password):
        LoginForm(self.browser).login_with_admin(username, password)
        self.verify_element_presence(LoginForm.ADMIN_PAGE_HEADER)
        return self
