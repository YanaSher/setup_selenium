from selenium.webdriver.common.by import By

class CatalogPage:
    CATALOG_HEADER = (By.CSS_SELECTOR, "h2")
    HEADER_TEXT = (By.XPATH, "//h2[text()='Cameras']")
    LIST_VIEW = (By.CSS_SELECTOR, "#list-view")
    GREED_VIEW = (By.CSS_SELECTOR, "#grid-view")
    BUTTON_SORT_BY = (By.CSS_SELECTOR, "#input-sort")
    BUTTON_SHOW = (By.CSS_SELECTOR, "#input-limit")
    BUTTON_DESKTOPS = (By.LINK_TEXT, "Desktops (13)")
    HEADER_DESKTOPS = (By.XPATH, "//h2[text()='Desktops']")
    BUTTON_LAPTOPS_NOTEBOOKS = (By.LINK_TEXT, "Laptops & Notebooks (5)")
    HEADER_LAPTOPS_NOTEBOOKS = (By.XPATH, "//h2[text()='Laptops & Notebooks']")
#    BUTTON_PARAMETRIZE = (By.LINK_TEXT, "f'{link_text}'")
#    HEADER_PARAMETRIZE = (By.XPATH, "//h2[text()=f'{h2_text}']")