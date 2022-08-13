from selenium.webdriver.common.by import By


class MainPageLocators:
    TOP_MENU = (By.CSS_SELECTOR, "#top")
    INPUT_SEARCH = (By.CSS_SELECTOR, ".input-lg")
    BUTTON_SEARCH = (By.CSS_SELECTOR, ".input-group-btn")
    FORM_CURRENCY = (By.CSS_SELECTOR, "#form-currency")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-block>.dropdown-toggle")
    LOGO = (By.CSS_SELECTOR, "#logo")
    EURO_CURRENCY = (By.CSS_SELECTOR, "[name=EUR]")
    GBP_CURRENCY = (By.CSS_SELECTOR, "[name=GBP]")
    USD_CURRENCY = (By.CSS_SELECTOR, "[name=USD]")
