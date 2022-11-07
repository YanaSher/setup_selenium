from selenium.webdriver.common.by import By


class AdminNavigatorMenuLocator:
    MENU_CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    GATALOG_PRODUCT = (By.CSS_SELECTOR, "#collapse1>li:nth-child(2)>a")
