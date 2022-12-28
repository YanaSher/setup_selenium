from selenium.webdriver.common.by import By


class AdminCustomersPageLocator:
    ADD_CUSTOMERS_BUTTON = (By.CSS_SELECTOR, ".pull-right>:nth-child(2)")
    DELETE_CUSTOMERS_BUTTON = (By.CSS_SELECTOR, ".pull-right>:nth-child(3)")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[name=firstname]")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[name=lastname]")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name=email]")
    TELEPHONE_INPUT = (By.CSS_SELECTOR, "input[name=telephone]")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name=password]")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name=confirm]")
    SAVE_BUTTON = (By.CSS_SELECTOR, ".pull-right>:nth-child(1)")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert")
    CHECK_BOX_IN_CUSTOMERS_TABLE = (By.CSS_SELECTOR, "input[type=checkbox]")
    INPUT_CUSTOMERS_NAME_IN_FILTER = (By.CSS_SELECTOR, "#input-name")
    BUTTON_FILTER = (By.CSS_SELECTOR, "#button-filter")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".text-danger")

