from selenium.webdriver.common.by import By


class ProductPageLocator:
    HEADER_PRODUCT = (By.XPATH, "//h1[text()='Nikon D300']")
    PRODUCT_PRICE = (By.XPATH, "//h2[text()='$98.00']")
    ADD_BUTTON = (By.CSS_SELECTOR, "#button-cart")
    TWIT_LINK = (By.XPATH, "//*[text()='Tweet']")
    COUNT_INPUT = (By.CSS_SELECTOR, "input[name=quantity]")
