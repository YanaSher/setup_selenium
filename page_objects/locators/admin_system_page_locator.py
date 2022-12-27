from selenium.webdriver.common.by import By


class AdminSystemPageLocator:
    ADD_USER_BUTTON = (By.CSS_SELECTOR, ".pull-right>:nth-child(1)")
    DELETE_USER_BUTTON = (By.CSS_SELECTOR, ".pull-right>:nth-child(2)")
    INPUT_USER_NAME = (By.CSS_SELECTOR, "#input-username")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[name=firstname]")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[name=lastname]")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name=email]")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name=password]")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name=confirm]")
    INPUT_USER_GROUP = (By.CSS_SELECTOR, "#input-user-group")
    CHOICE_GROUP_DEMONSTRATION = (By.XPATH, "//*[text()='Demonstration']")
    CHOICE_GROUP_ADMINISTRATOR = (By.XPATH, "//*[text()='Administrator']")
    INPUT_STATUS = (By.CSS_SELECTOR, "#input-status")
    CHOISE_STATUS_DISABLED = (By.XPATH, "//*[text()='Disabled']")
    CHOISE_STATUS_ENABLED = (By.XPATH, "//*[text()='Enabled']")
    SAVE_BUTTON = (By.CSS_SELECTOR, ".pull-right>:nth-child(1)")
    CANSEL_BUTTON = (By.CSS_SELECTOR, ".pull-right>:nth-child(2)")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert")

    @staticmethod
    def CHECK_BOX_IN_USER_TABLE(username):
        return By.XPATH, f"//td[text()='{username}']/../td[1]/input"
