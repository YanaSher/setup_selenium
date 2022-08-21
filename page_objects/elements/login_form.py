from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class LoginForm(BasePage):
    INPUT_EMAIL_LOGIN = (By.CSS_SELECTOR, "#input-email")
    INPUT_LOGIN = (By.CSS_SELECTOR, "#input-username")
    INPUT_PASSWORD_LOGIN = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type=submit]")
    ADMIN_PAGE_HEADER = (By.XPATH, "//h1[text()='Dashboard']")

    def login_with_admin(self, username, password):
        self.input_text(self.INPUT_LOGIN, username)
        self.input_text(self.INPUT_PASSWORD_LOGIN, password)
        self.click_element(self.LOGIN_BUTTON)
