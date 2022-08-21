from selenium.webdriver.common.by import By


class AdminPageLocator:
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[name=password]")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    OPENCART_LINK = (
    By.XPATH, "//*[text()='OpenCart']")  # не переписать через css, т.к. у него нет возможности поиска по тексту
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
