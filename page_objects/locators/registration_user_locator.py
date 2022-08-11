from selenium.webdriver.common.by import By


class RegistrationUserLocator:
    MI_ACCOUNT = (By.CSS_SELECTOR, ".list-inline>.dropdown")
    REGISTER_LINK = (By.XPATH, "//*[text()='Register']")
    HEADER_TEXT = (By.XPATH, "//h1[text()='Register Account']")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[name=firstname]")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[name=lastname]")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name=email]")
    TELEPHONE_INPUT = (By.CSS_SELECTOR, "input[name=telephone]")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name=password]")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name=confirm]")
    CHECK_BOX_POLICY = (By.CSS_SELECTOR, "input[type=checkbox]")
    POLICY_LINK = (By.XPATH, "//*[text()='Privacy Policy']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[value=Continue]")
