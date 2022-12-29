from selenium.webdriver.common.by import By


class AdminNavigatorMenuLocator:
    MENU_CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    GATALOG_PRODUCT = (By.CSS_SELECTOR, "#collapse1>li:nth-child(2)>a")
    MENU_SYSTEM = (By.CSS_SELECTOR, "#menu-system")
    SYSTEM_USERS = (By.CSS_SELECTOR, "#collapse7>li:nth-child(2)>a")
    USERS_USERS = (By.CSS_SELECTOR, "#collapse7-1>li:nth-child(1)>a")
    MENU_CUSTOMER = (By.CSS_SELECTOR, "#menu-customer")
    GATALOG_CUSTOMER = (By.CSS_SELECTOR, "#collapse5>li:nth-child(1)>a")
